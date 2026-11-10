from __future__ import annotations
import secrets
import threading
import time
import urllib.parse as urllib
from pathlib import Path
from app.core.env2 import config2Env
from app.log import logger
from app.modules.hdhive.oauth_token import JsonObject, JsonValue, extract_tokens, load_token_config, safe_int, save_token_config
from app.utils.http_client import HttpClient, HttpResponse
from app.utils.mjson import JsonUtils
BASE_URL = 'https://authx.771885.xyz'
DEFAULT_AUTHORIZE_BASE_URL = 'https://re0.me'
DEFAULT_API_PREFIX = '/api/hdhive'
DEFAULT_TOKEN_CONFIG_PATH = Path('/config/hdhive-openapi.json')
DEFAULT_CLIENT_ID = 'app_6e3ea0f056ec3ef20b9ccdf1'
DEFAULT_SCOPE = 'meta query unlock write vip'
DEFAULT_RESPONSE_MODE = 'redirect'
RETRYABLE_STATUS_CODES = {
    429,
    500,
    502,
    503,
    504}
MAX_RETRY_COUNT = 2
RETRY_INTERVAL_SECONDS = 0.5
SENSITIVE_KEYS = {
    'code',
    'access_token',
    'refresh_token'}
TOKEN_REFRESH_REQUIRED_CODE = 'OPENAPI_REFRESH_REQUIRED'
CONFIG_UPDATED_AT_KEY = 'config_updated_at'

class HDHiveProxyError(Exception):
    
    def __init__(self, message: str, request_url: str, status_code: int, response_body: str) -> None:
        super().__init__(message)
        self.message = message
        self.request_url = request_url
        self.status_code = status_code
        self.response_body = response_body

