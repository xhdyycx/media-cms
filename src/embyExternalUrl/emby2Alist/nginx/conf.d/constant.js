// 如果使用拆分配置,请注意填写 config 下使用到的配置文件

import commonConfig from "./config/constant-common.js";
import mountConfig from "./config/constant-mount.js";
import proConfig from "./config/constant-pro.js";
import symlinkConfig from "./config/constant-symlink.js";
import strmConfig from "./config/constant-strm.js";
import transcodeConfig from "./config/constant-transcode.js";
import extConfig from "./config/constant-ext.js";
import nginxConfig from "./config/constant-nginx.js";

// 必填项,根据实际情况修改下面的设置

// 这里默认 emby/jellyfin 的地址是宿主机,要注意 iptables 给容器放行端口
const embyHost = "http://172.17.0.1:8096";

// emby/jellyfin api key, 在 emby/jellyfin 后台设置
const embyApiKey = "f839390f50a648fd92108bc11ca6730a";

// 挂载工具 rclone/CD2 多出来的挂载目录, 例如将 od,gd 挂载到 /mnt 目录下: /mnt/onedrive /mnt/gd ,那么这里就填写 /mnt
// 通常配置一个远程挂载根路径就够了,默认非此路径开头文件将转给原始 emby 处理
// 如果没有挂载,全部使用 strm 文件,此项填[""],必须要是数组
const mediaMountPath = ["/mnt"];

// 路由规则,注意顺序是从上至下匹配,千万注意规则不要重叠,不然排错十分困难,字幕和图片走了缓存,不在此规则内
// 参数1: 指定处理模式,单规则的默认值为"proxy",但是注意整体规则都不匹配默认值为"redirect",然后下面参数序号-1
// "proxy": 原始媒体服务器处理(中转流量), "redirect": 直链 302,
// "transcode": 转码,稍微有些歧义,大部分情况等同于"proxy",这里只是不做转码参数修改,具体是否转码由 emby 客户端自己判断上报或客户端手动切换码率控制,
// "block": 屏蔽媒体播放和下载, "blockDownload": 只屏蔽下载, "blockPlay": 只屏蔽播放,
// 参数2: 分组名,组内为与关系(全部匹配),多个组和没有分组的规则是或关系(任一匹配),然后下面参数序号-1
// 参数3: 匹配类型或来源(字符串参数类型) "filePath": 文件路径(Item.Path), "alistRes": alist返回的链接
// 参数4: 0: startsWith(str), 1: endsWith(str), 2: includes(str), 3: match(/ain/g)
// 参数5: 匹配目标,为数组的多个参数时,数组内为或关系(任一匹配)
const routeRule = [
  // ["filePath", 0, "/mnt/sda1"],
  // ["filePath", 1, ".mp3"],
  // ["filePath", 2, "Google"],
  // ["alistRes", 2, "/NAS/"], // 例如使用 alias 聚合了 nas 本地文件,可能会存在卡顿或花屏
  // ["filePath", 3, /private/ig],
  // docker 注意必须为 host 模式,不然此变量全部为内网ip,判断无效,nginx 内置变量不带$,客户端地址($remote_addr)
  // ["r.variables.remote_addr", 0, strHead.lanIp],
  // ["r.headersIn.User-Agent", 2, "IE"], // 请求头参数,客户端UA
  // ["r.args.X-Emby-Device-Id", 0, "d4f30461-ec5c-488d-b04a-783e6f419eb1"], // 链接入参,设备id
  // ["r.args.X-Emby-Device-Name", 0, "Microsoft Edge Windows"], // 链接入参,设备名称
  // ["r.args.UserId", 0, "ac0d220d548f43bbb73cf9b44b2ddf0e"], // 链接入参,用户id
  // 注意非"proxy"无法使用"alistRes"条件,因为没有获取 alist 直链的过程
  ["proxy", "filePath", 0, ["/cms_local_file_path"]],
  // ["proxy", "直播走中转01", "r.XMedia.IsInfiniteStream", "===", true],
  // ["redirect", "filePath", 0, "/mnt/sda2"],
  // ["transcode", "filePath", 0, "/mnt/sda3"],
  // ["transcode", "115-local", "r.args.X-Emby-Client", 0, strHead.xEmbyClients.XXX],
  // ["transcode", "115-local", "filePath", 0, "/mnt/115"],
  // ["block", "filePath", 0, "/mnt/sda4"],

  // 高级分组规则,XMedia 为固定值,等于 Emby.MediaSources 数组中的单个目标对象
  // 注意设备id具有唯一性,不会跟随切换用户变更,取值参考 /PlaybackInfo 接口的出入参数
  // r.XMedia.MediaStreams 数组比较特殊,路由规则暂未做关键词抽取,但目前匹配视频流规则够用,多音频/字幕流不太好写规则
  // r.XMedia.MediaStreams.0 一般为视频流对象,不支持 r.XMedia.MediaStreams[0] 写法

  // 此条规则代表大于等于 3Mbps 码率的允许转码,平方使用双星号表示,无意义加减仅为示例,注意 emby/jellyfin 码率为 bps 单位
  // ["transcode", "高码率允许转码01", "r.XMedia.Bitrate", ">=", 3 * 1000 ** 2 + (1 * 1000 ** 2) - (1 * 1000 ** 2)],
  // 可选规则,结合上条规则做分组,同时满足才能生效,否则继续向下匹配
  // ["transcode", "高码率允许转码01", "r.args.X-Emby-Device-Id", "===", ["设备id01", "设备id02"]],
  // 此条规则代表 4K 分辨率的允许转码,但假如设备自身上报和上游决定走转码,不满足的也会转码,遵守上游倾向为播放成功率考虑
  // ["transcode", "高分辨率允许转码01", "r.XMedia.MediaStreams.0.DisplayTitle", "includes", "4K"],
  // 可选替换上条规则,更精确的分辨率规则,例如 21:9 视频,或某些 2.5 K 视频等不在标准分辨率划分内的
  // ["transcode", "高分辨率允许转码01", "r.XMedia.MediaStreams.0.Width", ">=", 4320],
  // 精确屏蔽指定功能,注意同样是整体规则都不匹配默认走"redirect",即不屏蔽,建议只用下方一条,太复杂的话需要自行测试
  // ["blockDownload", "屏蔽下载01", "r.headersIn.User-Agent", "includes", strHead.xUAs.blockDownload],
  // 非必须,该分组内细分为用户 id 白名单,结合上面一条代表 "屏蔽指定标识客户端的非指定用户的下载"
  // ["blockDownload", "屏蔽下载01", "r.args.UserId", "startsWith:not", ["用户id01", "用户id02"]],
  // 非必须,该分组内细分为入库路径黑名单,结合上面两条代表 "屏蔽指定标识客户端的非指定用户的指定入库路径的下载"
  // ["blockDownload", "屏蔽下载01", "filePath", "startsWith", ["/mnt/115"]],
];

