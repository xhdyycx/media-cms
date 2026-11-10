# File: log_handler.py (Restored from bytecode)
from blacksheep import Request
from app.log import logger
from app.utils.mjson import JsonUtils

async def log_handler_middlewares(request: Request, handler):
    """请求日志中间件"""
    method = str(request.method)
    path = str(request.path)
    
    if path.startswith('/d') or path.startswith('/s') or path.startswith('/api/logs/ws') or path.startswith('/api/wx/message'):
        return await handler(request)
        
    query_str = JsonUtils.to_str(request.query) if request.query else ''
    
    try:
        body = await request.json()
        body_str = JsonUtils.to_str(body) if body else ''
    except Exception:
        body_str = ''
        
    headers_dict = {}
    try:
        header_pairs = [(k.decode().lower(), v.decode()) for k, v in request.headers.items()]
        for k, v in header_pairs:
            if k == 'authorization':
                headers_dict[k] = f"{v[:20]}..." if v else ''
        if not headers_dict:
            headers_dict = ''
    except Exception as e:
        headers_dict = {'error': f"Failed to parse headers: {str(e)}"}
        
    logger.info(f"|request_in |{method}|{path}|query={query_str}|body={body_str}|headers={JsonUtils.to_str(headers_dict)}")
    
    try:
        response = await handler(request)
    except Exception as e:
        logger.exception(f"Unhandled exception in handler for {path}: {e}")
        raise
    
    try:
        resp_json = await response.json()
        resp_str = JsonUtils.to_str(resp_json)
    except Exception:
        resp_str = ''
        
    logger.info(f"|request_out|{method}|{path}|response_body={resp_str}")
    return response