class HDHiveProxyClient:
    '''HDHive 代理客户端。

    这个类同时负责三件事：
    1. 生成 OAuth 授权地址，并把 redirect_uri/state 持久化，方便回调兑换 token。
    2. 把 access_token/refresh_token 和有效期缓存在实例属性里，避免每次请求都读本地文件。
    3. 业务接口遇到 OPENAPI_REFRESH_REQUIRED 时自动刷新 token，并重放原请求一次。
    '''
    
    def __init__(self, base_url=BASE_URL, timeout_seconds=30, api_prefix=DEFAULT_API_PREFIX, token_config_path=DEFAULT_TOKEN_CONFIG_PATH, proxy=None, authorize_base_url=DEFAULT_AUTHORIZE_BASE_URL, client_id=DEFAULT_CLIENT_ID, scope=DEFAULT_SCOPE):
        _var_var_0 = base_url.strip().rstrip('/')
        _var_var_1 = authorize_base_url.strip().rstrip('/')
        _var_var_2 = '/' + api_prefix.strip().strip('/')
        _var_var_3 = client_id.strip()
        _var_var_4 = scope.strip()
        if not _var_var_0:
            raise ValueError('HDHive 代理服务地址不能为空')
        if not _var_var_1:
            raise ValueError('HDHive 授权服务地址不能为空')
        if not _var_var_3:
            raise ValueError('HDHive client_id 不能为空')
        if timeout_seconds <= 0:
            raise ValueError('HDHive 代理请求超时时间必须大于 0')
        self._base_url = _var_var_0
        self._authorize_base_url = _var_var_1
        self._api_prefix = _var_var_2
        self._token_config_path = token_config_path
        self._client_id = _var_var_3
        self._scope = _var_var_4
        self._token_config = load_token_config(self._token_config_path)
        self.access_token = ''
        self.refresh_token = ''
        self.expires_in = 0
        self.refresh_expires_in = 0
        self.token_updated_at = 0
        self.access_token_expires_at = 0
        self.refresh_token_expires_at = 0
        self._token_refresh_lock = threading.RLock()
        self._sync_token_attributes()
        self._http_client = HttpClient(timeout = timeout_seconds, proxy = proxy or None, default_headers = {
            'User-Agent': 'auth-admin-hdhive-proxy-python/1.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json' })

    
    def build_authorize_url(self, redirect_uri, state=None):
        '''生成 HDHive 授权 URL，并持久化 redirect_uri/state。

        redirect_uri 必须和后续 code 兑换 token 时传入的值一致。这里先写入本地配置，
        所以回调接口只拿到 code 时也能完成兑换，不需要调用方再重复保存 redirect_uri。
        '''
        _var_var_5 = redirect_uri.strip()
        if not _var_var_5:
            raise ValueError('HDHive redirect_uri 不能为空')
        _var_var_6 = state.strip() if state else secrets.token_urlsafe(24)
        if not _var_var_6:
            raise ValueError('HDHive OAuth state 不能为空')
        self._save_token_config({
            CONFIG_UPDATED_AT_KEY: _now_timestamp(),
            'state': _var_var_6,
            'redirect_uri': _var_var_5 })
        _var_var_7 = {
            'client_id': self._client_id,
            'redirect_uri': _var_var_5,
            'scope': self._scope,
            'state': _var_var_6,
            'response_mode': DEFAULT_RESPONSE_MODE }
        return f'''{self._authorize_base_url}/openapi/authorize?{urllib.parse.urlencode(_var_var_7)}'''

    
    def open_oauth_token(self, code, redirect_uri=None):
        '''使用授权码兑换 token。

        redirect_uri 可选：传入时会刷新本地配置；不传时使用 build_authorize_url 保存的值。
        兑换成功后会同步更新实例属性和本地文件。
        '''
        _var_var_8 = code.strip()
        _var_var_5 = self._resolve_redirect_uri(redirect_uri)
        if not _var_var_8:
            raise ValueError('HDHive 授权码不能为空')
        _var_var_9 = self._post_json('/oauth/token', {
            'code': _var_var_8,
            'redirect_uri': _var_var_5 })
        self._save_response_tokens(_var_var_9)
        return _var_var_9

    
    def open_refresh_token(self, refresh_token: str | None = None) -> JsonObject:
        '''刷新 access_token。

        refresh_token 可选；通常不需要外部传入，直接使用实例初始化时缓存的 self.refresh_token。
        '''
        if refresh_token is None:
            self._reload_token_config()
        token = (refresh_token or self.refresh_token).strip()
        if not token:
            raise ValueError('HDHive 刷新令牌不能为空')
        response = self._post_json('/oauth/refresh', {'refresh_token': token})
        self._save_response_tokens(response)
        return response
    def open_me(self):
        '''读取当前授权用户信息。access_token 由客户端实例自动提供。'''
        return self._post_json_with_access_token('/me', { })

    
    def open_checkin(self, is_gambler=False):
        '''每日签到'''
        return self._post_json_with_access_token('/checkin', {
            'is_gambler': is_gambler })

    
    def open_resources(self, resource_type: str, tmdb_id: str) -> JsonObject:
        '''查询资源列表。调用方只需要传业务参数，不需要关心 access_token。'''
        if not resource_type:
            raise ValueError('HDHive 资源类型不能为空')
        if not tmdb_id:
            raise ValueError('HDHive TMDB ID 不能为空')
        response = self._post_json_with_access_token('/resources', {'resource_type': resource_type, 'tmdb_id': f'{tmdb_id}'})
        items = response.get('data', [])
        filtered_items = [item for item in items if item.get('pan_type') in config2Env.hdhive_resource_types]
        for item in filtered_items:
            if item.get('unlock_points') is None:
                item['unlock_points'] = 0
        sort_reverse = True
        if config2Env.hdhive_sort_order == 'asc':
            sort_reverse = False
        sorted_items = sorted(filtered_items, key=lambda r: r.get(config2Env.hdhive_sort_by), reverse=sort_reverse)
        response['data'] = sorted_items
        return response
    @staticmethod
    def safe_int(value, default=0):
        """安全转换为整数，失败返回默认值"""
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def open_unlock_resource(self, slug='', slugs=None):
        '''解锁资源。支持单个 slug 或批量 slugs，二者不能同时传。'''
        _var_var_17 = _build_unlock_payload(slug, slugs)
        return self._post_json_with_access_token('/resources/unlock', _var_var_17)

    
    def _post_json(self, path: str, payload: JsonObject, allowed_error_codes: set[str] | None = None) -> JsonObject:
        '''发送 JSON POST 请求，并处理网络抖动重试。

        allowed_error_codes 用于允许某些业务错误以普通响应返回，例如 token 过期。
        这样上层可以看到 OPENAPI_REFRESH_REQUIRED 并执行刷新，而不是直接抛异常。
        '''
        request_path = f'{self._api_prefix}{path}'
        request_url = f'{self._base_url}{request_path}'
        last_error = None
        for attempt in range(1, MAX_RETRY_COUNT + 2):
            _log_request(request_path, payload, attempt)
            try:
                response = self._http_client.post(request_url, json_data=payload)
                response_json = _parse_json_response(response, request_path)
                _log_response(request_path, response, response_json, attempt)
                _raise_for_error_response(response, response_json, allowed_error_codes or set())
                return response_json
            except RuntimeError as error:
                last_error = HDHiveProxyError(f'HDHive 代理请求失败：{error}', request_url, 0, '')
            except HDHiveProxyError as error:
                last_error = error
                if error.status_code not in RETRYABLE_STATUS_CODES:
                    raise
            if attempt <= MAX_RETRY_COUNT:
                logger.warning(
                    'HDHive 代理请求失败，准备重试：request_path=%s attempt=%s max_retry_count=%s status_code=%s response_body=%s error=%s',
                    request_path,
                    attempt,
                    MAX_RETRY_COUNT,
                    last_error.status_code,
                    last_error.response_body,
                    last_error.message,
                )
                time.sleep(RETRY_INTERVAL_SECONDS)
        if last_error is None:
            raise HDHiveProxyError('HDHive 代理请求失败：没有响应', request_url, 0, '')
        raise last_error
    def _post_json_with_access_token(self, path: str, payload: JsonObject) -> JsonObject:
        '''为业务请求注入 access_token，并在 token 过期时自动刷新后重放一次。'''
        request_payload = {**payload, 'access_token': self._resolve_access_token()}
        response = self._post_json(path, request_payload, {TOKEN_REFRESH_REQUIRED_CODE})
        if response.get('code') != TOKEN_REFRESH_REQUIRED_CODE:
            return response
        logger.info('HDHive access_token 已失效，准备使用本地 refresh_token 刷新')
        request_payload['access_token'] = self._refresh_stored_access_token(request_payload['access_token'])
        return self._post_json(path, request_payload)
    def _resolve_access_token(self):
        '''从实例缓存读取 access_token；缺失时显式报错，避免发出无效请求。'''
        self._reload_token_config()
        return _normalize_access_token(self.access_token)

    
    def _refresh_stored_access_token(self, stale_access_token):
        '''使用最新 refresh_token 刷新 access_token，并返回可重放请求的新 access_token。'''
        with self._token_refresh_lock:
            self._reload_token_config()
            _var_var_25 = _normalize_access_token(self.access_token)
            if _var_var_25 != stale_access_token:
                logger.info('HDHive token 已被其他请求刷新，复用最新 access_token')
                return _var_var_25
            if not self.refresh_token:
                raise ValueError('HDHive access_token 已失效，且本地没有 refresh_token')
            try:
                _var_var_9 = self.open_refresh_token(self.refresh_token)
                if not _var_var_9.get('success'):
                    _var_var_26 = self._recover_refreshed_access_token(stale_access_token)
                    if _var_var_26:
                        return _var_var_26
                    raise HDHiveProxyError(_read_error_message(_var_var_9, 401), f'{self._base_url}{self._api_prefix}/oauth/refresh', 401, str(_mask_json_object(_var_var_9)))
                return _normalize_access_token(self.access_token)
            except HDHiveProxyError:
                _var_var_26 = self._recover_refreshed_access_token(stale_access_token)
                if _var_var_26:
                    return _var_var_26
                raise

    
    def _reload_token_config(self) -> None:
        '''重新读取磁盘 token 配置，避免长期单例继续使用旧 refresh_token。'''
        self._token_config = {**self._token_config, **load_token_config(self._token_config_path)}
        self._sync_token_attributes()
    def _recover_refreshed_access_token(self, stale_access_token):
        '''刷新失败后再次读取配置；若其他进程已刷新成功，则复用最新 access_token。'''
        self._reload_token_config()
        _var_var_25 = _normalize_access_token(self.access_token)
        if _var_var_25 == stale_access_token:
            return ''
        logger.info('HDHive refresh_token 已被其他请求轮换，复用最新 access_token')
        return _var_var_25

    
    def _resolve_redirect_uri(self, redirect_uri: str | None) -> str:
        '''解析 token 兑换所需 redirect_uri。

        OAuth 要求兑换 token 的 redirect_uri 和授权时完全一致。调用方传入时更新缓存；
        不传时读取实例缓存中的 redirect_uri，避免每次兑换都碰磁盘。
        '''
        if redirect_uri is not None and redirect_uri.strip():
            requested_redirect_uri = redirect_uri.strip()
            self._save_token_config({'redirect_uri': requested_redirect_uri, CONFIG_UPDATED_AT_KEY: _now_timestamp()})
            return requested_redirect_uri
        cached_redirect_uri = str(self._token_config.get('redirect_uri', '')).strip()
        if not cached_redirect_uri:
            raise ValueError('HDHive redirect_uri 不能为空')
        return cached_redirect_uri
    def _save_response_tokens(self, response: JsonObject) -> None:
        '''从响应中提取 token 字段，写入内存缓存和本地文件。'''
        tokens = extract_tokens(response)
        if not tokens:
            return
        self._save_token_config({**tokens, 'updated_at': _now_timestamp()})
    def _sync_token_attributes(self):
        '''把 _token_config 中的 token 字段同步到实例属性。

        对外暴露 access_token/refresh_token/有效时间属性，调用方如需查看当前状态，
        不必知道配置文件结构，也不需要自己计算 expires_at。
        '''
        self.access_token = str(self._token_config.get('access_token', '')).strip()
        self.refresh_token = str(self._token_config.get('refresh_token', '')).strip()
        self.expires_in = safe_int(self._token_config.get('expires_in'))
        self.refresh_expires_in = safe_int(self._token_config.get('refresh_expires_in'))
        self.token_updated_at = safe_int(self._token_config.get('updated_at'))
        self.access_token_expires_at = _build_expires_at(self.token_updated_at, self.expires_in)
        self.refresh_token_expires_at = _build_expires_at(self.token_updated_at, self.refresh_expires_in)
        return None

    
    def _save_token_config(self, values: JsonObject) -> None:
        '''更新实例缓存并落盘。

        文件只在授权 URL、token 兑换、token 刷新等状态变更时写入；普通业务请求不读写文件。
        '''
        with self._token_refresh_lock:
            self._token_config = {**self._token_config, **load_token_config(self._token_config_path), **values}
            save_token_config(self._token_config_path, self._token_config)
            self._sync_token_attributes()