// 路由缓存配置
const routeCacheConfig = {
  // 总开关,是否开启路由缓存,此为一级缓存,添加阶段为 redirect 和 proxy 之前
  // 短时间内同客户端访问相同资源不会再做判断和请求 alist,有限的防抖措施,出现问题可以关闭此选项
  enable: false,
  // 二级缓存开关,仅针对直链,添加阶段为进入单集详情页,clientSelfAlistRule 中的和首页直接播放的不生效
  // 非 web 端且限 UA 的不建议使用,效率太低,因部分客户端详情页 UA 和播放器 UA 存在不同的情况
  enableL2: false,
  // 缓存键表达式,默认值好处是命中范围大,但会导致 routeRule 中针对设备的规则失效,多个变量可自行组合修改,冒号分隔
  // 注意 jellyfin 是小写开头 mediaSourceId
  keyExpression: "r.uri:r.args.MediaSourceId", // "r.uri:r.args.MediaSourceId:r.args.X-Emby-Device-Id"
};

// for js_set
function getEmbyHost(r) {
  return embyHost;
}
function getTranscodeEnable(r) {
  return transcodeConfig.transcodeConfig.enable;
}
function getTranscodeType(r) {
  return transcodeConfig.transcodeConfig.type;
}
function getImageCachePolicy(r) {
  return extConfig.imageCachePolicy;
}

function getUsersItemsLatestFilterEnable(r) {
  return extConfig.itemHiddenRule.some(rule => !rule[2] || rule[2] == 0 || rule[2] == 4);
}

export default {
  embyHost,
  embyApiKey,
  mediaMountPath,
  strHead: commonConfig.strHead,

  alistAddr: mountConfig.alistAddr,
  alistToken: mountConfig.alistToken,
  alistSignEnable: mountConfig.alistSignEnable,
  alistSignExpireTime: mountConfig.alistSignExpireTime,
  alistPublicAddr: mountConfig.alistPublicAddr,
  clientSelfAlistRule: mountConfig.clientSelfAlistRule,
  redirectCheckEnable: mountConfig.redirectCheckEnable,
  fallbackUseOriginal: mountConfig.fallbackUseOriginal,

  redirectConfig: proConfig.redirectConfig,
  routeCacheConfig: routeCacheConfig,
  routeRule: routeRule,
  mediaPathMapping: proConfig.mediaPathMapping,
  alistRawUrlMapping: proConfig.alistRawUrlMapping,

  symlinkRule: symlinkConfig.symlinkRule,
  redirectStrmLastLinkRule: strmConfig.redirectStrmLastLinkRule,
  transcodeConfig: transcodeConfig.transcodeConfig,

  embyNotificationsAdmin: extConfig.embyNotificationsAdmin,
  embyRedirectSendMessage: extConfig.embyRedirectSendMessage,
  itemHiddenRule: extConfig.itemHiddenRule,
  streamConfig: extConfig.streamConfig,
  searchConfig: extConfig.searchConfig,
  webCookie115: extConfig.webCookie115,
  directHlsConfig: extConfig.directHlsConfig,
  playbackInfoConfig: extConfig.playbackInfoConfig,

  getEmbyHost,
  getTranscodeEnable,
  getTranscodeType,
  getImageCachePolicy,
  getUsersItemsLatestFilterEnable,

  nginxConfig: nginxConfig.nginxConfig,
  getDisableDocs: nginxConfig.getDisableDocs,
}