def _normalize_access_token(access_token):
    '''校验 access_token，失败时直接抛错，避免远端返回更难定位的 401。'''
    _var_var_29 = access_token.strip()
    if not _var_var_29:
        raise ValueError('HDHive access token 不能为空')


def _build_unlock_payload(slug: str, slugs: list[str] | None) -> JsonObject:
    '''构造解锁请求体，并保证单个 slug 和批量 slugs 不会混用。'''
    normalized_slug = slug.strip()
    normalized_slugs = [item.strip() for item in (slugs or []) if item.strip()]
    if normalized_slug and normalized_slugs:
        raise ValueError('HDHive 解锁资源时 slug 和 slugs 不能同时传')
    if normalized_slug:
        return {'slug': normalized_slug}
    if normalized_slugs:
        return {'slugs': normalized_slugs}
    raise ValueError('HDHive 解锁资源必须传 slug 或 slugs')
def _parse_json_response(response, request_path):
    '''解析代理响应，并把任意 JSON dict 归一化成 JsonObject。'''
    try:
        _var_var_33 = response.json()
        if not isinstance(_var_var_33, dict):
            logger.error('HDHive 代理响应 JSON 类型错误：request_path=%s status_code=%s json_type=%s response_body=%s', request_path, response.status_code, type(_var_var_33).__name__, response.text)
            raise HDHiveProxyError('HDHive 代理响应 JSON 不是对象', response.url, response.status_code, response.text)
        return _to_json_object(_var_var_33)
    except ValueError as _var_var_23:
        logger.error('HDHive 代理响应 JSON 解析失败：request_path=%s status_code=%s response_body=%s error=%s', request_path, response.status_code, response.text, _var_var_23)
        raise HDHiveProxyError('HDHive 代理响应不是合法 JSON', response.url, response.status_code, response.text) from _var_var_23


def _raise_for_error_response(response, response_json, allowed_error_codes):
    '''把 HTTP 错误响应转成带上下文的 HDHiveProxyError。'''
    if response.status_code < 400:
        return
    _var_var_34 = response_json.get('code')
    if isinstance(_var_var_34, str) and _var_var_34 in allowed_error_codes:
        return
    raise HDHiveProxyError(_read_error_message(response_json, response.status_code), response.url, response.status_code, response.text)


def _read_error_message(response_json, status_code):
    '''从代理错误响应中提取最有用的错误信息。'''
    _var_var_35 = response_json.get('detail')
    if isinstance(_var_var_35, str) and _var_var_35.strip():
        return f'''HDHive 代理请求失败：{_var_var_35.strip()}'''
    for _var_var_36 in ('description', 'message', 'code'):
        _var_var_37 = response_json.get(_var_var_36)
        if not isinstance(_var_var_37, str):
            continue
        if not _var_var_37.strip():
            continue
        return f'''HDHive 代理请求失败：{_var_var_37.strip()}'''


def _log_request(request_path, payload, attempt):
    '''记录请求日志；敏感字段会被遮罩。'''
    logger.info('开始请求 HDHive 代理接口：request_path=%s attempt=%s payload=%s', request_path, attempt, _mask_json_object(payload))


def _log_response(request_path, response, response_json, attempt):
    '''记录响应日志；token 等敏感字段不会明文输出。'''
    logger.info('HDHive 代理接口响应完成：request_path=%s attempt=%s status_code=%s response=%s', request_path, attempt, response.status_code, _mask_json_object(response_json))


def _to_json_object(raw: dict[object, object]) -> JsonObject:
    '''把未知 key/value 类型的 dict 转成稳定的 JSON 对象。'''
def _to_json_value(value: object) -> JsonValue:
    '''把无法直接序列化的响应值转成字符串，避免污染后续日志和落盘。'''
    if value is None or isinstance(value, bool | int | float | str):
        return value
    if isinstance(value, list):
        return [_to_json_value(item) for item in value]
    if isinstance(value, dict):
        return _to_json_object(value)
def _mask_json_object(value: JsonObject) -> JsonObject:
    '''递归遮罩 JSON 对象中的敏感字段。'''
def _mask_json_value(key: str, value: object) -> JsonValue:
    '''根据字段名决定是否遮罩；列表和对象递归处理。'''
    if key.lower() in SENSITIVE_KEYS:
        return _mask_secret(str(value))
    if isinstance(value, dict):
        return _mask_json_object(_to_json_object(value))
    if isinstance(value, list):
        return [_mask_json_value(key, item) for item in value]
def _mask_secret(value):
    '''保留首尾少量字符用于排查，避免日志泄露完整 token。'''
    _var_var_38 = value.strip()
    if not _var_var_38:
        return ''
    if len(_var_var_38) <= 8:
        return '*' * len(_var_var_38)


def _now_timestamp():
    '''返回当前秒级时间戳，统一本文件的时间写入格式。'''


def _build_expires_at(updated_at, expires_in):
    '''把 token 更新时间和有效秒数转换成绝对过期时间；缺字段时返回 0。'''
    if updated_at <= 0 or expires_in <= 0:
        return 0
