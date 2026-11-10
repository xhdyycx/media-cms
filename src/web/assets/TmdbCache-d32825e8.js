import{_ as ix,d as F0,g as sx,c as Go,i as lx,o as Vr,a as No,n as W0,b as cx,e as kn,G as ux,a6 as dx,a7 as vx,r as pr,a8 as fx,t as V0,s as J0,V as bv,p as ko,a4 as px,f as hx,J as Ah,j as ro,k as gt,w as zt,q as Si,M as Tr,m as qn,L as zh,C as gx,X as mx,K as bx,x as Ci,D as Ph,y as qr,z as cu,F as Nh,A as Rh,a9 as Ih,a0 as qh}from"./index-d0306a7b.js";import{s as yx,t as Io,L as jx,a as xx,i as wx,P as Dh,f as H0,b as kx,V as Q0,Q as Sx,R as Cx,E as hs,T as ed,U as K0,W as G0,O as Ox,o as Y0,m as Hs,z as Lh,I as _x,X as Ex,l as Tx,h as Mx,c as $x,g as Ax,j as zx,k as Px,n as Nx,p as Rx,q as Ix,r as qx,u as Dx,v as Lx,w as Ux,x as Bx,y as Fx,A as Wx,B as Vx,C as Jx,F as Hx,G as Qx,H as Kx,Y as Gx,Z as Yx,_ as Uh,$ as Bh,a0 as yv,a1 as Xx,J as Zx,N as Xl,a2 as ew,a3 as tw,a4 as nw,a5 as rw,a6 as ow,a7 as aw,a8 as iw}from"./index-8f271c9f.js";import{L as sw}from"./index-b32fd830.js";const lw=F0({name:"IconDesktop",props:{size:{type:[Number,String]},strokeWidth:{type:Number,default:4},strokeLinecap:{type:String,default:"butt",validator:e=>["butt","round","square"].includes(e)},strokeLinejoin:{type:String,default:"miter",validator:e=>["arcs","bevel","miter","miter-clip","round"].includes(e)},rotate:Number,spin:Boolean},emits:{click:e=>!0},setup(e,{emit:t}){const n=sx("icon"),o=Go(()=>[n,`${n}-desktop`,{[`${n}-spin`]:e.spin}]),i=Go(()=>{const s={};return e.size&&(s.fontSize=lx(e.size)?`${e.size}px`:e.size),e.rotate&&(s.transform=`rotate(${e.rotate}deg)`),s});return{cls:o,innerStyle:i,onClick:s=>{t("click",s)}}}}),cw=["stroke-width","stroke-linecap","stroke-linejoin"],uw=kn("path",{d:"M24 32v8m0 0h-9m9 0h9M7 32h34a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1v22a1 1 0 0 0 1 1Z"},null,-1),dw=[uw];function vw(e,t,n,o,i,a){return Vr(),No("svg",{viewBox:"0 0 48 48",fill:"none",xmlns:"http://www.w3.org/2000/svg",stroke:"currentColor",class:W0(e.cls),style:cx(e.innerStyle),"stroke-width":e.strokeWidth,"stroke-linecap":e.strokeLinecap,"stroke-linejoin":e.strokeLinejoin,onClick:t[0]||(t[0]=(...s)=>e.onClick&&e.onClick(...s))},dw,14,cw)}var jv=ix(lw,[["render",vw]]);const Fh=Object.assign(jv,{install:(e,t)=>{var n;const o=(n=t==null?void 0:t.iconPrefix)!=null?n:"";e.component(o+jv.name,jv)}});function Cr(e){return Array.isArray(e)}function $r(e){return e!==null&&typeof e=="object"&&(e.constructor===void 0||e.constructor.name==="Object")}function X0(e){return e&&typeof e=="object"?e.op==="add":!1}function Z0(e){return e&&typeof e=="object"?e.op==="remove":!1}function gp(e){return e&&typeof e=="object"?e.op==="replace":!1}function lf(e){return e&&typeof e=="object"?e.op==="copy":!1}function ks(e){return e&&typeof e=="object"?e.op==="move":!1}function fw(e,t){return JSON.stringify(e)===JSON.stringify(t)}function pw(e,t){return e===t}function e1(e){return e.slice(0,e.length-1)}function hw(e){return e[e.length-1]}function gw(e,t){let n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:pw;if(e.length<t.length)return!1;for(let o=0;o<t.length;o++)if(!n(e[o],t[o]))return!1;return!0}function t1(e){return typeof e=="object"&&e!==null}function mp(e){if(Cr(e)){const t=e.slice();return Object.getOwnPropertySymbols(e).forEach(n=>{t[n]=e[n]}),t}if($r(e)){const t={...e};return Object.getOwnPropertySymbols(e).forEach(n=>{t[n]=e[n]}),t}return e}function bp(e,t,n){if(e[t]===n)return e;const o=mp(e);return o[t]=n,o}function tt(e,t){let n=e,o=0;for(;o<t.length;)$r(n)?n=n[t[o]]:Cr(n)?n=n[Number.parseInt(t[o])]:n=void 0,o++;return n}function Co(e,t,n){let o=arguments.length>3&&arguments[3]!==void 0?arguments[3]:!1;if(t.length===0)return n;const i=t[0],a=Co(e?e[i]:void 0,t.slice(1),n,o);if($r(e)||Cr(e))return bp(e,i,a);if(o){const s=mw.test(i)?[]:{};return s[i]=a,s}throw new Error("Path does not exist")}const mw=/^\d+$/;function yp(e,t,n){if(t.length===0)return n(e);if(!t1(e))throw new Error("Path doesn't exist");const o=t[0],i=yp(e[o],t.slice(1),n);return bp(e,o,i)}function Pd(e,t){if(t.length===0)return e;if(!t1(e))throw new Error("Path does not exist");if(t.length===1){const i=t[0];if(!(i in e))return e;const a=mp(e);return Cr(a)&&a.splice(Number.parseInt(i),1),$r(a)&&delete a[i],a}const n=t[0],o=Pd(e[n],t.slice(1));return bp(e,n,o)}function jp(e,t,n){const o=t.slice(0,t.length-1),i=t[t.length-1];return yp(e,o,a=>{if(!Array.isArray(a))throw new TypeError(`Array expected at path ${JSON.stringify(o)}`);const s=mp(a);return s.splice(Number.parseInt(i),0,n),s})}function To(e,t){return e===void 0?!1:t.length===0?!0:e===null?!1:To(e[t[0]],t.slice(1))}function Mo(e){const t=e.split("/");return t.shift(),t.map(n=>n.replace(/~1/g,"/").replace(/~0/g,"~"))}function wt(e){return e.map(n1).join("")}function n1(e){return`/${String(e).replace(/~/g,"~0").replace(/\//g,"~1")}`}function uu(e,t){return e+n1(t)}function ga(e,t,n){let o=e;for(let i=0;i<t.length;i++){Cw(t[i]);let a=t[i];if(n!=null&&n.before){const c=n.before(o,a);if(c!==void 0){if(c.document!==void 0&&(o=c.document),c.json!==void 0)throw new Error('Deprecation warning: returned object property ".json" has been renamed to ".document"');c.operation!==void 0&&(a=c.operation)}}const s=o,l=ma(o,a.path);if(a.op==="add")o=jw(o,l,a.value);else if(a.op==="remove")o=yw(o,l);else if(a.op==="replace")o=bw(o,l,a.value);else if(a.op==="copy")o=xw(o,l,cf(a.from));else if(a.op==="move")o=ww(o,l,cf(a.from));else if(a.op==="test")kw(o,l,a.value);else throw new Error(`Unknown JSONPatch operation ${JSON.stringify(a)}`);if(n!=null&&n.after){const c=n.after(o,a,s);c!==void 0&&(o=c)}}return o}function bw(e,t,n){return To(e,t)?Co(e,t,n):e}function yw(e,t){return Pd(e,t)}function jw(e,t,n){return Vc(e,t)?jp(e,t,n):Co(e,t,n)}function xw(e,t,n){const o=tt(e,n);return Vc(e,t)?jp(e,t,o):Co(e,t,o)}function ww(e,t,n){const o=tt(e,n),i=Pd(e,n);return Vc(i,t)?jp(i,t,o):Co(i,t,o)}function kw(e,t,n){if(n===void 0)throw new Error(`Test failed: no value provided (path: "${wt(t)}")`);if(!To(e,t))throw new Error(`Test failed: path not found (path: "${wt(t)}")`);const o=tt(e,t);if(!fw(o,n))throw new Error(`Test failed, value differs (path: "${wt(t)}")`)}function Vc(e,t){if(t.length===0)return!1;const n=tt(e,e1(t));return Array.isArray(n)}function Sw(e,t){if(hw(t)!=="-")return t;const n=e1(t),o=tt(e,n);return n.concat(o.length)}function Cw(e){if(!["add","remove","replace","copy","move","test"].includes(e.op))throw new Error(`Unknown JSONPatch op ${JSON.stringify(e.op)}`);if(typeof e.path!="string")throw new Error(`Required property "path" missing or not a string in operation ${JSON.stringify(e)}`);if((e.op==="copy"||e.op==="move")&&typeof e.from!="string")throw new Error(`Required property "from" missing or not a string in operation ${JSON.stringify(e)}`)}function ma(e,t){return Sw(e,Mo(t))}function cf(e){return Mo(e)}function r1(e,t,n){let o=[];return ga(e,t,{before:(a,s)=>{let l;const c=ma(a,s.path);if(s.op==="add")l=i1(a,c);else if(s.op==="remove")l=a1(a,c);else if(s.op==="replace")l=o1(a,c);else if(s.op==="copy")l=Ow(a,c);else if(s.op==="move")l=_w(a,c,cf(s.from));else if(s.op==="test")l=[];else throw new Error(`Unknown JSONPatch operation ${JSON.stringify(s)}`);let u;if(n!=null&&n.before){const d=n.before(a,s,l);if(d!=null&&d.revertOperations&&(l=d.revertOperations),d!=null&&d.document&&(u=d.document),d!=null&&d.json)throw new Error('Deprecation warning: returned object property ".json" has been renamed to ".document"')}if(o=l.concat(o),u!==void 0)return{document:u}}}),o}function o1(e,t){return To(e,t)?[{op:"replace",path:wt(t),value:tt(e,t)}]:[]}function a1(e,t){return[{op:"add",path:wt(t),value:tt(e,t)}]}function i1(e,t){return Vc(e,t)||!To(e,t)?[{op:"remove",path:wt(t)}]:o1(e,t)}function Ow(e,t){return i1(e,t)}function _w(e,t,n){if(t.length<n.length&&gw(n,t))return[{op:"replace",path:wt(t),value:e}];const o={op:"move",from:wt(t),path:wt(n)};return!Vc(e,t)&&To(e,t)?[o,...a1(e,t)]:[o]}var Nd={},Wh={b:"\b",f:"\f",n:`
`,r:"\r",t:"	",'"':'"',"/":"/","\\":"\\"},Ew="a".charCodeAt();Nd.parse=function(e,t,n){var o={},i=0,a=0,s=0,l=n&&n.bigint&&typeof BigInt<"u";return{data:c("",!0),pointers:o};function c(C,z){u();var D;E(C,"value");var H=y();switch(H){case"t":p("rue"),D=!0;break;case"f":p("alse"),D=!1;break;case"n":p("ull"),D=null;break;case'"':D=d();break;case"[":D=f(C);break;case"{":D=h(C);break;default:j(),"-0123456789".indexOf(H)>=0?D=v():_()}return E(C,"valueEnd"),u(),z&&s<e.length&&_(),D}function u(){e:for(;s<e.length;){switch(e[s]){case" ":a++;break;case"	":a+=4;break;case"\r":a=0;break;case`
`:a=0,i++;break;default:break e}s++}}function d(){for(var C="",z;z=y(),z!='"';)z=="\\"?(z=y(),z in Wh?C+=Wh[z]:z=="u"?C+=b():A()):C+=z;return C}function v(){var C="",z=!0;e[s]=="-"&&(C+=y()),C+=e[s]=="0"?y():k(),e[s]=="."&&(C+=y()+k(),z=!1),(e[s]=="e"||e[s]=="E")&&(C+=y(),(e[s]=="+"||e[s]=="-")&&(C+=y()),C+=k(),z=!1);var D=+C;return l&&z&&(D>Number.MAX_SAFE_INTEGER||D<Number.MIN_SAFE_INTEGER)?BigInt(C):D}function f(C){u();var z=[],D=0;if(y()=="]")return z;for(j();;){var H=C+"/"+D;z.push(c(H)),u();var Q=y();if(Q=="]")break;Q!=","&&A(),u(),D++}return z}function h(C){u();var z={};if(y()=="}")return z;for(j();;){var D=w();y()!='"'&&A();var H=d(),Q=C+"/"+uf(H);O(Q,"key",D),E(Q,"keyEnd"),u(),y()!=":"&&A(),u(),z[H]=c(Q),u();var fe=y();if(fe=="}")break;fe!=","&&A(),u()}return z}function p(C){for(var z=0;z<C.length;z++)y()!==C[z]&&A()}function y(){q();var C=e[s];return s++,a++,C}function j(){s--,a--}function b(){for(var C=4,z=0;C--;){z<<=4;var D=y().toLowerCase();D>="a"&&D<="f"?z+=D.charCodeAt()-Ew+10:D>="0"&&D<="9"?z+=+D:A()}return String.fromCharCode(z)}function k(){for(var C="";e[s]>="0"&&e[s]<="9";)C+=y();if(C.length)return C;q(),_()}function E(C,z){O(C,z,w())}function O(C,z,D){o[C]=o[C]||{},o[C][z]=D}function w(){return{line:i,column:a,pos:s}}function _(){throw new SyntaxError("Unexpected token "+e[s]+" in JSON at position "+s)}function A(){j(),_()}function q(){if(s>=e.length)throw new SyntaxError("Unexpected end of JSON input")}};Nd.stringify=function(e,t,n){if(!du(e))return;var o=0,i,a,s=typeof n=="object"?n.space:n;switch(typeof s){case"number":var l=s>10?10:s<0?0:Math.floor(s);s=l&&O(l," "),i=l,a=l;break;case"string":s=s.slice(0,10),i=0,a=0;for(var c=0;c<s.length;c++){var u=s[c];switch(u){case" ":a++;break;case"	":a+=4;break;case"\r":a=0;break;case`
`:a=0,o++;break;default:throw new Error("whitespace characters not allowed in JSON")}i++}break;default:s=void 0}var d="",v={},f=0,h=0,p=0,y=n&&n.es6&&typeof Map=="function";return j(e,0,""),{json:d,pointers:v};function j(w,_,A){switch(E(A,"value"),typeof w){case"number":case"bigint":case"boolean":b(""+w);break;case"string":b(vu(w));break;case"object":w===null?b("null"):typeof w.toJSON=="function"?b(vu(w.toJSON())):Array.isArray(w)?q():y?w.constructor.BYTES_PER_ELEMENT?q():w instanceof Map?z():w instanceof Set?z(!0):C():C()}E(A,"valueEnd");function q(){if(w.length){b("[");for(var D=_+1,H=0;H<w.length;H++){H&&b(","),k(D);var Q=du(w[H])?w[H]:null,fe=A+"/"+H;j(Q,D,fe)}k(_),b("]")}else b("[]")}function C(){var D=Object.keys(w);if(D.length){b("{");for(var H=_+1,Q=0;Q<D.length;Q++){var fe=D[Q],Ie=w[fe];if(du(Ie)){Q&&b(",");var ge=A+"/"+uf(fe);k(H),E(ge,"key"),b(vu(fe)),E(ge,"keyEnd"),b(":"),s&&b(" "),j(Ie,H,ge)}}k(_),b("}")}else b("{}")}function z(D){if(w.size){b("{");for(var H=_+1,Q=!0,fe=w.entries(),Ie=fe.next();!Ie.done;){var ge=Ie.value,qe=ge[0],ce=D?!0:ge[1];if(du(ce)){Q||b(","),Q=!1;var ve=A+"/"+uf(qe);k(H),E(ve,"key"),b(vu(qe)),E(ve,"keyEnd"),b(":"),s&&b(" "),j(ce,H,ve)}Ie=fe.next()}k(_),b("}")}else b("{}")}}function b(w){h+=w.length,p+=w.length,d+=w}function k(w){if(s){for(d+=`
`+O(w,s),f++,h=0;w--;)o?(f+=o,h=a):h+=a,p+=i;p+=1}}function E(w,_){v[w]=v[w]||{},v[w][_]={line:f,column:h,pos:p}}function O(w,_){return Array(w+1).join(_)}};var Tw=["number","bigint","boolean","string","object"];function du(e){return Tw.indexOf(typeof e)>=0}var Mw=/"|\\/g,$w=/[\b]/g,Aw=/\f/g,zw=/\n/g,Pw=/\r/g,Nw=/\t/g;function vu(e){return e=e.replace(Mw,"\\$&").replace(Aw,"\\f").replace($w,"\\b").replace(zw,"\\n").replace(Pw,"\\r").replace(Nw,"\\t"),'"'+e+'"'}var Rw=/~/g,Iw=/\//g;function uf(e){return e.replace(Rw,"~0").replace(Iw,"~1")}class Qs extends Error{constructor(t,n){super(`${t} at position ${n}`),this.position=n}}const s1=32,qw=10,l1=9,c1=13,Dw=160,Lw=6158,Uw=8192,Bw=8203,Fw=8239,Ww=8287,Vw=12288,Jw=65279;function Hw(e){return/^[0-9A-Fa-f]$/.test(e)}function cs(e){return e>="0"&&e<="9"}function Qw(e){return e>=" "}function fu(e){return`,:[]/{}()
+`.includes(e)}function Vh(e){return e>="a"&&e<="z"||e>="A"&&e<="Z"||e==="_"||e==="$"}function Jh(e){return e>="a"&&e<="z"||e>="A"&&e<="Z"||e==="_"||e==="$"||e>="0"&&e<="9"}const Hh=/^(http|https|ftp|mailto|file|data|irc):\/\/$/,Qh=/^[A-Za-z0-9-._~:/?#@!$&'()*+;=]$/;function Kh(e){return`,[]/{}
+`.includes(e)}function Gh(e){return Lu(e)||Kw.test(e)}const Kw=/^[[{\w-]$/;function Gw(e){return e===`
`||e==="\r"||e==="	"||e==="\b"||e==="\f"}function bs(e,t){const n=e.charCodeAt(t);return n===s1||n===qw||n===l1||n===c1}function Yw(e,t){const n=e.charCodeAt(t);return n===s1||n===l1||n===c1}function Xw(e,t){const n=e.charCodeAt(t);return n===Dw||n===Lw||n>=Uw&&n<=Bw||n===Fw||n===Ww||n===Vw||n===Jw}function Lu(e){return u1(e)||df(e)}function u1(e){return e==='"'||e==="“"||e==="”"}function Yh(e){return e==='"'}function df(e){return e==="'"||e==="‘"||e==="’"||e==="`"||e==="´"}function Xh(e){return e==="'"}function Zl(e,t){let n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:!1;const o=e.lastIndexOf(t);return o!==-1?e.substring(0,o)+(n?"":e.substring(o+1)):e}function sa(e,t){let n=e.length;if(!bs(e,n-1))return e+t;for(;bs(e,n-1);)n--;return e.substring(0,n)+t+e.substring(n)}function Zw(e,t,n){return e.substring(0,t)+e.substring(t+n)}function e2(e){return/[,\n][ \t\r]*$/.test(e)}const t2={"\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","	":"\\t"},n2={'"':'"',"\\":"\\","/":"/",b:"\b",f:"\f",n:`
`,r:"\r",t:"	"};function Aa(e){let t=0,n="";u(["```","[```","{```"]),a()||fe(),u(["```","```]","```}"]);const i=v(",");for(i&&s(),Gh(e[t])&&e2(n)?(i||(n=sa(n,",")),b()):i&&(n=Zl(n,","));e[t]==="}"||e[t]==="]";)t++,s();if(t>=e.length)return n;Q();function a(){s();const ce=y()||j()||k()||O()||w()||A(!1)||q();return s(),ce}function s(){let ce=arguments.length>0&&arguments[0]!==void 0?arguments[0]:!0;const ve=t;let he=l(ce);do he=c(),he&&(he=l(ce));while(he);return t>ve}function l(ce){const ve=ce?bs:Yw;let he="";for(;;)if(ve(e,t))he+=e[t],t++;else if(Xw(e,t))he+=" ",t++;else break;return he.length>0?(n+=he,!0):!1}function c(){if(e[t]==="/"&&e[t+1]==="*"){for(;t<e.length&&!r2(e,t);)t++;return t+=2,!0}if(e[t]==="/"&&e[t+1]==="/"){for(;t<e.length&&e[t]!==`
`;)t++;return!0}return!1}function u(ce){if(d(ce)){if(Vh(e[t]))for(;t<e.length&&Jh(e[t]);)t++;return s(),!0}return!1}function d(ce){l(!0);for(const ve of ce){const he=t+ve.length;if(e.slice(t,he)===ve)return t=he,!0}return!1}function v(ce){return e[t]===ce?(n+=e[t],t++,!0):!1}function f(ce){return e[t]===ce?(t++,!0):!1}function h(){return f("\\")}function p(){return s(),e[t]==="."&&e[t+1]==="."&&e[t+2]==="."?(t+=3,s(),f(","),!0):!1}function y(){if(e[t]==="{"){n+="{",t++,s(),f(",")&&s();let ce=!0;for(;t<e.length&&e[t]!=="}";){let ve;if(ce?(ve=!0,ce=!1):(ve=v(","),ve||(n=sa(n,",")),s()),p(),!(k()||A(!0))){e[t]==="}"||e[t]==="{"||e[t]==="]"||e[t]==="["||e[t]===void 0?n=Zl(n,","):Ie();break}s();const Ue=v(":"),Re=t>=e.length;Ue||(Gh(e[t])||Re?n=sa(n,":"):ge()),a()||(Ue||Re?n+="null":ge())}return e[t]==="}"?(n+="}",t++):n=sa(n,"}"),!0}return!1}function j(){if(e[t]==="["){n+="[",t++,s(),f(",")&&s();let ce=!0;for(;t<e.length&&e[t]!=="]";)if(ce?ce=!1:v(",")||(n=sa(n,",")),p(),!a()){n=Zl(n,",");break}return e[t]==="]"?(n+="]",t++):n=sa(n,"]"),!0}return!1}function b(){let ce=!0,ve=!0;for(;ve;)ce?ce=!1:v(",")||(n=sa(n,",")),ve=a();ve||(n=Zl(n,",")),n=`[
${n}
]`}function k(){let ce=arguments.length>0&&arguments[0]!==void 0?arguments[0]:!1,ve=arguments.length>1&&arguments[1]!==void 0?arguments[1]:-1,he=e[t]==="\\";if(he&&(t++,he=!0),Lu(e[t])){const Ue=Yh(e[t])?Yh:Xh(e[t])?Xh:df(e[t])?df:u1,Re=t,we=n.length;let ue='"';for(t++;;){if(t>=e.length){const ie=C(t-1);return!ce&&fu(e.charAt(ie))?(t=Re,n=n.substring(0,we),k(!0)):(ue=sa(ue,'"'),n+=ue,!0)}if(t===ve)return ue=sa(ue,'"'),n+=ue,!0;if(Ue(e[t])){const ie=t,vt=ue.length;if(ue+='"',t++,n+=ue,s(!1),ce||t>=e.length||fu(e[t])||Lu(e[t])||cs(e[t]))return E(),!0;const ft=C(ie-1),kt=e.charAt(ft);if(kt===",")return t=Re,n=n.substring(0,we),k(!1,ft);if(fu(kt))return t=Re,n=n.substring(0,we),k(!0);n=n.substring(0,we),t=ie+1,ue=`${ue.substring(0,vt)}\\${ue.substring(vt)}`}else if(ce&&Kh(e[t])){if(e[t-1]===":"&&Hh.test(e.substring(Re+1,t+2)))for(;t<e.length&&Qh.test(e[t]);)ue+=e[t],t++;return ue=sa(ue,'"'),n+=ue,E(),!0}else if(e[t]==="\\"){const ie=e.charAt(t+1);if(n2[ie]!==void 0)ue+=e.slice(t,t+2),t+=2;else if(ie==="u"){let ft=2;for(;ft<6&&Hw(e[t+ft]);)ft++;ft===6?(ue+=e.slice(t,t+6),t+=6):t+ft>=e.length?t=e.length:qe()}else ie===`
`?(ue+="\\n",t+=2):(ue+=ie,t+=2)}else{const ie=e.charAt(t);ie==='"'&&e[t-1]!=="\\"?(ue+=`\\${ie}`,t++):Gw(ie)?(ue+=t2[ie],t++):(Qw(ie)||H(ie),ue+=ie,t++)}he&&h()}}return!1}function E(){let ce=!1;for(s();e[t]==="+";){ce=!0,t++,s(),n=Zl(n,'"',!0);const ve=n.length;k()?n=Zw(n,ve,1):n=sa(n,'"')}return ce}function O(){const ce=t;if(e[t]==="-"){if(t++,z())return D(ce),!0;if(!cs(e[t]))return t=ce,!1}for(;cs(e[t]);)t++;if(e[t]==="."){if(t++,z())return D(ce),!0;if(!cs(e[t]))return t=ce,!1;for(;cs(e[t]);)t++}if(e[t]==="e"||e[t]==="E"){if(t++,(e[t]==="-"||e[t]==="+")&&t++,z())return D(ce),!0;if(!cs(e[t]))return t=ce,!1;for(;cs(e[t]);)t++}if(!z())return t=ce,!1;if(t>ce){const ve=e.slice(ce,t),he=/^0\d/.test(ve);return n+=he?`"${ve}"`:ve,!0}return!1}function w(){return _("true","true")||_("false","false")||_("null","null")||_("True","true")||_("False","false")||_("None","null")}function _(ce,ve){return e.slice(t,t+ce.length)===ce?(n+=ve,t+=ce.length,!0):!1}function A(ce){const ve=t;if(Vh(e[t])){for(;t<e.length&&Jh(e[t]);)t++;let he=t;for(;bs(e,he);)he++;if(e[he]==="(")return t=he+1,a(),e[t]===")"&&(t++,e[t]===";"&&t++),!0}for(;t<e.length&&!Kh(e[t])&&!Lu(e[t])&&(!ce||e[t]!==":");)t++;if(e[t-1]===":"&&Hh.test(e.substring(ve,t+2)))for(;t<e.length&&Qh.test(e[t]);)t++;if(t>ve){for(;bs(e,t-1)&&t>0;)t--;const he=e.slice(ve,t);return n+=he==="undefined"?"null":JSON.stringify(he),e[t]==='"'&&t++,!0}}function q(){if(e[t]==="/"){const ce=t;for(t++;t<e.length&&(e[t]!=="/"||e[t-1]==="\\");)t++;return t++,n+=JSON.stringify(e.substring(ce,t)),!0}}function C(ce){let ve=ce;for(;ve>0&&bs(e,ve);)ve--;return ve}function z(){return t>=e.length||fu(e[t])||bs(e,t)}function D(ce){n+=`${e.slice(ce,t)}0`}function H(ce){throw new Qs(`Invalid character ${JSON.stringify(ce)}`,t)}function Q(){throw new Qs(`Unexpected character ${JSON.stringify(e[t])}`,t)}function fe(){throw new Qs("Unexpected end of json string",e.length)}function Ie(){throw new Qs("Object key expected",t)}function ge(){throw new Qs("Colon expected",t)}function qe(){const ce=e.slice(t,t+6);throw new Qs(`Invalid unicode character "${ce}"`,t)}}function r2(e,t){return e[t]==="*"&&e[t+1]==="/"}var o2=typeof global=="object"&&global&&global.Object===Object&&global;const d1=o2;var a2=typeof self=="object"&&self&&self.Object===Object&&self,i2=d1||a2||Function("return this")();const Sa=i2;var s2=Sa.Symbol;const ta=s2;var v1=Object.prototype,l2=v1.hasOwnProperty,c2=v1.toString,ec=ta?ta.toStringTag:void 0;function u2(e){var t=l2.call(e,ec),n=e[ec];try{e[ec]=void 0;var o=!0}catch{}var i=c2.call(e);return o&&(t?e[ec]=n:delete e[ec]),i}var d2=Object.prototype,v2=d2.toString;function f2(e){return v2.call(e)}var p2="[object Null]",h2="[object Undefined]",Zh=ta?ta.toStringTag:void 0;function ql(e){return e==null?e===void 0?h2:p2:Zh&&Zh in Object(e)?u2(e):f2(e)}function Gi(e){return e!=null&&typeof e=="object"}var g2="[object Symbol]";function Ts(e){return typeof e=="symbol"||Gi(e)&&ql(e)==g2}function pc(e,t){for(var n=-1,o=e==null?0:e.length,i=Array(o);++n<o;)i[n]=t(e[n],n,e);return i}var m2=Array.isArray;const mo=m2;var b2=1/0,eg=ta?ta.prototype:void 0,tg=eg?eg.toString:void 0;function f1(e){if(typeof e=="string")return e;if(mo(e))return pc(e,f1)+"";if(Ts(e))return tg?tg.call(e):"";var t=e+"";return t=="0"&&1/e==-b2?"-0":t}var y2=/\s/;function j2(e){for(var t=e.length;t--&&y2.test(e.charAt(t)););return t}var x2=/^\s+/;function w2(e){return e&&e.slice(0,j2(e)+1).replace(x2,"")}function Da(e){var t=typeof e;return e!=null&&(t=="object"||t=="function")}var ng=0/0,k2=/^[-+]0x[0-9a-f]+$/i,S2=/^0b[01]+$/i,C2=/^0o[0-7]+$/i,O2=parseInt;function vf(e){if(typeof e=="number")return e;if(Ts(e))return ng;if(Da(e)){var t=typeof e.valueOf=="function"?e.valueOf():e;e=Da(t)?t+"":t}if(typeof e!="string")return e===0?e:+e;e=w2(e);var n=S2.test(e);return n||C2.test(e)?O2(e.slice(2),n?2:8):k2.test(e)?ng:+e}var rg=1/0,_2=17976931348623157e292;function Uu(e){if(!e)return e===0?e:0;if(e=vf(e),e===rg||e===-rg){var t=e<0?-1:1;return t*_2}return e===e?e:0}function E2(e){var t=Uu(e),n=t%1;return t===t?n?t-n:t:0}function Jc(e){return e}var T2="[object AsyncFunction]",M2="[object Function]",$2="[object GeneratorFunction]",A2="[object Proxy]";function p1(e){if(!Da(e))return!1;var t=ql(e);return t==M2||t==$2||t==T2||t==A2}var z2=Sa["__core-js_shared__"];const xv=z2;var og=function(){var e=/[^.]+$/.exec(xv&&xv.keys&&xv.keys.IE_PROTO||"");return e?"Symbol(src)_1."+e:""}();function P2(e){return!!og&&og in e}var N2=Function.prototype,R2=N2.toString;function Ls(e){if(e!=null){try{return R2.call(e)}catch{}try{return e+""}catch{}}return""}var I2=/[\\^$.*+?()[\]{}|]/g,q2=/^\[object .+?Constructor\]$/,D2=Function.prototype,L2=Object.prototype,U2=D2.toString,B2=L2.hasOwnProperty,F2=RegExp("^"+U2.call(B2).replace(I2,"\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g,"$1.*?")+"$");function W2(e){if(!Da(e)||P2(e))return!1;var t=p1(e)?F2:q2;return t.test(Ls(e))}function V2(e,t){return e==null?void 0:e[t]}function Us(e,t){var n=V2(e,t);return W2(n)?n:void 0}var J2=Us(Sa,"WeakMap");const ff=J2;var ag=Object.create,H2=function(){function e(){}return function(t){if(!Da(t))return{};if(ag)return ag(t);e.prototype=t;var n=new e;return e.prototype=void 0,n}}();const Q2=H2;function K2(e,t,n){switch(n.length){case 0:return e.call(t);case 1:return e.call(t,n[0]);case 2:return e.call(t,n[0],n[1]);case 3:return e.call(t,n[0],n[1],n[2])}return e.apply(t,n)}function Dr(){}function G2(e,t){var n=-1,o=e.length;for(t||(t=Array(o));++n<o;)t[n]=e[n];return t}var Y2=800,X2=16,Z2=Date.now;function e4(e){var t=0,n=0;return function(){var o=Z2(),i=X2-(o-n);if(n=o,i>0){if(++t>=Y2)return arguments[0]}else t=0;return e.apply(void 0,arguments)}}function t4(e){return function(){return e}}var n4=function(){try{var e=Us(Object,"defineProperty");return e({},"",{}),e}catch{}}();const td=n4;var r4=td?function(e,t){return td(e,"toString",{configurable:!0,enumerable:!1,value:t4(t),writable:!0})}:Jc;const o4=r4;var a4=e4(o4);const i4=a4;function s4(e,t){for(var n=-1,o=e==null?0:e.length;++n<o&&t(e[n],n,e)!==!1;);return e}var l4=9007199254740991,c4=/^(?:0|[1-9]\d*)$/;function xp(e,t){var n=typeof e;return t=t??l4,!!t&&(n=="number"||n!="symbol"&&c4.test(e))&&e>-1&&e%1==0&&e<t}function Rd(e,t,n){t=="__proto__"&&td?td(e,t,{configurable:!0,enumerable:!0,value:n,writable:!0}):e[t]=n}function Id(e,t){return e===t||e!==e&&t!==t}var u4=Object.prototype,d4=u4.hasOwnProperty;function h1(e,t,n){var o=e[t];(!(d4.call(e,t)&&Id(o,n))||n===void 0&&!(t in e))&&Rd(e,t,n)}function qd(e,t,n,o){var i=!n;n||(n={});for(var a=-1,s=t.length;++a<s;){var l=t[a],c=o?o(n[l],e[l],l,n,e):void 0;c===void 0&&(c=e[l]),i?Rd(n,l,c):h1(n,l,c)}return n}var ig=Math.max;function v4(e,t,n){return t=ig(t===void 0?e.length-1:t,0),function(){for(var o=arguments,i=-1,a=ig(o.length-t,0),s=Array(a);++i<a;)s[i]=o[t+i];i=-1;for(var l=Array(t+1);++i<t;)l[i]=o[i];return l[t]=n(s),K2(e,this,l)}}function f4(e,t){return i4(v4(e,t,Jc),e+"")}var p4=9007199254740991;function wp(e){return typeof e=="number"&&e>-1&&e%1==0&&e<=p4}function Dl(e){return e!=null&&wp(e.length)&&!p1(e)}function pf(e,t,n){if(!Da(n))return!1;var o=typeof t;return(o=="number"?Dl(n)&&xp(t,n.length):o=="string"&&t in n)?Id(n[t],e):!1}var h4=Object.prototype;function Dd(e){var t=e&&e.constructor,n=typeof t=="function"&&t.prototype||h4;return e===n}function g1(e,t){for(var n=-1,o=Array(e);++n<e;)o[n]=t(n);return o}var g4="[object Arguments]";function sg(e){return Gi(e)&&ql(e)==g4}var m1=Object.prototype,m4=m1.hasOwnProperty,b4=m1.propertyIsEnumerable,y4=sg(function(){return arguments}())?sg:function(e){return Gi(e)&&m4.call(e,"callee")&&!b4.call(e,"callee")};const Ld=y4;function j4(){return!1}var b1=typeof exports=="object"&&exports&&!exports.nodeType&&exports,lg=b1&&typeof module=="object"&&module&&!module.nodeType&&module,x4=lg&&lg.exports===b1,cg=x4?Sa.Buffer:void 0,w4=cg?cg.isBuffer:void 0,k4=w4||j4;const Sc=k4;var S4="[object Arguments]",C4="[object Array]",O4="[object Boolean]",_4="[object Date]",E4="[object Error]",T4="[object Function]",M4="[object Map]",$4="[object Number]",A4="[object Object]",z4="[object RegExp]",P4="[object Set]",N4="[object String]",R4="[object WeakMap]",I4="[object ArrayBuffer]",q4="[object DataView]",D4="[object Float32Array]",L4="[object Float64Array]",U4="[object Int8Array]",B4="[object Int16Array]",F4="[object Int32Array]",W4="[object Uint8Array]",V4="[object Uint8ClampedArray]",J4="[object Uint16Array]",H4="[object Uint32Array]",wr={};wr[D4]=wr[L4]=wr[U4]=wr[B4]=wr[F4]=wr[W4]=wr[V4]=wr[J4]=wr[H4]=!0;wr[S4]=wr[C4]=wr[I4]=wr[O4]=wr[q4]=wr[_4]=wr[E4]=wr[T4]=wr[M4]=wr[$4]=wr[A4]=wr[z4]=wr[P4]=wr[N4]=wr[R4]=!1;function Q4(e){return Gi(e)&&wp(e.length)&&!!wr[ql(e)]}function Ud(e){return function(t){return e(t)}}var y1=typeof exports=="object"&&exports&&!exports.nodeType&&exports,hc=y1&&typeof module=="object"&&module&&!module.nodeType&&module,K4=hc&&hc.exports===y1,wv=K4&&d1.process,G4=function(){try{var e=hc&&hc.require&&hc.require("util").types;return e||wv&&wv.binding&&wv.binding("util")}catch{}}();const wl=G4;var ug=wl&&wl.isTypedArray,Y4=ug?Ud(ug):Q4;const kp=Y4;var X4=Object.prototype,Z4=X4.hasOwnProperty;function j1(e,t){var n=mo(e),o=!n&&Ld(e),i=!n&&!o&&Sc(e),a=!n&&!o&&!i&&kp(e),s=n||o||i||a,l=s?g1(e.length,String):[],c=l.length;for(var u in e)(t||Z4.call(e,u))&&!(s&&(u=="length"||i&&(u=="offset"||u=="parent")||a&&(u=="buffer"||u=="byteLength"||u=="byteOffset")||xp(u,c)))&&l.push(u);return l}function x1(e,t){return function(n){return e(t(n))}}var e3=x1(Object.keys,Object);const t3=e3;var n3=Object.prototype,r3=n3.hasOwnProperty;function w1(e){if(!Dd(e))return t3(e);var t=[];for(var n in Object(e))r3.call(e,n)&&n!="constructor"&&t.push(n);return t}function Ll(e){return Dl(e)?j1(e):w1(e)}function o3(e){var t=[];if(e!=null)for(var n in Object(e))t.push(n);return t}var a3=Object.prototype,i3=a3.hasOwnProperty;function s3(e){if(!Da(e))return o3(e);var t=Dd(e),n=[];for(var o in e)o=="constructor"&&(t||!i3.call(e,o))||n.push(o);return n}function Sp(e){return Dl(e)?j1(e,!0):s3(e)}var l3=/\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/,c3=/^\w*$/;function Cp(e,t){if(mo(e))return!1;var n=typeof e;return n=="number"||n=="symbol"||n=="boolean"||e==null||Ts(e)?!0:c3.test(e)||!l3.test(e)||t!=null&&e in Object(t)}var u3=Us(Object,"create");const Cc=u3;function d3(){this.__data__=Cc?Cc(null):{},this.size=0}function v3(e){var t=this.has(e)&&delete this.__data__[e];return this.size-=t?1:0,t}var f3="__lodash_hash_undefined__",p3=Object.prototype,h3=p3.hasOwnProperty;function g3(e){var t=this.__data__;if(Cc){var n=t[e];return n===f3?void 0:n}return h3.call(t,e)?t[e]:void 0}var m3=Object.prototype,b3=m3.hasOwnProperty;function y3(e){var t=this.__data__;return Cc?t[e]!==void 0:b3.call(t,e)}var j3="__lodash_hash_undefined__";function x3(e,t){var n=this.__data__;return this.size+=this.has(e)?0:1,n[e]=Cc&&t===void 0?j3:t,this}function Ms(e){var t=-1,n=e==null?0:e.length;for(this.clear();++t<n;){var o=e[t];this.set(o[0],o[1])}}Ms.prototype.clear=d3;Ms.prototype.delete=v3;Ms.prototype.get=g3;Ms.prototype.has=y3;Ms.prototype.set=x3;function w3(){this.__data__=[],this.size=0}function Bd(e,t){for(var n=e.length;n--;)if(Id(e[n][0],t))return n;return-1}var k3=Array.prototype,S3=k3.splice;function C3(e){var t=this.__data__,n=Bd(t,e);if(n<0)return!1;var o=t.length-1;return n==o?t.pop():S3.call(t,n,1),--this.size,!0}function O3(e){var t=this.__data__,n=Bd(t,e);return n<0?void 0:t[n][1]}function _3(e){return Bd(this.__data__,e)>-1}function E3(e,t){var n=this.__data__,o=Bd(n,e);return o<0?(++this.size,n.push([e,t])):n[o][1]=t,this}function yi(e){var t=-1,n=e==null?0:e.length;for(this.clear();++t<n;){var o=e[t];this.set(o[0],o[1])}}yi.prototype.clear=w3;yi.prototype.delete=C3;yi.prototype.get=O3;yi.prototype.has=_3;yi.prototype.set=E3;var T3=Us(Sa,"Map");const Oc=T3;function M3(){this.size=0,this.__data__={hash:new Ms,map:new(Oc||yi),string:new Ms}}function $3(e){var t=typeof e;return t=="string"||t=="number"||t=="symbol"||t=="boolean"?e!=="__proto__":e===null}function Fd(e,t){var n=e.__data__;return $3(t)?n[typeof t=="string"?"string":"hash"]:n.map}function A3(e){var t=Fd(this,e).delete(e);return this.size-=t?1:0,t}function z3(e){return Fd(this,e).get(e)}function P3(e){return Fd(this,e).has(e)}function N3(e,t){var n=Fd(this,e),o=n.size;return n.set(e,t),this.size+=n.size==o?0:1,this}function ji(e){var t=-1,n=e==null?0:e.length;for(this.clear();++t<n;){var o=e[t];this.set(o[0],o[1])}}ji.prototype.clear=M3;ji.prototype.delete=A3;ji.prototype.get=z3;ji.prototype.has=P3;ji.prototype.set=N3;var R3="Expected a function";function Op(e,t){if(typeof e!="function"||t!=null&&typeof t!="function")throw new TypeError(R3);var n=function(){var o=arguments,i=t?t.apply(this,o):o[0],a=n.cache;if(a.has(i))return a.get(i);var s=e.apply(this,o);return n.cache=a.set(i,s)||a,s};return n.cache=new(Op.Cache||ji),n}Op.Cache=ji;var I3=500;function q3(e){var t=Op(e,function(o){return n.size===I3&&n.clear(),o}),n=t.cache;return t}var D3=/[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|$))/g,L3=/\\(\\)?/g,U3=q3(function(e){var t=[];return e.charCodeAt(0)===46&&t.push(""),e.replace(D3,function(n,o,i,a){t.push(i?a.replace(L3,"$1"):o||n)}),t});const B3=U3;function k1(e){return e==null?"":f1(e)}function S1(e,t){return mo(e)?e:Cp(e,t)?[e]:B3(k1(e))}var F3=1/0;function Wd(e){if(typeof e=="string"||Ts(e))return e;var t=e+"";return t=="0"&&1/e==-F3?"-0":t}function _p(e,t){t=S1(t,e);for(var n=0,o=t.length;e!=null&&n<o;)e=e[Wd(t[n++])];return n&&n==o?e:void 0}function W3(e,t,n){var o=e==null?void 0:_p(e,t);return o===void 0?n:o}function Ep(e,t){for(var n=-1,o=t.length,i=e.length;++n<o;)e[i+n]=t[n];return e}var dg=ta?ta.isConcatSpreadable:void 0;function V3(e){return mo(e)||Ld(e)||!!(dg&&e&&e[dg])}function C1(e,t,n,o,i){var a=-1,s=e.length;for(n||(n=V3),i||(i=[]);++a<s;){var l=e[a];t>0&&n(l)?t>1?C1(l,t-1,n,o,i):Ep(i,l):o||(i[i.length]=l)}return i}var J3=x1(Object.getPrototypeOf,Object);const O1=J3;function H3(e,t,n){var o=-1,i=e.length;t<0&&(t=-t>i?0:i+t),n=n>i?i:n,n<0&&(n+=i),i=t>n?0:n-t>>>0,t>>>=0;for(var a=Array(i);++o<i;)a[o]=e[o+t];return a}function Q3(){this.__data__=new yi,this.size=0}function K3(e){var t=this.__data__,n=t.delete(e);return this.size=t.size,n}function G3(e){return this.__data__.get(e)}function Y3(e){return this.__data__.has(e)}var X3=200;function Z3(e,t){var n=this.__data__;if(n instanceof yi){var o=n.__data__;if(!Oc||o.length<X3-1)return o.push([e,t]),this.size=++n.size,this;n=this.__data__=new ji(o)}return n.set(e,t),this.size=n.size,this}function za(e){var t=this.__data__=new yi(e);this.size=t.size}za.prototype.clear=Q3;za.prototype.delete=K3;za.prototype.get=G3;za.prototype.has=Y3;za.prototype.set=Z3;function ek(e,t){return e&&qd(t,Ll(t),e)}function tk(e,t){return e&&qd(t,Sp(t),e)}var _1=typeof exports=="object"&&exports&&!exports.nodeType&&exports,vg=_1&&typeof module=="object"&&module&&!module.nodeType&&module,nk=vg&&vg.exports===_1,fg=nk?Sa.Buffer:void 0,pg=fg?fg.allocUnsafe:void 0;function rk(e,t){if(t)return e.slice();var n=e.length,o=pg?pg(n):new e.constructor(n);return e.copy(o),o}function ok(e,t){for(var n=-1,o=e==null?0:e.length,i=0,a=[];++n<o;){var s=e[n];t(s,n,e)&&(a[i++]=s)}return a}function E1(){return[]}var ak=Object.prototype,ik=ak.propertyIsEnumerable,hg=Object.getOwnPropertySymbols,sk=hg?function(e){return e==null?[]:(e=Object(e),ok(hg(e),function(t){return ik.call(e,t)}))}:E1;const Tp=sk;function lk(e,t){return qd(e,Tp(e),t)}var ck=Object.getOwnPropertySymbols,uk=ck?function(e){for(var t=[];e;)Ep(t,Tp(e)),e=O1(e);return t}:E1;const T1=uk;function dk(e,t){return qd(e,T1(e),t)}function M1(e,t,n){var o=t(e);return mo(e)?o:Ep(o,n(e))}function hf(e){return M1(e,Ll,Tp)}function vk(e){return M1(e,Sp,T1)}var fk=Us(Sa,"DataView");const gf=fk;var pk=Us(Sa,"Promise");const mf=pk;var hk=Us(Sa,"Set");const bf=hk;var gg="[object Map]",gk="[object Object]",mg="[object Promise]",bg="[object Set]",yg="[object WeakMap]",jg="[object DataView]",mk=Ls(gf),bk=Ls(Oc),yk=Ls(mf),jk=Ls(bf),xk=Ls(ff),gs=ql;(gf&&gs(new gf(new ArrayBuffer(1)))!=jg||Oc&&gs(new Oc)!=gg||mf&&gs(mf.resolve())!=mg||bf&&gs(new bf)!=bg||ff&&gs(new ff)!=yg)&&(gs=function(e){var t=ql(e),n=t==gk?e.constructor:void 0,o=n?Ls(n):"";if(o)switch(o){case mk:return jg;case bk:return gg;case yk:return mg;case jk:return bg;case xk:return yg}return t});const kl=gs;var wk=Object.prototype,kk=wk.hasOwnProperty;function Sk(e){var t=e.length,n=new e.constructor(t);return t&&typeof e[0]=="string"&&kk.call(e,"index")&&(n.index=e.index,n.input=e.input),n}var Ck=Sa.Uint8Array;const nd=Ck;function Mp(e){var t=new e.constructor(e.byteLength);return new nd(t).set(new nd(e)),t}function Ok(e,t){var n=t?Mp(e.buffer):e.buffer;return new e.constructor(n,e.byteOffset,e.byteLength)}var _k=/\w*$/;function Ek(e){var t=new e.constructor(e.source,_k.exec(e));return t.lastIndex=e.lastIndex,t}var xg=ta?ta.prototype:void 0,wg=xg?xg.valueOf:void 0;function Tk(e){return wg?Object(wg.call(e)):{}}function Mk(e,t){var n=t?Mp(e.buffer):e.buffer;return new e.constructor(n,e.byteOffset,e.length)}var $k="[object Boolean]",Ak="[object Date]",zk="[object Map]",Pk="[object Number]",Nk="[object RegExp]",Rk="[object Set]",Ik="[object String]",qk="[object Symbol]",Dk="[object ArrayBuffer]",Lk="[object DataView]",Uk="[object Float32Array]",Bk="[object Float64Array]",Fk="[object Int8Array]",Wk="[object Int16Array]",Vk="[object Int32Array]",Jk="[object Uint8Array]",Hk="[object Uint8ClampedArray]",Qk="[object Uint16Array]",Kk="[object Uint32Array]";function Gk(e,t,n){var o=e.constructor;switch(t){case Dk:return Mp(e);case $k:case Ak:return new o(+e);case Lk:return Ok(e,n);case Uk:case Bk:case Fk:case Wk:case Vk:case Jk:case Hk:case Qk:case Kk:return Mk(e,n);case zk:return new o;case Pk:case Ik:return new o(e);case Nk:return Ek(e);case Rk:return new o;case qk:return Tk(e)}}function Yk(e){return typeof e.constructor=="function"&&!Dd(e)?Q2(O1(e)):{}}var Xk="[object Map]";function Zk(e){return Gi(e)&&kl(e)==Xk}var kg=wl&&wl.isMap,e6=kg?Ud(kg):Zk;const t6=e6;var n6="[object Set]";function r6(e){return Gi(e)&&kl(e)==n6}var Sg=wl&&wl.isSet,o6=Sg?Ud(Sg):r6;const a6=o6;var i6=1,s6=2,l6=4,$1="[object Arguments]",c6="[object Array]",u6="[object Boolean]",d6="[object Date]",v6="[object Error]",A1="[object Function]",f6="[object GeneratorFunction]",p6="[object Map]",h6="[object Number]",z1="[object Object]",g6="[object RegExp]",m6="[object Set]",b6="[object String]",y6="[object Symbol]",j6="[object WeakMap]",x6="[object ArrayBuffer]",w6="[object DataView]",k6="[object Float32Array]",S6="[object Float64Array]",C6="[object Int8Array]",O6="[object Int16Array]",_6="[object Int32Array]",E6="[object Uint8Array]",T6="[object Uint8ClampedArray]",M6="[object Uint16Array]",$6="[object Uint32Array]",hr={};hr[$1]=hr[c6]=hr[x6]=hr[w6]=hr[u6]=hr[d6]=hr[k6]=hr[S6]=hr[C6]=hr[O6]=hr[_6]=hr[p6]=hr[h6]=hr[z1]=hr[g6]=hr[m6]=hr[b6]=hr[y6]=hr[E6]=hr[T6]=hr[M6]=hr[$6]=!0;hr[v6]=hr[A1]=hr[j6]=!1;function gc(e,t,n,o,i,a){var s,l=t&i6,c=t&s6,u=t&l6;if(n&&(s=i?n(e,o,i,a):n(e)),s!==void 0)return s;if(!Da(e))return e;var d=mo(e);if(d){if(s=Sk(e),!l)return G2(e,s)}else{var v=kl(e),f=v==A1||v==f6;if(Sc(e))return rk(e,l);if(v==z1||v==$1||f&&!i){if(s=c||f?{}:Yk(e),!l)return c?dk(e,tk(s,e)):lk(e,ek(s,e))}else{if(!hr[v])return i?e:{};s=Gk(e,v,l)}}a||(a=new za);var h=a.get(e);if(h)return h;a.set(e,s),a6(e)?e.forEach(function(j){s.add(gc(j,t,n,j,e,a))}):t6(e)&&e.forEach(function(j,b){s.set(b,gc(j,t,n,b,e,a))});var p=u?c?vk:hf:c?Sp:Ll,y=d?void 0:p(e);return s4(y||e,function(j,b){y&&(b=j,j=e[b]),h1(s,b,gc(j,t,n,b,e,a))}),s}var A6=1,z6=4;function yf(e){return gc(e,A6|z6)}var P6=1,N6=4;function R6(e,t){return t=typeof t=="function"?t:void 0,gc(e,P6|N6,t)}var I6="__lodash_hash_undefined__";function q6(e){return this.__data__.set(e,I6),this}function D6(e){return this.__data__.has(e)}function rd(e){var t=-1,n=e==null?0:e.length;for(this.__data__=new ji;++t<n;)this.add(e[t])}rd.prototype.add=rd.prototype.push=q6;rd.prototype.has=D6;function L6(e,t){for(var n=-1,o=e==null?0:e.length;++n<o;)if(t(e[n],n,e))return!0;return!1}function U6(e,t){return e.has(t)}var B6=1,F6=2;function P1(e,t,n,o,i,a){var s=n&B6,l=e.length,c=t.length;if(l!=c&&!(s&&c>l))return!1;var u=a.get(e),d=a.get(t);if(u&&d)return u==t&&d==e;var v=-1,f=!0,h=n&F6?new rd:void 0;for(a.set(e,t),a.set(t,e);++v<l;){var p=e[v],y=t[v];if(o)var j=s?o(y,p,v,t,e,a):o(p,y,v,e,t,a);if(j!==void 0){if(j)continue;f=!1;break}if(h){if(!L6(t,function(b,k){if(!U6(h,k)&&(p===b||i(p,b,n,o,a)))return h.push(k)})){f=!1;break}}else if(!(p===y||i(p,y,n,o,a))){f=!1;break}}return a.delete(e),a.delete(t),f}function W6(e){var t=-1,n=Array(e.size);return e.forEach(function(o,i){n[++t]=[i,o]}),n}function V6(e){var t=-1,n=Array(e.size);return e.forEach(function(o){n[++t]=o}),n}var J6=1,H6=2,Q6="[object Boolean]",K6="[object Date]",G6="[object Error]",Y6="[object Map]",X6="[object Number]",Z6="[object RegExp]",e8="[object Set]",t8="[object String]",n8="[object Symbol]",r8="[object ArrayBuffer]",o8="[object DataView]",Cg=ta?ta.prototype:void 0,kv=Cg?Cg.valueOf:void 0;function a8(e,t,n,o,i,a,s){switch(n){case o8:if(e.byteLength!=t.byteLength||e.byteOffset!=t.byteOffset)return!1;e=e.buffer,t=t.buffer;case r8:return!(e.byteLength!=t.byteLength||!a(new nd(e),new nd(t)));case Q6:case K6:case X6:return Id(+e,+t);case G6:return e.name==t.name&&e.message==t.message;case Z6:case t8:return e==t+"";case Y6:var l=W6;case e8:var c=o&J6;if(l||(l=V6),e.size!=t.size&&!c)return!1;var u=s.get(e);if(u)return u==t;o|=H6,s.set(e,t);var d=P1(l(e),l(t),o,i,a,s);return s.delete(e),d;case n8:if(kv)return kv.call(e)==kv.call(t)}return!1}var i8=1,s8=Object.prototype,l8=s8.hasOwnProperty;function c8(e,t,n,o,i,a){var s=n&i8,l=hf(e),c=l.length,u=hf(t),d=u.length;if(c!=d&&!s)return!1;for(var v=c;v--;){var f=l[v];if(!(s?f in t:l8.call(t,f)))return!1}var h=a.get(e),p=a.get(t);if(h&&p)return h==t&&p==e;var y=!0;a.set(e,t),a.set(t,e);for(var j=s;++v<c;){f=l[v];var b=e[f],k=t[f];if(o)var E=s?o(k,b,f,t,e,a):o(b,k,f,e,t,a);if(!(E===void 0?b===k||i(b,k,n,o,a):E)){y=!1;break}j||(j=f=="constructor")}if(y&&!j){var O=e.constructor,w=t.constructor;O!=w&&"constructor"in e&&"constructor"in t&&!(typeof O=="function"&&O instanceof O&&typeof w=="function"&&w instanceof w)&&(y=!1)}return a.delete(e),a.delete(t),y}var u8=1,Og="[object Arguments]",_g="[object Array]",pu="[object Object]",d8=Object.prototype,Eg=d8.hasOwnProperty;function v8(e,t,n,o,i,a){var s=mo(e),l=mo(t),c=s?_g:kl(e),u=l?_g:kl(t);c=c==Og?pu:c,u=u==Og?pu:u;var d=c==pu,v=u==pu,f=c==u;if(f&&Sc(e)){if(!Sc(t))return!1;s=!0,d=!1}if(f&&!d)return a||(a=new za),s||kp(e)?P1(e,t,n,o,i,a):a8(e,t,c,n,o,i,a);if(!(n&u8)){var h=d&&Eg.call(e,"__wrapped__"),p=v&&Eg.call(t,"__wrapped__");if(h||p){var y=h?e.value():e,j=p?t.value():t;return a||(a=new za),i(y,j,n,o,a)}}return f?(a||(a=new za),c8(e,t,n,o,i,a)):!1}function Vd(e,t,n,o,i){return e===t?!0:e==null||t==null||!Gi(e)&&!Gi(t)?e!==e&&t!==t:v8(e,t,n,o,Vd,i)}var f8=1,p8=2;function h8(e,t,n,o){var i=n.length,a=i,s=!o;if(e==null)return!a;for(e=Object(e);i--;){var l=n[i];if(s&&l[2]?l[1]!==e[l[0]]:!(l[0]in e))return!1}for(;++i<a;){l=n[i];var c=l[0],u=e[c],d=l[1];if(s&&l[2]){if(u===void 0&&!(c in e))return!1}else{var v=new za;if(o)var f=o(u,d,c,e,t,v);if(!(f===void 0?Vd(d,u,f8|p8,o,v):f))return!1}}return!0}function N1(e){return e===e&&!Da(e)}function g8(e){for(var t=Ll(e),n=t.length;n--;){var o=t[n],i=e[o];t[n]=[o,i,N1(i)]}return t}function R1(e,t){return function(n){return n==null?!1:n[e]===t&&(t!==void 0||e in Object(n))}}function m8(e){var t=g8(e);return t.length==1&&t[0][2]?R1(t[0][0],t[0][1]):function(n){return n===e||h8(n,e,t)}}function b8(e,t){return e!=null&&t in Object(e)}function y8(e,t,n){t=S1(t,e);for(var o=-1,i=t.length,a=!1;++o<i;){var s=Wd(t[o]);if(!(a=e!=null&&n(e,s)))break;e=e[s]}return a||++o!=i?a:(i=e==null?0:e.length,!!i&&wp(i)&&xp(s,i)&&(mo(e)||Ld(e)))}function j8(e,t){return e!=null&&y8(e,t,b8)}var x8=1,w8=2;function k8(e,t){return Cp(e)&&N1(t)?R1(Wd(e),t):function(n){var o=W3(n,e);return o===void 0&&o===t?j8(n,e):Vd(t,o,x8|w8)}}function S8(e){return function(t){return t==null?void 0:t[e]}}function C8(e){return function(t){return _p(t,e)}}function O8(e){return Cp(e)?S8(Wd(e)):C8(e)}function Hc(e){return typeof e=="function"?e:e==null?Jc:typeof e=="object"?mo(e)?k8(e[0],e[1]):m8(e):O8(e)}function _8(e,t,n,o){for(var i=-1,a=e==null?0:e.length;++i<a;){var s=e[i];t(o,s,n(s),e)}return o}function I1(e){return function(t,n,o){for(var i=-1,a=Object(t),s=o(t),l=s.length;l--;){var c=s[e?l:++i];if(n(a[c],c,a)===!1)break}return t}}var E8=I1();const T8=E8;function q1(e,t){return e&&T8(e,t,Ll)}function D1(e,t){return function(n,o){if(n==null)return n;if(!Dl(n))return e(n,o);for(var i=n.length,a=t?i:-1,s=Object(n);(t?a--:++a<i)&&o(s[a],a,s)!==!1;);return n}}var M8=D1(q1);const L1=M8;function $8(e,t,n,o){return L1(e,function(i,a,s){t(o,i,n(i),s)}),o}function U1(e,t){return function(n,o){var i=mo(n)?_8:$8,a=t?t():{};return i(n,e,Hc(o),a)}}var A8=function(){return Sa.Date.now()};const Sv=A8;var z8="Expected a function",P8=Math.max,N8=Math.min;function od(e,t,n){var o,i,a,s,l,c,u=0,d=!1,v=!1,f=!0;if(typeof e!="function")throw new TypeError(z8);t=vf(t)||0,Da(n)&&(d=!!n.leading,v="maxWait"in n,a=v?P8(vf(n.maxWait)||0,t):a,f="trailing"in n?!!n.trailing:f);function h(_){var A=o,q=i;return o=i=void 0,u=_,s=e.apply(q,A),s}function p(_){return u=_,l=setTimeout(b,t),d?h(_):s}function y(_){var A=_-c,q=_-u,C=t-A;return v?N8(C,a-q):C}function j(_){var A=_-c,q=_-u;return c===void 0||A>=t||A<0||v&&q>=a}function b(){var _=Sv();if(j(_))return k(_);l=setTimeout(b,y(_))}function k(_){return l=void 0,f&&o?h(_):(o=i=void 0,s)}function E(){l!==void 0&&clearTimeout(l),u=0,o=c=i=l=void 0}function O(){return l===void 0?s:k(Sv())}function w(){var _=Sv(),A=j(_);if(o=arguments,i=this,c=_,A){if(l===void 0)return p(c);if(v)return clearTimeout(l),l=setTimeout(b,t),h(c)}return l===void 0&&(l=setTimeout(b,t)),s}return w.cancel=E,w.flush=O,w}function Xt(e){var t=e==null?0:e.length;return t?e[t-1]:void 0}function B1(e){return typeof e=="function"?e:Jc}function R8(e,t){for(var n=e==null?0:e.length;n--&&t(e[n],n,e)!==!1;);return e}var I8=I1(!0);const q8=I8;function D8(e,t){return e&&q8(e,t,Ll)}var L8=D1(D8,!0);const U8=L8;function B8(e,t){var n=mo(e)?R8:U8;return n(e,B1(t))}function ai(e){return e&&e.length?e[0]:void 0}function F1(e,t){var n=-1,o=Dl(e)?Array(e.length):[];return L1(e,function(i,a,s){o[++n]=t(i,a,s)}),o}function F8(e,t){var n=mo(e)?pc:F1;return n(e,Hc(t))}var W8=Object.prototype,V8=W8.hasOwnProperty,J8=U1(function(e,t,n){V8.call(e,n)?e[n].push(t):Rd(e,n,[t])});const H8=J8;function cn(e){var t=e==null?0:e.length;return t?H3(e,0,-1):[]}var Q8="[object Map]",K8="[object Set]",G8=Object.prototype,Y8=G8.hasOwnProperty;function gn(e){if(e==null)return!0;if(Dl(e)&&(mo(e)||typeof e=="string"||typeof e.splice=="function"||Sc(e)||kp(e)||Ld(e)))return!e.length;var t=kl(e);if(t==Q8||t==K8)return!e.size;if(Dd(e))return!w1(e).length;for(var n in e)if(Y8.call(e,n))return!1;return!0}function Gt(e,t){return Vd(e,t)}function X8(e,t){return e<t}function Z8(e,t){var n={};return t=Hc(t),q1(e,function(o,i,a){Rd(n,i,t(o,i,a))}),n}function eS(e,t,n){for(var o=-1,i=e.length;++o<i;){var a=e[o],s=t(a);if(s!=null&&(l===void 0?s===s&&!Ts(s):n(s,l)))var l=s,c=a}return c}function hu(e,t){return e&&e.length?eS(e,Hc(t),X8):void 0}function tS(e,t){var n=e.length;for(e.sort(t);n--;)e[n]=e[n].value;return e}function nS(e,t){if(e!==t){var n=e!==void 0,o=e===null,i=e===e,a=Ts(e),s=t!==void 0,l=t===null,c=t===t,u=Ts(t);if(!l&&!u&&!a&&e>t||a&&s&&c&&!l&&!u||o&&s&&c||!n&&c||!i)return 1;if(!o&&!a&&!u&&e<t||u&&n&&i&&!o&&!a||l&&n&&i||!s&&i||!c)return-1}return 0}function rS(e,t,n){for(var o=-1,i=e.criteria,a=t.criteria,s=i.length,l=n.length;++o<s;){var c=nS(i[o],a[o]);if(c){if(o>=l)return c;var u=n[o];return c*(u=="desc"?-1:1)}}return e.index-t.index}function oS(e,t,n){t.length?t=pc(t,function(a){return mo(a)?function(s){return _p(s,a.length===1?a[0]:a)}:a}):t=[Jc];var o=-1;t=pc(t,Ud(Hc));var i=F1(e,function(a,s,l){var c=pc(t,function(u){return u(a)});return{criteria:c,index:++o,value:a}});return tS(i,function(a,s){return rS(a,s,n)})}var aS=U1(function(e,t,n){e[n?0:1].push(t)},function(){return[[],[]]});const iS=aS;var sS=Math.ceil,lS=Math.max;function cS(e,t,n,o){for(var i=-1,a=lS(sS((t-e)/(n||1)),0),s=Array(a);a--;)s[o?a:++i]=e,e+=n;return s}function uS(e){return function(t,n,o){return o&&typeof o!="number"&&pf(t,n,o)&&(n=o=void 0),t=Uu(t),n===void 0?(n=t,t=0):n=Uu(n),o=o===void 0?t<n?1:-1:Uu(o),cS(t,n,o,e)}}var dS=uS();const W1=dS;var vS=f4(function(e,t){if(e==null)return[];var n=t.length;return n>1&&pf(e,t[0],t[1])?t=[]:n>2&&pf(t[0],t[1],t[2])&&(t=[t[0]]),oS(e,C1(t,1),[])});const fS=vS;var pS=9007199254740991,Cv=4294967295,hS=Math.min;function gS(e,t){if(e=E2(e),e<1||e>pS)return[];var n=Cv,o=hS(e,Cv);t=B1(t),e-=Cv;for(var i=g1(o,t);++n<e;)t(n);return i}var mS=0;function Sl(e){var t=++mS;return k1(e)+t}const Fi=e=>Array.isArray(e),bS=e=>e!==null&&typeof e=="object"&&!Fi(e),yS=e=>typeof e=="string",js=(e,t)=>e===t?!0:e!==null&&t!==null&&typeof e=="object"&&typeof t=="object"&&Object.keys(e).length===Object.keys(t).length&&Object.entries(e).every(([n,o])=>js(o,t[n])),Tg=(e,t)=>{const n=e==null?void 0:e[t];if(n!==void 0){if(!Object.hasOwn(e,t)||Array.isArray(e)&&!/^\d+$/.test(t)||typeof e!="object")throw new TypeError(`Unsupported property "${t}"`);return n}};function Wr(e){return(...t)=>{const n=t.map(a=>Jr(a)),o=n[0],i=n[1];return n.length===1?a=>e(o(a)):n.length===2?a=>e(o(a),i(a)):a=>e(...n.map(s=>s(a)))}}const mc={boolean:0,number:1,string:2},Mg=3,V1=(e,t)=>typeof e==typeof t&&typeof e in mc?e>t:!1,jS=(e,t)=>js(e,t)||V1(e,t),J1=(e,t)=>typeof e==typeof t&&typeof e in mc?e<t:!1,xS=(e,t)=>js(e,t)||J1(e,t),uc={pipe:(...e)=>{const t=e.map(n=>Jr(n));return n=>t.reduce((o,i)=>i(o),n)},object:e=>{const t=Object.keys(e).map(n=>[n,Jr(e[n])]);return n=>{const o={};for(const[i,a]of t)o[i]=a(n);return o}},array:(...e)=>{const t=e.map(n=>Jr(n));return n=>t.map(o=>o(n))},get:(...e)=>{if(e.length===0)return t=>t??null;if(e.length===1){const t=e[0];return n=>Tg(n,t)??null}return t=>{let n=t;for(const o of e)n=Tg(n,o);return n??null}},map:e=>{const t=Jr(e);return n=>n.map(t)},mapObject:e=>{const t=Jr(e);return n=>{const o={};for(const i of Object.keys(n)){const a=t({key:i,value:n[i]});o[a.key]=a.value}return o}},mapKeys:e=>{const t=Jr(e);return n=>{const o={};for(const i of Object.keys(n)){const a=t(i);o[a]=n[i]}return o}},mapValues:e=>{const t=Jr(e);return n=>{const o={};for(const i of Object.keys(n))o[i]=t(n[i]);return o}},filter:e=>{const t=Jr(e);return n=>n.filter(o=>$g(t(o)))},sort:(e=["get"],t)=>{const n=Jr(e),o=t==="desc"?-1:1;function i(a,s){const l=n(a),c=n(s);if(typeof l!=typeof c){const u=mc[typeof l]??Mg,d=mc[typeof c]??Mg;return u>d?o:u<d?-o:0}return typeof l in mc?l>c?o:l<c?-o:0:0}return a=>a.slice().sort(i)},reverse:()=>e=>e.toReversed(),pick:(...e)=>{const t=e.map(([o,...i])=>[i[i.length-1],uc.get(...i)]),n=(o,i)=>{const a={};for(const[s,l]of i)a[s]=l(o);return a};return o=>Fi(o)?o.map(i=>n(i,t)):n(o,t)},groupBy:e=>{const t=Jr(e);return n=>{const o={};for(const i of n){const a=t(i);o[a]?o[a].push(i):o[a]=[i]}return o}},keyBy:e=>{const t=Jr(e);return n=>{const o={};for(const i of n){const a=t(i);a in o||(o[a]=i)}return o}},flatten:()=>e=>e.flat(),join:(e="")=>t=>t.join(e),split:Wr((e,t)=>t!==void 0?e.split(t):e.trim().split(/\s+/)),substring:Wr((e,t,n)=>e.slice(Math.max(t,0),n)),uniq:()=>e=>{const t=[];for(const n of e)t.findIndex(o=>js(o,n))===-1&&t.push(n);return t},uniqBy:e=>t=>Object.values(uc.keyBy(e)(t)),limit:e=>t=>t.slice(0,Math.max(e,0)),size:()=>e=>e.length,keys:()=>Object.keys,values:()=>Object.values,prod:()=>e=>tc(e,(t,n)=>t*n),sum:()=>e=>Fi(e)?e.reduce((t,n)=>t+n,0):jf(),average:()=>e=>Fi(e)?e.length>0?e.reduce((t,n)=>t+n)/e.length:null:jf(),min:()=>e=>tc(e,(t,n)=>Math.min(t,n)),max:()=>e=>tc(e,(t,n)=>Math.max(t,n)),and:Wr((...e)=>tc(e,(t,n)=>!!(t&&n))),or:Wr((...e)=>tc(e,(t,n)=>!!(t||n))),not:Wr(e=>!e),exists:e=>{const t=e.slice(1),n=t.pop(),o=uc.get(...t);return i=>{const a=o(i);return!!a&&Object.hasOwnProperty.call(a,n)}},if:(e,t,n)=>{const o=Jr(e),i=Jr(t),a=Jr(n);return s=>$g(o(s))?i(s):a(s)},in:(e,t)=>{const n=Jr(e),o=Jr(t);return i=>{const a=n(i);return o(i).findIndex(s=>js(s,a))!==-1}},"not in":(e,t)=>{const n=uc.in(e,t);return o=>!n(o)},regex:(e,t,n)=>{const o=new RegExp(t,n),i=Jr(e);return a=>o.test(i(a))},match:(e,t,n)=>{const o=new RegExp(t,n),i=Jr(e);return a=>{const s=i(a).match(o);return s?Ag(s):null}},matchAll:(e,t,n)=>{const o=new RegExp(t,`${n??""}g`),i=Jr(e);return a=>Array.from(i(a).matchAll(o)).map(Ag)},eq:Wr(js),gt:Wr(V1),gte:Wr(jS),lt:Wr(J1),lte:Wr(xS),ne:Wr((e,t)=>!js(e,t)),add:Wr((e,t)=>e+t),subtract:Wr((e,t)=>e-t),multiply:Wr((e,t)=>e*t),divide:Wr((e,t)=>e/t),mod:Wr((e,t)=>e%t),pow:Wr((e,t)=>e**t),abs:Wr(Math.abs),round:Wr((e,t=0)=>+`${Math.round(+`${e}e${t}`)}e${-t}`),number:Wr(e=>{const t=Number(e);return Number.isNaN(Number(e))?null:t}),string:Wr(String)},$g=e=>e!==null&&e!==0&&e!==!1,tc=(e,t)=>(Fi(e)||jf(),e.length===0?null:e.reduce(t)),Ag=e=>{const[t,...n]=e,o=e.groups;return n.length?o?{value:t,groups:n,namedGroups:o}:{value:t,groups:n}:{value:t}},jf=()=>{$p("Array expected")},$p=e=>{throw new TypeError(e)},gu=[];function Jr(e,t){gu.unshift({...uc,...gu[0],...t==null?void 0:t.functions});try{const n=Fi(e)?wS(e,gu[0]):bS(e)?$p(`Function notation ["object", {...}] expected but got ${JSON.stringify(e)}`):()=>e;return o=>{try{return n(o)}catch(i){throw i.jsonquery=[{data:o,query:e},...i.jsonquery??[]],i}}}finally{gu.shift()}}function wS(e,t){const[n,...o]=e,i=t[n];return i||$p(`Unknown function '${n}'`),i(...o)}const H1=[{pow:"^"},{multiply:"*",divide:"/",mod:"%"},{add:"+",subtract:"-"},{gt:">",gte:">=",lt:"<",lte:"<=",in:"in","not in":"not in"},{eq:"==",ne:"!="},{and:"and"},{or:"or"},{pipe:"|"}],kS=["|","and","or"],Q1=["|","and","or","*","/","%","+","-"];function K1(e,t){if(!Fi(t))throw new Error("Invalid custom operators");return t.reduce(SS,e)}function SS(e,{name:t,op:n,at:o,after:i,before:a}){if(o)return e.map(c=>Object.values(c).includes(o)?{...c,[t]:n}:c);const s=i??a,l=e.findIndex(c=>Object.values(c).includes(s));if(l!==-1)return e.toSpliced(l+(i?1:0),0,{[t]:n});throw new Error("Invalid custom operator")}const CS=/^[a-zA-Z_$][a-zA-Z\d_$]*$/,OS=/^[a-zA-Z_$][a-zA-Z\d_$]*/,_S=/^"(?:[^"\\]|\\.)*"/,ES=/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/,TS=/^(0|[1-9][0-9]*)/,MS=/^(true|false|null)/,$S=/^[ \n\t\r]+/;function G1(e,t){const n=(t==null?void 0:t.operators)??[],o=K1(H1,n),i=Object.assign({},...o),a=kS.concat(n.filter(z=>z.vararg).map(z=>z.op)),s=Q1.concat(n.filter(z=>z.leftAssociative).map(z=>z.op)),l=(z=o.length-1)=>{const D=o[z];if(!D)return u();const H=e[q]==="(";let Q=l(z-1);for(;;){if(w(),e[q]==="."&&"pipe"in D){const ve=d();Q=Q[0]==="pipe"?[...Q,ve]:["pipe",Q,ve];continue}const fe=q,Ie=c(D);if(!Ie)break;const ge=l(z-1),qe=Q[0],ce=Ie===qe&&!H;if(ce&&!s.includes(i[Ie])){q=fe;break}Q=ce&&a.includes(i[Ie])?[...Q,ge]:[Ie,Q,ge]}return Q},c=z=>{const D=Object.keys(z).sort((H,Q)=>Q.length-H.length);for(const H of D){const Q=z[H];if(e.substring(q,q+Q.length)===Q)return q+=Q.length,w(),H}},u=()=>{if(w(),e[q]==="("){q++;const z=l();return _(")"),z}return d()},d=()=>{if(e[q]==="."){const z=[];for(;e[q]===".";)q++,z.push(p()??y()??b()??A("Property expected")),w();return["get",...z]}return v()},v=()=>{const z=q,D=y();if(w(),!D||e[q]!=="(")return q=z,f();q++,w();const H=e[q]!==")"?[l()]:[];for(;q<e.length&&e[q]!==")";)w(),_(","),H.push(l());return _(")"),[D,...H]},f=()=>{if(e[q]==="{"){q++,w();const z={};let D=!0;for(;q<e.length&&e[q]!=="}";){D?D=!1:(_(","),w());const H=p()??y()??b()??A("Key expected");w(),_(":"),z[H]=l()}return _("}"),["object",z]}return h()},h=()=>{if(e[q]==="["){q++,w();const z=[];let D=!0;for(;q<e.length&&e[q]!=="]";)D?D=!1:(_(","),w()),z.push(l());return _("]"),["array",...z]}return p()??j()??k()},p=()=>O(_S,JSON.parse),y=()=>O(OS,z=>z),j=()=>O(ES,JSON.parse),b=()=>O(TS,JSON.parse),k=()=>{const z=O(MS,JSON.parse);if(z!==void 0)return z;A("Value expected")},E=()=>{w(),q<e.length&&A(`Unexpected part '${e.substring(q)}'`)},O=(z,D)=>{const H=e.substring(q).match(z);if(H)return q+=H[0].length,D(H[0])},w=()=>O($S,z=>z),_=z=>{e[q]!==z&&A(`Character '${z}' expected`),q++},A=(z,D=q)=>{throw new SyntaxError(`${z} (pos: ${D})`)};let q=0;const C=l();return E(),C}const AS=40,zS="  ",PS=(e,t)=>{const n=(t==null?void 0:t.indentation)??zS,o=(t==null?void 0:t.operators)??[],i=K1(H1,o),a=Object.assign({},...i),s=Q1.concat(o.filter(h=>h.leftAssociative).map(h=>h.op)),l=(h,p,y=!1)=>Fi(h)?c(h,p,y):JSON.stringify(h),c=(h,p,y)=>{const[j,...b]=h;if(j==="get"&&b.length>0)return d(b);if(j==="object")return u(b[0],p);if(j==="array"){const w=b.map(_=>l(_,p));return f(w,["[",", ","]"],[`[
${p+n}`,`,
${p+n}`,`
${p}]`])}const k=a[j];if(k){const w=y?"(":"",_=y?")":"",A=b.map((q,C)=>{const z=q==null?void 0:q[0],D=i.findIndex(fe=>j in fe),H=i.findIndex(fe=>z in fe),Q=D<H||D===H&&C>0||j===z&&!s.includes(k);return l(q,p+n,Q)});return f(A,[w,` ${k} `,_],[w,`
${p+n}${k} `,_])}const E=b.length===1?p:p+n,O=b.map(w=>l(w,E));return f(O,[`${j}(`,", ",")"],b.length===1?[`${j}(`,`,
${p}`,")"]:[`${j}(
${E}`,`,
${E}`,`
${p})`])},u=(h,p)=>{const y=p+n,j=Object.entries(h).map(([b,k])=>`${v(b)}: ${l(k,y)}`);return f(j,["{ ",", "," }"],[`{
${y}`,`,
${y}`,`
${p}}`])},d=h=>h.map(p=>`.${v(p)}`).join(""),v=h=>CS.test(h)?h:JSON.stringify(h),f=(h,[p,y,j],[b,k,E])=>p.length+h.reduce((O,w)=>O+w.length+y.length,0)-y.length+j.length<=((t==null?void 0:t.maxLineLength)??AS)?p+h.join(y)+j:b+h.join(k)+E;return l(e,"")};function NS(e,t,n){return Jr(yS(t)?G1(t,n):t,n)(e)}/*!
 * Font Awesome Free 7.2.0 by @fontawesome - https://fontawesome.com
 * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
 * Copyright 2026 Fonticons, Inc.
 */var RS={prefix:"far",iconName:"clock",icon:[512,512,[128339,"clock-four"],"f017","M464 256a208 208 0 1 1 -416 0 208 208 0 1 1 416 0zM0 256a256 256 0 1 0 512 0 256 256 0 1 0 -512 0zM232 120l0 136c0 8 4 15.5 10.7 20l96 64c11 7.4 25.9 4.4 33.3-6.7s4.4-25.9-6.7-33.3L280 243.2 280 120c0-13.3-10.7-24-24-24s-24 10.7-24 24z"]},IS={prefix:"far",iconName:"square-check",icon:[448,512,[9745,9989,61510,"check-square"],"f14a","M384 32c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96C0 60.7 28.7 32 64 32l320 0zM64 80c-8.8 0-16 7.2-16 16l0 320c0 8.8 7.2 16 16 16l320 0c8.8 0 16-7.2 16-16l0-320c0-8.8-7.2-16-16-16L64 80zm230.7 89.9c7.8-10.7 22.8-13.1 33.5-5.3 10.7 7.8 13.1 22.8 5.3 33.5L211.4 366.1c-4.1 5.7-10.5 9.3-17.5 9.8-7 .5-13.9-2-18.8-6.9l-55.9-55.9c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l36 36 105.6-145.2z"]},Y1=IS,qS={prefix:"far",iconName:"lightbulb",icon:[384,512,[128161],"f0eb","M296.5 291.1C321 265.2 336 230.4 336 192 336 112.5 271.5 48 192 48S48 112.5 48 192c0 38.4 15 73.2 39.5 99.1 21.3 22.4 44.9 54 53.3 92.9l102.4 0c8.4-39 32-70.5 53.3-92.9zm34.8 33C307.7 349 288 379.4 288 413.7l0 18.3c0 44.2-35.8 80-80 80l-32 0c-44.2 0-80-35.8-80-80l0-18.3C96 379.4 76.3 349 52.7 324.1 20 289.7 0 243.2 0 192 0 86 86 0 192 0S384 86 384 192c0 51.2-20 97.7-52.7 132.1zM144 184c0 13.3-10.7 24-24 24s-24-10.7-24-24c0-48.6 39.4-88 88-88 13.3 0 24 10.7 24 24s-10.7 24-24 24c-22.1 0-40 17.9-40 40z"]},X1={prefix:"far",iconName:"square",icon:[448,512,[9632,9723,9724,61590],"f0c8","M384 80c8.8 0 16 7.2 16 16l0 320c0 8.8-7.2 16-16 16L64 432c-8.8 0-16-7.2-16-16L48 96c0-8.8 7.2-16 16-16l320 0zM64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32z"]};/*!
 * Font Awesome Free 7.2.0 by @fontawesome - https://fontawesome.com
 * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
 * Copyright 2026 Fonticons, Inc.
 */var DS={prefix:"fas",iconName:"rotate",icon:[512,512,[128260,"sync-alt"],"f2f1","M480.1 192l7.9 0c13.3 0 24-10.7 24-24l0-144c0-9.7-5.8-18.5-14.8-22.2S477.9 .2 471 7L419.3 58.8C375 22.1 318 0 256 0 127 0 20.3 95.4 2.6 219.5 .1 237 12.2 253.2 29.7 255.7s33.7-9.7 36.2-27.1C79.2 135.5 159.3 64 256 64 300.4 64 341.2 79 373.7 104.3L327 151c-6.9 6.9-8.9 17.2-5.2 26.2S334.3 192 344 192l136.1 0zm29.4 100.5c2.5-17.5-9.7-33.7-27.1-36.2s-33.7 9.7-36.2 27.1c-13.3 93-93.4 164.5-190.1 164.5-44.4 0-85.2-15-117.7-40.3L185 361c6.9-6.9 8.9-17.2 5.2-26.2S177.7 320 168 320L24 320c-13.3 0-24 10.7-24 24L0 488c0 9.7 5.8 18.5 14.8 22.2S34.1 511.8 41 505l51.8-51.8C137 489.9 194 512 256 512 385 512 491.7 416.6 509.4 292.5z"]},Z1={prefix:"fas",iconName:"paste",icon:[512,512,["file-clipboard"],"f0ea","M64 0C28.7 0 0 28.7 0 64L0 384c0 35.3 28.7 64 64 64l112 0 0-224c0-61.9 50.1-112 112-112l64 0 0-48c0-35.3-28.7-64-64-64L64 0zM248 112l-144 0c-13.3 0-24-10.7-24-24s10.7-24 24-24l144 0c13.3 0 24 10.7 24 24s-10.7 24-24 24zm40 48c-35.3 0-64 28.7-64 64l0 224c0 35.3 28.7 64 64 64l160 0c35.3 0 64-28.7 64-64l0-165.5c0-17-6.7-33.3-18.7-45.3l-58.5-58.5c-12-12-28.3-18.7-45.3-18.7L288 160z"]},LS={prefix:"fas",iconName:"crop-simple",icon:[512,512,["crop-alt"],"f565","M128 32c0-17.7-14.3-32-32-32S64 14.3 64 32l0 32-32 0C14.3 64 0 78.3 0 96s14.3 32 32 32l32 0 0 256c0 35.3 28.7 64 64 64l208 0 0-64-208 0 0-352zM384 480c0 17.7 14.3 32 32 32s32-14.3 32-32l0-32 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-32 0 0-256c0-35.3-28.7-64-64-64l-208 0 0 64 208 0 0 352z"]},US=LS,ad={prefix:"fas",iconName:"filter",icon:[512,512,[],"f0b0","M32 64C19.1 64 7.4 71.8 2.4 83.8S.2 109.5 9.4 118.6L192 301.3 192 416c0 8.5 3.4 16.6 9.4 22.6l64 64c9.2 9.2 22.9 11.9 34.9 6.9S320 492.9 320 480l0-178.7 182.6-182.6c9.2-9.2 11.9-22.9 6.9-34.9S492.9 64 480 64L32 64z"]},BS={prefix:"fas",iconName:"square-caret-down",icon:[448,512,["caret-square-down"],"f150","M384 480c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0zM224 352c-6.7 0-13-2.8-17.6-7.7l-104-112c-6.5-7-8.2-17.2-4.4-25.9S110.5 192 120 192l208 0c9.5 0 18.2 5.7 22 14.4s2.1 18.9-4.4 25.9l-104 112c-4.5 4.9-10.9 7.7-17.6 7.7z"]},FS=BS,_c={prefix:"fas",iconName:"caret-right",icon:[256,512,[],"f0da","M249.3 235.8c10.2 12.6 9.5 31.1-2.2 42.8l-128 128c-9.2 9.2-22.9 11.9-34.9 6.9S64.5 396.9 64.5 384l0-256c0-12.9 7.8-24.6 19.8-29.6s25.7-2.2 34.9 6.9l128 128 2.2 2.4z"]},WS={prefix:"fas",iconName:"magnifying-glass",icon:[512,512,[128269,"search"],"f002","M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376C296.3 401.1 253.9 416 208 416 93.1 416 0 322.9 0 208S93.1 0 208 0 416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"]},Jd=WS,VS={prefix:"fas",iconName:"eye",icon:[576,512,[128065],"f06e","M288 32c-80.8 0-145.5 36.8-192.6 80.6-46.8 43.5-78.1 95.4-93 131.1-3.3 7.9-3.3 16.7 0 24.6 14.9 35.7 46.2 87.7 93 131.1 47.1 43.7 111.8 80.6 192.6 80.6s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1 3.3-7.9 3.3-16.7 0-24.6-14.9-35.7-46.2-87.7-93-131.1-47.1-43.7-111.8-80.6-192.6-80.6zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64-11.5 0-22.3-3-31.7-8.4-1 10.9-.1 22.1 2.9 33.2 13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-12.2-45.7-55.5-74.8-101.1-70.8 5.3 9.3 8.4 20.1 8.4 31.7z"]},JS={prefix:"fas",iconName:"caret-left",icon:[256,512,[],"f0d9","M7.7 235.8c-10.3 12.6-9.5 31.1 2.2 42.8l128 128c9.2 9.2 22.9 11.9 34.9 6.9s19.8-16.6 19.8-29.6l0-256c0-12.9-7.8-24.6-19.8-29.6s-25.7-2.2-34.9 6.9l-128 128-2.2 2.4z"]},HS={prefix:"fas",iconName:"chevron-up",icon:[448,512,[],"f077","M201.4 105.4c12.5-12.5 32.8-12.5 45.3 0l192 192c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L224 173.3 54.6 342.6c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3l192-192z"]},QS={prefix:"fas",iconName:"circle-notch",icon:[512,512,[],"f1ce","M222.7 32.1c5 16.9-4.6 34.8-21.5 39.8-79.3 23.6-137.1 97.1-137.1 184.1 0 106 86 192 192 192s192-86 192-192c0-86.9-57.8-160.4-137.1-184.1-16.9-5-26.6-22.9-21.5-39.8s22.9-26.6 39.8-21.5C434.9 42.1 512 140 512 256 512 397.4 397.4 512 256 512S0 397.4 0 256c0-116 77.1-213.9 182.9-245.4 16.9-5 34.8 4.6 39.8 21.5z"]},KS={prefix:"fas",iconName:"ellipsis-vertical",icon:[128,512,["ellipsis-v"],"f142","M64 144a56 56 0 1 1 0-112 56 56 0 1 1 0 112zm0 224c30.9 0 56 25.1 56 56s-25.1 56-56 56-56-25.1-56-56 25.1-56 56-56zm56-112c0 30.9-25.1 56-56 56s-56-25.1-56-56 25.1-56 56-56 56 25.1 56 56z"]},eb=KS,GS={prefix:"fas",iconName:"pen-to-square",icon:[512,512,["edit"],"f044","M471.6 21.7c-21.9-21.9-57.3-21.9-79.2 0L368 46.1 465.9 144 490.3 119.6c21.9-21.9 21.9-57.3 0-79.2L471.6 21.7zm-299.2 220c-6.1 6.1-10.8 13.6-13.5 21.9l-29.6 88.8c-2.9 8.6-.6 18.1 5.8 24.6s15.9 8.7 24.6 5.8l88.8-29.6c8.2-2.7 15.7-7.4 21.9-13.5L432 177.9 334.1 80 172.4 241.7zM96 64C43 64 0 107 0 160L0 416c0 53 43 96 96 96l256 0c53 0 96-43 96-96l0-96c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 96c0 17.7-14.3 32-32 32L96 448c-17.7 0-32-14.3-32-32l0-256c0-17.7 14.3-32 32-32l96 0c17.7 0 32-14.3 32-32s-14.3-32-32-32L96 64z"]},YS=GS,tb={prefix:"fas",iconName:"clone",icon:[512,512,[],"f24d","M288 448l-224 0 0-224 48 0 0-64-48 0c-35.3 0-64 28.7-64 64L0 448c0 35.3 28.7 64 64 64l224 0c35.3 0 64-28.7 64-64l0-48-64 0 0 48zm-64-96l224 0c35.3 0 64-28.7 64-64l0-224c0-35.3-28.7-64-64-64L224 0c-35.3 0-64 28.7-64 64l0 224c0 35.3 28.7 64 64 64z"]},XS={prefix:"fas",iconName:"square-check",icon:[448,512,[9745,9989,61510,"check-square"],"f14a","M384 32c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96C0 60.7 28.7 32 64 32l320 0zM342 145.7c-10.7-7.8-25.7-5.4-33.5 5.3L189.1 315.2 137 263.1c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9l72 72c5 5 11.9 7.5 18.8 7s13.4-4.1 17.5-9.8L347.3 179.2c7.8-10.7 5.4-25.7-5.3-33.5z"]},nb=XS,ZS={prefix:"fas",iconName:"square-caret-up",icon:[448,512,["caret-square-up"],"f151","M64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32zM224 160c6.7 0 13 2.8 17.6 7.7l104 112c6.5 7 8.2 17.2 4.4 25.9S337.5 320 328 320l-208 0c-9.5 0-18.2-5.7-22-14.4s-2.1-18.9 4.4-25.9l104-112c4.5-4.9 10.9-7.7 17.6-7.7z"]},eC=ZS,id={prefix:"fas",iconName:"code",icon:[576,512,[],"f121","M360.8 1.2c-17-4.9-34.7 5-39.6 22l-128 448c-4.9 17 5 34.7 22 39.6s34.7-5 39.6-22l128-448c4.9-17-5-34.7-22-39.6zm64.6 136.1c-12.5 12.5-12.5 32.8 0 45.3l73.4 73.4-73.4 73.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l96-96c12.5-12.5 12.5-32.8 0-45.3l-96-96c-12.5-12.5-32.8-12.5-45.3 0zm-274.7 0c-12.5-12.5-32.8-12.5-45.3 0l-96 96c-12.5 12.5-12.5 32.8 0 45.3l96 96c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L77.3 256 150.6 182.6c12.5-12.5 12.5-32.8 0-45.3z"]},rb={prefix:"fas",iconName:"angle-right",icon:[256,512,[8250],"f105","M247.1 233.4c12.5 12.5 12.5 32.8 0 45.3l-160 160c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L179.2 256 41.9 118.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l160 160z"]},tC={prefix:"fas",iconName:"gear",icon:[512,512,[9881,"cog"],"f013","M195.1 9.5C198.1-5.3 211.2-16 226.4-16l59.8 0c15.2 0 28.3 10.7 31.3 25.5L332 79.5c14.1 6 27.3 13.7 39.3 22.8l67.8-22.5c14.4-4.8 30.2 1.2 37.8 14.4l29.9 51.8c7.6 13.2 4.9 29.8-6.5 39.9L447 233.3c.9 7.4 1.3 15 1.3 22.7s-.5 15.3-1.3 22.7l53.4 47.5c11.4 10.1 14 26.8 6.5 39.9l-29.9 51.8c-7.6 13.1-23.4 19.2-37.8 14.4l-67.8-22.5c-12.1 9.1-25.3 16.7-39.3 22.8l-14.4 69.9c-3.1 14.9-16.2 25.5-31.3 25.5l-59.8 0c-15.2 0-28.3-10.7-31.3-25.5l-14.4-69.9c-14.1-6-27.2-13.7-39.3-22.8L73.5 432.3c-14.4 4.8-30.2-1.2-37.8-14.4L5.8 366.1c-7.6-13.2-4.9-29.8 6.5-39.9l53.4-47.5c-.9-7.4-1.3-15-1.3-22.7s.5-15.3 1.3-22.7L12.3 185.8c-11.4-10.1-14-26.8-6.5-39.9L35.7 94.1c7.6-13.2 23.4-19.2 37.8-14.4l67.8 22.5c12.1-9.1 25.3-16.7 39.3-22.8L195.1 9.5zM256.3 336a80 80 0 1 0 -.6-160 80 80 0 1 0 .6 160z"]},nC=tC,rC={prefix:"fas",iconName:"up-right-and-down-left-from-center",icon:[512,512,["expand-alt"],"f424","M344 0L488 0c13.3 0 24 10.7 24 24l0 144c0 9.7-5.8 18.5-14.8 22.2s-19.3 1.7-26.2-5.2l-39-39-87 87c-9.4 9.4-24.6 9.4-33.9 0l-32-32c-9.4-9.4-9.4-24.6 0-33.9l87-87-39-39c-6.9-6.9-8.9-17.2-5.2-26.2S334.3 0 344 0zM168 512L24 512c-13.3 0-24-10.7-24-24L0 344c0-9.7 5.8-18.5 14.8-22.2S34.1 320.2 41 327l39 39 87-87c9.4-9.4 24.6-9.4 33.9 0l32 32c9.4 9.4 9.4 24.6 0 33.9l-87 87 39 39c6.9 6.9 8.9 17.2 5.2 26.2S177.7 512 168 512z"]},Yi={prefix:"fas",iconName:"wrench",icon:[576,512,[128295],"f0ad","M509.4 98.6c7.6-7.6 20.3-5.7 24.1 4.3 6.8 17.7 10.5 37 10.5 57.1 0 88.4-71.6 160-160 160-17.5 0-34.4-2.8-50.2-8L146.9 498.9c-28.1 28.1-73.7 28.1-101.8 0s-28.1-73.7 0-101.8L232 210.2c-5.2-15.8-8-32.6-8-50.2 0-88.4 71.6-160 160-160 20.1 0 39.4 3.7 57.1 10.5 10 3.8 11.8 16.5 4.3 24.1l-88.7 88.7c-3 3-4.7 7.1-4.7 11.3l0 41.4c0 8.8 7.2 16 16 16l41.4 0c4.2 0 8.3-1.7 11.3-4.7l88.7-88.7z"]},xf={prefix:"fas",iconName:"trash-can",icon:[448,512,[61460,"trash-alt"],"f2ed","M136.7 5.9C141.1-7.2 153.3-16 167.1-16l113.9 0c13.8 0 26 8.8 30.4 21.9L320 32 416 32c17.7 0 32 14.3 32 32s-14.3 32-32 32L32 96C14.3 96 0 81.7 0 64S14.3 32 32 32l96 0 8.7-26.1zM32 144l384 0 0 304c0 35.3-28.7 64-64 64L96 512c-35.3 0-64-28.7-64-64l0-304zm88 64c-13.3 0-24 10.7-24 24l0 192c0 13.3 10.7 24 24 24s24-10.7 24-24l0-192c0-13.3-10.7-24-24-24zm104 0c-13.3 0-24 10.7-24 24l0 192c0 13.3 10.7 24 24 24s24-10.7 24-24l0-192c0-13.3-10.7-24-24-24zm104 0c-13.3 0-24 10.7-24 24l0 192c0 13.3 10.7 24 24 24s24-10.7 24-24l0-192c0-13.3-10.7-24-24-24z"]},Ap={prefix:"fas",iconName:"check",icon:[448,512,[10003,10004],"f00c","M434.8 70.1c14.3 10.4 17.5 30.4 7.1 44.7l-256 352c-5.5 7.6-14 12.3-23.4 13.1s-18.5-2.7-25.1-9.3l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l101.5 101.5 234-321.7c10.4-14.3 30.4-17.5 44.7-7.1z"]},ob={prefix:"fas",iconName:"xmark",icon:[384,512,[128473,10005,10006,10060,215,"close","multiply","remove","times"],"f00d","M55.1 73.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L147.2 256 9.9 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192.5 301.3 329.9 438.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.8 256 375.1 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192.5 210.7 55.1 73.4z"]},oC=ob,Hd=ob,pl={prefix:"fas",iconName:"pen",icon:[512,512,[128394],"f304","M352.9 21.2L308 66.1 445.9 204 490.8 159.1C504.4 145.6 512 127.2 512 108s-7.6-37.6-21.2-51.1L455.1 21.2C441.6 7.6 423.2 0 404 0s-37.6 7.6-51.1 21.2zM274.1 100L58.9 315.1c-10.7 10.7-18.5 24.1-22.6 38.7L.9 481.6c-2.3 8.3 0 17.3 6.2 23.4s15.1 8.5 23.4 6.2l127.8-35.5c14.6-4.1 27.9-11.8 38.7-22.6L412 237.9 274.1 100z"]},aC={prefix:"fas",iconName:"chevron-down",icon:[448,512,[],"f078","M201.4 406.6c12.5 12.5 32.8 12.5 45.3 0l192-192c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 338.7 54.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l192 192z"]},iC={prefix:"fas",iconName:"angle-down",icon:[384,512,[8964],"f107","M169.4 374.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 306.7 54.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"]},sC={prefix:"fas",iconName:"arrow-down-short-wide",icon:[576,512,["sort-amount-desc","sort-amount-down-alt"],"f884","M246.6 374.6l-96 96c-12.5 12.5-32.8 12.5-45.3 0l-96-96c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L96 370.7 96 64c0-17.7 14.3-32 32-32s32 14.3 32 32l0 306.7 41.4-41.4c12.5-12.5 32.8-12.5 45.3 0s12.5 32.8 0 45.3zM320 32l32 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-32 0c-17.7 0-32-14.3-32-32s14.3-32 32-32zm0 128l96 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-96 0c-17.7 0-32-14.3-32-32s14.3-32 32-32zm0 128l160 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-160 0c-17.7 0-32-14.3-32-32s14.3-32 32-32zm0 128l224 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-224 0c-17.7 0-32-14.3-32-32s14.3-32 32-32z"]},sd=sC,lC={prefix:"fas",iconName:"triangle-exclamation",icon:[512,512,[9888,"exclamation-triangle","warning"],"f071","M256 0c14.7 0 28.2 8.1 35.2 21l216 400c6.7 12.4 6.4 27.4-.8 39.5S486.1 480 472 480L40 480c-14.1 0-27.2-7.4-34.4-19.5s-7.5-27.1-.8-39.5l216-400c7-12.9 20.5-21 35.2-21zm0 352a32 32 0 1 0 0 64 32 32 0 1 0 0-64zm0-192c-18.2 0-32.7 15.5-31.4 33.7l7.4 104c.9 12.5 11.4 22.3 23.9 22.3 12.6 0 23-9.7 23.9-22.3l7.4-104c1.3-18.2-13.1-33.7-31.4-33.7z"]},$s=lC,cC={prefix:"fas",iconName:"scissors",icon:[512,512,[9984,9986,9988,"cut"],"f0c4","M192 256l-39.5 39.5c-12.6-4.9-26.2-7.5-40.5-7.5-61.9 0-112 50.1-112 112s50.1 112 112 112 112-50.1 112-112c0-14.3-2.7-27.9-7.5-40.5L499.2 76.8c7.1-7.1 7.1-18.5 0-25.6-28.3-28.3-74.1-28.3-102.4 0L256 192 216.5 152.5c4.9-12.6 7.5-26.2 7.5-40.5 0-61.9-50.1-112-112-112S0 50.1 0 112 50.1 224 112 224c14.3 0 27.9-2.7 40.5-7.5L192 256zm97.9 97.9L396.8 460.8c28.3 28.3 74.1 28.3 102.4 0 7.1-7.1 7.1-18.5 0-25.6l-145.3-145.3-64 64zM64 112a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm48 240a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"]},hl=cC,mu={prefix:"fas",iconName:"arrow-right-arrow-left",icon:[512,512,[8644,"exchange"],"f0ec","M502.6 150.6l-96 96c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L402.7 160 32 160c-17.7 0-32-14.3-32-32S14.3 96 32 96l370.7 0-41.4-41.4c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l96 96c12.5 12.5 12.5 32.8 0 45.3zm-397.3 352l-96-96c-12.5-12.5-12.5-32.8 0-45.3l96-96c12.5-12.5 32.8-12.5 45.3 0s12.5 32.8 0 45.3L109.3 352 480 352c17.7 0 32 14.3 32 32s-14.3 32-32 32l-370.7 0 41.4 41.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0z"]},zg={prefix:"fas",iconName:"caret-up",icon:[320,512,[],"f0d8","M140.3 135.2c12.6-10.3 31.1-9.5 42.8 2.2l128 128c9.2 9.2 11.9 22.9 6.9 34.9S301.4 320 288.5 320l-256 0c-12.9 0-24.6-7.8-29.6-19.8S.7 274.5 9.9 265.4l128-128 2.4-2.2z"]},uC={prefix:"fas",iconName:"down-left-and-up-right-to-center",icon:[512,512,["compress-alt"],"f422","M439.5 7c9.4-9.4 24.6-9.4 33.9 0l32 32c9.4 9.4 9.4 24.6 0 33.9l-87 87 39 39c6.9 6.9 8.9 17.2 5.2 26.2S450.2 240 440.5 240l-144 0c-13.3 0-24-10.7-24-24l0-144c0-9.7 5.8-18.5 14.8-22.2s19.3-1.7 26.2 5.2l39 39 87-87zM72.5 272l144 0c13.3 0 24 10.7 24 24l0 144c0 9.7-5.8 18.5-14.8 22.2s-19.3 1.7-26.2-5.2l-39-39-87 87c-9.4 9.4-24.6 9.4-33.9 0l-32-32c-9.4-9.4-9.4-24.6 0-33.9l87-87-39-39c-6.9-6.9-8.9-17.2-5.2-26.2S62.8 272 72.5 272z"]},il={prefix:"fas",iconName:"plus",icon:[448,512,[10133,61543,"add"],"2b","M256 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 160-160 0c-17.7 0-32 14.3-32 32s14.3 32 32 32l160 0 0 160c0 17.7 14.3 32 32 32s32-14.3 32-32l0-160 160 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-160 0 0-160z"]},Ri={prefix:"fas",iconName:"copy",icon:[448,512,[],"f0c5","M192 0c-35.3 0-64 28.7-64 64l0 256c0 35.3 28.7 64 64 64l192 0c35.3 0 64-28.7 64-64l0-200.6c0-17.4-7.1-34.1-19.7-46.2L370.6 17.8C358.7 6.4 342.8 0 326.3 0L192 0zM64 128c-35.3 0-64 28.7-64 64L0 448c0 35.3 28.7 64 64 64l192 0c35.3 0 64-28.7 64-64l0-16-64 0 0 16-192 0 0-256 16 0 0-64-16 0z"]},dC={prefix:"fas",iconName:"arrow-rotate-right",icon:[512,512,[8635,"arrow-right-rotate","arrow-rotate-forward","redo"],"f01e","M436.7 74.7L448 85.4 448 32c0-17.7 14.3-32 32-32s32 14.3 32 32l0 128c0 17.7-14.3 32-32 32l-128 0c-17.7 0-32-14.3-32-32s14.3-32 32-32l47.9 0-7.6-7.2c-.2-.2-.4-.4-.6-.6-75-75-196.5-75-271.5 0s-75 196.5 0 271.5 196.5 75 271.5 0c8.2-8.2 15.5-16.9 21.9-26.1 10.1-14.5 30.1-18 44.6-7.9s18 30.1 7.9 44.6c-8.5 12.2-18.2 23.8-29.1 34.7-100 100-262.1 100-362 0S-25 175 75 75c99.9-99.9 261.7-100 361.7-.3z"]},zp=dC,di={prefix:"fas",iconName:"caret-down",icon:[320,512,[],"f0d7","M140.3 376.8c12.6 10.2 31.1 9.5 42.8-2.2l128-128c9.2-9.2 11.9-22.9 6.9-34.9S301.4 192 288.5 192l-256 0c-12.9 0-24.6 7.8-29.6 19.8S.7 237.5 9.9 246.6l128 128 2.4 2.2z"]},vC={prefix:"fas",iconName:"arrow-rotate-left",icon:[512,512,[8634,"arrow-left-rotate","arrow-rotate-back","arrow-rotate-backward","undo"],"f0e2","M256 64c-56.8 0-107.9 24.7-143.1 64l47.1 0c17.7 0 32 14.3 32 32s-14.3 32-32 32L32 192c-17.7 0-32-14.3-32-32L0 32C0 14.3 14.3 0 32 0S64 14.3 64 32l0 54.7C110.9 33.6 179.5 0 256 0 397.4 0 512 114.6 512 256S397.4 512 256 512c-87 0-163.9-43.4-210.1-109.7-10.1-14.5-6.6-34.4 7.9-44.6s34.4-6.6 44.6 7.9c34.8 49.8 92.4 82.3 157.6 82.3 106 0 192-86 192-192S362 64 256 64z"]},Pp=vC,ab={prefix:"fas",iconName:"square",icon:[448,512,[9632,9723,9724,61590],"f0c8","M64 32l320 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96C0 60.7 28.7 32 64 32z"]},Pg={prefix:"fas",iconName:"arrow-down",icon:[384,512,[8595],"f063","M169.4 502.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 402.7 224 32c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 370.7-105.4-105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"]},ib={exports:{}};/*
 * @version    1.4.0
 * @date       2015-10-26
 * @stability  3 - Stable
 * @author     Lauri Rooden (https://github.com/litejs/natural-compare-lite)
 * @license    MIT License
 */var Ng=function(e,t){var n,o,i=1,a=0,s=0,l=String.alphabet;function c(u,d,v){if(v){for(n=d;v=c(u,n),v<76&&v>65;)++n;return+u.slice(d-1,n)}return v=l&&l.indexOf(u.charAt(d)),v>-1?v+76:(v=u.charCodeAt(d)||0,v<45||v>127?v:v<46?65:v<48?v-1:v<58?v+18:v<65?v-11:v<91?v+11:v<97?v-37:v<123?v+5:v-63)}if((e+="")!=(t+="")){for(;i;)if(o=c(e,a++),i=c(t,s++),o<76&&i<76&&o>66&&i>66&&(o=c(e,a,a),i=c(t,s,a=n),s=n),o!=i)return o<i?-1:1}return 0};try{ib.exports=Ng}catch{String.naturalCompare=Ng}var fC=ib.exports;const pC=ux(fC);var Rg=Number.isNaN||function(t){return typeof t=="number"&&t!==t};function hC(e,t){return!!(e===t||Rg(e)&&Rg(t))}function gC(e,t){if(e.length!==t.length)return!1;for(var n=0;n<e.length;n++)if(!hC(e[n],t[n]))return!1;return!0}function Ec(e,t){t===void 0&&(t=gC);var n=null;function o(){for(var i=[],a=0;a<arguments.length;a++)i[a]=arguments[a];if(n&&n.lastThis===this&&t(i,n.lastArgs))return n.lastResult;var s=e.apply(this,i);return n={lastResult:s,lastArgs:i,lastThis:this},s}return o.clear=function(){n=null},o}var mC={};(function(e){(function(t){function n(S){return S!==null?Object.prototype.toString.call(S)==="[object Array]":!1}function o(S){return S!==null?Object.prototype.toString.call(S)==="[object Object]":!1}function i(S,$){if(S===$)return!0;var N=Object.prototype.toString.call(S);if(N!==Object.prototype.toString.call($))return!1;if(n(S)===!0){if(S.length!==$.length)return!1;for(var G=0;G<S.length;G++)if(i(S[G],$[G])===!1)return!1;return!0}if(o(S)===!0){var W={};for(var de in S)if(hasOwnProperty.call(S,de)){if(i(S[de],$[de])===!1)return!1;W[de]=!0}for(var Me in $)if(hasOwnProperty.call($,Me)&&W[Me]!==!0)return!1;return!0}return!1}function a(S){if(S===""||S===!1||S===null)return!0;if(n(S)&&S.length===0)return!0;if(o(S)){for(var $ in S)if(S.hasOwnProperty($))return!1;return!0}else return!1}function s(S){for(var $=Object.keys(S),N=[],G=0;G<$.length;G++)N.push(S[$[G]]);return N}var l;typeof String.prototype.trimLeft=="function"?l=function(S){return S.trimLeft()}:l=function(S){return S.match(/^\s*(.*)/)[1]};var c=0,u=1,d=2,v=3,f=4,h=5,p=6,y=7,j=8,b=9,k={0:"number",1:"any",2:"string",3:"array",4:"object",5:"boolean",6:"expression",7:"null",8:"Array<number>",9:"Array<string>"},E="EOF",O="UnquotedIdentifier",w="QuotedIdentifier",_="Rbracket",A="Rparen",q="Comma",C="Colon",z="Rbrace",D="Number",H="Current",Q="Expref",fe="Pipe",Ie="Or",ge="And",qe="EQ",ce="GT",ve="LT",he="GTE",Ue="LTE",Re="NE",we="Flatten",ue="Star",ie="Filter",vt="Dot",ft="Not",kt="Lbrace",oe="Lbracket",Ze="Lparen",te="Literal",X={".":vt,"*":ue,",":q,":":C,"{":kt,"}":z,"]":_,"(":Ze,")":A,"@":H},B={"<":!0,">":!0,"=":!0,"!":!0},Ne={" ":!0,"	":!0,"\n":!0};function ee(S){return S>="a"&&S<="z"||S>="A"&&S<="Z"||S==="_"}function L(S){return S>="0"&&S<="9"||S==="-"}function pt(S){return S>="a"&&S<="z"||S>="A"&&S<="Z"||S>="0"&&S<="9"||S==="_"}function ht(){}ht.prototype={tokenize:function(S){var $=[];this._current=0;for(var N,G,W;this._current<S.length;)if(ee(S[this._current]))N=this._current,G=this._consumeUnquotedIdentifier(S),$.push({type:O,value:G,start:N});else if(X[S[this._current]]!==void 0)$.push({type:X[S[this._current]],value:S[this._current],start:this._current}),this._current++;else if(L(S[this._current]))W=this._consumeNumber(S),$.push(W);else if(S[this._current]==="[")W=this._consumeLBracket(S),$.push(W);else if(S[this._current]==='"')N=this._current,G=this._consumeQuotedIdentifier(S),$.push({type:w,value:G,start:N});else if(S[this._current]==="'")N=this._current,G=this._consumeRawStringLiteral(S),$.push({type:te,value:G,start:N});else if(S[this._current]==="`"){N=this._current;var de=this._consumeLiteral(S);$.push({type:te,value:de,start:N})}else if(B[S[this._current]]!==void 0)$.push(this._consumeOperator(S));else if(Ne[S[this._current]]!==void 0)this._current++;else if(S[this._current]==="&")N=this._current,this._current++,S[this._current]==="&"?(this._current++,$.push({type:ge,value:"&&",start:N})):$.push({type:Q,value:"&",start:N});else if(S[this._current]==="|")N=this._current,this._current++,S[this._current]==="|"?(this._current++,$.push({type:Ie,value:"||",start:N})):$.push({type:fe,value:"|",start:N});else{var Me=new Error("Unknown character:"+S[this._current]);throw Me.name="LexerError",Me}return $},_consumeUnquotedIdentifier:function(S){var $=this._current;for(this._current++;this._current<S.length&&pt(S[this._current]);)this._current++;return S.slice($,this._current)},_consumeQuotedIdentifier:function(S){var $=this._current;this._current++;for(var N=S.length;S[this._current]!=='"'&&this._current<N;){var G=this._current;S[G]==="\\"&&(S[G+1]==="\\"||S[G+1]==='"')?G+=2:G++,this._current=G}return this._current++,JSON.parse(S.slice($,this._current))},_consumeRawStringLiteral:function(S){var $=this._current;this._current++;for(var N=S.length;S[this._current]!=="'"&&this._current<N;){var G=this._current;S[G]==="\\"&&(S[G+1]==="\\"||S[G+1]==="'")?G+=2:G++,this._current=G}this._current++;var W=S.slice($+1,this._current-1);return W.replace("\\'","'")},_consumeNumber:function(S){var $=this._current;this._current++;for(var N=S.length;L(S[this._current])&&this._current<N;)this._current++;var G=parseInt(S.slice($,this._current));return{type:D,value:G,start:$}},_consumeLBracket:function(S){var $=this._current;return this._current++,S[this._current]==="?"?(this._current++,{type:ie,value:"[?",start:$}):S[this._current]==="]"?(this._current++,{type:we,value:"[]",start:$}):{type:oe,value:"[",start:$}},_consumeOperator:function(S){var $=this._current,N=S[$];if(this._current++,N==="!")return S[this._current]==="="?(this._current++,{type:Re,value:"!=",start:$}):{type:ft,value:"!",start:$};if(N==="<")return S[this._current]==="="?(this._current++,{type:Ue,value:"<=",start:$}):{type:ve,value:"<",start:$};if(N===">")return S[this._current]==="="?(this._current++,{type:he,value:">=",start:$}):{type:ce,value:">",start:$};if(N==="="&&S[this._current]==="=")return this._current++,{type:qe,value:"==",start:$}},_consumeLiteral:function(S){this._current++;for(var $=this._current,N=S.length,G;S[this._current]!=="`"&&this._current<N;){var W=this._current;S[W]==="\\"&&(S[W+1]==="\\"||S[W+1]==="`")?W+=2:W++,this._current=W}var de=l(S.slice($,this._current));return de=de.replace("\\`","`"),this._looksLikeJSON(de)?G=JSON.parse(de):G=JSON.parse('"'+de+'"'),this._current++,G},_looksLikeJSON:function(S){var $='[{"',N=["true","false","null"],G="-0123456789";if(S==="")return!1;if($.indexOf(S[0])>=0)return!0;if(N.indexOf(S)>=0)return!0;if(G.indexOf(S[0])>=0)try{return JSON.parse(S),!0}catch{return!1}else return!1}};var _e={};_e[E]=0,_e[O]=0,_e[w]=0,_e[_]=0,_e[A]=0,_e[q]=0,_e[z]=0,_e[D]=0,_e[H]=0,_e[Q]=0,_e[fe]=1,_e[Ie]=2,_e[ge]=3,_e[qe]=5,_e[ce]=5,_e[ve]=5,_e[he]=5,_e[Ue]=5,_e[Re]=5,_e[we]=9,_e[ue]=20,_e[ie]=21,_e[vt]=40,_e[ft]=45,_e[kt]=50,_e[oe]=55,_e[Ze]=60;function at(){}at.prototype={parse:function(S){this._loadTokens(S),this.index=0;var $=this.expression(0);if(this._lookahead(0)!==E){var N=this._lookaheadToken(0),G=new Error("Unexpected token type: "+N.type+", value: "+N.value);throw G.name="ParserError",G}return $},_loadTokens:function(S){var $=new ht,N=$.tokenize(S);N.push({type:E,value:"",start:S.length}),this.tokens=N},expression:function(S){var $=this._lookaheadToken(0);this._advance();for(var N=this.nud($),G=this._lookahead(0);S<_e[G];)this._advance(),N=this.led(G,N),G=this._lookahead(0);return N},_lookahead:function(S){return this.tokens[this.index+S].type},_lookaheadToken:function(S){return this.tokens[this.index+S]},_advance:function(){this.index++},nud:function(S){var $,N,G;switch(S.type){case te:return{type:"Literal",value:S.value};case O:return{type:"Field",name:S.value};case w:var W={type:"Field",name:S.value};if(this._lookahead(0)===Ze)throw new Error("Quoted identifier not allowed for function names.");return W;case ft:return N=this.expression(_e.Not),{type:"NotExpression",children:[N]};case ue:return $={type:"Identity"},N=null,this._lookahead(0)===_?N={type:"Identity"}:N=this._parseProjectionRHS(_e.Star),{type:"ValueProjection",children:[$,N]};case ie:return this.led(S.type,{type:"Identity"});case kt:return this._parseMultiselectHash();case we:return $={type:we,children:[{type:"Identity"}]},N=this._parseProjectionRHS(_e.Flatten),{type:"Projection",children:[$,N]};case oe:return this._lookahead(0)===D||this._lookahead(0)===C?(N=this._parseIndexExpression(),this._projectIfSlice({type:"Identity"},N)):this._lookahead(0)===ue&&this._lookahead(1)===_?(this._advance(),this._advance(),N=this._parseProjectionRHS(_e.Star),{type:"Projection",children:[{type:"Identity"},N]}):this._parseMultiselectList();case H:return{type:H};case Q:return G=this.expression(_e.Expref),{type:"ExpressionReference",children:[G]};case Ze:for(var de=[];this._lookahead(0)!==A;)this._lookahead(0)===H?(G={type:H},this._advance()):G=this.expression(0),de.push(G);return this._match(A),de[0];default:this._errorToken(S)}},led:function(S,$){var N;switch(S){case vt:var G=_e.Dot;return this._lookahead(0)!==ue?(N=this._parseDotRHS(G),{type:"Subexpression",children:[$,N]}):(this._advance(),N=this._parseProjectionRHS(G),{type:"ValueProjection",children:[$,N]});case fe:return N=this.expression(_e.Pipe),{type:fe,children:[$,N]};case Ie:return N=this.expression(_e.Or),{type:"OrExpression",children:[$,N]};case ge:return N=this.expression(_e.And),{type:"AndExpression",children:[$,N]};case Ze:for(var W=$.name,de=[],Me,pe;this._lookahead(0)!==A;)this._lookahead(0)===H?(Me={type:H},this._advance()):Me=this.expression(0),this._lookahead(0)===q&&this._match(q),de.push(Me);return this._match(A),pe={type:"Function",name:W,children:de},pe;case ie:var le=this.expression(0);return this._match(_),this._lookahead(0)===we?N={type:"Identity"}:N=this._parseProjectionRHS(_e.Filter),{type:"FilterProjection",children:[$,N,le]};case we:var St={type:we,children:[$]},lt=this._parseProjectionRHS(_e.Flatten);return{type:"Projection",children:[St,lt]};case qe:case Re:case ce:case he:case ve:case Ue:return this._parseComparator($,S);case oe:var Xe=this._lookaheadToken(0);return Xe.type===D||Xe.type===C?(N=this._parseIndexExpression(),this._projectIfSlice($,N)):(this._match(ue),this._match(_),N=this._parseProjectionRHS(_e.Star),{type:"Projection",children:[$,N]});default:this._errorToken(this._lookaheadToken(0))}},_match:function(S){if(this._lookahead(0)===S)this._advance();else{var $=this._lookaheadToken(0),N=new Error("Expected "+S+", got: "+$.type);throw N.name="ParserError",N}},_errorToken:function(S){var $=new Error("Invalid token ("+S.type+'): "'+S.value+'"');throw $.name="ParserError",$},_parseIndexExpression:function(){if(this._lookahead(0)===C||this._lookahead(1)===C)return this._parseSliceExpression();var S={type:"Index",value:this._lookaheadToken(0).value};return this._advance(),this._match(_),S},_projectIfSlice:function(S,$){var N={type:"IndexExpression",children:[S,$]};return $.type==="Slice"?{type:"Projection",children:[N,this._parseProjectionRHS(_e.Star)]}:N},_parseSliceExpression:function(){for(var S=[null,null,null],$=0,N=this._lookahead(0);N!==_&&$<3;){if(N===C)$++,this._advance();else if(N===D)S[$]=this._lookaheadToken(0).value,this._advance();else{var G=this._lookahead(0),W=new Error("Syntax error, unexpected token: "+G.value+"("+G.type+")");throw W.name="Parsererror",W}N=this._lookahead(0)}return this._match(_),{type:"Slice",children:S}},_parseComparator:function(S,$){var N=this.expression(_e[$]);return{type:"Comparator",name:$,children:[S,N]}},_parseDotRHS:function(S){var $=this._lookahead(0),N=[O,w,ue];if(N.indexOf($)>=0)return this.expression(S);if($===oe)return this._match(oe),this._parseMultiselectList();if($===kt)return this._match(kt),this._parseMultiselectHash()},_parseProjectionRHS:function(S){var $;if(_e[this._lookahead(0)]<10)$={type:"Identity"};else if(this._lookahead(0)===oe)$=this.expression(S);else if(this._lookahead(0)===ie)$=this.expression(S);else if(this._lookahead(0)===vt)this._match(vt),$=this._parseDotRHS(S);else{var N=this._lookaheadToken(0),G=new Error("Sytanx error, unexpected token: "+N.value+"("+N.type+")");throw G.name="ParserError",G}return $},_parseMultiselectList:function(){for(var S=[];this._lookahead(0)!==_;){var $=this.expression(0);if(S.push($),this._lookahead(0)===q&&(this._match(q),this._lookahead(0)===_))throw new Error("Unexpected token Rbracket")}return this._match(_),{type:"MultiSelectList",children:S}},_parseMultiselectHash:function(){for(var S=[],$=[O,w],N,G,W,de;;){if(N=this._lookaheadToken(0),$.indexOf(N.type)<0)throw new Error("Expecting an identifier token, got: "+N.type);if(G=N.value,this._advance(),this._match(C),W=this.expression(0),de={type:"KeyValuePair",name:G,value:W},S.push(de),this._lookahead(0)===q)this._match(q);else if(this._lookahead(0)===z){this._match(z);break}}return{type:"MultiSelectHash",children:S}}};function We(S){this.runtime=S}We.prototype={search:function(S,$){return this.visit(S,$)},visit:function(S,$){var N,G,W,de,Me,pe,le,St,lt,Xe;switch(S.type){case"Field":return $!==null&&o($)?(pe=$[S.name],pe===void 0?null:pe):null;case"Subexpression":for(W=this.visit(S.children[0],$),Xe=1;Xe<S.children.length;Xe++)if(W=this.visit(S.children[1],W),W===null)return null;return W;case"IndexExpression":return le=this.visit(S.children[0],$),St=this.visit(S.children[1],le),St;case"Index":if(!n($))return null;var Ae=S.value;return Ae<0&&(Ae=$.length+Ae),W=$[Ae],W===void 0&&(W=null),W;case"Slice":if(!n($))return null;var $t=S.children.slice(0),sn=this.computeSliceParams($.length,$t),Un=sn[0],Yt=sn[1],Zt=sn[2];if(W=[],Zt>0)for(Xe=Un;Xe<Yt;Xe+=Zt)W.push($[Xe]);else for(Xe=Un;Xe>Yt;Xe+=Zt)W.push($[Xe]);return W;case"Projection":var Dt=this.visit(S.children[0],$);if(!n(Dt))return null;for(lt=[],Xe=0;Xe<Dt.length;Xe++)G=this.visit(S.children[1],Dt[Xe]),G!==null&&lt.push(G);return lt;case"ValueProjection":if(Dt=this.visit(S.children[0],$),!o(Dt))return null;lt=[];var hn=s(Dt);for(Xe=0;Xe<hn.length;Xe++)G=this.visit(S.children[1],hn[Xe]),G!==null&&lt.push(G);return lt;case"FilterProjection":if(Dt=this.visit(S.children[0],$),!n(Dt))return null;var Hn=[],J=[];for(Xe=0;Xe<Dt.length;Xe++)N=this.visit(S.children[2],Dt[Xe]),a(N)||Hn.push(Dt[Xe]);for(var V=0;V<Hn.length;V++)G=this.visit(S.children[1],Hn[V]),G!==null&&J.push(G);return J;case"Comparator":switch(de=this.visit(S.children[0],$),Me=this.visit(S.children[1],$),S.name){case qe:W=i(de,Me);break;case Re:W=!i(de,Me);break;case ce:W=de>Me;break;case he:W=de>=Me;break;case ve:W=de<Me;break;case Ue:W=de<=Me;break;default:throw new Error("Unknown comparator: "+S.name)}return W;case we:var Ve=this.visit(S.children[0],$);if(!n(Ve))return null;var ye=[];for(Xe=0;Xe<Ve.length;Xe++)G=Ve[Xe],n(G)?ye.push.apply(ye,G):ye.push(G);return ye;case"Identity":return $;case"MultiSelectList":if($===null)return null;for(lt=[],Xe=0;Xe<S.children.length;Xe++)lt.push(this.visit(S.children[Xe],$));return lt;case"MultiSelectHash":if($===null)return null;lt={};var rt;for(Xe=0;Xe<S.children.length;Xe++)rt=S.children[Xe],lt[rt.name]=this.visit(rt.value,$);return lt;case"OrExpression":return N=this.visit(S.children[0],$),a(N)&&(N=this.visit(S.children[1],$)),N;case"AndExpression":return de=this.visit(S.children[0],$),a(de)===!0?de:this.visit(S.children[1],$);case"NotExpression":return de=this.visit(S.children[0],$),a(de);case"Literal":return S.value;case fe:return le=this.visit(S.children[0],$),this.visit(S.children[1],le);case H:return $;case"Function":var dt=[];for(Xe=0;Xe<S.children.length;Xe++)dt.push(this.visit(S.children[Xe],$));return this.runtime.callFunction(S.name,dt);case"ExpressionReference":var At=S.children[0];return At.jmespathType=Q,At;default:throw new Error("Unknown node type: "+S.type)}},computeSliceParams:function(S,$){var N=$[0],G=$[1],W=$[2],de=[null,null,null];if(W===null)W=1;else if(W===0){var Me=new Error("Invalid slice, step cannot be 0");throw Me.name="RuntimeError",Me}var pe=W<0;return N===null?N=pe?S-1:0:N=this.capSliceRange(S,N,W),G===null?G=pe?-1:S:G=this.capSliceRange(S,G,W),de[0]=N,de[1]=G,de[2]=W,de},capSliceRange:function(S,$,N){return $<0?($+=S,$<0&&($=N<0?-1:0)):$>=S&&($=N<0?S-1:S),$}};function Ye(S){this._interpreter=S,this.functionTable={abs:{_func:this._functionAbs,_signature:[{types:[c]}]},avg:{_func:this._functionAvg,_signature:[{types:[j]}]},ceil:{_func:this._functionCeil,_signature:[{types:[c]}]},contains:{_func:this._functionContains,_signature:[{types:[d,v]},{types:[u]}]},ends_with:{_func:this._functionEndsWith,_signature:[{types:[d]},{types:[d]}]},floor:{_func:this._functionFloor,_signature:[{types:[c]}]},length:{_func:this._functionLength,_signature:[{types:[d,v,f]}]},map:{_func:this._functionMap,_signature:[{types:[p]},{types:[v]}]},max:{_func:this._functionMax,_signature:[{types:[j,b]}]},merge:{_func:this._functionMerge,_signature:[{types:[f],variadic:!0}]},max_by:{_func:this._functionMaxBy,_signature:[{types:[v]},{types:[p]}]},sum:{_func:this._functionSum,_signature:[{types:[j]}]},starts_with:{_func:this._functionStartsWith,_signature:[{types:[d]},{types:[d]}]},min:{_func:this._functionMin,_signature:[{types:[j,b]}]},min_by:{_func:this._functionMinBy,_signature:[{types:[v]},{types:[p]}]},type:{_func:this._functionType,_signature:[{types:[u]}]},keys:{_func:this._functionKeys,_signature:[{types:[f]}]},values:{_func:this._functionValues,_signature:[{types:[f]}]},sort:{_func:this._functionSort,_signature:[{types:[b,j]}]},sort_by:{_func:this._functionSortBy,_signature:[{types:[v]},{types:[p]}]},join:{_func:this._functionJoin,_signature:[{types:[d]},{types:[b]}]},reverse:{_func:this._functionReverse,_signature:[{types:[d,v]}]},to_array:{_func:this._functionToArray,_signature:[{types:[u]}]},to_string:{_func:this._functionToString,_signature:[{types:[u]}]},to_number:{_func:this._functionToNumber,_signature:[{types:[u]}]},not_null:{_func:this._functionNotNull,_signature:[{types:[u],variadic:!0}]}}}Ye.prototype={callFunction:function(S,$){var N=this.functionTable[S];if(N===void 0)throw new Error("Unknown function: "+S+"()");return this._validateArgs(S,$,N._signature),N._func.call(this,$)},_validateArgs:function(S,$,N){var G;if(N[N.length-1].variadic){if($.length<N.length)throw G=N.length===1?" argument":" arguments",new Error("ArgumentError: "+S+"() takes at least"+N.length+G+" but received "+$.length)}else if($.length!==N.length)throw G=N.length===1?" argument":" arguments",new Error("ArgumentError: "+S+"() takes "+N.length+G+" but received "+$.length);for(var W,de,Me,pe=0;pe<N.length;pe++){Me=!1,W=N[pe].types,de=this._getTypeName($[pe]);for(var le=0;le<W.length;le++)if(this._typeMatches(de,W[le],$[pe])){Me=!0;break}if(!Me){var St=W.map(function(lt){return k[lt]}).join(",");throw new Error("TypeError: "+S+"() expected argument "+(pe+1)+" to be type "+St+" but received type "+k[de]+" instead.")}}},_typeMatches:function(S,$,N){if($===u)return!0;if($===b||$===j||$===v){if($===v)return S===v;if(S===v){var G;$===j?G=c:$===b&&(G=d);for(var W=0;W<N.length;W++)if(!this._typeMatches(this._getTypeName(N[W]),G,N[W]))return!1;return!0}}else return S===$},_getTypeName:function(S){switch(Object.prototype.toString.call(S)){case"[object String]":return d;case"[object Number]":return c;case"[object Array]":return v;case"[object Boolean]":return h;case"[object Null]":return y;case"[object Object]":return S.jmespathType===Q?p:f}},_functionStartsWith:function(S){return S[0].lastIndexOf(S[1])===0},_functionEndsWith:function(S){var $=S[0],N=S[1];return $.indexOf(N,$.length-N.length)!==-1},_functionReverse:function(S){var $=this._getTypeName(S[0]);if($===d){for(var N=S[0],G="",W=N.length-1;W>=0;W--)G+=N[W];return G}else{var de=S[0].slice(0);return de.reverse(),de}},_functionAbs:function(S){return Math.abs(S[0])},_functionCeil:function(S){return Math.ceil(S[0])},_functionAvg:function(S){for(var $=0,N=S[0],G=0;G<N.length;G++)$+=N[G];return $/N.length},_functionContains:function(S){return S[0].indexOf(S[1])>=0},_functionFloor:function(S){return Math.floor(S[0])},_functionLength:function(S){return o(S[0])?Object.keys(S[0]).length:S[0].length},_functionMap:function(S){for(var $=[],N=this._interpreter,G=S[0],W=S[1],de=0;de<W.length;de++)$.push(N.visit(G,W[de]));return $},_functionMerge:function(S){for(var $={},N=0;N<S.length;N++){var G=S[N];for(var W in G)$[W]=G[W]}return $},_functionMax:function(S){if(S[0].length>0){var $=this._getTypeName(S[0][0]);if($===c)return Math.max.apply(Math,S[0]);for(var N=S[0],G=N[0],W=1;W<N.length;W++)G.localeCompare(N[W])<0&&(G=N[W]);return G}else return null},_functionMin:function(S){if(S[0].length>0){var $=this._getTypeName(S[0][0]);if($===c)return Math.min.apply(Math,S[0]);for(var N=S[0],G=N[0],W=1;W<N.length;W++)N[W].localeCompare(G)<0&&(G=N[W]);return G}else return null},_functionSum:function(S){for(var $=0,N=S[0],G=0;G<N.length;G++)$+=N[G];return $},_functionType:function(S){switch(this._getTypeName(S[0])){case c:return"number";case d:return"string";case v:return"array";case f:return"object";case h:return"boolean";case p:return"expref";case y:return"null"}},_functionKeys:function(S){return Object.keys(S[0])},_functionValues:function(S){for(var $=S[0],N=Object.keys($),G=[],W=0;W<N.length;W++)G.push($[N[W]]);return G},_functionJoin:function(S){var $=S[0],N=S[1];return N.join($)},_functionToArray:function(S){return this._getTypeName(S[0])===v?S[0]:[S[0]]},_functionToString:function(S){return this._getTypeName(S[0])===d?S[0]:JSON.stringify(S[0])},_functionToNumber:function(S){var $=this._getTypeName(S[0]),N;return $===c?S[0]:$===d&&(N=+S[0],!isNaN(N))?N:null},_functionNotNull:function(S){for(var $=0;$<S.length;$++)if(this._getTypeName(S[$])!==y)return S[$];return null},_functionSort:function(S){var $=S[0].slice(0);return $.sort(),$},_functionSortBy:function(S){var $=S[0].slice(0);if($.length===0)return $;var N=this._interpreter,G=S[1],W=this._getTypeName(N.visit(G,$[0]));if([c,d].indexOf(W)<0)throw new Error("TypeError");for(var de=this,Me=[],pe=0;pe<$.length;pe++)Me.push([pe,$[pe]]);Me.sort(function(St,lt){var Xe=N.visit(G,St[1]),Ae=N.visit(G,lt[1]);if(de._getTypeName(Xe)!==W)throw new Error("TypeError: expected "+W+", received "+de._getTypeName(Xe));if(de._getTypeName(Ae)!==W)throw new Error("TypeError: expected "+W+", received "+de._getTypeName(Ae));return Xe>Ae?1:Xe<Ae?-1:St[0]-lt[0]});for(var le=0;le<Me.length;le++)$[le]=Me[le][1];return $},_functionMaxBy:function(S){for(var $=S[1],N=S[0],G=this.createKeyFunction($,[c,d]),W=-1/0,de,Me,pe=0;pe<N.length;pe++)Me=G(N[pe]),Me>W&&(W=Me,de=N[pe]);return de},_functionMinBy:function(S){for(var $=S[1],N=S[0],G=this.createKeyFunction($,[c,d]),W=1/0,de,Me,pe=0;pe<N.length;pe++)Me=G(N[pe]),Me<W&&(W=Me,de=N[pe]);return de},createKeyFunction:function(S,$){var N=this,G=this._interpreter,W=function(de){var Me=G.visit(S,de);if($.indexOf(N._getTypeName(Me))<0){var pe="TypeError: expected one of "+$+", received "+N._getTypeName(Me);throw new Error(pe)}return Me};return W}};function Tt(S){var $=new at,N=$.parse(S);return N}function He(S){var $=new ht;return $.tokenize(S)}function qt(S,$){var N=new at,G=new Ye,W=new We(G);G._interpreter=W;var de=N.parse($);return W.search(de,S)}t.tokenize=He,t.compile=Tt,t.search=qt,t.strictDeepEqual=i})(e)})(mC);class bC{add(t,n,o){if(typeof arguments[0]!="string")for(let i in arguments[0])this.add(i,arguments[0][i],arguments[1]);else(Array.isArray(t)?t:[t]).forEach(function(i){this[i]=this[i]||[],n&&this[i][o?"unshift":"push"](n)},this)}run(t,n){this[t]=this[t]||[],this[t].forEach(function(o){o.call(n&&n.context?n.context:n,n)})}}class yC{constructor(t){this.jsep=t,this.registered={}}register(){for(var t=arguments.length,n=new Array(t),o=0;o<t;o++)n[o]=arguments[o];n.forEach(i=>{if(typeof i!="object"||!i.name||!i.init)throw new Error("Invalid JSEP plugin format");this.registered[i.name]||(i.init(this.jsep),this.registered[i.name]=i)})}}class me{static get version(){return"1.4.0"}static toString(){return"JavaScript Expression Parser (JSEP) v"+me.version}static addUnaryOp(t){return me.max_unop_len=Math.max(t.length,me.max_unop_len),me.unary_ops[t]=1,me}static addBinaryOp(t,n,o){return me.max_binop_len=Math.max(t.length,me.max_binop_len),me.binary_ops[t]=n,o?me.right_associative.add(t):me.right_associative.delete(t),me}static addIdentifierChar(t){return me.additional_identifier_chars.add(t),me}static addLiteral(t,n){return me.literals[t]=n,me}static removeUnaryOp(t){return delete me.unary_ops[t],t.length===me.max_unop_len&&(me.max_unop_len=me.getMaxKeyLen(me.unary_ops)),me}static removeAllUnaryOps(){return me.unary_ops={},me.max_unop_len=0,me}static removeIdentifierChar(t){return me.additional_identifier_chars.delete(t),me}static removeBinaryOp(t){return delete me.binary_ops[t],t.length===me.max_binop_len&&(me.max_binop_len=me.getMaxKeyLen(me.binary_ops)),me.right_associative.delete(t),me}static removeAllBinaryOps(){return me.binary_ops={},me.max_binop_len=0,me}static removeLiteral(t){return delete me.literals[t],me}static removeAllLiterals(){return me.literals={},me}get char(){return this.expr.charAt(this.index)}get code(){return this.expr.charCodeAt(this.index)}constructor(t){this.expr=t,this.index=0}static parse(t){return new me(t).parse()}static getMaxKeyLen(t){return Math.max(0,...Object.keys(t).map(n=>n.length))}static isDecimalDigit(t){return t>=48&&t<=57}static binaryPrecedence(t){return me.binary_ops[t]||0}static isIdentifierStart(t){return t>=65&&t<=90||t>=97&&t<=122||t>=128&&!me.binary_ops[String.fromCharCode(t)]||me.additional_identifier_chars.has(String.fromCharCode(t))}static isIdentifierPart(t){return me.isIdentifierStart(t)||me.isDecimalDigit(t)}throwError(t){const n=new Error(t+" at character "+this.index);throw n.index=this.index,n.description=t,n}runHook(t,n){if(me.hooks[t]){const o={context:this,node:n};return me.hooks.run(t,o),o.node}return n}searchHook(t){if(me.hooks[t]){const n={context:this};return me.hooks[t].find(function(o){return o.call(n.context,n),n.node}),n.node}}gobbleSpaces(){let t=this.code;for(;t===me.SPACE_CODE||t===me.TAB_CODE||t===me.LF_CODE||t===me.CR_CODE;)t=this.expr.charCodeAt(++this.index);this.runHook("gobble-spaces")}parse(){this.runHook("before-all");const t=this.gobbleExpressions(),n=t.length===1?t[0]:{type:me.COMPOUND,body:t};return this.runHook("after-all",n)}gobbleExpressions(t){let n=[],o,i;for(;this.index<this.expr.length;)if(o=this.code,o===me.SEMCOL_CODE||o===me.COMMA_CODE)this.index++;else if(i=this.gobbleExpression())n.push(i);else if(this.index<this.expr.length){if(o===t)break;this.throwError('Unexpected "'+this.char+'"')}return n}gobbleExpression(){const t=this.searchHook("gobble-expression")||this.gobbleBinaryExpression();return this.gobbleSpaces(),this.runHook("after-expression",t)}gobbleBinaryOp(){this.gobbleSpaces();let t=this.expr.substr(this.index,me.max_binop_len),n=t.length;for(;n>0;){if(me.binary_ops.hasOwnProperty(t)&&(!me.isIdentifierStart(this.code)||this.index+t.length<this.expr.length&&!me.isIdentifierPart(this.expr.charCodeAt(this.index+t.length))))return this.index+=n,t;t=t.substr(0,--n)}return!1}gobbleBinaryExpression(){let t,n,o,i,a,s,l,c,u;if(s=this.gobbleToken(),!s||(n=this.gobbleBinaryOp(),!n))return s;for(a={value:n,prec:me.binaryPrecedence(n),right_a:me.right_associative.has(n)},l=this.gobbleToken(),l||this.throwError("Expected expression after "+n),i=[s,a,l];n=this.gobbleBinaryOp();){if(o=me.binaryPrecedence(n),o===0){this.index-=n.length;break}a={value:n,prec:o,right_a:me.right_associative.has(n)},u=n;const d=v=>a.right_a&&v.right_a?o>v.prec:o<=v.prec;for(;i.length>2&&d(i[i.length-2]);)l=i.pop(),n=i.pop().value,s=i.pop(),t={type:me.BINARY_EXP,operator:n,left:s,right:l},i.push(t);t=this.gobbleToken(),t||this.throwError("Expected expression after "+u),i.push(a,t)}for(c=i.length-1,t=i[c];c>1;)t={type:me.BINARY_EXP,operator:i[c-1].value,left:i[c-2],right:t},c-=2;return t}gobbleToken(){let t,n,o,i;if(this.gobbleSpaces(),i=this.searchHook("gobble-token"),i)return this.runHook("after-token",i);if(t=this.code,me.isDecimalDigit(t)||t===me.PERIOD_CODE)return this.gobbleNumericLiteral();if(t===me.SQUOTE_CODE||t===me.DQUOTE_CODE)i=this.gobbleStringLiteral();else if(t===me.OBRACK_CODE)i=this.gobbleArray();else{for(n=this.expr.substr(this.index,me.max_unop_len),o=n.length;o>0;){if(me.unary_ops.hasOwnProperty(n)&&(!me.isIdentifierStart(this.code)||this.index+n.length<this.expr.length&&!me.isIdentifierPart(this.expr.charCodeAt(this.index+n.length)))){this.index+=o;const a=this.gobbleToken();return a||this.throwError("missing unaryOp argument"),this.runHook("after-token",{type:me.UNARY_EXP,operator:n,argument:a,prefix:!0})}n=n.substr(0,--o)}me.isIdentifierStart(t)?(i=this.gobbleIdentifier(),me.literals.hasOwnProperty(i.name)?i={type:me.LITERAL,value:me.literals[i.name],raw:i.name}:i.name===me.this_str&&(i={type:me.THIS_EXP})):t===me.OPAREN_CODE&&(i=this.gobbleGroup())}return i?(i=this.gobbleTokenProperty(i),this.runHook("after-token",i)):this.runHook("after-token",!1)}gobbleTokenProperty(t){this.gobbleSpaces();let n=this.code;for(;n===me.PERIOD_CODE||n===me.OBRACK_CODE||n===me.OPAREN_CODE||n===me.QUMARK_CODE;){let o;if(n===me.QUMARK_CODE){if(this.expr.charCodeAt(this.index+1)!==me.PERIOD_CODE)break;o=!0,this.index+=2,this.gobbleSpaces(),n=this.code}this.index++,n===me.OBRACK_CODE?(t={type:me.MEMBER_EXP,computed:!0,object:t,property:this.gobbleExpression()},t.property||this.throwError('Unexpected "'+this.char+'"'),this.gobbleSpaces(),n=this.code,n!==me.CBRACK_CODE&&this.throwError("Unclosed ["),this.index++):n===me.OPAREN_CODE?t={type:me.CALL_EXP,arguments:this.gobbleArguments(me.CPAREN_CODE),callee:t}:(n===me.PERIOD_CODE||o)&&(o&&this.index--,this.gobbleSpaces(),t={type:me.MEMBER_EXP,computed:!1,object:t,property:this.gobbleIdentifier()}),o&&(t.optional=!0),this.gobbleSpaces(),n=this.code}return t}gobbleNumericLiteral(){let t="",n,o;for(;me.isDecimalDigit(this.code);)t+=this.expr.charAt(this.index++);if(this.code===me.PERIOD_CODE)for(t+=this.expr.charAt(this.index++);me.isDecimalDigit(this.code);)t+=this.expr.charAt(this.index++);if(n=this.char,n==="e"||n==="E"){for(t+=this.expr.charAt(this.index++),n=this.char,(n==="+"||n==="-")&&(t+=this.expr.charAt(this.index++));me.isDecimalDigit(this.code);)t+=this.expr.charAt(this.index++);me.isDecimalDigit(this.expr.charCodeAt(this.index-1))||this.throwError("Expected exponent ("+t+this.char+")")}return o=this.code,me.isIdentifierStart(o)?this.throwError("Variable names cannot start with a number ("+t+this.char+")"):(o===me.PERIOD_CODE||t.length===1&&t.charCodeAt(0)===me.PERIOD_CODE)&&this.throwError("Unexpected period"),{type:me.LITERAL,value:parseFloat(t),raw:t}}gobbleStringLiteral(){let t="";const n=this.index,o=this.expr.charAt(this.index++);let i=!1;for(;this.index<this.expr.length;){let a=this.expr.charAt(this.index++);if(a===o){i=!0;break}else if(a==="\\")switch(a=this.expr.charAt(this.index++),a){case"n":t+=`
`;break;case"r":t+="\r";break;case"t":t+="	";break;case"b":t+="\b";break;case"f":t+="\f";break;case"v":t+="\v";break;default:t+=a}else t+=a}return i||this.throwError('Unclosed quote after "'+t+'"'),{type:me.LITERAL,value:t,raw:this.expr.substring(n,this.index)}}gobbleIdentifier(){let t=this.code,n=this.index;for(me.isIdentifierStart(t)?this.index++:this.throwError("Unexpected "+this.char);this.index<this.expr.length&&(t=this.code,me.isIdentifierPart(t));)this.index++;return{type:me.IDENTIFIER,name:this.expr.slice(n,this.index)}}gobbleArguments(t){const n=[];let o=!1,i=0;for(;this.index<this.expr.length;){this.gobbleSpaces();let a=this.code;if(a===t){o=!0,this.index++,t===me.CPAREN_CODE&&i&&i>=n.length&&this.throwError("Unexpected token "+String.fromCharCode(t));break}else if(a===me.COMMA_CODE){if(this.index++,i++,i!==n.length){if(t===me.CPAREN_CODE)this.throwError("Unexpected token ,");else if(t===me.CBRACK_CODE)for(let s=n.length;s<i;s++)n.push(null)}}else if(n.length!==i&&i!==0)this.throwError("Expected comma");else{const s=this.gobbleExpression();(!s||s.type===me.COMPOUND)&&this.throwError("Expected comma"),n.push(s)}}return o||this.throwError("Expected "+String.fromCharCode(t)),n}gobbleGroup(){this.index++;let t=this.gobbleExpressions(me.CPAREN_CODE);if(this.code===me.CPAREN_CODE)return this.index++,t.length===1?t[0]:t.length?{type:me.SEQUENCE_EXP,expressions:t}:!1;this.throwError("Unclosed (")}gobbleArray(){return this.index++,{type:me.ARRAY_EXP,elements:this.gobbleArguments(me.CBRACK_CODE)}}}const jC=new bC;Object.assign(me,{hooks:jC,plugins:new yC(me),COMPOUND:"Compound",SEQUENCE_EXP:"SequenceExpression",IDENTIFIER:"Identifier",MEMBER_EXP:"MemberExpression",LITERAL:"Literal",THIS_EXP:"ThisExpression",CALL_EXP:"CallExpression",UNARY_EXP:"UnaryExpression",BINARY_EXP:"BinaryExpression",ARRAY_EXP:"ArrayExpression",TAB_CODE:9,LF_CODE:10,CR_CODE:13,SPACE_CODE:32,PERIOD_CODE:46,COMMA_CODE:44,SQUOTE_CODE:39,DQUOTE_CODE:34,OPAREN_CODE:40,CPAREN_CODE:41,OBRACK_CODE:91,CBRACK_CODE:93,QUMARK_CODE:63,SEMCOL_CODE:59,COLON_CODE:58,unary_ops:{"-":1,"!":1,"~":1,"+":1},binary_ops:{"||":1,"??":1,"&&":2,"|":3,"^":4,"&":5,"==":6,"!=":6,"===":6,"!==":6,"<":7,">":7,"<=":7,">=":7,"<<":8,">>":8,">>>":8,"+":9,"-":9,"*":10,"/":10,"%":10,"**":11},right_associative:new Set(["**"]),additional_identifier_chars:new Set(["$","_"]),literals:{true:!0,false:!1,null:null},this_str:"this"});me.max_unop_len=me.getMaxKeyLen(me.unary_ops);me.max_binop_len=me.getMaxKeyLen(me.binary_ops);const vi=e=>new me(e).parse(),xC=Object.getOwnPropertyNames(class{});Object.getOwnPropertyNames(me).filter(e=>!xC.includes(e)&&vi[e]===void 0).forEach(e=>{vi[e]=me[e]});vi.Jsep=me;const wC="ConditionalExpression";var kC={name:"ternary",init(e){e.hooks.add("after-expression",function(n){if(n.node&&this.code===e.QUMARK_CODE){this.index++;const o=n.node,i=this.gobbleExpression();if(i||this.throwError("Expected expression"),this.gobbleSpaces(),this.code===e.COLON_CODE){this.index++;const a=this.gobbleExpression();if(a||this.throwError("Expected expression"),n.node={type:wC,test:o,consequent:i,alternate:a},o.operator&&e.binary_ops[o.operator]<=.9){let s=o;for(;s.right.operator&&e.binary_ops[s.right.operator]<=.9;)s=s.right;n.node.test=s.right,s.right=n.node,n.node=o}}else this.throwError("Expected :")}})}};vi.plugins.register(kC);const Ig=47,SC=92;var CC={name:"regex",init(e){e.hooks.add("gobble-token",function(n){if(this.code===Ig){const o=++this.index;let i=!1;for(;this.index<this.expr.length;){if(this.code===Ig&&!i){const a=this.expr.slice(o,this.index);let s="";for(;++this.index<this.expr.length;){const c=this.code;if(c>=97&&c<=122||c>=65&&c<=90||c>=48&&c<=57)s+=this.char;else break}let l;try{l=new RegExp(a,s)}catch(c){this.throwError(c.message)}return n.node={type:e.LITERAL,value:l,raw:this.expr.slice(o-1,this.index)},n.node=this.gobbleTokenProperty(n.node),n.node}this.code===e.OBRACK_CODE?i=!0:i&&this.code===e.CBRACK_CODE&&(i=!1),this.index+=this.code===SC?2:1}this.throwError("Unclosed Regex")}})}};const Ov=43,OC=45,tl={name:"assignment",assignmentOperators:new Set(["=","*=","**=","/=","%=","+=","-=","<<=",">>=",">>>=","&=","^=","|=","||=","&&=","??="]),updateOperators:[Ov,OC],assignmentPrecedence:.9,init(e){const t=[e.IDENTIFIER,e.MEMBER_EXP];tl.assignmentOperators.forEach(o=>e.addBinaryOp(o,tl.assignmentPrecedence,!0)),e.hooks.add("gobble-token",function(i){const a=this.code;tl.updateOperators.some(s=>s===a&&s===this.expr.charCodeAt(this.index+1))&&(this.index+=2,i.node={type:"UpdateExpression",operator:a===Ov?"++":"--",argument:this.gobbleTokenProperty(this.gobbleIdentifier()),prefix:!0},(!i.node.argument||!t.includes(i.node.argument.type))&&this.throwError(`Unexpected ${i.node.operator}`))}),e.hooks.add("after-token",function(i){if(i.node){const a=this.code;tl.updateOperators.some(s=>s===a&&s===this.expr.charCodeAt(this.index+1))&&(t.includes(i.node.type)||this.throwError(`Unexpected ${i.node.operator}`),this.index+=2,i.node={type:"UpdateExpression",operator:a===Ov?"++":"--",argument:i.node,prefix:!1})}}),e.hooks.add("after-expression",function(i){i.node&&n(i.node)});function n(o){tl.assignmentOperators.has(o.operator)?(o.type="AssignmentExpression",n(o.left),n(o.right)):o.operator||Object.values(o).forEach(i=>{i&&typeof i=="object"&&n(i)})}}};vi.plugins.register(CC,tl);vi.addUnaryOp("typeof");vi.addUnaryOp("void");vi.addLiteral("null",null);vi.addLiteral("undefined",void 0);const _C=yx({String:Io.string,Number:Io.number,"True False":Io.bool,PropertyName:Io.propertyName,Null:Io.null,", :":Io.separator,"[ ]":Io.squareBracket,"{ }":Io.brace}),EC=sw.deserialize({version:14,states:"$bOVQPOOOOQO'#Cb'#CbOnQPO'#CeOvQPO'#ClOOQO'#Cr'#CrQOQPOOOOQO'#Cg'#CgO}QPO'#CfO!SQPO'#CtOOQO,59P,59PO![QPO,59PO!aQPO'#CuOOQO,59W,59WO!iQPO,59WOVQPO,59QOqQPO'#CmO!nQPO,59`OOQO1G.k1G.kOVQPO'#CnO!vQPO,59aOOQO1G.r1G.rOOQO1G.l1G.lOOQO,59X,59XOOQO-E6k-E6kOOQO,59Y,59YOOQO-E6l-E6l",stateData:"#O~OeOS~OQSORSOSSOTSOWQO_ROgPO~OVXOgUO~O^[O~PVO[^O~O]_OVhX~OVaO~O]bO^iX~O^dO~O]_OVha~O]bO^ia~O",goto:"!kjPPPPPPkPPkqwPPPPk{!RPPP!XP!e!hXSOR^bQWQRf_TVQ_Q`WRg`QcZRicQTOQZRQe^RhbRYQR]R",nodeNames:"⚠ JsonText True False Null Number String } { Object Property PropertyName : , ] [ Array",maxTerm:25,nodeProps:[["isolate",-2,6,11,""],["openedBy",7,"{",14,"["],["closedBy",8,"}",15,"]"]],propSources:[_C],skippedNodes:[0],repeatNodeCount:2,tokenData:"(|~RaXY!WYZ!W]^!Wpq!Wrs!]|}$u}!O$z!Q!R%T!R![&c![!]&t!}#O&y#P#Q'O#Y#Z'T#b#c'r#h#i(Z#o#p(r#q#r(w~!]Oe~~!`Wpq!]qr!]rs!xs#O!]#O#P!}#P;'S!];'S;=`$o<%lO!]~!}Og~~#QXrs!]!P!Q!]#O#P!]#U#V!]#Y#Z!]#b#c!]#f#g!]#h#i!]#i#j#m~#pR!Q![#y!c!i#y#T#Z#y~#|R!Q![$V!c!i$V#T#Z$V~$YR!Q![$c!c!i$c#T#Z$c~$fR!Q![!]!c!i!]#T#Z!]~$rP;=`<%l!]~$zO]~~$}Q!Q!R%T!R![&c~%YRT~!O!P%c!g!h%w#X#Y%w~%fP!Q![%i~%nRT~!Q![%i!g!h%w#X#Y%w~%zR{|&T}!O&T!Q![&Z~&WP!Q![&Z~&`PT~!Q![&Z~&hST~!O!P%c!Q![&c!g!h%w#X#Y%w~&yO[~~'OO_~~'TO^~~'WP#T#U'Z~'^P#`#a'a~'dP#g#h'g~'jP#X#Y'm~'rOR~~'uP#i#j'x~'{P#`#a(O~(RP#`#a(U~(ZOS~~(^P#f#g(a~(dP#i#j(g~(jP#X#Y(m~(rOQ~~(wOW~~(|OV~",tokenizers:[0],topRules:{JsonText:[0,1]},tokenPrec:0}),TC=xx.define({name:"json",parser:EC.configure({props:[wx.add({Object:Dh({except:/^\s*\}/}),Array:Dh({except:/^\s*\]/})}),H0.add({"Object Array":kx})]}),languageData:{closeBrackets:{brackets:["[","{",'"']},indentOnInput:/^\s*[\}\]]$/}});function MC(){return new jx(TC)}function $C(e,t=e.state){const n=new Set;for(const{from:o,to:i}of e.visibleRanges){let a=o;for(;a<=i;){const s=t.doc.lineAt(a);n.has(s)||n.add(s),a=s.to+1}}return n}function wf(e){const t=e.selection.main.head;return e.doc.lineAt(t)}function qg(e,t){let n=0;e:for(let o=0;o<e.length;o++)switch(e[o]){case" ":case" ":{n+=1;continue e}case"	":{n+=t-n%t;continue e}case"\r":continue e;default:break e}return n}const ld=Sx.define({combine(e){return Cx(e,{highlightActiveBlock:!0,hideFirstIndent:!1,markerType:"fullScope",thickness:1})}});class AC{constructor(t,n,o,i){this.lines=t,this.state=n,this.map=new Map,this.unitWidth=o,this.markerType=i;for(const a of this.lines)this.add(a);this.state.facet(ld).highlightActiveBlock&&this.findAndSetActiveLines()}has(t){return this.map.has(typeof t=="number"?t:t.number)}get(t){const n=this.map.get(typeof t=="number"?t:t.number);if(!n)throw new Error("Line not found in indentation map");return n}set(t,n,o){const i=!t.text.trim().length,a={line:t,col:n,level:o,empty:i};return this.map.set(a.line.number,a),a}add(t){if(this.has(t))return this.get(t);if(!t.length||!t.text.trim().length){if(t.number===1)return this.set(t,0,0);if(t.number===this.state.doc.lines){const s=this.closestNonEmpty(t,-1);return this.set(t,0,s.level)}const i=this.closestNonEmpty(t,-1),a=this.closestNonEmpty(t,1);return i.level>=a.level&&this.markerType!=="codeOnly"?this.set(t,0,i.level):i.empty&&i.level===0&&a.level!==0?this.set(t,0,0):a.level>i.level?this.set(t,0,i.level+1):this.set(t,0,a.level)}const n=qg(t.text,this.state.tabSize),o=Math.floor(n/this.unitWidth);return this.set(t,n,o)}closestNonEmpty(t,n){let o=t.number+n;for(;n===-1?o>=1:o<=this.state.doc.lines;){if(this.has(o)){const s=this.get(o);if(!s.empty)return s}const a=this.state.doc.line(o);if(a.text.trim().length){const s=qg(a.text,this.state.tabSize),l=Math.floor(s/this.unitWidth);return this.set(a,s,l)}o+=n}const i=this.state.doc.line(n===-1?1:this.state.doc.lines);return this.set(i,0,0)}findAndSetActiveLines(){const t=wf(this.state);if(!this.has(t))return;let n=this.get(t);if(this.has(n.line.number+1)){const a=this.get(n.line.number+1);a.level>n.level&&(n=a)}if(this.has(n.line.number-1)){const a=this.get(n.line.number-1);a.level>n.level&&(n=a)}if(n.level===0)return;n.active=n.level;let o,i;for(o=n.line.number;o>1;o--){if(!this.has(o-1))continue;const a=this.get(o-1);if(a.level<n.level)break;a.active=n.level}for(i=n.line.number;i<this.state.doc.lines;i++){if(!this.has(i+1))continue;const a=this.get(i+1);if(a.level<n.level)break;a.active=n.level}}}function zC(e){const t={light:"#F0F1F2",dark:"#2B3245",activeLight:"#E4E5E6",activeDark:"#3C445C"};let n=t;return e&&(n=Object.assign(Object.assign({},t),e)),hs.baseTheme({"&light":{"--indent-marker-bg-color":n.light,"--indent-marker-active-bg-color":n.activeLight},"&dark":{"--indent-marker-bg-color":n.dark,"--indent-marker-active-bg-color":n.activeDark},".cm-line":{position:"relative"},".cm-indent-markers::before":{content:'""',position:"absolute",top:0,left:"2px",right:0,bottom:0,background:"var(--indent-markers)",pointerEvents:"none",zIndex:"-1"}})}function bu(e,t,n,o,i){return`${`repeating-linear-gradient(to right, var(${e}) 0 ${t}px, transparent ${t}px ${n}ch)`} ${o*n}.5ch/calc(${n*i}ch - 1px) no-repeat`}function PC(e,t,n,o,i){const{level:a,active:s}=e;if(i=i??o,n&&a===0)return[];const l=n?1:0,c=[];if(s!==void 0){const u=s-l-1;u>0&&c.push(bu("--indent-marker-bg-color",o,t,l,u)),c.push(bu("--indent-marker-active-bg-color",i,t,s-1,1)),s!==a&&c.push(bu("--indent-marker-bg-color",o,t,s,a-s))}else c.push(bu("--indent-marker-bg-color",o,t,l,a-l));return c.join(",")}class NC{constructor(t){this.view=t,this.unitWidth=ed(t.state),this.currentLineNumber=wf(t.state).number,this.generate(t.state)}update(t){const n=ed(t.state),o=n!==this.unitWidth;o&&(this.unitWidth=n);const i=wf(t.state).number,a=i!==this.currentLineNumber;this.currentLineNumber=i;const s=t.state.facet(ld).highlightActiveBlock&&a;(t.docChanged||t.viewportChanged||o||s)&&this.generate(t.state)}generate(t){const n=new G0,o=$C(this.view,t),{hideFirstIndent:i,markerType:a,thickness:s,activeThickness:l}=t.facet(ld),c=new AC(o,t,this.unitWidth,a);for(const u of o){const d=c.get(u.number);if(!(d!=null&&d.level))continue;const v=PC(d,this.unitWidth,i,s,l);n.add(u.from,u.from,K0.line({class:"cm-indent-markers",attributes:{style:`--indent-markers: ${v}`}}))}this.decorations=n.finish()}}function RC(e={}){return[ld.of(e),zC(e.colors),Q0.fromClass(NC,{decorations:t=>t.decorations})]}var _v,sb,Ev,IC=["mainAxis","crossAxis","fallbackPlacements","fallbackStrategy","fallbackAxisSideDirection","flipAlignment"],qC=["mainAxis","crossAxis","limiter"];function lb(e,t){if(e==null)return{};var n,o,i=function(s,l){if(s==null)return{};var c={};for(var u in s)if({}.hasOwnProperty.call(s,u)){if(l.indexOf(u)!==-1)continue;c[u]=s[u]}return c}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(o=0;o<a.length;o++)n=a[o],t.indexOf(n)===-1&&{}.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}function Dg(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter(function(i){return Object.getOwnPropertyDescriptor(e,i).enumerable})),n.push.apply(n,o)}return n}function De(e){for(var t=1;t<arguments.length;t++){var n=arguments[t]!=null?arguments[t]:{};t%2?Dg(Object(n),!0).forEach(function(o){va(e,o,n[o])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):Dg(Object(n)).forEach(function(o){Object.defineProperty(e,o,Object.getOwnPropertyDescriptor(n,o))})}return e}function Lg(e,t,n,o,i,a,s){try{var l=e[a](s),c=l.value}catch(u){return void n(u)}l.done?t(c):Promise.resolve(c).then(o,i)}function Pt(e){return function(){var t=this,n=arguments;return new Promise(function(o,i){var a=e.apply(t,n);function s(c){Lg(a,o,i,s,l,"next",c)}function l(c){Lg(a,o,i,s,l,"throw",c)}s(void 0)})}}function cb(e,t){ub(e,t),t.add(e)}function En(e,t,n){ub(e,t),t.set(e,n)}function ub(e,t){if(t.has(e))throw new TypeError("Cannot initialize the same private elements twice on an object")}function rr(e,t,n){return e.set(Lr(e,t),n),n}function je(e,t){return e.get(Lr(e,t))}function Lr(e,t,n){if(typeof e=="function"?e===t:e.has(t))return arguments.length<3?t:n;throw new TypeError("Private element is not present on this object")}function va(e,t,n){return(t=function(o){var i=function(a,s){if(typeof a!="object"||!a)return a;var l=a[Symbol.toPrimitive];if(l!==void 0){var c=l.call(a,s||"default");if(typeof c!="object")return c;throw new TypeError("@@toPrimitive must return a primitive value.")}return(s==="string"?String:Number)(a)}(o,"string");return typeof i=="symbol"?i:i+""}(t))in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}var Ug,Tv,Bg,Mv;typeof window<"u"&&((Tv=(Ug=(Mv=(Bg=window).__svelte)!==null&&Mv!==void 0?Mv:Bg.__svelte={}).v)!==null&&Tv!==void 0?Tv:Ug.v=new Set).add("5");var Ul=!1;Ul=!0;var io=Symbol(),db="http://www.w3.org/1999/xhtml",Qc=Array.isArray,DC=Array.prototype.indexOf,Cl=Array.prototype.includes,Bu=Array.from,LC=Object.defineProperty,ii=Object.getOwnPropertyDescriptor,vb=Object.getOwnPropertyDescriptors,UC=Object.prototype,BC=Array.prototype,Np=Object.getPrototypeOf,Fg=Object.isExtensible;function nc(e){return typeof e=="function"}var fb=()=>{};function FC(e){return e()}function kf(e){for(var t=0;t<e.length;t++)e[t]()}function pb(){var e,t;return{promise:new Promise((n,o)=>{e=n,t=o}),resolve:e,reject:t}}var WC=1<<24,Kc=16,Bl=32,hb=64,Xo=512,Xr=1024,$o=2048,Ba=4096,Pa=8192,si=16384,Bs=32768,Sf=1<<25,As=65536,VC=1<<17,gb=1<<19,Ea=1<<25,cd=65536,Cf=1<<21,Wi=1<<23,Na=Symbol("$state"),mb=Symbol("legacy props"),JC=Symbol(""),Ya=new class extends Error{constructor(){super(...arguments),va(this,"name","StaleReactionError"),va(this,"message","The reaction that called `getAbortSignal()` was re-run or destroyed")}},Rp=!((_v=globalThis.document)===null||_v===void 0||!_v.contentType)&&globalThis.document.contentType.includes("xml");function Gc(e){throw new Error("https://svelte.dev/e/lifecycle_outside_component")}function bb(e){return e===this.v}function yb(e,t){return e!=e?t==t:e!==t||e!==null&&typeof e=="object"||typeof e=="function"}function jb(e){return!yb(e,this.v)}var Ln=null;function Ol(e){Ln=e}function rs(e){return xb().get(e)}function yt(e){Ln={p:Ln,i:!1,c:null,e:null,s:e,x:null,r:pn,l:Ul&&!(arguments.length>1&&arguments[1]!==void 0&&arguments[1])?{s:null,u:null,$:[]}:null}}function jt(e){var t=Ln,n=t.e;if(n!==null)for(var o of(t.e=null,n))Fb(o);return e!==void 0&&(t.x=e),t.i=!0,Ln=t.p,e??{}}function Fl(){return!Ul||Ln!==null&&Ln.l===null}function xb(e){var t,n;return Ln===null&&Gc(),(n=(t=Ln).c)!==null&&n!==void 0?n:t.c=new Map(function(o){for(var i=o.p;i!==null;){var a=i.c;if(a!==null)return a;i=i.p}return null}(Ln)||void 0)}var xs=[];function wb(){var e=xs;xs=[],kf(e)}function Vi(e){if(xs.length===0&&!bc){var t=xs;queueMicrotask(()=>{t===xs&&wb()})}xs.push(e)}function HC(){for(;xs.length>0;)wb()}function kb(e){var t=pn;if(t===null)return Sn.f|=Wi,e;if(!(t.f&Bs)&&!(4&t.f))throw e;Ii(e,t)}function Ii(e,t){for(;t!==null;){if(128&t.f){if(!(t.f&Bs))throw e;try{return void t.b.error(e)}catch(n){e=n}}t=t.parent}throw e}var QC=-7169;function Ur(e,t){e.f=e.f&QC|t}function Ip(e){e.f&Xo||e.deps===null?Ur(e,Xr):Ur(e,Ba)}function Sb(e){if(e!==null)for(var t of e)2&t.f&&t.f&cd&&(t.f^=cd,Sb(t.deps))}function Cb(e,t,n){e.f&$o?t.add(e):e.f&Ba&&n.add(e),Sb(e.deps),Ur(e,Xr)}var yu=!1,qi=new Set,Vn=null,fa=null,Of=null,bc=!1,$v=!1,_l=null,ud=null,Ob=0,KC=1,dd=new WeakMap,ju=new WeakMap,ms=new WeakMap,Ai=new WeakMap,Fu=new WeakMap,ca=new WeakMap,_f=new WeakMap,El=new WeakMap,Ss=new WeakMap,Ni=new WeakMap,xu=new WeakMap,yc=new WeakMap,qo=new WeakSet;let Wl=class _b{constructor(){cb(this,qo),va(this,"id",KC++),va(this,"current",new Map),va(this,"previous",new Map),En(this,dd,new Set),En(this,ju,new Set),En(this,ms,new Map),En(this,Ai,new Map),En(this,Fu,null),En(this,ca,[]),En(this,_f,[]),En(this,El,new Set),En(this,Ss,new Set),En(this,Ni,new Map),va(this,"is_fork",!1),En(this,xu,!1),En(this,yc,new Set)}skip_effect(t){je(Ni,this).has(t)||je(Ni,this).set(t,{d:[],m:[]})}unskip_effect(t){var n=je(Ni,this).get(t);if(n){for(var o of(je(Ni,this).delete(t),n.d))Ur(o,$o),this.schedule(o);for(o of n.m)Ur(o,Ba),this.schedule(o)}}capture(t,n){var o,i=arguments.length>2&&arguments[2]!==void 0&&arguments[2];n===io||this.previous.has(t)||this.previous.set(t,n),!(t.f&Wi)&&(this.current.set(t,[t.v,i]),(o=fa)===null||o===void 0||o.set(t,t.v))}activate(){Vn=this}deactivate(){Vn=null,fa=null}flush(){try{$v=!0,Vn=this,Lr(qo,this,qp).call(this)}finally{Ob=0,Of=null,_l=null,ud=null,$v=!1,Vn=null,fa=null,Ji.clear()}}discard(){for(var t of je(ju,this))t(this);je(ju,this).clear(),qi.delete(this)}register_created_effect(t){je(_f,this).push(t)}increment(t,n){var o,i=(o=je(ms,this).get(n))!==null&&o!==void 0?o:0;if(je(ms,this).set(n,i+1),t){var a,s=(a=je(Ai,this).get(n))!==null&&a!==void 0?a:0;je(Ai,this).set(n,s+1)}}decrement(t,n,o){var i,a=(i=je(ms,this).get(n))!==null&&i!==void 0?i:0;if(a===1?je(ms,this).delete(n):je(ms,this).set(n,a-1),t){var s,l=(s=je(Ai,this).get(n))!==null&&s!==void 0?s:0;l===1?je(Ai,this).delete(n):je(Ai,this).set(n,l-1)}je(xu,this)||o||(rr(xu,this,!0),Vi(()=>{rr(xu,this,!1),this.flush()}))}transfer_effects(t,n){for(var o of t)je(El,this).add(o);for(var i of n)je(Ss,this).add(i);t.clear(),n.clear()}oncommit(t){je(dd,this).add(t)}ondiscard(t){je(ju,this).add(t)}settled(){var t;return((t=je(Fu,this))!==null&&t!==void 0?t:rr(Fu,this,pb())).promise}static ensure(){if(Vn===null){var t=Vn=new _b;$v||(qi.add(Vn),bc||Vi(()=>{Vn===t&&t.flush()}))}return Vn}apply(){fa=null}schedule(t){var n;if(Of=t,(n=t.b)!==null&&n!==void 0&&n.is_pending&&16777228&t.f&&(t.f&Bs)===0)t.b.defer_effect(t);else{for(var o=t;o.parent!==null;){var i=(o=o.parent).f;if(!(_l===null||o!==pn||Sn!==null&&2&Sn.f))return;if(96&i){if(!(i&Xr))return;o.f^=Xr}}je(ca,this).push(o)}}};function Ef(){return this.is_fork||je(Ai,this).size>0}function GC(){for(var e of je(yc,this))for(var t of je(Ai,e).keys()){for(var n=!1,o=t;o.parent!==null;){if(je(Ni,this).has(o)){n=!0;break}o=o.parent}if(!n)return!0}return!1}function qp(){if(Ob++>1e3&&(qi.delete(this),function(){try{(function(){throw new Error("https://svelte.dev/e/effect_update_depth_exceeded")})()}catch(j){Ii(j,Of)}}()),!Lr(qo,this,Ef).call(this)){for(var e of je(El,this))je(Ss,this).delete(e),Ur(e,$o),this.schedule(e);for(var t of je(Ss,this))Ur(t,Ba),this.schedule(t)}var n=je(ca,this);rr(ca,this,[]),this.apply();var o=_l=[],i=[],a=ud=[];for(var s of n)try{Lr(qo,this,Eb).call(this,s,o,i)}catch(j){throw $b(s),j}if(Vn=null,a.length>0){var l=sb.ensure();for(var c of a)l.schedule(c)}if(_l=null,ud=null,Lr(qo,this,Ef).call(this)||Lr(qo,this,GC).call(this))for(var[u,d]of(Lr(qo,this,Wg).call(this,i),Lr(qo,this,Wg).call(this,o),je(Ni,this)))Mb(u,d);else{var v;for(var f of(je(ms,this).size===0&&qi.delete(this),je(El,this).clear(),je(Ss,this).clear(),je(dd,this)))f(this);je(dd,this).clear(),Vg(i),Vg(o),(v=je(Fu,this))===null||v===void 0||v.resolve()}var h,p=Vn;if(je(ca,this).length>0){var y=p??(p=this);je(ca,y).push(...je(ca,this).filter(j=>!je(ca,y).includes(j)))}p!==null&&(qi.add(p),Lr(qo,h=p,qp).call(h)),qi.has(this)||Lr(qo,this,YC).call(this)}function Eb(e,t,n){e.f^=Xr;for(var o=e.first;o!==null;){var i=o.f,a=!!(96&i);if(!(a&&i&Xr||i&Pa||je(Ni,this).has(o))&&o.fn!==null){a?o.f^=Xr:4&i?t.push(o):Hl(o)&&(i&Kc&&je(Ss,this).add(o),zs(o));var s=o.first;if(s!==null){o=s;continue}}for(;o!==null;){var l=o.next;if(l!==null){o=l;break}o=o.parent}}}function Wg(e){for(var t=0;t<e.length;t+=1)Cb(e[t],je(El,this),je(Ss,this))}function YC(){for(var e of qi){var t=e.id<this.id,n=[];for(var[o,[i,a]]of this.current){if(e.current.has(o)){var s=e.current.get(o)[0];if(!t||i===s)continue;e.current.set(o,[i,a])}n.push(o)}var l=[...e.current.keys()].filter(y=>!this.current.has(y));if(l.length===0)t&&e.discard();else if(n.length>0){e.activate();var c=new Set,u=new Map;for(var d of n)Tb(d,l,c,u);u=new Map;var v=[...e.current.keys()].filter(y=>!this.current.has(y)||this.current.get(y)[0]!==y);for(var f of je(_f,this))155648&f.f||!Dp(f,v,u)||(4194320&f.f?(Ur(f,$o),e.schedule(f)):je(El,e).add(f));if(je(ca,e).length>0){for(var h of(e.apply(),je(ca,e)))Lr(qo,e,Eb).call(e,h,[],[]);rr(ca,e,[])}e.deactivate()}}for(var p of qi)je(yc,p).has(this)&&(je(yc,p).delete(this),je(yc,p).size!==0||Lr(qo,p,Ef).call(p)||(p.activate(),Lr(qo,p,qp).call(p)))}function Xn(e){var t=bc;bc=!0;try{for(;;){if(HC(),Vn===null)return;Vn.flush()}}finally{bc=t}}sb=Wl;var Ga=null;function Vg(e){var t=e.length;if(t!==0){for(var n=0;n<t;){var o,i=e[n++];if(!(24576&i.f)&&Hl(i)&&(Ga=new Set,zs(i),i.deps===null&&i.first===null&&i.nodes===null&&i.teardown===null&&i.ac===null&&Hb(i),((o=Ga)===null||o===void 0?void 0:o.size)>0)){for(var a of(Ji.clear(),Ga))if(!(24576&a.f)){for(var s=[a],l=a.parent;l!==null;)Ga.has(l)&&(Ga.delete(l),s.push(l)),l=l.parent;for(var c=s.length-1;c>=0;c--){var u=s[c];24576&u.f||zs(u)}}Ga.clear()}}Ga=null}}function Tb(e,t,n,o){if(!n.has(e)&&(n.add(e),e.reactions!==null))for(var i of e.reactions){var a=i.f;2&a?Tb(i,t,n,o):4194320&a&&!(a&$o)&&Dp(i,t,o)&&(Ur(i,$o),Lp(i))}}function Dp(e,t,n){var o=n.get(e);if(o!==void 0)return o;if(e.deps!==null)for(var i of e.deps){if(Cl.call(t,i))return!0;if(2&i.f&&Dp(i,t,n))return n.set(i,!0),!0}return n.set(e,!1),!1}function Lp(e){Vn.schedule(e)}function Mb(e,t){if(!(e.f&Bl)||!(e.f&Xr)){e.f&$o?t.d.push(e):e.f&Ba&&t.m.push(e),Ur(e,Xr);for(var n=e.first;n!==null;)Mb(n,t),n=n.next}}function $b(e){Ur(e,Xr);for(var t=e.first;t!==null;)$b(t),t=t.next}var gl=new WeakMap,XC=new WeakMap,nl=new WeakMap,Tf=new WeakMap,Jo=new WeakMap,sl=new WeakMap,Di=new WeakMap,Oi=new WeakMap,jc=new WeakMap,rl=new WeakMap,ml=new WeakMap,wu=new WeakMap,Mf=new WeakMap,$f=new WeakMap,us=new WeakMap,Jg=new WeakMap,Xa=new WeakSet;let ZC=class{constructor(t,n,o,i){var a,s,l,c,u,d;cb(this,Xa),va(this,"parent",void 0),va(this,"is_pending",!1),va(this,"transform_error",void 0),En(this,gl,void 0),En(this,XC,null),En(this,nl,void 0),En(this,Tf,void 0),En(this,Jo,void 0),En(this,sl,null),En(this,Di,null),En(this,Oi,null),En(this,jc,null),En(this,rl,0),En(this,ml,0),En(this,wu,!1),En(this,Mf,new Set),En(this,$f,new Set),En(this,us,null),En(this,Jg,(l=()=>(rr(us,this,fi(je(rl,this))),()=>{rr(us,this,null)}),u=0,d=fi(0),()=>{Bp()&&(r(d),Vl(()=>(u===0&&(c=F(()=>l(()=>xc(d)))),u+=1,()=>{Vi(()=>{var v;(u-=1)==0&&((v=c)===null||v===void 0||v(),c=void 0,xc(d))})})))})),rr(gl,this,t),rr(nl,this,n),rr(Tf,this,v=>{var f=pn;f.b=this,f.f|=128,o(v)}),this.parent=pn.b,this.transform_error=(a=i??((s=this.parent)===null||s===void 0?void 0:s.transform_error))!==null&&a!==void 0?a:v=>v,rr(Jo,this,Jl(()=>{Lr(Xa,this,Hg).call(this)},589824))}defer_effect(t){Cb(t,je(Mf,this),je($f,this))}is_rendered(){return!this.is_pending&&(!this.parent||this.parent.is_rendered())}has_pending_snippet(){return!!je(nl,this).pending}update_pending_count(t,n){Lr(Xa,this,zb).call(this,t,n),rr(rl,this,je(rl,this)+t),je(us,this)&&!je(wu,this)&&(rr(wu,this,!0),Vi(()=>{rr(wu,this,!1),je(us,this)&&Tl(je(us,this),je(rl,this))}))}get_effect_pending(){return je(Jg,this).call(this),r(je(us,this))}error(t){var n=je(nl,this).onerror,o=je(nl,this).failed;if(!n&&!o)throw t;je(sl,this)&&(uo(je(sl,this)),rr(sl,this,null)),je(Di,this)&&(uo(je(Di,this)),rr(Di,this,null)),je(Oi,this)&&(uo(je(Oi,this)),rr(Oi,this,null));var i=!1,a=!1,s=()=>{i?console.warn("https://svelte.dev/e/svelte_boundary_reset_noop"):(i=!0,a&&function(){throw new Error("https://svelte.dev/e/svelte_boundary_reset_onerror")}(),je(Oi,this)!==null&&Ml(je(Oi,this),()=>{rr(Oi,this,null)}),Lr(Xa,this,Qg).call(this,()=>{Lr(Xa,this,Hg).call(this)}))},l=c=>{try{a=!0,n==null||n(c,s),a=!1}catch(u){Ii(u,je(Jo,this)&&je(Jo,this).parent)}o&&rr(Oi,this,Lr(Xa,this,Qg).call(this,()=>{try{return pi(()=>{var u=pn;u.b=this,u.f|=128,o(je(gl,this),()=>c,()=>s)})}catch(u){return Ii(u,je(Jo,this).parent),null}}))};Vi(()=>{var c;try{c=this.transform_error(t)}catch(u){return void Ii(u,je(Jo,this)&&je(Jo,this).parent)}c!==null&&typeof c=="object"&&typeof c.then=="function"?c.then(l,u=>Ii(u,je(Jo,this)&&je(Jo,this).parent)):l(c)})}};function Hg(){try{if(this.is_pending=this.has_pending_snippet(),rr(ml,this,0),rr(rl,this,0),rr(sl,this,pi(()=>{je(Tf,this).call(this,je(gl,this))})),je(ml,this)>0){var e=rr(jc,this,document.createDocumentFragment());Wp(je(sl,this),e);var t=je(nl,this).pending;rr(Di,this,pi(()=>t(je(gl,this))))}else Lr(Xa,this,Ab).call(this,Vn)}catch(n){this.error(n)}}function Ab(e){this.is_pending=!1,e.transfer_effects(je(Mf,this),je($f,this))}function Qg(e){var t=pn,n=Sn,o=Ln;Ao(je(Jo,this)),na(je(Jo,this)),Ol(je(Jo,this).ctx);try{return Wl.ensure(),e()}catch(i){return kb(i),null}finally{Ao(t),na(n),Ol(o)}}function zb(e,t){var n;this.has_pending_snippet()?(rr(ml,this,je(ml,this)+e),je(ml,this)===0&&(Lr(Xa,this,Ab).call(this,t),je(Di,this)&&Ml(je(Di,this),()=>{rr(Di,this,null)}),je(jc,this)&&(je(gl,this).before(je(jc,this)),rr(jc,this,null)))):this.parent&&Lr(Xa,n=this.parent,zb).call(n,e,t)}function Pb(e,t,n,o){var i=Fl()?Yc:nt,a=e.filter(j=>!j.settled);if(n.length!==0||a.length!==0){var s,l,c,u,d=pn,v=(s=pn,l=Sn,c=Ln,u=Vn,function(){var j=!(arguments.length>0&&arguments[0]!==void 0)||arguments[0];Ao(s),na(l),Ol(c),j&&!(s.f&si)&&(u==null||u.activate(),u==null||u.apply())}),f=a.length===1?a[0].promise:a.length>1?Promise.all(a.map(j=>j.promise)):null;if(n.length!==0){var h=Kg();f?f.then(()=>{v(),y(),ku()}):y()}else f.then(()=>p(t.map(i)))}else o(t.map(i));function p(j){v();try{o(j)}catch(b){!(d.f&si)&&Ii(b,d)}ku()}function y(){Promise.all(n.map(j=>function(b){var k=pn;k===null&&function(){throw new Error("https://svelte.dev/e/async_derived_orphan")}();var E=void 0,O=fi(io),w=!Sn,_=new Map;return function(A){Ca(4718592,A)}(()=>{var A=pn,q=pb();E=q.promise;try{Promise.resolve(b()).then(q.resolve,q.reject).finally(ku)}catch(fe){q.reject(fe),ku()}var C=Vn;if(w){if(A.f&Bs)var z=Kg();if(k.b.is_rendered()){var D;(D=_.get(C))===null||D===void 0||D.reject(Ya),_.delete(C)}else{for(var H of _.values())H.reject(Ya);_.clear()}_.set(C,q)}var Q=function(fe){var Ie=arguments.length>1&&arguments[1]!==void 0?arguments[1]:void 0;if(z&&z(Ie===Ya),Ie!==Ya&&!(A.f&si)){if(C.activate(),Ie)O.f|=Wi,Tl(O,Ie);else for(var[ge,qe]of(O.f&Wi&&(O.f^=Wi),Tl(O,fe),_)){if(_.delete(ge),ge===C)break;qe.reject(Ya)}C.deactivate()}};q.promise.then(Q,fe=>Q(null,fe||"unknown"))}),Kd(()=>{for(var A of _.values())A.reject(Ya)}),new Promise(A=>{function q(C){function z(){C===E?A(O):q(E)}C.then(z,z)}q(E)})}(j))).then(j=>p([...t.map(i),...j])).catch(j=>Ii(j,d)).finally(()=>h())}}function ku(){var e,t=!(arguments.length>0&&arguments[0]!==void 0)||arguments[0];Ao(null),na(null),Ol(null),t&&((e=Vn)===null||e===void 0||e.deactivate())}function Kg(){var e=pn,t=e.b,n=Vn,o=t.is_rendered();return t.update_pending_count(1,n),n.increment(o,e),function(){var i=arguments.length>0&&arguments[0]!==void 0&&arguments[0];t.update_pending_count(-1,n),n.decrement(o,e,i)}}function Yc(e){var t=Sn!==null&&2&Sn.f?Sn:null;return pn!==null&&(pn.f|=gb),{ctx:Ln,deps:null,effects:null,equals:bb,f:2050,fn:e,reactions:null,rv:0,v:io,wv:0,parent:t??pn,ac:null}}function Kt(e){var t=Yc(e);return Gb(t),t}function nt(e){var t=Yc(e);return t.equals=jb,t}function Up(e){var t,n=pn;Ao(function(o){for(var i=o.parent;i!==null;){if(!(2&i.f))return i.f&si?null:i;i=i.parent}return null}(e));try{e.f&=-65537,function(o){var i=o.effects;if(i!==null){o.effects=null;for(var a=0;a<i.length;a+=1)uo(i[a])}}(e),t=ey(e)}finally{Ao(n)}return t}function Nb(e){var t,n,o,i=e.v,a=Up(e);if(!e.equals(a)&&(e.wv=Xb(),!((t=Vn)!==null&&t!==void 0&&t.is_fork&&e.deps!==null||(e.v=a,(n=Vn)===null||n===void 0||n.capture(e,i,!0),e.deps!==null))))return void Ur(e,Xr);Xi||(fa!==null?(Bp()||(o=Vn)!==null&&o!==void 0&&o.is_fork)&&fa.set(e,a):Ip(e))}function Rb(e){if(e.effects!==null)for(var t of e.effects)t.teardown&&zs(t)}var li,Ib,qb,Db,Av=new Set,Ji=new Map,Gg=!1;function fi(e,t){return{f:0,v:e,reactions:null,equals:bb,rv:0,wv:0}}function Ka(e,t){var n=fi(e);return Gb(n),n}function R(e){var t,n,o=arguments.length>1&&arguments[1]!==void 0&&arguments[1],i=!(arguments.length>2&&arguments[2]!==void 0)||arguments[2],a=fi(e);return o||(a.equals=jb),Ul&&i&&Ln!==null&&Ln.l!==null&&((n=(t=Ln.l).s)!==null&&n!==void 0?n:t.s=[]).push(a),a}function Lo(e,t){return g(e,F(()=>r(e))),t}function g(e,t){var n=arguments.length>2&&arguments[2]!==void 0&&arguments[2];return Sn===null||pa&&!(Sn.f&VC)||!Fl()||!(4325394&Sn.f)||Zo!==null&&Cl.call(Zo,e)||function(){throw new Error("https://svelte.dev/e/state_unsafe_mutation")}(),Tl(e,n?ll(t):t,ud)}function Tl(e,t){var n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:null;if(!e.equals(t)){var o=e.v;Xi?Ji.set(e,t):Ji.set(e,o),e.v=t;var i=Wl.ensure();if(i.capture(e,o),2&e.f){var a=e;e.f&$o&&Up(a),fa===null&&Ip(a)}e.wv=Xb(),Lb(e,$o,n),!Fl()||pn===null||!(pn.f&Xr)||96&pn.f||(Ho===null?function(s){Ho=s}([e]):Ho.push(e)),!i.is_fork&&Av.size>0&&!Gg&&function(){for(var s of(Gg=!1,Av))s.f&Xr&&Ur(s,Ba),Hl(s)&&zs(s);Av.clear()}()}return t}function Yg(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:1,n=r(e),o=t===1?n++:n--;return g(e,n),o}function xc(e){g(e,e.v+1)}function Lb(e,t,n){var o=e.reactions;if(o!==null)for(var i=Fl(),a=o.length,s=0;s<a;s++){var l=o[s],c=l.f;if(i||l!==pn){var u=(c&$o)===0;if(u&&Ur(l,t),2&c){var d,v=l;(d=fa)===null||d===void 0||d.delete(v),!(c&cd)&&(c&Xo&&(l.f|=cd),Lb(v,Ba,n))}else if(u){var f=l;c&Kc&&Ga!==null&&Ga.add(f),n!==null?n.push(f):Lp(f)}}}}function ll(e){if(typeof e!="object"||e===null||Na in e)return e;var t=Np(e);if(t!==UC&&t!==BC)return e;var n=new Map,o=Qc(e),i=Ka(0),a=Os,s=l=>{if(Os===a)return l();var c=Sn,u=Os;na(null),tm(a);var d=l();return na(c),tm(u),d};return o&&n.set("length",Ka(e.length)),new Proxy(e,{defineProperty(l,c,u){"value"in u&&u.configurable!==!1&&u.enumerable!==!1&&u.writable!==!1||function(){throw new Error("https://svelte.dev/e/state_descriptors_fixed")}();var d=n.get(c);return d===void 0?s(()=>{var v=Ka(u.value);return n.set(c,v),v}):g(d,u.value,!0),!0},deleteProperty(l,c){var u=n.get(c);if(u===void 0){if(c in l){var d=s(()=>Ka(io));n.set(c,d),xc(i)}}else g(u,io),xc(i);return!0},get(l,c,u){var d;if(c===Na)return e;var v=n.get(c),f=c in l;if(v===void 0&&(!f||(d=ii(l,c))!==null&&d!==void 0&&d.writable)&&(v=s(()=>Ka(ll(f?l[c]:io))),n.set(c,v)),v!==void 0){var h=r(v);return h===io?void 0:h}return Reflect.get(l,c,u)},getOwnPropertyDescriptor(l,c){var u=Reflect.getOwnPropertyDescriptor(l,c);if(u&&"value"in u){var d=n.get(c);d&&(u.value=r(d))}else if(u===void 0){var v=n.get(c),f=v==null?void 0:v.v;if(v!==void 0&&f!==io)return{enumerable:!0,configurable:!0,value:f,writable:!0}}return u},has(l,c){var u;if(c===Na)return!0;var d=n.get(c),v=d!==void 0&&d.v!==io||Reflect.has(l,c);return(d!==void 0||pn!==null&&(!v||(u=ii(l,c))!==null&&u!==void 0&&u.writable))&&(d===void 0&&(d=s(()=>Ka(v?ll(l[c]):io)),n.set(c,d)),r(d)===io)?!1:v},set(l,c,u,d){var v,f=n.get(c),h=c in l;if(o&&c==="length")for(var p=u;p<f.v;p+=1){var y=n.get(p+"");y!==void 0?g(y,io):p in l&&(y=s(()=>Ka(io)),n.set(p+"",y))}f===void 0?(!h||(v=ii(l,c))!==null&&v!==void 0&&v.writable)&&(g(f=s(()=>Ka(void 0)),ll(u)),n.set(c,f)):(h=f.v!==io,g(f,s(()=>ll(u))));var j=Reflect.getOwnPropertyDescriptor(l,c);if(j!=null&&j.set&&j.set.call(d,u),!h){if(o&&typeof c=="string"){var b=n.get("length"),k=Number(c);Number.isInteger(k)&&k>=b.v&&g(b,k+1)}xc(i)}return!0},ownKeys(l){r(i);var c=Reflect.ownKeys(l).filter(v=>{var f=n.get(v);return f===void 0||f.v!==io});for(var[u,d]of n)d.v===io||u in l||c.push(u);return c},setPrototypeOf(){(function(){throw new Error("https://svelte.dev/e/state_prototype_fixed")})()}})}function Xg(e){try{if(e!==null&&typeof e=="object"&&Na in e)return e[Na]}catch{}return e}function e9(e,t){return Object.is(Xg(e),Xg(t))}function Cs(){var e=arguments.length>0&&arguments[0]!==void 0?arguments[0]:"";return document.createTextNode(e)}function Uo(e){return qb.call(e)}function Xc(e){return Db.call(e)}function I(e,t){return Uo(e)}function Mt(e){var t=Uo(e);return t instanceof Comment&&t.data===""?Xc(t):t}function Y(e){for(var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:1,n=e;t--;)n=Xc(n);return n}function Ub(e,t,n){return document.createElementNS(t??db,e,void 0)}var Zg=!1;function Qd(e){var t=Sn,n=pn;na(null),Ao(null);try{return e()}finally{na(t),Ao(n)}}function t9(e,t,n){var o=arguments.length>3&&arguments[3]!==void 0?arguments[3]:n;e.addEventListener(t,()=>Qd(n));var i=e.__on_r;e.__on_r=i?()=>{i(),o(!0)}:()=>o(!0),Zg||(Zg=!0,document.addEventListener("reset",a=>{Promise.resolve().then(()=>{if(!a.defaultPrevented)for(var s of a.target.elements){var l;(l=s.__on_r)===null||l===void 0||l.call(s)}})},{capture:!0}))}function Bb(e){pn===null&&(Sn===null&&function(){throw new Error("https://svelte.dev/e/effect_orphan")}(),function(){throw new Error("https://svelte.dev/e/effect_in_unowned_derived")}()),Xi&&function(){throw new Error("https://svelte.dev/e/effect_in_teardown")}()}function Ca(e,t){var n,o=pn;o!==null&&o.f&Pa&&(e|=Pa);var i={ctx:Ln,deps:null,nodes:null,f:e|$o|Xo,first:null,fn:t,last:null,next:null,parent:o,b:o&&o.b,prev:null,teardown:null,wv:0,ac:null};(n=Vn)===null||n===void 0||n.register_created_effect(i);var a=i;if(4&e)_l!==null?_l.push(i):Wl.ensure().schedule(i);else if(t!==null){try{zs(i)}catch(c){throw uo(i),c}a.deps===null&&a.teardown===null&&a.nodes===null&&a.first===a.last&&!(a.f&gb)&&(a=a.first,e&Kc&&e&As&&a!==null&&(a.f|=As))}if(a!==null&&(a.parent=o,o!==null&&function(c,u){var d=u.last;d===null?u.last=u.first=c:(d.next=c,c.prev=d,u.last=c)}(a,o),Sn!==null&&2&Sn.f&&(e&hb)===0)){var s,l=Sn;((s=l.effects)!==null&&s!==void 0?s:l.effects=[]).push(a)}return i}function Bp(){return Sn!==null&&!pa}function Kd(e){var t=Ca(8,null);return Ur(t,Xr),t.teardown=e,t}function Af(e){Bb();var t=pn.f;if(!(!Sn&&t&Bl&&!(t&Bs)))return Fb(e);var n,o=Ln;((n=o.e)!==null&&n!==void 0?n:o.e=[]).push(e)}function Fb(e){return Ca(1048580,e)}function so(e){return Ca(4,e)}function ne(e,t){var n={effect:null,ran:!1,deps:e};Ln.l.$.push(n),n.effect=Vl(()=>{if(e(),!n.ran){n.ran=!0;var o=pn;try{Ao(o.parent),F(t)}finally{Ao(o)}}})}function Mn(){var e=Ln;Vl(()=>{for(var t of e.l.$){t.deps();var n=t.effect;n.f&Xr&&n.deps!==null&&Ur(n,Ba),Hl(n)&&zs(n),t.ran=!1}})}function Vl(e){return Ca(8|(arguments.length>1&&arguments[1]!==void 0?arguments[1]:0),e)}function Le(e){Pb(arguments.length>3&&arguments[3]!==void 0?arguments[3]:[],arguments.length>1&&arguments[1]!==void 0?arguments[1]:[],arguments.length>2&&arguments[2]!==void 0?arguments[2]:[],t=>{Ca(8,()=>e(...t.map(r)))})}function Jl(e){return Ca(Kc|(arguments.length>1&&arguments[1]!==void 0?arguments[1]:0),e)}function Wb(e){return Ca(WC|(arguments.length>1&&arguments[1]!==void 0?arguments[1]:0),e)}function pi(e){return Ca(524320,e)}function Vb(e){var t=e.teardown;if(t!==null){var n=Xi,o=Sn;em(!0),na(null);try{t.call(null)}finally{em(n),na(o)}}}function Fp(e){var t=arguments.length>1&&arguments[1]!==void 0&&arguments[1],n=e.first;e.first=e.last=null;for(var o,i=function(){var a=n.ac;a!==null&&Qd(()=>{a.abort(Ya)}),o=n.next,n.f&hb?n.parent=null:uo(n,t),n=o};n!==null;)i()}function uo(e){var t=!(arguments.length>1&&arguments[1]!==void 0)||arguments[1],n=!1;(t||262144&e.f)&&e.nodes!==null&&e.nodes.end!==null&&(Jb(e.nodes.start,e.nodes.end),n=!0),Ur(e,Sf),Fp(e,t&&!n),Tc(e,0);var o=e.nodes&&e.nodes.t;if(o!==null)for(var i of o)i.stop();Vb(e),e.f^=Sf,e.f|=si;var a=e.parent;a!==null&&a.first!==null&&Hb(e),e.next=e.prev=e.teardown=e.ctx=e.deps=e.fn=e.nodes=e.ac=e.b=null}function Jb(e,t){for(;e!==null;){var n=e===t?null:Xc(e);e.remove(),e=n}}function Hb(e){var t=e.parent,n=e.prev,o=e.next;n!==null&&(n.next=o),o!==null&&(o.prev=n),t!==null&&(t.first===e&&(t.first=o),t.last===e&&(t.last=n))}function Ml(e,t){var n=!(arguments.length>2&&arguments[2]!==void 0)||arguments[2],o=[];Qb(e,o,!0);var i=()=>{n&&uo(e),t&&t()},a=o.length;if(a>0){var s=()=>--a||i();for(var l of o)l.out(s)}else i()}function Qb(e,t,n){if(!(e.f&Pa)){e.f^=Pa;var o=e.nodes&&e.nodes.t;if(o!==null)for(var i of o)(i.is_global||n)&&t.push(i);for(var a=e.first;a!==null;){var s=a.next;Qb(a,t,!!(a.f&As||a.f&Bl&&e.f&Kc)&&n),a=s}}}function zf(e){Kb(e,!0)}function Kb(e,t){if(e.f&Pa){e.f^=Pa,!(e.f&Xr)&&(Ur(e,$o),Wl.ensure().schedule(e));for(var n=e.first;n!==null;){var o=n.next;Kb(n,!!(n.f&As||n.f&Bl)&&t),n=o}var i=e.nodes&&e.nodes.t;if(i!==null)for(var a of i)(a.is_global||t)&&a.in()}}function Wp(e,t){if(e.nodes)for(var n=e.nodes.start,o=e.nodes.end;n!==null;){var i=n===o?null:Xc(n);t.append(n),n=i}}var Wu=!1,Xi=!1;function em(e){Xi=e}var Sn=null,pa=!1;function na(e){Sn=e}var pn=null;function Ao(e){pn=e}var Zo=null;function Gb(e){Sn!==null&&(Zo===null?Zo=[e]:Zo.push(e))}var So=null,Ro=0,Ho=null,Yb=1,ws=0,Os=ws;function tm(e){Os=e}function Xb(){return++Yb}function Hl(e){var t=e.f;if(t&$o)return!0;if(2&t&&(e.f&=-65537),(t&Ba)!==0){for(var n=e.deps,o=n.length,i=0;i<o;i++){var a=n[i];if(Hl(a)&&Nb(a),a.wv>e.wv)return!0}t&Xo&&fa===null&&Ur(e,Xr)}return!1}function Zb(e,t){var n=!(arguments.length>2&&arguments[2]!==void 0)||arguments[2],o=e.reactions;if(o!==null&&(Zo===null||!Cl.call(Zo,e)))for(var i=0;i<o.length;i++){var a=o[i];2&a.f?Zb(a,t,!1):t===a&&(n?Ur(a,$o):a.f&Xr&&Ur(a,Ba),Lp(a))}}function ey(e){var t=So,n=Ro,o=Ho,i=Sn,a=Zo,s=Ln,l=pa,c=Os,u=e.f;So=null,Ro=0,Ho=null,Sn=96&u?null:e,Zo=null,Ol(e.ctx),pa=!1,Os=++ws,e.ac!==null&&(Qd(()=>{e.ac.abort(Ya)}),e.ac=null);try{var d;e.f|=Cf;var v=(0,e.fn)();e.f|=Bs;var f=e.deps,h=(d=Vn)===null||d===void 0?void 0:d.is_fork;if(So!==null){var p;if(h||Tc(e,Ro),f!==null&&Ro>0)for(f.length=Ro+So.length,p=0;p<So.length;p++)f[Ro+p]=So[p];else e.deps=f=So;if(Bp()&&e.f&Xo)for(p=Ro;p<f.length;p++){var y,j;((j=(y=f[p]).reactions)!==null&&j!==void 0?j:y.reactions=[]).push(e)}}else!h&&f!==null&&Ro<f.length&&(Tc(e,Ro),f.length=Ro);if(Fl()&&Ho!==null&&!pa&&f!==null&&!(6146&e.f))for(p=0;p<Ho.length;p++)Zb(Ho[p],e);if(i!==null&&i!==e){if(ws++,i.deps!==null)for(var b=0;b<n;b+=1)i.deps[b].rv=ws;if(t!==null)for(var k of t)k.rv=ws;Ho!==null&&(o===null?o=Ho:o.push(...Ho))}return e.f&Wi&&(e.f^=Wi),v}catch(E){return kb(E)}finally{e.f^=Cf,So=t,Ro=n,Ho=o,Sn=i,Zo=a,Ol(s),pa=l,Os=c}}function n9(e,t){var n=t.reactions;if(n!==null){var o=DC.call(n,e);if(o!==-1){var i=n.length-1;i===0?n=t.reactions=null:(n[o]=n[i],n.pop())}}if(n===null&&2&t.f&&(So===null||!Cl.call(So,t))){var a=t;a.f&Xo&&(a.f^=Xo,a.f&=-65537),Ip(a),function(s){if(s.effects!==null)for(var l of s.effects){var c,u;(l.teardown||l.ac)&&((c=l.teardown)===null||c===void 0||c.call(l),(u=l.ac)===null||u===void 0||u.abort(Ya),l.teardown=fb,l.ac=null,Tc(l,0),Fp(l))}}(a),Tc(a,0)}}function Tc(e,t){var n=e.deps;if(n!==null)for(var o=t;o<n.length;o++)n9(e,n[o])}function zs(e){var t=e.f;if(!(t&si)){Ur(e,Xr);var n=pn,o=Wu;pn=e,Wu=!0;try{16777232&t?function(a){for(var s=a.first;s!==null;){var l=s.next;!(s.f&Bl)&&uo(s),s=l}}(e):Fp(e),Vb(e);var i=ey(e);e.teardown=typeof i=="function"?i:null,e.wv=Yb}finally{Wu=o,pn=n}}}function ty(){return ny.apply(this,arguments)}function ny(){return(ny=Pt(function*(){yield Promise.resolve(),Xn()})).apply(this,arguments)}function r(e){var t,n=!!(2&e.f);if(Sn!==null&&!pa&&!(pn!==null&&pn.f&si||Zo!==null&&Cl.call(Zo,e))){var o=Sn.deps;if(Sn.f&Cf)e.rv<ws&&(e.rv=ws,So===null&&o!==null&&o[Ro]===e?Ro++:So===null?So=[e]:So.push(e));else{var i,a;((a=(i=Sn).deps)!==null&&a!==void 0?a:i.deps=[]).push(e);var s=e.reactions;s===null?e.reactions=[Sn]:Cl.call(s,Sn)||s.push(Sn)}}if(Xi&&Ji.has(e))return Ji.get(e);if(n){var l=e;if(Xi){var c=l.v;return(!(l.f&Xr)&&l.reactions!==null||oy(l))&&(c=Up(l)),Ji.set(l,c),c}var u=(l.f&Xo)===0&&!pa&&Sn!==null&&(Wu||(Sn.f&Xo)!==0),d=(l.f&Bs)===0;Hl(l)&&(u&&(l.f|=Xo),Nb(l)),u&&!d&&(Rb(l),ry(l))}if((t=fa)!==null&&t!==void 0&&t.has(e))return fa.get(e);if(e.f&Wi)throw e.v;return e.v}function ry(e){if(e.f|=Xo,e.deps!==null)for(var t of e.deps){var n;((n=t.reactions)!==null&&n!==void 0?n:t.reactions=[]).push(e),2&t.f&&!(t.f&Xo)&&(Rb(t),ry(t))}}function oy(e){if(e.v===io)return!0;if(e.deps===null)return!1;for(var t of e.deps)if(Ji.has(t)||2&t.f&&oy(t))return!0;return!1}function F(e){var t=pa;try{return pa=!0,e()}finally{pa=t}}function x(e){if(typeof e=="object"&&e&&!(e instanceof EventTarget)){if(Na in e)Pf(e);else if(!Array.isArray(e))for(var t in e){var n=e[t];typeof n=="object"&&n&&Na in n&&Pf(n)}}}function Pf(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:new Set;if(!(typeof e!="object"||e===null||e instanceof EventTarget||t.has(e))){for(var n in t.add(e),e instanceof Date&&e.getTime(),e)try{Pf(e[n],t)}catch{}var o=Np(e);if(o!==Object.prototype&&o!==Array.prototype&&o!==Map.prototype&&o!==Set.prototype&&o!==Date.prototype){var i=vb(o);for(var a in i){var s=i[a].get;if(s)try{s.call(e)}catch{}}}}}var cl=Symbol("events"),ay=new Set,Nf=new Set;function iy(e,t,n){var o=arguments.length>3&&arguments[3]!==void 0?arguments[3]:{};function i(a){if(o.capture||Rf.call(t,a),!a.cancelBubble)return Qd(()=>n==null?void 0:n.call(this,a))}return e.startsWith("pointer")||e.startsWith("touch")||e==="wheel"?Vi(()=>{t.addEventListener(e,i,o)}):t.addEventListener(e,i,o),i}function ze(e,t,n,o,i){var a={capture:o,passive:i},s=iy(e,t,n,a);(t===document.body||t===window||t===document||t instanceof HTMLMediaElement)&&Kd(()=>{t.removeEventListener(e,s,a)})}function ha(e,t,n){var o;((o=t[cl])!==null&&o!==void 0?o:t[cl]={})[e]=n}function Zc(e){for(var t=0;t<e.length;t++)ay.add(e[t]);for(var n of Nf)n(e)}function Rf(e){var t,n=this,o=n.ownerDocument,i=e.type,a=((t=e.composedPath)===null||t===void 0?void 0:t.call(e))||[],s=a[0]||e.target,l=0,c=e===e&&e[cl];if(c){var u=a.indexOf(c);if(u!==-1&&(n===document||n===window))return void(e[cl]=n);var d=a.indexOf(n);if(d===-1)return;u<=d&&(l=u)}if((s=a[l]||e.target)!==n){LC(e,"currentTarget",{configurable:!0,get:()=>s||o});var v=Sn,f=pn;na(null),Ao(null);try{for(var h,p=[];s!==null;){var y=s.assignedSlot||s.parentNode||s.host||null;try{var j,b=(j=s[cl])===null||j===void 0?void 0:j[i];b==null||s.disabled&&e.target!==s||b.call(s,e)}catch(O){h?p.push(O):h=O}if(e.cancelBubble||y===n||y===null)break;s=y}if(h){var k=function(O){queueMicrotask(()=>{throw O})};for(var E of p)k(E);throw h}}finally{e[cl]=n,delete e.currentTarget,na(v),Ao(f)}}}var nm=(globalThis==null||(Ev=globalThis.window)===null||Ev===void 0?void 0:Ev.trustedTypes)&&globalThis.window.trustedTypes.createPolicy("svelte-trusted-html",{createHTML:e=>e});function sy(e){var t=Ub("template");return t.innerHTML=function(n){var o;return(o=nm==null?void 0:nm.createHTML(n))!==null&&o!==void 0?o:n}(e.replaceAll("<!>","<!---->")),t.content}function Zi(e,t){var n=pn;n.nodes===null&&(n.nodes={start:e,end:t,a:null,t:null})}function re(e,t){var n,o=!!(1&t),i=!!(2&t),a=!e.startsWith("<!>");return()=>{n===void 0&&(n=sy(a?e:"<!>"+e),o||(n=Uo(n)));var s=i||Ib?document.importNode(n,!0):n.cloneNode(!0);return o?Zi(Uo(s),s.lastChild):Zi(s,s),s}}function os(e,t){return function(n,o){var i,a=arguments.length>2&&arguments[2]!==void 0?arguments[2]:"svg",s=!n.startsWith("<!>"),l=!!(1&o),c="<".concat(a,">").concat(s?n:"<!>"+n,"</").concat(a,">");return()=>{if(!i){var u=Uo(sy(c));if(l)for(i=document.createDocumentFragment();Uo(u);)i.appendChild(Uo(u));else i=Uo(u)}var d=i.cloneNode(!0);return l?Zi(Uo(d),d.lastChild):Zi(d,d),d}}(e,t,"svg")}function oo(){var e=Cs((arguments.length>0&&arguments[0]!==void 0?arguments[0]:"")+"");return Zi(e,e),e}function br(){var e=document.createDocumentFragment(),t=document.createComment(""),n=Cs();return e.append(t,n),Zi(t,n),e}function U(e,t){e!==null&&e.before(t)}var r9=["beforeinput","click","change","dblclick","contextmenu","focusin","focusout","input","keydown","keyup","mousedown","mousemove","mouseout","mouseover","mouseup","pointerdown","pointermove","pointerout","pointerover","pointerup","touchend","touchmove","touchstart"],o9={formnovalidate:"formNoValidate",ismap:"isMap",nomodule:"noModule",playsinline:"playsInline",readonly:"readOnly",defaultvalue:"defaultValue",defaultchecked:"defaultChecked",srcobject:"srcObject",novalidate:"noValidate",allowfullscreen:"allowFullscreen",disablepictureinpicture:"disablePictureInPicture",disableremoteplayback:"disableRemotePlayback"},a9=["touchstart","touchmove"];function i9(e){return a9.includes(e)}function xt(e,t){var n,o=t==null?"":typeof t=="object"?"".concat(t):t;o!==((n=e.__t)!==null&&n!==void 0?n:e.__t=e.nodeValue)&&(e.__t=o,e.nodeValue="".concat(o))}function s9(e,t){return function(n,o){var{target:i,anchor:a,props:s={},events:l,context:c,intro:u=!0,transformError:d}=o;(function(){if(li===void 0){li=window,Ib=/Firefox/.test(navigator.userAgent);var h=Element.prototype,p=Node.prototype,y=Text.prototype;qb=ii(p,"firstChild").get,Db=ii(p,"nextSibling").get,Fg(h)&&(h.__click=void 0,h.__className=void 0,h.__attributes=null,h.__style=void 0,h.__e=void 0),Fg(y)&&(y.__t=void 0)}})();var v=void 0,f=function(h){Wl.ensure();var p=Ca(524352,h);return function(){var y=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{};return new Promise(j=>{y.outro?Ml(p,()=>{uo(p),j(void 0)}):(uo(p),j(void 0))})}}(()=>{var h=a??i.appendChild(Cs());(function(j,b,k,E){new ZC(j,b,k,E)})(h,{pending:()=>{}},j=>{yt({}),c&&(Ln.c=c),l&&(s.$$events=l),v=n(j,s)||{},jt()},d);var p=new Set,y=j=>{for(var b=0;b<j.length;b++){var k=j[b];if(!p.has(k)){p.add(k);var E=i9(k);for(var O of[i,document]){var w=Su.get(O);w===void 0&&(w=new Map,Su.set(O,w));var _=w.get(k);_===void 0?(O.addEventListener(k,Rf,{passive:E}),w.set(k,1)):w.set(k,_+1)}}}};return y(Bu(ay)),Nf.add(y),()=>{for(var j of p)for(var b of[i,document]){var k=Su.get(b),E=k.get(j);--E==0?(b.removeEventListener(j,Rf),k.delete(j),k.size===0&&Su.delete(b)):k.set(j,E)}var O;Nf.delete(y),h!==a&&((O=h.parentNode)===null||O===void 0||O.removeChild(h))}});return If.set(v,f),v}(e,t)}var Su=new Map,If=new WeakMap,Ha=new WeakMap,ds=new WeakMap,Qa=new WeakMap,rc=new WeakMap,zv=new WeakMap,rm=new WeakMap,l9=new WeakMap;let Gd=class{constructor(t){var n=this,o=!(arguments.length>1&&arguments[1]!==void 0)||arguments[1];va(this,"anchor",void 0),En(this,Ha,new Map),En(this,ds,new Map),En(this,Qa,new Map),En(this,rc,new Set),En(this,zv,!0),En(this,rm,i=>{if(je(Ha,this).has(i)){var a=je(Ha,this).get(i),s=je(ds,this).get(a);if(s)zf(s),je(rc,this).delete(a);else{var l=je(Qa,this).get(a);l&&(je(ds,this).set(a,l.effect),je(Qa,this).delete(a),l.fragment.lastChild.remove(),this.anchor.before(l.fragment),s=l.effect)}for(var[c,u]of je(Ha,this)){if(je(Ha,this).delete(c),c===i)break;var d=je(Qa,this).get(u);d&&(uo(d.effect),je(Qa,this).delete(u))}var v=function(p,y){if(p===a||je(rc,n).has(p))return 1;var j=()=>{if(Array.from(je(Ha,n).values()).includes(p)){var b=document.createDocumentFragment();Wp(y,b),b.append(Cs()),je(Qa,n).set(p,{effect:y,fragment:b})}else uo(y);je(rc,n).delete(p),je(ds,n).delete(p)};je(zv,n)||!s?(je(rc,n).add(p),Ml(y,j,!1)):j()};for(var[f,h]of je(ds,this))v(f,h)}}),En(this,l9,i=>{je(Ha,this).delete(i);var a=Array.from(je(Ha,this).values());for(var[s,l]of je(Qa,this))a.includes(s)||(uo(l.effect),je(Qa,this).delete(s))}),this.anchor=t,rr(zv,this,o)}ensure(t,n){var o=Vn;!n||je(ds,this).has(t)||je(Qa,this).has(t)||je(ds,this).set(t,pi(()=>n(this.anchor))),je(Ha,this).set(o,t),je(rm,this).call(this,o)}};function vo(e){Ln===null&&Gc(),Ul&&Ln.l!==null?ly(Ln).m.push(e):Af(()=>{var t=F(e);if(typeof t=="function")return t})}function ra(e){Ln===null&&Gc(),vo(()=>()=>F(e))}function c9(){var e=Ln;return e===null&&Gc(),(t,n,o)=>{var i,a=(i=e.s.$$events)===null||i===void 0?void 0:i[t];if(a){var s=Qc(a)?a.slice():[a],l=function(u,d){var{bubbles:v=!1,cancelable:f=!1}=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{};return new CustomEvent(u,{detail:d,bubbles:v,cancelable:f})}(t,n,o);for(var c of s)c.call(e.x,l);return!l.defaultPrevented}return!0}}function u9(e){Ln===null&&Gc(),Ln.l===null&&function(){throw new Error("https://svelte.dev/e/lifecycle_legacy_only")}(),ly(Ln).b.push(e)}function ly(e){var t,n=e.l;return(t=n.u)!==null&&t!==void 0?t:n.u={a:[],b:[],m:[]}}function be(e,t){var n=arguments.length>2&&arguments[2]!==void 0&&arguments[2],o=new Gd(e);function i(a,s){o.ensure(a,s)}Jl(()=>{var a=!1;t(function(s){a=!0,i(arguments.length>1&&arguments[1]!==void 0?arguments[1]:0,s)}),a||i(-1,null)},n?As:0)}var Ks,d9=Symbol("NaN");function cy(e,t,n){var o=new Gd(e),i=!Fl();Jl(()=>{var a=t();a!=a&&(a=d9),i&&a!==null&&typeof a=="object"&&(a={}),o.ensure(a,n)})}function Pr(e,t){return t}function Pv(e,t){var n,o=!(arguments.length>2&&arguments[2]!==void 0)||arguments[2];if(e.pending.size>0)for(var i of(n=new Set,e.pending.values()))for(var a of i)n.add(e.items.get(a).e);for(var s=0;s<t.length;s++){var l,c=t[s];(l=n)!==null&&l!==void 0&&l.has(c)?(c.f|=Ea,Wp(c,document.createDocumentFragment())):uo(t[s],o)}}function Or(e,t,n,o,i){var a=arguments.length>5&&arguments[5]!==void 0?arguments[5]:null,s=e,l=new Map;!(4&t)||(s=e.appendChild(Cs()));var c,u=null,d=nt(()=>{var j=n();return Qc(j)?j:j==null?[]:Bu(j)}),v=new Map,f=!0;function h(j){!(y.effect.f&si)&&(y.pending.delete(j),y.fallback=u,function(b,k,E,O,w){var _,A,q,C,z,D=!!(8&O),H=k.length,Q=b.items,fe=oc(b.effect.first),Ie=null,ge=[],qe=[];if(D)for(z=0;z<H;z+=1){var ce;q=w(k[z],z),!((C=Q.get(q).e).f&Ea)&&((ce=C.nodes)===null||ce===void 0||(ce=ce.a)===null||ce===void 0||ce.measure(),(A??(A=new Set)).add(C))}for(z=0;z<H;z+=1){if(q=w(k[z],z),C=Q.get(q).e,b.outrogroups!==null)for(var ve of b.outrogroups)ve.pending.delete(C),ve.done.delete(C);var he;if(C.f&Pa&&(zf(C),D&&((he=C.nodes)===null||he===void 0||(he=he.a)===null||he===void 0||he.unfix(),(A??(A=new Set)).delete(C))),C.f&Ea){if(C.f^=Ea,C!==fe){var Ue=Ie?Ie.next:fe;C===b.effect.last&&(b.effect.last=C.prev),C.prev&&(C.prev.next=C.next),C.next&&(C.next.prev=C.prev),_i(b,Ie,C),_i(b,C,Ue),ac(C,Ue,E),ge=[],qe=[],fe=oc((Ie=C).next);continue}ac(C,null,E)}if(C!==fe){if(_!==void 0&&_.has(C)){if(ge.length<qe.length){var Re,we=qe[0];Ie=we.prev;var ue=ge[0],ie=ge[ge.length-1];for(Re=0;Re<ge.length;Re+=1)ac(ge[Re],we,E);for(Re=0;Re<qe.length;Re+=1)_.delete(qe[Re]);_i(b,ue.prev,ie.next),_i(b,Ie,ue),_i(b,ie,we),fe=we,Ie=ie,z-=1,ge=[],qe=[]}else _.delete(C),ac(C,fe,E),_i(b,C.prev,C.next),_i(b,C,Ie===null?b.effect.first:Ie.next),_i(b,Ie,C),Ie=C;continue}for(ge=[],qe=[];fe!==null&&fe!==C;)(_??(_=new Set)).add(fe),qe.push(fe),fe=oc(fe.next);if(fe===null)continue}!(C.f&Ea)&&ge.push(C),Ie=C,fe=oc(C.next)}if(b.outrogroups!==null){for(var vt of b.outrogroups){var ft;vt.pending.size===0&&(Pv(b,Bu(vt.done)),(ft=b.outrogroups)===null||ft===void 0||ft.delete(vt))}b.outrogroups.size===0&&(b.outrogroups=null)}if(fe!==null||_!==void 0){var kt=[];if(_!==void 0)for(C of _)!(C.f&Pa)&&kt.push(C);for(;fe!==null;)!(fe.f&Pa)&&fe!==b.fallback&&kt.push(fe),fe=oc(fe.next);var oe=kt.length;if(oe>0){var Ze=4&O&&H===0?E:null;if(D){for(z=0;z<oe;z+=1){var te;(te=kt[z].nodes)===null||te===void 0||(te=te.a)===null||te===void 0||te.measure()}for(z=0;z<oe;z+=1){var X;(X=kt[z].nodes)===null||X===void 0||(X=X.a)===null||X===void 0||X.fix()}}(function(B,Ne,ee){for(var L,pt=Ne.length,ht=Ne.length,_e=function(){var qt=Ne[at];Ml(qt,()=>{if(L){if(L.pending.delete(qt),L.done.add(qt),L.pending.size===0){var S=B.outrogroups;Pv(B,Bu(L.done)),S.delete(L),S.size===0&&(B.outrogroups=null)}}else ht-=1},!1)},at=0;at<pt;at++)_e();if(ht===0){var We=ee!==null;if(We){var Ye=ee,Tt=Ye.parentNode;Tt.textContent="",Tt.append(Ye),B.items.clear()}Pv(B,Ne,!We)}else{var He;L={pending:new Set(Ne),done:new Set},((He=B.outrogroups)!==null&&He!==void 0?He:B.outrogroups=new Set).add(L)}})(b,kt,Ze)}}D&&Vi(()=>{if(A!==void 0)for(C of A){var B;(B=C.nodes)===null||B===void 0||(B=B.a)===null||B===void 0||B.apply()}})}(y,c,s,t,o),u!==null&&(c.length===0?u.f&Ea?(u.f^=Ea,ac(u,null,s)):zf(u):Ml(u,()=>{u=null})))}var p=Jl(()=>{for(var j=(c=r(d)).length,b=new Set,k=Vn,E=0;E<j;E+=1){var O=c[E],w=o(O,E),_=f?null:l.get(w);_?(_.v&&Tl(_.v,O),_.i&&Tl(_.i,E)):(_=v9(l,f?s:Ks??(Ks=Cs()),O,w,E,i,t,n),f||(_.e.f|=Ea),l.set(w,_)),b.add(w)}j===0&&a&&!u&&(f?u=pi(()=>a(s)):(u=pi(()=>a(Ks??(Ks=Cs())))).f|=Ea),j>b.size&&function(){throw new Error("https://svelte.dev/e/each_key_duplicate")}(),f||(v.set(k,b),h(k)),r(d)}),y={effect:p,items:l,pending:v,outrogroups:null,fallback:u};f=!1}function oc(e){for(;e!==null&&!(e.f&Bl);)e=e.next;return e}function v9(e,t,n,o,i,a,s,l){var c=1&s?16&s?fi(n):R(n,!1,!1):null,u=2&s?fi(i):null;return{v:c,i:u,e:pi(()=>(a(t,c??n,u??i,l),()=>{e.delete(o)}))}}function ac(e,t,n){if(e.nodes)for(var o=e.nodes.start,i=e.nodes.end,a=t&&!(t.f&Ea)?t.nodes.start:n;o!==null;){var s=Xc(o);if(a.before(o),o===i)return;o=s}}function _i(e,t,n){t===null?e.effect.first=n:t.next=n,n===null?e.effect.last=t:n.prev=t}function uy(e,t){var n=arguments.length>2&&arguments[2]!==void 0&&arguments[2],o=arguments.length>3&&arguments[3]!==void 0&&arguments[3],i=arguments.length>4&&arguments[4]!==void 0&&arguments[4],a=e,s="";if(n)var l=e;Le(()=>{var c,u=pn;if(s!==(s=(c=t())!==null&&c!==void 0?c:"")){if(n)return u.nodes=null,l.innerHTML=s,void(s!==""&&Zi(Uo(l),l.lastChild));if(u.nodes!==null&&(Jb(u.nodes.start,u.nodes.end),u.nodes=null),s!==""){var d=Ub(o?"svg":i?"math":"template",o?"http://www.w3.org/2000/svg":i?"http://www.w3.org/1998/Math/MathML":void 0);d.innerHTML=s;var v=o||i?d:d.content;if(Zi(Uo(v),v.lastChild),o||i)for(;Uo(v);)a.before(Uo(v));else a.before(v)}}})}function Sr(e,t,n,o,i){var a,s=(a=t.$$slots)===null||a===void 0?void 0:a[n],l=!1;s===!0&&(s=t[n==="default"?"children":n],l=!0),s===void 0?i!==null&&i(e):s(e,l?()=>o:o)}function dy(e,t,n){var o=new Gd(e);Jl(()=>{var i,a=(i=t())!==null&&i!==void 0?i:null;o.ensure(a,a&&(s=>n(s,a)))},As)}function go(e,t,n){so(()=>{var o=F(()=>t(e,n==null?void 0:n())||{});if(n&&o!=null&&o.update){var i=!1,a={};Vl(()=>{var s=n();x(s),i&&yb(a,s)&&(a=s,o.update(s))}),i=!0}if(o!=null&&o.destroy)return()=>o.destroy()})}function f9(e,t){var n,o=void 0;Wb(()=>{o!==(o=t())&&(n&&(uo(n),n=null),o&&(n=pi(()=>{so(()=>o(e))})))})}function vy(e){var t,n,o="";if(typeof e=="string"||typeof e=="number")o+=e;else if(typeof e=="object")if(Array.isArray(e)){var i=e.length;for(t=0;t<i;t++)e[t]&&(n=vy(e[t]))&&(o&&(o+=" "),o+=n)}else for(n in e)e[n]&&(o&&(o+=" "),o+=n);return o}function es(e){return typeof e=="object"?function(){for(var t,n,o=0,i="",a=arguments.length;o<a;o++)(t=arguments[o])&&(n=vy(t))&&(i&&(i+=" "),i+=n);return i}(e):e??""}var om=[...` 	
\r\f \v\uFEFF`];function am(e){var t=arguments.length>1&&arguments[1]!==void 0&&arguments[1]?" !important;":";",n="";for(var o of Object.keys(e)){var i=e[o];i!=null&&i!==""&&(n+=" "+o+": "+i+t)}return n}function Nv(e){return e[0]!=="-"||e[1]!=="-"?e.toLowerCase():e}function Bt(e,t,n,o,i,a){var s=e.__className;if(s!==n||s===void 0){var l=function(d,v,f){var h=d==null?"":""+d;if(v&&(h=h?h+" "+v:v),f){for(var p of Object.keys(f))if(f[p])h=h?h+" "+p:p;else if(h.length)for(var y=p.length,j=0;(j=h.indexOf(p,j))>=0;){var b=j+y;j!==0&&!om.includes(h[j-1])||b!==h.length&&!om.includes(h[b])?j=b:h=(j===0?"":h.substring(0,j))+h.substring(b+1)}}return h===""?null:h}(n,o,a);l==null?e.removeAttribute("class"):t?e.className=l:e.setAttribute("class",l),e.__className=n}else if(a&&i!==a)for(var c in a){var u=!!a[c];i!=null&&u===!!i[c]||e.classList.toggle(c,u)}return a}function Rv(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},n=arguments.length>2?arguments[2]:void 0,o=arguments.length>3?arguments[3]:void 0;for(var i in n){var a=n[i];t[i]!==a&&(n[i]==null?e.style.removeProperty(i):e.style.setProperty(i,a,o))}}function ea(e,t,n,o){if(e.__style!==t){var i=function(a,s){if(s){var l,c,u="";if(Array.isArray(s)?(l=s[0],c=s[1]):l=s,a){a=String(a).replaceAll(/\s*\/\*.*?\*\/\s*/g,"").trim();var d=!1,v=0,f=!1,h=[];l&&h.push(...Object.keys(l).map(Nv)),c&&h.push(...Object.keys(c).map(Nv));for(var p=0,y=-1,j=a.length,b=0;b<j;b++){var k=a[b];if(f?k==="/"&&a[b-1]==="*"&&(f=!1):d?d===k&&(d=!1):k==="/"&&a[b+1]==="*"?f=!0:k==='"'||k==="'"?d=k:k==="("?v++:k===")"&&v--,!f&&d===!1&&v===0){if(k===":"&&y===-1)y=b;else if(k===";"||b===j-1){if(y!==-1){var E=Nv(a.substring(p,y).trim());h.includes(E)||(k!==";"&&b++,u+=" "+a.substring(p,b).trim()+";")}p=b+1,y=-1}}}}return l&&(u+=am(l)),c&&(u+=am(c,!0)),(u=u.trim())===""?null:u}return a==null?null:String(a)}(t,o);i==null?e.removeAttribute("style"):e.style.cssText=i,e.__style=t}else o&&(Array.isArray(o)?(Rv(e,n==null?void 0:n[0],o[0]),Rv(e,n==null?void 0:n[1],o[1],"important")):Rv(e,n,o));return o}function qf(e,t){var n=arguments.length>2&&arguments[2]!==void 0&&arguments[2];if(e.multiple){if(t==null)return;if(!Qc(t))return void console.warn("https://svelte.dev/e/select_multiple_invalid_value");for(var o of e.options)o.selected=t.includes(im(o))}else{for(o of e.options)if(e9(im(o),t))return void(o.selected=!0);n&&t===void 0||(e.selectedIndex=-1)}}function p9(e){var t=new MutationObserver(()=>{qf(e,e.__value)});t.observe(e,{childList:!0,subtree:!0,attributes:!0,attributeFilter:["value"]}),Kd(()=>{t.disconnect()})}function im(e){return"__value"in e?e.__value:e.value}var ol=Symbol("class"),ic=Symbol("style"),fy=Symbol("is custom element"),py=Symbol("is html"),h9=Rp?"option":"OPTION",g9=Rp?"select":"SELECT",m9=Rp?"progress":"PROGRESS";function Ps(e,t){var n=Vp(e);n.value!==(n.value=t??void 0)&&(e.value!==t||t===0&&e.nodeName===m9)&&(e.value=t??"")}function Tn(e,t,n,o){var i=Vp(e);i[t]!==(i[t]=n)&&(t==="loading"&&(e[JC]=n),n==null?e.removeAttribute(t):typeof n!="string"&&hy(e).includes(t)?e[t]=n:e.setAttribute(t,n))}function b9(e,t,n,o){var i,a=Vp(e),s=a[fy],l=!a[py],c=t||{},u=e.nodeName===h9;for(var d in t)d in n||(n[d]=null);n.class?n.class=es(n.class):(o||n[ol])&&(n.class=null),n[ic]&&((i=n.style)!==null&&i!==void 0||(n.style=null));var v,f,h,p,y,j,b=hy(e),k=function(O){var w=n[O];if(u&&O==="value"&&w==null)return e.value=e.__value="",c[O]=w,0;if(O==="class")return v=e.namespaceURI==="http://www.w3.org/1999/xhtml",Bt(e,v,w,o,t==null?void 0:t[ol],n[ol]),c[O]=w,c[ol]=n[ol],0;if(O==="style")return ea(e,w,t==null?void 0:t[ic],n[ic]),c[O]=w,c[ic]=n[ic],0;if(w===(f=c[O])&&(w!==void 0||!e.hasAttribute(O))||(c[O]=w,(h=O[0]+O[1])==="$$"))return 0;if(h==="on"){var _={},A="$$"+O,q=O.slice(2);if(p=function(Q){return r9.includes(Q)}(q),function(Q){return Q.endsWith("capture")&&Q!=="gotpointercapture"&&Q!=="lostpointercapture"}(q)&&(q=q.slice(0,-7),_.capture=!0),!p&&f){if(w!=null)return 0;e.removeEventListener(q,c[A],_),c[A]=null}if(p)ha(q,e,w),Zc([q]);else if(w!=null){let Q=function(fe){c[O].call(this,fe)};c[A]=iy(q,e,Q,_)}}else if(O==="style")Tn(e,O,w);else if(O==="autofocus")(function(Q,fe){if(fe){var Ie=document.body;Q.autofocus=!0,Vi(()=>{document.activeElement===Ie&&Q.focus()})}})(e,!!w);else if(s||O!=="__value"&&(O!=="value"||w==null))if(O==="selected"&&u)(function(Q,fe){fe?Q.hasAttribute("selected")||Q.setAttribute("selected",""):Q.removeAttribute("selected")})(e,w);else if(y=O,l||(y=function(Q){var fe;return Q=Q.toLowerCase(),(fe=o9[Q])!==null&&fe!==void 0?fe:Q}(y)),j=y==="defaultValue"||y==="defaultChecked",w!=null||s||j)j||b.includes(y)&&(s||typeof w!="string")?(e[y]=w,y in a&&(a[y]=io)):typeof w!="function"&&Tn(e,y,w);else if(a[O]=null,y==="value"||y==="checked"){var C=e,z=t===void 0;if(y==="value"){var D=C.defaultValue;C.removeAttribute(y),C.defaultValue=D,C.value=C.__value=z?D:null}else{var H=C.defaultChecked;C.removeAttribute(y),C.defaultChecked=H,C.checked=!!z&&H}}else e.removeAttribute(O);else e.value=e.__value=w};for(var E in n)k(E);return c}function Vu(e,t){var n=arguments.length>5?arguments[5]:void 0,o=arguments.length>6&&arguments[6]!==void 0&&arguments[6],i=arguments.length>7&&arguments[7]!==void 0&&arguments[7];Pb(arguments.length>4&&arguments[4]!==void 0?arguments[4]:[],arguments.length>2&&arguments[2]!==void 0?arguments[2]:[],arguments.length>3&&arguments[3]!==void 0?arguments[3]:[],a=>{var s=void 0,l={},c=e.nodeName===g9,u=!1;if(Wb(()=>{var v=t(...a.map(r)),f=b9(e,s,v,n,o,i);for(var h of(u&&c&&"value"in v&&qf(e,v.value),Object.getOwnPropertySymbols(l)))v[h]||uo(l[h]);for(var p of Object.getOwnPropertySymbols(v)){var y=v[p];p.description!=="@attach"||s&&y===s[p]||(l[p]&&uo(l[p]),l[p]=pi(()=>f9(e,()=>y))),f[p]=y}s=f}),c){var d=e;so(()=>{qf(d,s.value,!0),p9(d)})}u=!0})}function Vp(e){var t;return(t=e.__attributes)!==null&&t!==void 0?t:e.__attributes={[fy]:e.nodeName.includes("-"),[py]:e.namespaceURI===db}}var sm=new Map;function hy(e){var t,n=e.getAttribute("is")||e.nodeName,o=sm.get(n);if(o)return o;sm.set(n,o=[]);for(var i=e,a=Element.prototype;a!==i;){for(var s in t=vb(i))t[s].set&&o.push(s);i=Np(i)}return o}function vd(e,t){var n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:t,o=new WeakSet;t9(e,"input",function(){var i=Pt(function*(a){var s=a?e.defaultValue:e.value;if(s=Iv(e)?qv(s):s,n(s),Vn!==null&&o.add(Vn),yield ty(),s!==(s=t())){var l=e.selectionStart,c=e.selectionEnd,u=e.value.length;if(e.value=s??"",c!==null){var d=e.value.length;l===c&&c===u&&d>u?(e.selectionStart=d,e.selectionEnd=d):(e.selectionStart=l,e.selectionEnd=Math.min(c,d))}}});return function(a){return i.apply(this,arguments)}}()),F(t)==null&&e.value&&(n(Iv(e)?qv(e.value):e.value),Vn!==null&&o.add(Vn)),Vl(()=>{var i=t();if(e===document.activeElement){var a=Vn;if(o.has(a))return}Iv(e)&&i===qv(e.value)||(e.type!=="date"||i||e.value)&&i!==e.value&&(e.value=i??"")})}function Iv(e){var t=e.type;return t==="number"||t==="range"}function qv(e){return e===""?null:+e}function Rt(e,t,n){var o=ii(e,t);o&&o.set&&(e[t]=n,Kd(()=>{e[t]=null}))}function lm(e,t){return e===t||(e==null?void 0:e[Na])===t}function or(){var e=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0,n=arguments.length>2?arguments[2]:void 0,o=Ln.r,i=pn;return so(()=>{var a,s;return Vl(()=>{a=s,s=[],F(()=>{e!==n(...s)&&(t(e,...s),a&&lm(n(...a),e)&&t(null,...a))})}),()=>{for(var l=i;l!==o&&l.parent!==null&&l.parent.f&Sf;)l=l.parent;var c=l.teardown;l.teardown=()=>{s&&lm(n(...s),e)&&t(null,...s),c==null||c()}}}),e}function Za(e){return function(){for(var t=arguments.length,n=new Array(t),o=0;o<t;o++)n[o]=arguments[o];return n[0].stopPropagation(),e==null?void 0:e.apply(this,n)}}function Ti(e){return function(){for(var t=arguments.length,n=new Array(t),o=0;o<t;o++)n[o]=arguments[o];return n[0].preventDefault(),e==null?void 0:e.apply(this,n)}}function Ft(){var e=arguments.length>0&&arguments[0]!==void 0&&arguments[0],t=Ln,n=t.l.u;if(n){var o,i=()=>x(t.s);if(e){var a=0,s={},l=Yc(()=>{var c=!1,u=t.s;for(var d in u)u[d]!==s[d]&&(s[d]=u[d],c=!0);return c&&a++,a});i=()=>r(l)}n.b.length&&(o=()=>{cm(t,i),kf(n.b)},Bb(),Ca(1048584,o)),Af(()=>{var c=F(()=>n.m.map(FC));return()=>{for(var u of c)typeof u=="function"&&u()}}),n.a.length&&Af(()=>{cm(t,i),kf(n.a)})}}function cm(e,t){if(e.l.s)for(var n of e.l.s)r(n);t()}function Yd(e){var t=fi(0);return function(){return arguments.length===1?(g(t,r(t)+1),arguments[0]):(r(t),e())}}function dc(e,t){var n,o=(n=e.$$events)===null||n===void 0?void 0:n[t.type],i=Qc(o)?o.slice():o==null?[]:[o];for(var a of i)a.call(this,t)}var y9={get(e,t){if(!e.exclude.includes(t))return r(e.version),t in e.special?e.special[t]():e.props[t]},set(e,t,n){if(!(t in e.special)){var o=pn;try{Ao(e.parent_effect),e.special[t]=m({get[t](){return e.props[t]}},t,4)}finally{Ao(o)}}return e.special[t](n),Yg(e.version),!0},getOwnPropertyDescriptor(e,t){if(!e.exclude.includes(t))return t in e.props?{enumerable:!0,configurable:!0,value:e.props[t]}:void 0},deleteProperty:(e,t)=>(e.exclude.includes(t)||(e.exclude.push(t),Yg(e.version)),!0),has:(e,t)=>!e.exclude.includes(t)&&t in e.props,ownKeys:e=>Reflect.ownKeys(e.props).filter(t=>!e.exclude.includes(t))};function Cu(e,t){return new Proxy({props:e,exclude:t,special:{},version:fi(0),parent_effect:pn},y9)}var j9={get(e,t){for(var n=e.props.length;n--;){var o=e.props[n];if(nc(o)&&(o=o()),typeof o=="object"&&o!==null&&t in o)return o[t]}},set(e,t,n){for(var o=e.props.length;o--;){var i=e.props[o];nc(i)&&(i=i());var a=ii(i,t);if(a&&a.set)return a.set(n),!0}return!1},getOwnPropertyDescriptor(e,t){for(var n=e.props.length;n--;){var o=e.props[n];if(nc(o)&&(o=o()),typeof o=="object"&&o!==null&&t in o){var i=ii(o,t);return i&&!i.configurable&&(i.configurable=!0),i}}},has(e,t){if(t===Na||t===mb)return!1;for(var n of e.props)if(nc(n)&&(n=n()),n!=null&&t in n)return!0;return!1},ownKeys(e){var t=[];for(var n of e.props)if(nc(n)&&(n=n()),n){for(var o in n)t.includes(o)||t.push(o);for(var i of Object.getOwnPropertySymbols(n))t.includes(i)||t.push(i)}return t}};function Hi(){for(var e=arguments.length,t=new Array(e),n=0;n<e;n++)t[n]=arguments[n];return new Proxy({props:t},j9)}function m(e,t,n,o){var i,a,s=!Ul||!!(2&n),l=!!(8&n),c=!!(16&n),u=o,d=!0,v=()=>(d&&(d=!1,u=c?F(o):o),u);if(l){var f,h,p=Na in e||mb in e;i=(f=(h=ii(e,t))===null||h===void 0?void 0:h.set)!==null&&f!==void 0?f:p&&t in e?w=>e[t]=w:void 0}var y,j=!1;if(l?[a,j]=function(w){var _=yu;try{return yu=!1,[w(),yu]}finally{yu=_}}(()=>e[t]):a=e[t],a===void 0&&o!==void 0&&(a=v(),i&&(s&&function(){throw new Error("https://svelte.dev/e/props_invalid_value")}(),i(a))),y=s?()=>{var w=e[t];return w===void 0?v():(d=!0,w)}:()=>{var w=e[t];return w!==void 0&&(u=void 0),w===void 0?u:w},s&&!(4&n))return y;if(i){var b=e.$$legacy;return function(w,_){return arguments.length>0?(s&&_&&!b&&!j||i(_?y():w),w):y()}}var k=!1,E=(1&n?Yc:nt)(()=>(k=!1,y()));l&&r(E);var O=pn;return function(w,_){if(arguments.length>0){var A=_?r(E):s&&l?ll(w):w;return g(E,A),k=!0,u!==void 0&&(u=A),w}return Xi&&k||O.f&si?E.v:r(E)}}function Zr(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:function(o){var i=function(a){try{if(typeof window<"u"&&window.localStorage!==void 0)return window.localStorage[a]}catch{}}("debug");return i!=null&&i.endsWith("*")?o.startsWith(i.slice(0,-1)):o===i}(e);if(!t)return x9;var n=function(o){for(var i=0,a=0;a<o.length;a++)i=(i<<5)-i+o.charCodeAt(a),i|=0;return um[Math.abs(i)%um.length]}(e);return function(){for(var o=arguments.length,i=new Array(o),a=0;a<o;a++)i[a]=arguments[a];console.log("%c".concat(e),"color:".concat(n),...i)}}function x9(){}var um=["#0000CC","#0099FF","#009400","#8dd200","#CCCC00","#CC9933","#ae04e7","#ff35d7","#FF3333","#FF6600","#FF9933","#FFCC33"],w9=0;function ul(){return++w9}function lo(e){return parseInt(e,10)}function Jp(e){return k9.test(e)}var k9=/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$/;function Cn(e){return typeof e=="object"&&e!==null&&(e.constructor===void 0||e.constructor.name==="Object")}function mr(e){return typeof e=="object"&&e!==null&&(e.constructor===void 0||e.constructor.name==="Object"||e.constructor.name==="Array")}function S9(e){return e===!0||e===!1}function Df(e){if(typeof e=="number")return e>9466848e5&&isFinite(e)&&Math.floor(e)===e&&!isNaN(new Date(e).valueOf());if(typeof e=="bigint")return Df(Number(e));try{var t=e&&e.valueOf();if(t!==e)return Df(t)}catch{return!1}return!1}function gy(e){(Ou=Ou||window.document.createElement("div")).style.color="",Ou.style.color=e;var t=Ou.style.color;return t!==""?t.replace(/\s+/g,"").toLowerCase():void 0}var Ou=void 0;function C9(e){return typeof e=="string"&&e.length<99&&!!gy(e)}function Hp(e,t){if(typeof e=="number"||typeof e=="string"||typeof e=="boolean"||e===void 0)return typeof e;if(typeof e=="bigint")return"number";if(e===null)return"null";if(Array.isArray(e))return"array";if(Cn(e))return"object";var n=t.stringify(e);return n&&Jp(n)?"number":n==="true"||n==="false"?"boolean":n==="null"?"null":"unknown"}var O9=/^https?:\/\/\S+$/;function Xd(e){return typeof e=="string"&&O9.test(e)}function Ql(e,t){if(e==="")return"";var n=e.trim();return n==="null"?null:n==="true"||n!=="false"&&(Jp(n)?t.parse(n):e)}var _9=[];function dm(e,t){if(e.length!==t.length)return!1;for(var n=0;n<e.length;n++)if(e[n]!==t[n])return!1;return!0}function Lf(e){var t=arguments.length>1&&arguments[1]!==void 0&&arguments[1],n={};if(!Array.isArray(e))throw new TypeError("Array expected");function o(s,l){(!Array.isArray(s)&&!Cn(s)||t&&l.length>0)&&(n[wt(l)]=!0),Cn(s)&&Object.keys(s).forEach(c=>{o(s[c],l.concat(c))})}for(var i=Math.min(e.length,1e4),a=0;a<i;a++)o(e[a],_9);return Object.keys(n).sort().map(Mo)}function my(e,t,n){if(!(t<=e))for(var o=e;o<t;o++)n(o)}function fd(e,t){return e.length>t?e.slice(0,t):e}function vm(e){return De({},e)}function fm(e){return Object.values(e)}function pm(e,t,n,o){var i=e.slice(0),a=i.splice(t,n);return i.splice.apply(i,[t+o,0,...a]),i}function E9(e,t,n){return e.slice(0,t).concat(n).concat(e.slice(t))}function eu(e,t){try{return t.parse(e)}catch{return t.parse(Aa(e))}}function by(e,t){try{return eu(e,t)}catch{return}}function tu(e,t){e=e.replace(jy,"");try{return t(e)}catch{}try{return t("{"+e+"}")}catch{}try{return t("["+e+"]")}catch{}throw new Error("Failed to parse partial JSON")}function yy(e){e=e.replace(jy,"");try{return Aa(e)}catch{}try{var t=Aa("["+e+"]");return t.substring(1,t.length-1)}catch{}try{var n=Aa("{"+e+"}");return n.substring(1,n.length-1)}catch{}throw new Error("Failed to repair partial JSON")}var jy=/,\s*$/;function $l(e,t){var n=gm.exec(t);if(n){var o=lo(n[2]),i=function(h,p){for(var y=arguments.length>2&&arguments[2]!==void 0?arguments[2]:0,j=arguments.length>3&&arguments[3]!==void 0?arguments[3]:h.length,b=0,k=y;k<j;k++)h.charAt(k)===p&&b++;return b}(e,`
`,0,o),a=o-e.lastIndexOf(`
`,o)-1;return{position:o,line:i,column:a,message:t.replace(gm,()=>"line ".concat(i+1," column ").concat(a+1))}}var s=A9.exec(t),l=s?lo(s[1]):void 0,c=l!==void 0?l-1:void 0,u=z9.exec(t),d=u?lo(u[1]):void 0,v=d!==void 0?d-1:void 0,f=c!==void 0&&v!==void 0?function(h,p,y){for(var j=h.indexOf(`
`),b=1;b<p&&j!==-1;)j=h.indexOf(`
`,j+1),b++;return j!==-1?j+y+1:void 0}(e,c,v):void 0;return{position:f,line:c,column:v,message:t.replace(/^JSON.parse: /,"").replace(/ of the JSON data$/,"")}}function Dv(e,t){try{var n=Nd.parse(e),o=wt(t),i=n.pointers[o];if(i)return{path:t,line:i.key?i.key.line:i.value?i.value.line:0,column:i.key?i.key.column:i.value?i.value.column:0,from:i.key?i.key.pos:i.value?i.value.pos:0,to:i.keyEnd?i.keyEnd.pos:i.valueEnd?i.valueEnd.pos:0}}catch(a){console.error(a)}return{path:t,line:0,column:0,from:0,to:0}}function Lv(e){return Cn(e)?e.json!==void 0?e.text!==void 0?'Content must contain either a property "json" or a property "text" but not both':void 0:e.text===void 0?'Content must contain either a property "json" or a property "text"':typeof e.text!="string"?'Content "text" property must be a string containing a JSON document. Did you mean to use the "json" property instead?':void 0:"Content must be an object"}function Mc(e){return Cn(e)&&typeof e.text=="string"}function $c(e){return Cn(e)&&e.json!==void 0}function T9(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:void 0,n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:JSON;return Mc(e)?e:{text:n.stringify(e.json,null,t)}}function hm(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:JSON;return $c(e)?e:{json:t.parse(e.text)}}function Uf(e,t,n){return T9(e,t,n).text}function M9(e,t){return $9(e,t)>t}function $9(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:1/0;if(Mc(e))return e.text.length;var n=e.json,o=0;return function i(a){if(Array.isArray(a)){if((o+=a.length-1+2)>t)return;for(var s=0;s<a.length;s++)if(i(a[s]),o>t)return}else if(Cn(a)){var l=Object.keys(a);o+=2+l.length+(l.length-1);for(var c=0;c<l.length;c++){var u=l[c],d=a[u];o+=u.length+2,i(d)}}else o+=typeof a=="string"?a.length+2:String(a).length}(n),o}var gm=/(position|char) (\d+)/,A9=/line (\d+)/,z9=/column (\d+)/;function xy(e,t){return e.parse===t.parse&&e.stringify===t.stringify}function mm(e){var t=e.substring(0,999).trim();return!t.includes(`
`)&&P9.test(t)}var Mr,Dn,da,ba,ya,Yo,Qi,P9=/[,:]\S/;function Qp(e){var{escapeControlCharacters:t,escapeUnicodeCharacters:n}=e;return t?n?N9:R9:n?I9:q9}(function(e){e.text="text",e.tree="tree",e.table="table"})(Mr||(Mr={})),function(e){e.after="after",e.inside="inside",e.key="key",e.value="value",e.multi="multi",e.text="text"}(Dn||(Dn={})),function(e){e.after="after",e.key="key",e.value="value",e.inside="inside"}(da||(da={})),function(e){e.info="info",e.warning="warning",e.error="error"}(ba||(ba={})),function(e){e.key="key",e.value="value"}(ya||(ya={})),function(e){e.asc="asc",e.desc="desc"}(Yo||(Yo={})),function(e){e.no="no",e.self="self",e.nextInside="nextInside"}(Qi||(Qi={}));var N9={escapeValue:e=>wy(Cy(String(e))),unescapeValue:e=>Oy(ky(e))},R9={escapeValue:e=>Cy(String(e)),unescapeValue:e=>Oy(e)},I9={escapeValue:e=>wy(String(e)),unescapeValue:e=>ky(e)},q9={escapeValue:e=>String(e),unescapeValue:e=>e};function wy(e){return e.replace(/[^\x20-\x7F]/g,t=>{var n;return t==="\b"||t==="\f"||t===`
`||t==="\r"||t==="	"?t:"\\u"+("000"+((n=t.codePointAt(0))===null||n===void 0?void 0:n.toString(16))).slice(-4)})}function ky(e){return e.replace(/\\u[a-fA-F0-9]{4}/g,t=>{try{var n=JSON.parse('"'+t+'"');return Sy[n]||n}catch{return t}})}var Sy={'"':'\\"',"\\":"\\\\","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","	":"\\t"},D9={'\\"':'"',"\\\\":"\\","\\/":"/","\\b":"\b","\\f":"\f","\\n":`
`,"\\r":"\r","\\t":"	"};function Cy(e){return e.replace(/["\b\f\n\r\t\\]/g,t=>Sy[t]||t)}function Oy(e){return e.replace(/\\["bfnrt\\]/g,t=>D9[t]||t)}function Al(e){return typeof e!="string"?String(e):e.endsWith(`
`)?e+`
`:e}function _y(e,t){return Kl(e,n=>n.nodeName.toUpperCase()===t.toUpperCase())}function Li(e,t,n){return Kl(e,o=>function(i,a,s){return typeof i.getAttribute=="function"&&i.getAttribute(a)===s}(o,t,n))}function Kl(e,t){return!!Kp(e,t)}function Kp(e,t){for(var n=e;n&&!t(n);)n=n.parentNode;return n}function nu(e){var t,n;return(t=e==null||(n=e.ownerDocument)===null||n===void 0?void 0:n.defaultView)!==null&&t!==void 0?t:void 0}function Gp(e){var t=nu(e),n=t==null?void 0:t.document.activeElement;return!!n&&Kl(n,o=>o===e)}function Ey(e,t){return Kp(e,n=>n.nodeName===t)}function Uv(e){return Li(e,"data-type","selectable-key")?Dn.key:Li(e,"data-type","selectable-value")?Dn.value:Li(e,"data-type","insert-selection-area-inside")?Dn.inside:Li(e,"data-type","insert-selection-area-after")?Dn.after:Dn.multi}function Ju(e){return encodeURIComponent(wt(e))}function Ty(e){var t,n=Kp(e,i=>!(i==null||!i.hasAttribute)&&i.hasAttribute("data-path")),o=(t=n==null?void 0:n.getAttribute("data-path"))!==null&&t!==void 0?t:void 0;return o?Mo(decodeURIComponent(o)):void 0}function L9(e){var{allElements:t,currentElement:n,direction:o,hasPrio:i=()=>!0,margin:a=10}=e,s=F8(t.filter(function(b){var k=b.getBoundingClientRect();return k.width>0&&k.height>0}),c),l=c(n);function c(b){var k=b.getBoundingClientRect();return{x:k.left+k.width/2,y:k.top+k.height/2,rect:k,element:b}}function u(b,k){var E=arguments.length>2&&arguments[2]!==void 0?arguments[2]:1,O=b.x-k.x,w=(b.y-k.y)*E;return Math.sqrt(O*O+w*w)}var d=b=>u(b,l);if(o==="Left"||o==="Right"){var v=o==="Left"?s.filter(b=>{return k=l,b.rect.left+a<k.rect.left;var k}):s.filter(b=>{return k=l,b.rect.right>k.rect.right+a;var k}),f=v.filter(b=>{return k=b,E=l,Math.abs(k.y-E.y)<a;var k,E}),h=hu(f,d)||hu(v,b=>u(b,l,10));return h==null?void 0:h.element}if(o==="Up"||o==="Down"){var p=o==="Up"?s.filter(b=>{return k=l,b.y+a<k.y;var k}):s.filter(b=>{return k=l,b.y>k.y+a;var k}),y=p.filter(b=>i(b.element)),j=hu(y,d)||hu(p,d);return j==null?void 0:j.element}}function Yp(){var e,t,n,o;return typeof navigator<"u"&&(e=(t=(n=navigator)===null||n===void 0||(n=n.platform)===null||n===void 0?void 0:n.toUpperCase().includes("MAC"))!==null&&t!==void 0?t:(o=navigator)===null||o===void 0||(o=o.userAgentData)===null||o===void 0||(o=o.platform)===null||o===void 0?void 0:o.toUpperCase().includes("MAC"))!==null&&e!==void 0&&e}function hi(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:"+",n=[];Xp(e,arguments.length>2&&arguments[2]!==void 0?arguments[2]:Yp)&&n.push("Ctrl"),e.altKey&&n.push("Alt"),e.shiftKey&&n.push("Shift");var o=e.key.length===1?e.key.toUpperCase():e.key;return o in U9||n.push(o),n.join(t)}function Xp(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:Yp;return e.ctrlKey||e.metaKey&&t()}var U9={Ctrl:!0,Command:!0,Control:!0,Alt:!0,Option:!0,Shift:!0};function It(e,t){t===void 0&&(t={});var n=t.insertAt;if(e&&typeof document<"u"){var o=document.head||document.getElementsByTagName("head")[0],i=document.createElement("style");i.type="text/css",n==="top"&&o.firstChild?o.insertBefore(i,o.firstChild):o.appendChild(i),i.styleSheet?i.styleSheet.cssText=e:i.appendChild(document.createTextNode(e))}}It(`.jse-absolute-popup.svelte-enkkpn {
  position: relative;
  left: 0;
  top: 0;
  width: 0;
  height: 0;
  z-index: 1001;
}
.jse-absolute-popup.svelte-enkkpn .jse-hidden-input:where(.svelte-enkkpn) {
  position: fixed;
  left: 0;
  top: 0;
  width: 0;
  height: 0;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  overflow: hidden;
}
.jse-absolute-popup.svelte-enkkpn .jse-absolute-popup-content:where(.svelte-enkkpn) {
  position: absolute;
}`);var B9=re('<div class="jse-absolute-popup-content svelte-enkkpn"><input type="text" readonly="" tabindex="-1" class="jse-hidden-input svelte-enkkpn"/> <!></div>'),F9=re('<div role="none" class="jse-absolute-popup svelte-enkkpn"><!></div>');function W9(e,t){yt(t,!1);var n=m(t,"popup",8),o=m(t,"closeAbsolutePopup",8),i=R(),a=R();function s(v){n().options&&n().options.closeOnOuterClick&&!Kl(v.target,f=>f===r(i))&&o()(n().id)}function l(v){hi(v)==="Escape"&&(v.preventDefault(),v.stopPropagation(),o()(n().id))}vo(function(){r(a)&&r(a).focus()}),Ft();var c=F9();ze("mousedown",li,function(v){s(v)},!0),ze("keydown",li,l,!0),ze("wheel",li,function(v){s(v)},!0);var u=I(c),d=v=>{var f=B9(),h=I(f);or(h,p=>g(a,p),()=>r(a)),dy(Y(h,2),()=>n().component,(p,y)=>{y(p,Hi(()=>n().props))}),Le(p=>ea(f,p),[()=>(r(i),x(n()),F(()=>function(p,y){var j=p.getBoundingClientRect(),{left:b,top:k,positionAbove:E,positionLeft:O}=function(){if(y.anchor){var{anchor:w,width:_=0,height:A=0,offsetTop:q=0,offsetLeft:C=0,position:z}=y,{left:D,top:H,bottom:Q,right:fe}=w.getBoundingClientRect(),Ie=z==="top"||H+A>window.innerHeight&&H>A,ge=z==="left"||D+_>window.innerWidth&&D>_;return{left:ge?fe-C:D+C,top:Ie?H-q:Q+q,positionAbove:Ie,positionLeft:ge}}if(typeof y.left=="number"&&typeof y.top=="number"){var{left:qe,top:ce,width:ve=0,height:he=0}=y;return{left:qe,top:ce,positionAbove:ce+he>window.innerHeight&&ce>he,positionLeft:qe+ve>window.innerWidth&&qe>ve}}throw new Error('Invalid config: pass either "left" and "top", or pass "anchor"')}();return(E?"bottom: ".concat(j.top-k,"px;"):"top: ".concat(k-j.top,"px;"))+(O?"right: ".concat(j.left-b,"px;"):"left: ".concat(b-j.left,"px;"))}(r(i),n().options)))]),U(v,f)};be(u,v=>{r(i)&&v(d)}),or(c,v=>g(i,v),()=>r(i)),ze("mousedown",c,function(v){v.stopPropagation()}),ze("keydown",c,l),U(e,c),jt()}var V9=re("<!> <!>",1);function Bf(e,t){yt(t,!1);var n=Zr("jsoneditor:AbsolutePopup"),o=R([],!0);function i(l){var c=r(o).findIndex(d=>d.id===l);if(c!==-1){var u=r(o)[c];u.options.onClose&&u.options.onClose(),g(o,r(o).filter(d=>d.id!==l))}}(function(l,c){xb().set(l,c)})("absolute-popup",{openAbsolutePopup:function(l,c,u){n("open...",c,u);var d={id:ul(),component:l,props:c||{},options:u||{}};return g(o,[...r(o),d]),d.id},closeAbsolutePopup:i}),ne(()=>r(o),()=>{n("popups",r(o))}),Mn(),Ft(!0);var a=V9(),s=Mt(a);Or(s,1,()=>r(o),Pr,(l,c)=>{W9(l,{get popup(){return r(c)},closeAbsolutePopup:i})}),Sr(Y(s,2),t,"default",{},null),U(e,a),jt()}function ru(e,t){for(var n=new Set(t),o=e.replace(/ \(copy( \d+)?\)$/,""),i=e,a=1;n.has(i);){var s="copy"+(a>1?" "+a:"");i="".concat(o," (").concat(s,")"),a++}return i}function ti(e,t){var n=t-3;return e.length>t?e.substring(0,n)+"...":e}function J9(e){if(e==="")return"";var t=e.toLowerCase();if(t==="null")return null;if(t==="true")return!0;if(t==="false")return!1;if(t!=="undefined"){var n=Number(e),o=parseFloat(e);return isNaN(n)||isNaN(o)?e:n}}var H9={id:"jsonquery",name:"JSONQuery",description:`
<p>
  Enter a <a href="https://jsonquerylang.org" target="_blank" 
  rel="noopener noreferrer">JSON Query</a> function to filter, sort, or transform the data.
  You can use functions like <code>get</code>, <code>filter</code>,
  <code>sort</code>, <code>pick</code>, <code>groupBy</code>, <code>uniq</code>, etcetera. 
  Example query: <code>filter(.age >= 18)</code>
</p>
`,createQuery:function(e,t){var{filter:n,sort:o,projection:i}=t,a=[];n&&n.path&&n.relation&&n.value&&a.push(["filter",[(s=n.relation,G1("1 ".concat(s," 1"))[0]),_u(n.path),J9(n.value)]]);var s;return o&&o.path&&o.direction&&a.push(["sort",_u(o.path),o.direction==="desc"?"desc":"asc"]),i&&i.paths&&(i.paths.length>1?a.push(["pick",...i.paths.map(_u)]):a.push(["map",_u(i.paths[0])])),PS(["pipe",...a])},executeQuery:function(e,t,n){var o=xy(n,JSON)?e:function(i){var a=n.stringify(i);return a!==void 0?JSON.parse(a):void 0}(e);return t.trim()!==""?NS(o,t):o}};function _u(e){return["get",...e]}var Q9=os("<g></g>");function K9(e,t){yt(t,!1);var n=870711,o=R(""),i=m(t,"data",8);function a(l){if(!l||!l.raw)return"";var c=l.raw,u={};return c=c.replace(/\s(?:xml:)?id=["']?([^"')\s]+)/g,(d,v)=>{var f="fa-".concat((n+=1).toString(16));return u[v]=f,' id="'.concat(f,'"')}),c=c.replace(/#(?:([^'")\s]+)|xpointer\(id\((['"]?)([^')]+)\2\)\))/g,(d,v,f,h)=>{var p=v||h;return p&&u[p]?"#".concat(u[p]):d}),c}ne(()=>x(i()),()=>{g(o,a(i()))}),Mn();var s=Q9();uy(s,()=>r(o),!0),U(e,s),jt()}It(`
  .fa-icon.svelte-v67cny {
    display: inline-block;
    fill: currentColor;
  }
  .fa-flip-horizontal.svelte-v67cny {
    transform: scale(-1, 1);
  }
  .fa-flip-vertical.svelte-v67cny {
    transform: scale(1, -1);
  }
  .fa-spin.svelte-v67cny {
    animation: svelte-v67cny-fa-spin 1s 0s infinite linear;
  }
  .fa-inverse.svelte-v67cny {
    color: #fff;
  }
  .fa-pulse.svelte-v67cny {
    animation: svelte-v67cny-fa-spin 1s infinite steps(8);
  }
  @keyframes svelte-v67cny-fa-spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
`);var G9=os("<svg><!></svg>"),Y9=os("<path></path>"),X9=os("<polygon></polygon>"),Z9=os("<!><!><!>",1);function un(e,t){var n=Cu(t,["children","$$slots","$$events","$$legacy"]),o=Cu(n,["class","data","scale","spin","inverse","pulse","flip","label","style"]);yt(t,!1);var i=m(t,"class",8,""),a=m(t,"data",8),s=R(),l=m(t,"scale",8,1),c=m(t,"spin",8,!1),u=m(t,"inverse",8,!1),d=m(t,"pulse",8,!1),v=m(t,"flip",8,void 0),f=m(t,"label",8,""),h=m(t,"style",8,""),p=R(10),y=R(10),j=R(),b=R();function k(){var O=1;return l()!==void 0&&(O=Number(l())),isNaN(O)||O<=0?(console.warn('Invalid prop: prop "scale" should be a number over 0.'),1):1*O}function E(){return r(s)?Math.max(r(s).width,r(s).height)/16:1}ne(()=>(x(a()),x(h()),x(l())),()=>{g(s,function(O){var w;if(O){if(!("definition"in O)){if("iconName"in O&&"icon"in O){O.iconName;var[_,A,,,q]=O.icon;w={width:_,height:A,paths:(Array.isArray(q)?q:[q]).map(C=>({d:C}))}}else w=O[Object.keys(O)[0]];return w}console.error("`import faIconName from '@fortawesome/package-name/faIconName` not supported - Please use `import { faIconName } from '@fortawesome/package-name/faIconName'` instead")}}(a())),h(),l(),g(p,r(s)?r(s).width/E()*k():0),g(y,r(s)?r(s).height/E()*k():0),g(j,function(){var O="";h()!==null&&(O+=h());var w=k();return w===1?O.length===0?"":O:(O===""||O.endsWith(";")||(O+="; "),"".concat(O,"font-size: ").concat(w,"em"))}()),g(b,r(s)?"0 0 ".concat(r(s).width," ").concat(r(s).height):"0 0 ".concat(r(p)," ").concat(r(y)))}),Mn(),Ft(),function(O,w){var _=Cu(w,["children","$$slots","$$events","$$legacy"]),A=Cu(_,["class","width","height","box","spin","inverse","pulse","flip","style","label"]),q=m(w,"class",8,""),C=m(w,"width",8),z=m(w,"height",8),D=m(w,"box",8,"0 0 0 0"),H=m(w,"spin",8,!1),Q=m(w,"inverse",8,!1),fe=m(w,"pulse",8,!1),Ie=m(w,"flip",8,"none"),ge=m(w,"style",8,""),qe=m(w,"label",8,""),ce=G9();Vu(ce,()=>{var ve;return De(De({version:"1.1",class:"fa-icon ".concat((ve=q())!==null&&ve!==void 0?ve:""),width:C(),height:z(),"aria-label":qe(),role:qe()?"img":"presentation",viewBox:D(),style:ge()},A),{},{[ol]:{"fa-spin":H(),"fa-pulse":fe(),"fa-inverse":Q(),"fa-flip-horizontal":Ie()==="horizontal","fa-flip-vertical":Ie()==="vertical"}})},void 0,void 0,void 0,"svelte-v67cny"),Sr(I(ce),w,"default",{},null),U(O,ce)}(e,Hi({get label(){return f()},get width(){return r(p)},get height(){return r(y)},get box(){return r(b)},get style(){return r(j)},get spin(){return c()},get flip(){return v()},get inverse(){return u()},get pulse(){return d()},get class(){return i()}},()=>o,{children:(O,w)=>{var _=br();Sr(Mt(_),t,"default",{},A=>{var q=Z9(),C=Mt(q);Or(C,1,()=>(r(s),F(()=>{var Q;return((Q=r(s))===null||Q===void 0?void 0:Q.paths)||[]})),Pr,(Q,fe)=>{var Ie=Y9();Vu(Ie,()=>De({},r(fe))),U(Q,Ie)});var z=Y(C);Or(z,1,()=>(r(s),F(()=>{var Q;return((Q=r(s))===null||Q===void 0?void 0:Q.polygons)||[]})),Pr,(Q,fe)=>{var Ie=X9();Vu(Ie,()=>De({},r(fe))),U(Q,Ie)});var D=Y(z),H=Q=>{K9(Q,{get data(){return r(s)},set data(fe){g(s,fe)},$$legacy:!0})};be(D,Q=>{r(s),F(()=>{var fe;return(fe=r(s))===null||fe===void 0?void 0:fe.raw})&&Q(H)}),U(A,q)}),U(O,_)},$$slots:{default:!0}})),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-boolean-toggle.svelte-eli4ob {
  padding: 0;
  margin: 1px 0 0;
  vertical-align: top;
  display: inline-flex;
  color: var(--jse-value-color-boolean, #ff8c00);
}

.jse-boolean-toggle.svelte-eli4ob:not(.jse-readonly) {
  cursor: pointer;
}`);var e5=re('<div role="checkbox" tabindex="-1"><!></div>');function t5(e,t){yt(t,!1);var n=m(t,"path",9),o=m(t,"value",9),i=m(t,"readOnly",9),a=m(t,"onPatch",9),s=m(t,"focus",9);Ft(!0);var l,c=e5(),u=I(c),d=nt(()=>o()===!0?Y1:X1);un(u,{get data(){return r(d)}}),Le(()=>{Tn(c,"aria-checked",o()===!0),l=Bt(c,1,"jse-boolean-toggle svelte-eli4ob",null,l,{"jse-readonly":i()}),Tn(c,"title",i()?"Boolean value ".concat(o()):"Click to toggle this boolean value")}),ze("mousedown",c,function(v){v.stopPropagation(),i()||(a()([{op:"replace",path:wt(n()),value:!o()}]),s()())}),U(e,c),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-color-picker-popup.svelte-v77py2 .picker_wrapper.popup,
.jse-color-picker-popup.svelte-v77py2 .picker_wrapper.popup .picker_arrow::before,
.jse-color-picker-popup.svelte-v77py2 .picker_wrapper.popup .picker_arrow::after {
  background: var(--jse-color-picker-background, var(--jse-panel-background, #ebebeb));
  line-height: normal;
}
.jse-color-picker-popup.svelte-v77py2 .picker_slider,
.jse-color-picker-popup.svelte-v77py2 .picker_sl,
.jse-color-picker-popup.svelte-v77py2 .picker_editor input,
.jse-color-picker-popup.svelte-v77py2 .picker_sample,
.jse-color-picker-popup.svelte-v77py2 .picker_done button {
  box-shadow: var(--jse-color-picker-border-box-shadow, #cbcbcb 0 0 0 1px);
}
.jse-color-picker-popup.svelte-v77py2 .picker_editor input {
  background: var(--jse-background-color, #fff);
  color: var(--jse-text-color, #4d4d4d);
}
.jse-color-picker-popup.svelte-v77py2 .picker_done button {
  background: var(--jse-button-background, #e0e0e0);
  color: var(--jse-button-color, var(--jse-text-color, #4d4d4d));
}
.jse-color-picker-popup.svelte-v77py2 .picker_done button:hover {
  background: var(--jse-button-background-highlight, #e7e7e7);
}`);var n5=re('<div class="jse-color-picker-popup svelte-v77py2"></div>');function r5(e,t){yt(t,!1);var n=m(t,"color",8),o=m(t,"onChange",8),i=m(t,"showOnTop",8),a=R(),s=()=>{};vo(Pt(function*(){var c,u=new((c=yield dx(()=>import("./vanilla-picker-2033e4d0.js"),[]))===null||c===void 0?void 0:c.default)({parent:r(a),color:n(),popup:i()?"top":"bottom",onDone(d){var v=d.rgba[3]===1?d.hex.substring(0,7):d.hex;o()(v)}});u.show(),s=()=>{u.destroy()}})),ra(()=>{s()}),Ft();var l=n5();or(l,c=>g(a,c),()=>r(a)),U(e,l),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-color-picker-button.svelte-13mgyo6 {
  font-size: var(--jse-font-size-mono, 14px);
  width: var(--jse-color-picker-button-size, 1em);
  height: var(--jse-color-picker-button-size, 1em);
  box-sizing: border-box;
  padding: 0;
  margin: 2px 0 0 calc(0.5 * var(--jse-padding, 10px));
  display: inline-flex;
  vertical-align: top;
  border: 1px solid var(--jse-text-color, #4d4d4d);
  border-radius: 2px;
  background: inherit;
  outline: none;
}

.jse-color-picker-button.svelte-13mgyo6:not(.jse-readonly) {
  cursor: pointer;
}`);var o5=re('<button type="button"></button>');function a5(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),{openAbsolutePopup:i}=rs("absolute-popup"),a=m(t,"path",9),s=m(t,"value",9),l=m(t,"readOnly",9),c=m(t,"onPatch",9),u=m(t,"focus",9);function d(p){c()([{op:"replace",path:wt(a()),value:p}]),v()}function v(){u()()}ne(()=>x(s()),()=>{g(n,gy(s()))}),ne(()=>(x(l()),x(s())),()=>{g(o,l()?"Color ".concat(s()):"Click to open a color picker")}),Mn(),Ft(!0);var f,h=o5();Le(()=>{var p;f=Bt(h,1,"jse-color-picker-button svelte-13mgyo6",null,f,{"jse-readonly":l()}),ea(h,"background: ".concat((p=r(n))!==null&&p!==void 0?p:"")),Tn(h,"title",r(o)),Tn(h,"aria-label",r(o))}),ze("click",h,function(p){var y,j;if(!l()){var b=p.target,k=b.getBoundingClientRect().top,E=((y=(j=nu(b))===null||j===void 0?void 0:j.innerHeight)!==null&&y!==void 0?y:0)-k<300&&k>300,O={color:s(),onChange:d,showOnTop:E};i(r5,O,{anchor:b,closeOnOuterClick:!0,onClose:v,offsetTop:18,offsetLeft:-8,height:300})}}),U(e,h),jt()}var Bv=1e3,Ac=100,Eu=100,pd=2e4,bl=[{start:0,end:Ac}],i5=1048576,s5=1048576,Fv="Insert or paste contents, enter [ insert a new array, enter { to insert a new object, or start typing to insert a new value",Zp="Open context menu (Click here, right click on the selection, or use the context menu button or Ctrl+Q)",vs="hover-insert-inside",Tu="hover-insert-after",bm="hover-collection",Wv="valid",ym="repairable",ni=336,ri=260,vc=100,jm={[Yo.asc]:"ascending",[Yo.desc]:"descending"};function My(e){for(var t=fS(e,l=>l.start),n=[t[0]],o=0;o<t.length;o++){var i=n.length-1,a=n[i],s=t[o];s.start<=a.end?n[i]={start:Math.min(a.start,s.start),end:Math.max(a.end,s.end)}:n.push(s)}return n}function Ff(e){return hd(e)+Ac}function hd(e){return Math.floor(e/Ac)*Ac}function Wf(e){return!!e&&(e.type==="space"||e.space===!0)}function zi(e){return!!e&&(e.type==="separator"||e.separator===!0)}function xm(e){return!!e&&e.type==="label"&&typeof e.text=="string"}function ei(e){return!!e&&typeof e.onClick=="function"}function Gs(e){return!!e&&e.type==="dropdown-button"&&ei(e.main)&&Array.isArray(e.items)}function wm(e){return!!e&&e.type==="row"&&Array.isArray(e.items)}function km(e){return!!e&&e.type==="column"&&Array.isArray(e.items)}function Sm(e){return Cn(e)&&Cn(e.parseError)}function l5(e){return Cn(e)&&Array.isArray(e.validationErrors)}function c5(e){return Cn(e)&&Array.isArray(e.path)&&typeof e.message=="string"&&"severity"in e}function u5(e){return Cn(e)&&c5(e)&&typeof e.isChildError=="boolean"}function d5(e){return Cn(e)&&typeof e.action=="function"&&Cn(e.props)}function Oo(e){return e!==void 0&&e.type==="object"}function Gr(e){return e!==void 0&&e.type==="array"}function eh(e){return e!==void 0&&e.type==="value"}function Ns(e){return Oo(e)||Gr(e)}function $y(e){return e!==void 0&&Array.isArray(e.searchResults)}function gd(e){return!!e&&e.type==="tree"}function Cm(e){return!!e&&e.type==="text"}function Om(e){return!!e&&e.type==="mode"}function Vf(e){var{json:t,expand:n}=e,o=function(i){var{json:a,factory:s}=i;return Array.isArray(a)?s.createArrayDocumentState():Cn(a)?s.createObjectDocumentState():a!==void 0?s.createValueDocumentState():void 0}({json:t,factory:rh});return n&&o?la(t,o,[],n):o}function th(){var{expanded:e}=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{expanded:!1};return{type:"array",expanded:e,visibleSections:bl,items:[]}}function nh(){var{expanded:e}=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{expanded:!1};return{type:"object",expanded:e,properties:{}}}var rh={createObjectDocumentState:nh,createArrayDocumentState:th,createValueDocumentState:function(){return{type:"value"}}};function Ay(e,t,n,o){var{createObjectDocumentState:i,createArrayDocumentState:a,createValueDocumentState:s}=o;return function l(c,u,d){if(Array.isArray(c)){var v=Gr(u)?u:a();if(d.length===0)return v;var f=lo(d[0]),h=l(c[f],v.items[f],d.slice(1));return Co(v,["items",d[0]],h)}if(Cn(c)){var p=Oo(u)?u:i();if(d.length===0)return p;var y=d[0],j=l(c[y],p.properties[y],d.slice(1));return Co(p,["properties",y],j)}return eh(u)?u:s()}(e,t,n)}function Do(e,t){return zc(e,t,arguments.length>2&&arguments[2]!==void 0?arguments[2]:[],(n,o)=>{if(n!==void 0&&o!==void 0)return Array.isArray(n)?Gr(o)?o:th({expanded:!!Ns(o)&&o.expanded}):Cn(n)?Oo(o)?o:nh({expanded:!!Ns(o)&&o.expanded}):eh(o)?o:void 0},()=>!0)}function zc(e,t,n,o,i){var a=o(e,t,n);if(Array.isArray(e)&&Gr(a)&&i(a)){var s=[];return oh(e,a.visibleSections,c=>{var u=n.concat(String(c)),d=zc(e[c],a.items[c],u,o,i);d!==void 0&&(s[c]=d)}),dm(s,a.items)?a:De(De({},a),{},{items:s})}if(Cn(e)&&Oo(a)&&i(a)){var l={};return Object.keys(e).forEach(c=>{var u=n.concat(c),d=zc(e[c],a.properties[c],u,o,i);d!==void 0&&(l[c]=d)}),dm(Object.values(l),Object.values(a.properties))?a:De(De({},a),{},{properties:l})}return a}function oh(e,t,n){t.forEach(o=>{var{start:i,end:a}=o;my(i,Math.min(e.length,a),n)})}function Pc(e,t){for(var n=e,o=[],i=0;i<t.length;){if(Array.isArray(n)){var a=t[i];o.push("items",a),n=n[lo(a)]}else{if(!Cn(n))throw new Error("Cannot convert path: Object or Array expected at index ".concat(i));var s=t[i];o.push("properties",s),n=n[s]}i++}return o}function la(e,t,n,o){for(var i=t,a=function(l){var c=n.slice(0,l);i=zl(e,i,c,(u,d)=>{var v=Ns(d)&&!d.expanded?De(De({},d),{},{expanded:!0}):d;return Gr(v)?function(f,h){if(function(j,b){return j.some(k=>b>=k.start&&b<k.end)}(f.visibleSections,h))return f;var p=hd(h),y={start:p,end:Ff(p)};return De(De({},f),{},{visibleSections:My(f.visibleSections.concat(y))})}(v,lo(n[l])):v})},s=0;s<n.length;s++)a(s);return zl(e,i,n,(l,c)=>function(u,d,v,f){return zc(u,d,v,(h,p,y)=>Array.isArray(h)&&f(y)?Gr(p)?p.expanded?p:De(De({},p),{},{expanded:!0}):th({expanded:!0}):Cn(h)&&f(y)?Oo(p)?p.expanded?p:De(De({},p),{},{expanded:!0}):nh({expanded:!0}):p,h=>Ns(h)&&h.expanded)}(l,c,[],o))}function _m(e,t,n,o){return zl(e,t,n,(i,a)=>o?function(s,l,c){return zc(s,l,c,(u,d)=>Em(d),()=>!0)}(i,a,n):Em(a))}function Em(e){return Gr(e)&&e.expanded?De(De({},e),{},{expanded:!1,visibleSections:bl}):Oo(e)&&e.expanded?De(De({},e),{},{expanded:!1}):e}function zy(e,t,n){var o={json:e,documentState:t},i=n.reduce((a,s)=>({json:ga(a.json,[s]),documentState:v5(a.json,a.documentState,s)}),o);return{json:i.json,documentState:Do(i.json,i.documentState)}}function v5(e,t,n){if(X0(n))return Tm(e,t,n,void 0);if(Z0(n))return Mm(e,t,n);if(gp(n)){var o=ma(e,n.path),i=$a(e,t,o);return i?Zd(e,t,o,{type:"value",enforceString:i}):t}return lf(n)||ks(n)?function(a,s,l){if(ks(l)&&l.from===l.path)return s;var c=s,u=ma(a,l.from),d=Ta(a,c,u);return ks(l)&&(c=Mm(a,c,{path:l.from})),c=Tm(a,c,{path:l.path},d),c}(e,t,n):t}function Ta(e,t,n){try{return tt(t,Pc(e,n))}catch{return}}function ah(e,t,n,o,i){var a=Ay(e,t,n,i);return yp(a,Pc(e,n),s=>{var l=tt(e,n);return o(l,s)})}function Zd(e,t,n,o){return function(i,a,s,l,c){var u=Ay(i,a,s,c);return Co(u,Pc(i,s),l)}(e,t,n,o,rh)}function zl(e,t,n,o){return ah(e,t,n,o,rh)}function Tm(e,t,n,o){var i=ma(e,n.path),a=t;return a=zl(e,a,cn(i),(s,l)=>{if(!Gr(l))return l;var c=lo(Xt(i)),{items:u,visibleSections:d}=l;return De(De({},l),{},{items:c<u.length?E9(u,c,o!==void 0?[o]:Array(1)):u,visibleSections:Py(d,c,1)})}),Zd(e,a,i,o)}function Mm(e,t,n){var o=ma(e,n.path),i=cn(o),a=tt(e,i);return Array.isArray(a)?zl(e,t,i,(s,l)=>{if(!Gr(l))return l;var c=lo(Xt(o)),{items:u,visibleSections:d}=l;return De(De({},l),{},{items:u.slice(0,c).concat(u.slice(c+1)),visibleSections:Py(d,c,-1)})}):function(s,l,c){var u=Pc(s,c);return To(l,u)?Pd(l,Pc(s,c)):l}(e,t,o)}function Py(e,t,n){return function(o){for(var i=o.slice(0),a=1;a<i.length;)i[a-1].end===i[a].start&&(i[a-1]={start:i[a-1].start,end:i[a].end},i.splice(a)),a++;return i}(e.map(o=>({start:o.start>t?o.start+n:o.start,end:o.end>t?o.end+n:o.end})))}function $a(e,t,n){var o,i=tt(e,n),a=Ta(e,t,n),s=eh(a)?a.enforceString:void 0;return typeof s=="boolean"?s:typeof(o=i)=="string"&&typeof Ql(o,JSON)!="string"}function ou(e,t){var n=arguments.length>2&&arguments[2]!==void 0&&arguments[2],o=e.indexOf(t);return o!==-1?n?e.slice(o):e.slice(o+1):[]}function ih(e,t){var n=[];return function o(i,a,s){n.push(s),Cr(i)&&Gr(a)&&a.expanded&&oh(i,a.visibleSections,l=>{o(i[l],a.items[l],s.concat(String(l)))}),$r(i)&&Oo(a)&&a.expanded&&Object.keys(i).forEach(l=>{o(i[l],a.properties[l],s.concat(l))})}(e,t,[]),n}function Ny(e,t){var n=!(arguments.length>2&&arguments[2]!==void 0)||arguments[2],o=[];return function i(a,s){o.push({path:s,type:da.value});var l=Ta(e,t,s);if(a&&Ns(l)&&l.expanded){if(n&&o.push({path:s,type:da.inside}),Cr(a)){var c=Gr(l)?l.visibleSections:bl;oh(a,c,u=>{var d=s.concat(String(u));i(a[u],d),n&&o.push({path:d,type:da.after})})}$r(a)&&Object.keys(a).forEach(u=>{var d=s.concat(u);o.push({path:d,type:da.key}),i(a[u],d),n&&o.push({path:d,type:da.after})})}}(e,[]),o}function Vv(e,t,n){var o=ih(e,t),i=o.map(wt).indexOf(wt(n));if(i!==-1&&i<o.length-1)return o[i+1]}function Rs(e,t,n){var o=arguments.length>3&&arguments[3]!==void 0?arguments[3]:10240;return la(e,t,n,M9({json:tt(e,n)},o)?fc:sh)}function Jv(e,t,n){var o=Ta(e,t,n);return Ns(o)&&o.expanded?t:Rs(e,t,n)}function fc(e){return e.length===0||e.length===1&&e[0]==="0"}function Jf(e){return e.length===0}function sh(){return!0}function Hu(){return!1}function _o(e){return e&&e.type===Dn.after||!1}function Hr(e){return e&&e.type===Dn.inside||!1}function Yr(e){return e&&e.type===Dn.key||!1}function bn(e){return e&&e.type===Dn.value||!1}function Jn(e){return e&&e.type===Dn.multi||!1}function ev(e){return Jn(e)&&Gt(e.focusPath,e.anchorPath)}function Nc(e){return Jn(e)||_o(e)||Hr(e)||Yr(e)||bn(e)}function Hv(e){return e&&e.type===Dn.text||!1}function ts(e,t){var n=[];return function(o,i,a){if(i){var s=_s(i),l=st(i);if(Gt(s,l))return a(s);if(o!==void 0){var c=Iy(s,l);if(s.length===c.length||l.length===c.length)return a(c);var u=po(s,l),d=oi(o,u),v=Ki(o,u),f=ui(o,u,d),h=ui(o,u,v);if(!(f===-1||h===-1)){var p=tt(o,c);if($r(p)){for(var y=Object.keys(p),j=f;j<=h;j++){var b=a(c.concat(y[j]));if(b!==void 0)return b}return}if(Cr(p)){for(var k=f;k<=h;k++){var E=a(c.concat(String(k)));if(E!==void 0)return E}return}throw new Error("Failed to create selection")}}}}(e,t,o=>{n.push(o)}),n}function Ry(e){return Hr(e)?e.path:cn(st(e))}function oi(e,t){if(!Jn(t))return t.path;var n=ui(e,t,t.anchorPath);return ui(e,t,t.focusPath)<n?t.focusPath:t.anchorPath}function Ki(e,t){if(!Jn(t))return t.path;var n=ui(e,t,t.anchorPath);return ui(e,t,t.focusPath)>n?t.focusPath:t.anchorPath}function $m(e,t,n){var o=arguments.length>3&&arguments[3]!==void 0&&arguments[3];if(n){var i=o?st(n):oi(e,n),a=function(c,u,d){var v=ih(c,u),f=v.map(wt),h=wt(d),p=f.indexOf(h);if(p!==-1&&p>0)return v[p-1]}(e,t,i);if(o)return Hr(n)||_o(n)?a!==void 0?po(i,i):void 0:a!==void 0?po(_s(n),a):void 0;if(_o(n)||Hr(n))return rn(i);if(Yr(n)){if(a===void 0||a.length===0)return;var s=cn(a),l=tt(e,s);return Array.isArray(l)||gn(a)?rn(a):gi(a)}return bn(n),a!==void 0?rn(a):void 0}}function Am(e,t,n,o){if(!n)return{caret:void 0,previous:void 0,next:void 0};var i=Ny(e,t,o),a=i.findIndex(s=>Gt(s.path,st(n))&&String(s.type)===String(n.type));return{caret:a!==-1?i[a]:void 0,previous:a!==-1&&a>0?i[a-1]:void 0,next:a!==-1&&a<i.length-1?i[a+1]:void 0}}function Ys(e,t){for(var n=ih(e,t),o=0;o<n.length-1&&n[o+1].length>n[o].length;)o++;var i=n[o];return i===void 0||i.length===0||Array.isArray(tt(e,cn(i)))?rn(i):gi(i)}function Pl(e,t){if(t.length===1){var n=ai(t);if(n.op==="replace")return rn(ma(e,n.path))}if(!gn(t)&&t.every(s=>s.op==="move")){var o=ai(t),i=t.slice(1);if((lf(o)||ks(o))&&o.from!==o.path&&i.every(s=>(lf(s)||ks(s))&&s.from===s.path))return gi(ma(e,o.path))}var a=t.filter(s=>s.op!=="test"&&s.op!=="remove"&&(s.op!=="move"||s.from!==s.path)&&typeof s.path=="string").map(s=>ma(e,s.path));if(!gn(a))return{type:Dn.multi,anchorPath:ai(a),focusPath:Xt(a)}}function Iy(e,t){for(var n=0;n<e.length&&n<t.length&&e[n]===t[n];)n++;return e.slice(0,n)}function md(e){return Yr(e)||bn(e)||ev(e)}function zm(e,t){return md(t)&&mr(tt(e,st(t)))?st(t):cn(st(t))}function Ra(e,t){if(e.length<t.length)return!1;for(var n=0;n<t.length;n++)if(e[n]!==t[n])return!1;return!0}function Ma(e){if(Kr(e)){var{type:t,path:n}=e;return{type:t,path:n}}return e}function gi(e){return{type:Dn.key,path:e}}function lh(e,t){return{type:Dn.key,path:e,edit:!0,initialValue:t}}function rn(e){return{type:Dn.value,path:e}}function bd(e,t){return{type:Dn.value,path:e,edit:!0,initialValue:t}}function mi(e){return{type:Dn.inside,path:e}}function ci(e){return{type:Dn.after,path:e}}function po(e,t){var n=Iy(e,t),o=e.length>n.length&&t.length>n.length;return{type:Dn.multi,anchorPath:o?n.concat(e[n.length]):n,focusPath:o?n.concat(t[n.length]):n}}function qy(e,t,n,o){if(Yr(t))return String(Xt(t.path));if(bn(t)){var i=tt(e,t.path);return typeof i=="string"?i:o.stringify(i,null,n)}if(Jn(t)){if(gn(t.focusPath))return o.stringify(e,null,n);var a=Ry(t),s=tt(e,a);if(Array.isArray(s)){if(ev(t)){var l=tt(e,t.focusPath);return o.stringify(l,null,n)}return ts(e,t).map(c=>{var u=tt(e,c);return"".concat(o.stringify(u,null,n),",")}).join(`
`)}return ts(e,t).map(c=>{var u=Xt(c),d=tt(e,c);return"".concat(o.stringify(u),": ").concat(o.stringify(d,null,n),",")}).join(`
`)}}function Kr(e){return(Yr(e)||bn(e))&&e.edit===!0}function dl(e){return Yr(e)||bn(e)||Jn(e)}function Mu(e){return Yr(e)||bn(e)||ev(e)}function Hf(e){switch(e.type){case da.key:return gi(e.path);case da.value:return rn(e.path);case da.after:return ci(e.path);case da.inside:return mi(e.path)}}function Pm(e,t){switch(e){case Dn.key:return gi(t);case Dn.value:return rn(t);case Dn.after:return ci(t);case Dn.inside:return mi(t);case Dn.multi:case Dn.text:return po(t,t)}}function $u(e,t,n){if(t)return Rc(e,t,n)||Ra(Jn(t)?cn(t.focusPath):t.path,n)?t:void 0}function Rc(e,t,n){if(e===void 0||!t)return!1;if(Yr(t)||Hr(t)||_o(t))return Gt(t.path,n);if(bn(t))return Ra(n,t.path);if(Jn(t)){var o=oi(e,t),i=Ki(e,t),a=cn(t.focusPath);if(!Ra(n,a)||n.length<=a.length)return!1;var s=ui(e,t,o),l=ui(e,t,i),c=ui(e,t,n);return c!==-1&&c>=s&&c<=l}return!1}function ui(e,t,n){var o=cn(t.focusPath);if(!Ra(n,o)||n.length<=o.length)return-1;var i=n[o.length],a=tt(e,o);if($r(a))return Object.keys(a).indexOf(i);if(Cr(a)){var s=lo(i);if(s<a.length)return s}return-1}function st(e){return Jn(e)?e.focusPath:e.path}function _s(e){return Jn(e)?e.anchorPath:e.path}function ka(){for(var e=[],t=arguments.length,n=new Array(t),o=0;o<t;o++)n[o]=arguments[o];for(var i of n)if(typeof i=="string"&&e.push(i),i&&typeof i=="object")for(var a in i)Object.hasOwnProperty.call(i,a)&&i[a]&&e.push(a);return e.join(" ")}function Dy(e,t,n){return ka("jse-value","jse-"+Hp(e,n),{"jse-url":Xd(e),"jse-empty":typeof e=="string"&&e.length===0,"jse-table-cell":t===Mr.table})}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-value.jse-string.svelte-1r0oryi {
  color: var(--jse-value-color-string, #008000);
}
.jse-value.jse-object.svelte-1r0oryi, .jse-value.jse-array.svelte-1r0oryi {
  min-width: 16px;
  color: var(--jse-delimiter-color, rgba(0, 0, 0, 0.38));
}
.jse-value.jse-number.svelte-1r0oryi {
  color: var(--jse-value-color-number, #ee422e);
}
.jse-value.jse-boolean.svelte-1r0oryi {
  color: var(--jse-value-color-boolean, #ff8c00);
}
.jse-value.jse-null.svelte-1r0oryi {
  color: var(--jse-value-color-null, #004ed0);
}
.jse-value.jse-invalid.svelte-1r0oryi {
  color: var(--jse-text-color, #4d4d4d);
}
.jse-value.jse-url.svelte-1r0oryi {
  color: var(--jse-value-color-url, #008000);
  text-decoration: underline;
}

div.jse-editable-div.svelte-1r0oryi {
  min-width: 2em;
  padding: 0 5px;
  box-sizing: border-box;
  outline: none;
  border-radius: 1px;
  vertical-align: top;
  cursor: text !important;
  word-break: normal;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}
div.jse-editable-div.jse-short-text.svelte-1r0oryi {
  overflow-wrap: normal;
}
div.jse-editable-div.jse-table-cell.svelte-1r0oryi {
  overflow-wrap: normal;
  white-space: nowrap;
}
div.jse-editable-div[contenteditable=true].svelte-1r0oryi {
  outline: var(--jse-edit-outline, 2px solid #656565);
  background: var(--jse-background-color, #fff);
  position: relative;
  display: inline-block;
  border-radius: 0;
  z-index: 3;
}
div.jse-editable-div.jse-empty.svelte-1r0oryi:not(:focus) {
  outline: 1px dotted var(--jse-tag-background, rgba(0, 0, 0, 0.2));
  -moz-outline-radius: 2px;
}
div.jse-editable-div.jse-empty.svelte-1r0oryi::after {
  pointer-events: none;
  color: var(--jse-tag-background, rgba(0, 0, 0, 0.2));
}`);var f5=re('<div role="textbox" tabindex="0" contenteditable="true" spellcheck="false"></div>');function Ly(e,t){yt(t,!1);var n=Zr("jsoneditor:EditableDiv"),o=m(t,"value",9),i=m(t,"initialValue",9),a=m(t,"shortText",9,!1),s=m(t,"label",9),l=m(t,"onChange",9),c=m(t,"onCancel",9),u=m(t,"onFind",9),d=m(t,"onPaste",9,Dr),v=m(t,"onValueClass",9,()=>""),f=R(void 0,!0),h=R(void 0,!0),p=!1;function y(){return r(f)?function(k){return k.replace(/\n$/,"")}(r(f).innerText):""}function j(k){r(f)&&Lo(f,r(f).innerText=Al(k))}vo(()=>{n("onMount",{value:o(),initialValue:i()}),j(i()!==void 0?i():o()),r(f)&&function(k){if(k.firstChild!=null){var E=document.createRange(),O=window.getSelection();E.setStart(k,1),E.collapse(!0),O==null||O.removeAllRanges(),O==null||O.addRange(E)}else k.focus()}(r(f))}),ra(()=>{var k=y();n("onDestroy",{closed:p,value:o(),newValue:k}),p||k===o()||l()(k,Qi.no)}),ne(()=>(x(v()),x(o())),()=>{g(h,v()(o()))}),Mn(),Ft(!0);var b=f5();or(b,k=>g(f,k),()=>r(f)),Le(k=>{Tn(b,"aria-label",s()),Bt(b,1,k,"svelte-1r0oryi")},[()=>es((x(ka),r(h),x(a()),F(()=>ka("jse-editable-div",r(h),{"jse-short-text":a()}))))]),ze("input",b,function(){var k=y();k===""&&j(""),g(h,v()(k))}),ze("keydown",b,function(k){k.stopPropagation();var E=hi(k);if(E==="Escape"&&(k.preventDefault(),p=!0,c()()),E==="Enter"||E==="Tab"){k.preventDefault(),p=!0;var O=y();l()(O,Qi.nextInside)}E==="Ctrl+F"&&(k.preventDefault(),u()(!1)),E==="Ctrl+H"&&(k.preventDefault(),u()(!0))}),ze("paste",b,function(k){if(k.stopPropagation(),d()&&k.clipboardData){var E=k.clipboardData.getData("text/plain");d()(E)}}),ze("blur",b,function(){var k=document.hasFocus(),E=y();n("handleBlur",{hasFocus:k,closed:p,value:o(),newValue:E}),document.hasFocus()&&!p&&(p=!0,E!==o()&&l()(E,Qi.self))}),U(e,b),jt()}function p5(e,t){yt(t,!1);var n=m(t,"path",9),o=m(t,"value",9),i=m(t,"selection",9),a=m(t,"mode",9),s=m(t,"parser",9),l=m(t,"normalization",9),c=m(t,"enforceString",9),u=m(t,"onPatch",9),d=m(t,"onPasteJson",9),v=m(t,"onSelect",9),f=m(t,"onFind",9),h=m(t,"focus",9),p=m(t,"findNextInside",9);function y(E){return c()?E:Ql(E,s())}function j(){v()(rn(n())),h()()}Ft(!0);var b=nt(()=>(x(l()),x(o()),F(()=>l().escapeValue(o())))),k=nt(()=>(x(Kr),x(i()),F(()=>Kr(i())?i().initialValue:void 0)));Ly(e,{get value(){return r(b)},get initialValue(){return r(k)},label:"Edit value",onChange:function(E,O){u()([{op:"replace",path:wt(n()),value:y(l().unescapeValue(E))}],(w,_,A)=>{if(!A||Gt(n(),st(A)))return{state:_,selection:O===Qi.nextInside?p()(n()):rn(n())}}),h()()},onCancel:j,onPaste:function(E){try{var O=s().parse(E);mr(O)&&d()({path:n(),contents:O,onPasteAsJson:()=>{j();var w=[{op:"replace",path:wt(n()),value:O}];u()(w,(_,A)=>({state:Rs(_,A,n())}))}})}catch{}},get onFind(){return f()},onValueClass:function(E){return Dy(y(l().unescapeValue(E)),a(),s())}}),jt()}function vl(e,t,n){var o=cn(t),i=tt(e,o);if(Cr(i)){var a=lo(Xt(t));return n.map((u,d)=>({op:"add",path:wt(o.concat(String(a+d))),value:u.value}))}if($r(i)){var s=Xt(t),l=Object.keys(i),c=s!==void 0?ou(l,s,!0):[];return[...n.map(u=>{var d=ru(u.key,l);return{op:"add",path:wt(o.concat(d)),value:u.value}}),...c.map(u=>ns(o,u))]}throw new Error("Cannot create insert operations: parent must be an Object or Array")}function Qf(e,t,n){var o=tt(e,t);if(Array.isArray(o)){var i=o.length;return n.map((a,s)=>({op:"add",path:wt(t.concat(String(i+s))),value:a.value}))}return n.map(a=>{var s=ru(a.key,Object.keys(o));return{op:"add",path:wt(t.concat(s)),value:a.value}})}function au(e,t,n,o){var i=t.filter(l=>l!==n),a=ru(o,i),s=ou(t,n,!1);return[{op:"move",from:wt(e.concat(n)),path:wt(e.concat(a))},...s.map(l=>ns(e,l))]}function Uy(e,t){var n=Xt(t);if(gn(n))throw new Error("Cannot duplicate root object");var o=cn(n),i=Xt(n),a=tt(e,o);if(Cr(a)){var s=Xt(t),l=s?lo(Xt(s))+1:0;return[...t.map((d,v)=>({op:"copy",from:wt(d),path:wt(o.concat(String(v+l)))}))]}if($r(a)){var c=Object.keys(a),u=i!==void 0?ou(c,i,!1):[];return[...t.map(d=>{var v=ru(Xt(d),c);return{op:"copy",from:wt(d),path:wt(o.concat(v))}}),...u.map(d=>ns(o,d))]}throw new Error("Cannot create duplicate operations: parent must be an Object or Array")}function By(e,t){if(bn(t))return[{op:"move",from:wt(t.path),path:""}];if(!Jn(t))throw new Error("Cannot create extract operations: parent must be an Object or Array");var n=cn(t.focusPath),o=tt(e,n);if(Cr(o)){var i=ts(e,t).map(s=>{var l=lo(Xt(s));return o[l]});return[{op:"replace",path:"",value:i}]}if($r(o)){var a={};return ts(e,t).forEach(s=>{var l=String(Xt(s));a[l]=o[l]}),[{op:"replace",path:"",value:a}]}throw new Error("Cannot extract: unsupported type of selection "+JSON.stringify(t))}function Fy(e,t,n,o){if(Yr(t)){var i=by(n,o),a=cn(t.path),s=tt(e,a);return au(a,Object.keys(s),Xt(t.path),typeof i=="string"?i:n)}if(bn(t)||Jn(t)&&gn(t.focusPath))try{return[{op:"replace",path:wt(st(t)),value:tu(n,_=>eu(_,o))}]}catch{return[{op:"replace",path:wt(st(t)),value:n}]}if(Jn(t)){var l=Qv(n,o);return function(_,A,q){var C=ai(A),z=cn(C),D=tt(_,z);if(Cr(D)){var H=ai(A),Q=H?lo(Xt(H)):0;return[...yd(A),...q.map((Ue,Re)=>({op:"add",path:wt(z.concat(String(Re+Q))),value:Ue.value}))]}if($r(D)){var fe=Xt(A),Ie=cn(fe),ge=Xt(fe),qe=Object.keys(D),ce=ge!==void 0?ou(qe,ge,!1):[],ve=new Set(A.map(Ue=>Xt(Ue))),he=qe.filter(Ue=>!ve.has(Ue));return[...yd(A),...q.map(Ue=>{var Re=ru(Ue.key,he);return{op:"add",path:wt(Ie.concat(Re)),value:Ue.value}}),...ce.map(Ue=>ns(Ie,Ue))]}throw new Error("Cannot create replace operations: parent must be an Object or Array")}(e,ts(e,t),l)}if(_o(t)){var c=Qv(n,o),u=t.path,d=cn(u),v=tt(e,d);if(Cr(v)){var f=lo(Xt(u));return vl(e,d.concat(String(f+1)),c)}if($r(v)){var h=String(Xt(u)),p=Object.keys(v);if(gn(p)||Xt(p)===h)return Qf(e,d,c);var y=p.indexOf(h),j=p[y+1];return vl(e,d.concat(j),c)}throw new Error("Cannot create insert operations: parent must be an Object or Array")}if(Hr(t)){var b=Qv(n,o),k=t.path,E=tt(e,k);if(Cr(E))return vl(e,k.concat("0"),b);if($r(E)){var O=Object.keys(E);if(gn(O))return Qf(e,k,b);var w=ai(O);return vl(e,k.concat(w),b)}throw new Error("Cannot create insert operations: parent must be an Object or Array")}throw new Error("Cannot insert: unsupported type of selection "+JSON.stringify(t))}function yd(e){return e.map(t=>({op:"remove",path:wt(t)})).reverse()}function ns(e,t){return{op:"move",from:wt(e.concat(t)),path:wt(e.concat(t))}}function Qv(e,t){var n=/^\s*{/.test(e),o=/^\s*\[/.test(e),i=by(e,t),a=i!==void 0?i:tu(e,s=>eu(s,t));return n&&Cn(a)||o&&Array.isArray(a)?[{key:"New item",value:a}]:Array.isArray(a)?a.map((s,l)=>({key:"New item "+l,value:s})):Cn(a)?Object.keys(a).map(s=>({key:s,value:a[s]})):[{key:"New item",value:a}]}function Wy(e,t){if(Yr(t)){var n=cn(t.path),o=tt(e,n),i=au(n,Object.keys(o),Xt(t.path),"");return{operations:i,newSelection:Pl(e,i)}}if(bn(t))return{operations:[{op:"replace",path:wt(t.path),value:""}],newSelection:t};if(Jn(t)){var a=ts(e,t),s=yd(a),l=Xt(a);if(gn(l))return{operations:[{op:"replace",path:"",value:""}],newSelection:rn([])};var c=cn(l),u=tt(e,c);if(Cr(u)){var d=ai(a),v=lo(Xt(d));return{operations:s,newSelection:v===0?mi(c):ci(c.concat(String(v-1)))}}if($r(u)){var f=Object.keys(u),h=ai(a),p=Xt(h),y=f.indexOf(p),j=f[y-1];return{operations:s,newSelection:y===0?mi(c):ci(c.concat(j))}}throw new Error("Cannot create remove operations: parent must be an Object or Array")}throw new Error("Cannot remove: unsupported type of selection "+JSON.stringify(t))}function Vy(e,t){var n=function(o,i){if(gn(i)||!i.every(ks))return i;var a=[];for(var s of i){var l=Nm(Mo(s.from)),c=Nm(Mo(s.path));if(!l||!c)return i;a.push({from:l,path:c,operation:s})}var u=a[0].path.parent,d=tt(o,u);if(!$r(d)||!a.every(p=>function(y,j){return Gt(y.from.parent,j)&&Gt(y.path.parent,j)}(p,u)))return i;var v=function(p,y){var j=Object.keys(y),b=j.slice();for(var k of p){var E=b.indexOf(k.from.key);E!==-1&&(b.splice(E,1),b.push(k.path.key))}for(var O=0;O<j.length&&j[O]===b[O];)O++;return b[O]}(a,o),f=p=>p.operation,h=a.filter(p=>p.operation.from!==p.operation.path);return h.some(p=>p.path.key===v)?h.map(f):[ns(u,v),...h.map(f)]}(e,t);return r1(e,n,{before:(o,i,a)=>{if(Z0(i)){var s=Mo(i.path);return{revertOperations:[...a,...Kv(o,s)]}}if(ks(i)){var l=Mo(i.from);return{revertOperations:i.from===i.path?[i,...Kv(o,l)]:[...a,...Kv(o,l)]}}return{document:o}}})}function Nm(e){return e.length>0?{parent:cn(e),key:Xt(e)}:void 0}function Kv(e,t){var n=cn(t),o=Xt(t),i=tt(e,n);return $r(i)?ou(Object.keys(i),o,!1).map(a=>ns(n,a)):[]}function Rm(e){var t=e.activeIndex<e.items.length-1?e.activeIndex+1:e.items.length>0?0:-1,n=e.items[t],o=e.items.map((i,a)=>De(De({},i),{},{active:a===t}));return De(De({},e),{},{items:o,activeItem:n,activeIndex:t})}function Im(e,t){var n,o=arguments.length>2&&arguments[2]!==void 0?arguments[2]:{},i=e.toLowerCase(),a=(n=o==null?void 0:o.maxResults)!==null&&n!==void 0?n:1/0,s=o==null?void 0:o.columns,l=[],c=[];function u(j){l.length>=a||l.push(j)}function d(j,b){if(Cr(b)){var k=c.length;c.push("0");for(var E=0;E<b.length;E++)if(c[k]=String(E),d(j,b[E]),l.length>=a)return;c.pop()}else if($r(b)){var O=Object.keys(b),w=c.length;for(var _ of(c.push(""),O))if(c[w]=_,qm(_,j,c,ya.key,u),d(j,b[_]),l.length>=a)return;c.pop()}else qm(String(b),j,c,ya.value,u)}if(e==="")return[];if(s){if(!Array.isArray(t))throw new Error("json must be an Array when option columns is defined");for(var v=0;v<t.length;v++){c[0]=String(v);for(var f=t[v],h=0;h<s.length;h++){var p=s[h];if(p.length===1)c[1]=p[0];else for(var y=0;y<p.length;y++)c[y+1]=p[y];for(;c.length>p.length+1;)c.pop();d(i,tt(f,p))}if(l.length>=a)break}return l}return d(i,t),l}function qm(e,t,n,o,i){var a=e.toLowerCase(),s=0,l=-1,c=-1;do(c=a.indexOf(t,l))!==-1&&(l=c+t.length,i({path:n.slice(0),field:o,fieldIndex:s,start:c,end:l}),s++);while(c!==-1)}function Kf(e,t,n,o){return e.substring(0,n)+t+e.substring(o)}function Dm(e,t,n){var o=e;return B8(n,i=>{o=Kf(o,t,i.start,i.end)}),o}function h5(e,t,n,o,i){var{field:a,path:s,start:l,end:c}=o;if(a===ya.key){var u=cn(s),d=tt(e,u),v=Xt(s),f=au(u,Object.keys(d),v,Kf(v,n,l,c));return{newSelection:Pl(e,f),operations:f}}if(a===ya.value){var h=tt(e,s);if(h===void 0)throw new Error("Cannot replace: path not found ".concat(wt(s)));var p=typeof h=="string"?h:String(h),y=$a(e,t,s),j=Kf(p,n,l,c),b=[{op:"replace",path:wt(s),value:y?j:Ql(j,i)}];return{newSelection:Pl(e,b),operations:b}}throw new Error("Cannot replace: unknown type of search result field ".concat(a))}function Lm(e){return e.path.concat(e.field,String(e.fieldIndex))}function Um(e){var t=$y(e)?e.searchResults.filter(n=>n.field===ya.key):void 0;return t&&t.length>0?t:void 0}function Bm(e){var t=$y(e)?e.searchResults.filter(n=>n.field===ya.value):void 0;return t&&t.length>0?t:void 0}var g5={createObjectDocumentState:()=>({type:"object",properties:{}}),createArrayDocumentState:()=>({type:"array",items:[]}),createValueDocumentState:()=>({type:"value"})};function Jy(e,t){return t.reduce((n,o)=>function(i,a,s,l){return ah(i,a,s,l,g5)}(e,n,o.path,(i,a)=>De(De({},a),{},{searchResults:a.searchResults?a.searchResults.concat(o):[o]})),void 0)}function jd(e){var t,n=(t=e==null?void 0:e.searchResults)!==null&&t!==void 0?t:[],o=Oo(e)?Object.values(e.properties).flatMap(jd):Gr(e)?e.items.flatMap(jd):[];return n.concat(o)}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-highlight.svelte-19qyvy6 {
  background-color: var(--jse-search-match-color, #ffe665);
  outline: var(--jse-search-match-outline, none);
}
.jse-highlight.jse-active.svelte-19qyvy6 {
  background-color: var(--jse-search-match-active-color, var(--jse-search-match-color, #ffe665));
  outline: var(--jse-search-match-outline, 2px solid #e0be00);
}`);var m5=re("<span> </span>");function Hy(e,t){yt(t,!1);var n=R(),o=m(t,"text",8),i=m(t,"searchResultItems",8);ne(()=>(x(o()),x(i())),()=>{g(n,function(s,l){var c=[],u=0;for(var d of l){var v=s.slice(u,d.start);v!==""&&c.push({resultIndex:void 0,type:"normal",text:v,active:!1});var f=s.slice(d.start,d.end);c.push({resultIndex:d.resultIndex,type:"highlight",text:f,active:d.active}),u=d.end}var h=Xt(l);return h&&h.end<s.length&&c.push({type:"normal",text:s.slice(h.end),resultIndex:void 0,active:!1}),c}(String(o()),i()))}),Mn(),Ft();var a=br();Or(Mt(a),1,()=>r(n),Pr,(s,l)=>{var c=br(),u=Mt(c),d=f=>{var h=oo();Le(()=>xt(h,(r(l),F(()=>r(l).text)))),U(f,h)},v=f=>{var h,p=m5(),y=I(p);Le((j,b)=>{h=Bt(p,1,"jse-highlight svelte-19qyvy6",null,h,{"jse-active":r(l).active}),Tn(p,"data-search-result-index",j),xt(y,b)},[()=>(r(l),F(()=>String(r(l).resultIndex))),()=>(x(Al),r(l),F(()=>Al(r(l).text)))]),U(f,p)};be(u,f=>{r(l),F(()=>r(l).type==="normal")?f(d):f(v,-1)}),U(s,c)}),U(e,a),jt()}function Qu(e){var t=1e3;if(e<900)return e.toFixed()+" B";var n=e/t;if(n<900)return n.toFixed(1)+" KB";var o=n/t;if(o<900)return o.toFixed(1)+" MB";var i=o/t;return i<900?i.toFixed(1)+" GB":(i/t).toFixed(1)+" TB"}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-tag.svelte-ubve9r {
  border: none;
  font-size: 80%;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  color: var(--jse-tag-color, var(--jse-text-color-inverse, #fff));
  background: var(--jse-tag-background, rgba(0, 0, 0, 0.2));
  border-radius: 2px;
  cursor: pointer;
  display: inline-block;
  padding: 0 4px;
  line-height: normal;
  margin: 1px 0;
}
.jse-tag.svelte-ubve9r:hover {
  opacity: 0.8;
}
.jse-tag.disabled.svelte-ubve9r {
  opacity: 0.7;
  cursor: inherit;
}`);var b5=re('<button type="button"><!></button>');function Ku(e,t){yt(t,!0);var n,o=Kt(()=>t.onclick?a=>{a.preventDefault(),a.stopPropagation(),t.onclick()}:void 0),i=b5();(function(a,s){for(var l=arguments.length,c=new Array(l>2?l-2:0),u=2;u<l;u++)c[u-2]=arguments[u];var d=new Gd(a);Jl(()=>{var v,f=(v=s())!==null&&v!==void 0?v:null;d.ensure(f,f&&(h=>f(h,...c)))},As)})(I(i),()=>{var a;return(a=t.children)!==null&&a!==void 0?a:fb}),Le(()=>n=Bt(i,1,"jse-tag svelte-ubve9r",null,n,{disabled:!t.onclick})),ha("click",i,function(){for(var a,s=arguments.length,l=new Array(s),c=0;c<s;c++)l[c]=arguments[c];(a=r(o))===null||a===void 0||a.apply(this,l)}),U(e,i),jt()}Zc(["click"]);It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-value.jse-string.svelte-1saqp8c {
  color: var(--jse-value-color-string, #008000);
}
.jse-value.jse-object.svelte-1saqp8c, .jse-value.jse-array.svelte-1saqp8c {
  min-width: 16px;
  color: var(--jse-delimiter-color, rgba(0, 0, 0, 0.38));
}
.jse-value.jse-number.svelte-1saqp8c {
  color: var(--jse-value-color-number, #ee422e);
}
.jse-value.jse-boolean.svelte-1saqp8c {
  color: var(--jse-value-color-boolean, #ff8c00);
}
.jse-value.jse-null.svelte-1saqp8c {
  color: var(--jse-value-color-null, #004ed0);
}
.jse-value.jse-invalid.svelte-1saqp8c {
  color: var(--jse-text-color, #4d4d4d);
}
.jse-value.jse-url.svelte-1saqp8c {
  color: var(--jse-value-color-url, #008000);
  text-decoration: underline;
}

.jse-value.svelte-1saqp8c {
  display: inline-block;
  min-width: 2em;
  padding: 0 5px;
  box-sizing: border-box;
  outline: none;
  border-radius: 1px;
  vertical-align: top;
  word-break: normal;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}
.jse-value.jse-table-cell.svelte-1saqp8c {
  overflow-wrap: normal;
  white-space: nowrap;
}
.jse-value.jse-empty.svelte-1saqp8c {
  min-width: 4em;
  outline: 1px dotted var(--jse-tag-background, rgba(0, 0, 0, 0.2));
  -moz-outline-radius: 2px;
}
.jse-value.jse-empty.svelte-1saqp8c::after {
  pointer-events: none;
  color: var(--jse-tag-background, rgba(0, 0, 0, 0.2));
  content: "value";
}`);var y5=re('<div role="button" tabindex="-1" data-type="selectable-value"><!> <!></div>');function j5(e,t){yt(t,!0);var n=Ka(!0),o=Kt(()=>r(n)&&typeof t.value=="string"&&t.value.length>t.truncateTextSize&&(!t.searchResultItems||!t.searchResultItems.some(h=>h.active&&h.end>t.truncateTextSize))),i=Kt(()=>r(o)&&typeof t.value=="string"?t.value.substring(0,t.truncateTextSize).trim():t.value),a=Kt(()=>Xd(t.value));function s(){g(n,!1)}var l=y5(),c=I(l),u=h=>{var p=Kt(()=>t.normalization.escapeValue(r(i)));Hy(h,{get text(){return r(p)},get searchResultItems(){return t.searchResultItems}})},d=h=>{var p=oo();Le(y=>xt(p,y),[()=>Al(t.normalization.escapeValue(r(i)))]),U(h,p)};be(c,h=>{t.searchResultItems?h(u):h(d,-1)});var v=Y(c,2),f=h=>{Ku(h,{onclick:s,children:(p,y)=>{var j=oo();Le(b=>xt(j,"Show more (".concat(b??"",")")),[()=>Qu(t.value.length)]),U(p,j)},$$slots:{default:!0}})};be(v,h=>{r(o)&&typeof t.value=="string"&&h(f)}),Le(h=>{Bt(l,1,h,"svelte-1saqp8c"),Tn(l,"title",r(a)?"Ctrl+Click or Ctrl+Enter to open url in new window":void 0)},[()=>es(Dy(t.value,t.mode,t.parser))]),ha("click",l,function(h){typeof t.value=="string"&&r(a)&&Xp(h)&&(h.preventDefault(),h.stopPropagation(),window.open(t.value,"_blank"))}),ha("dblclick",l,function(h){t.readOnly||(h.preventDefault(),t.onSelect(bd(t.path)))}),U(e,l),jt()}Zc(["click","dblclick"]);It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-tooltip.svelte-brt1mq {
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  line-height: normal;
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px);
  border-radius: 3px;
  background: var(--jse-context-menu-background, #656565);
  color: var(--jse-context-menu-color, var(--jse-text-color-inverse, #fff));
  white-space: nowrap;
  box-shadow: var(--jse-controls-box-shadow, 0 2px 6px 0 rgba(0, 0, 0, 0.24));
}`);var x5=re('<div class="jse-tooltip svelte-brt1mq"> </div>');function w5(e,t){var n=m(t,"text",8),o=x5(),i=I(o);Le(()=>xt(i,n())),U(e,o)}function Nl(e,t){var n,{text:o,openAbsolutePopup:i,closeAbsolutePopup:a}=t;function s(){n=i(w5,{text:o},{position:"top",width:10*o.length,offsetTop:3,anchor:e,closeOnOuterClick:!0})}function l(){a(n)}return e.addEventListener("mouseenter",s),e.addEventListener("mouseleave",l),{destroy(){e.removeEventListener("mouseenter",s),e.removeEventListener("mouseleave",l)}}}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-timestamp.svelte-1jcpman {
  padding: 0;
  margin: 0;
  vertical-align: middle;
  display: inline-flex;
  color: var(--jse-value-color-number, #ee422e);
}`);var k5=re('<div class="jse-timestamp svelte-1jcpman"><!></div>');function S5(e,t){yt(t,!1);var n=R(void 0,!0),o=rs("absolute-popup"),i=m(t,"value",9);ne(()=>x(i()),()=>{g(n,"Time: ".concat(new Date(i()).toString()))}),Mn(),Ft(!0);var a=k5();un(I(a),{get data(){return RS}}),go(a,(s,l)=>Nl==null?void 0:Nl(s,l),()=>De({text:r(n)},o)),U(e,a),jt()}function C5(e){var t=[];return!e.isEditing&&S9(e.value)&&t.push({component:t5,props:e}),!e.isEditing&&C9(e.value)&&t.push({component:a5,props:e}),e.isEditing&&t.push({component:p5,props:e}),e.isEditing||t.push({component:j5,props:e}),!e.isEditing&&Df(e.value)&&t.push({component:S5,props:e}),t}function Eo(e){return e.map((t,n)=>_5.test(t)?"["+t+"]":/[.[\]]/.test(t)||t===""?'["'+function(o){return o.replace(/"/g,'\\"')}(t)+'"]':(n>0?".":"")+t).join("")}function O5(e){for(var t=[],n=0;n<e.length;)e[n]==="."&&n++,e[n]==="["?(n++,e[n]==='"'?(n++,t.push(o(a=>a==='"',!0)),i('"')):t.push(o(a=>a==="]")),i("]")):t.push(o(a=>a==="."||a==="["));function o(a){for(var s=arguments.length>1&&arguments[1]!==void 0&&arguments[1],l="";n<e.length&&!a(e[n]);)s&&e[n]==="\\"&&e[n+1]==='"'?(l+='"',n+=2):(l+=e[n],n++);return l}function i(a){if(e[n]!==a)throw new SyntaxError("Invalid JSON path: ".concat(a," expected at position ").concat(n));n++}return t}function Pi(e){return{value:e,label:gn(e)?"(item root)":Eo(e)}}var _5=/^\d+$/,E5={},T5={showWizard:!0,showOriginal:!0},xd=Math.min,Es=Math.max,wd=Math.round,Au=Math.floor,Ia=e=>({x:e,y:e}),M5={left:"right",right:"left",bottom:"top",top:"bottom"};function Fm(e,t,n){return Es(e,xd(t,n))}function tv(e,t){return typeof e=="function"?e(t):e}function Is(e){return e.split("-")[0]}function nv(e){return e.split("-")[1]}function Qy(e){return e==="x"?"y":"x"}function Ky(e){return e==="y"?"height":"width"}function Ui(e){var t=e[0];return t==="t"||t==="b"?"y":"x"}function Gy(e){return Qy(Ui(e))}function Gf(e){return e.includes("start")?e.replace("start","end"):e.replace("end","start")}var Wm=["left","right"],Vm=["right","left"],$5=["top","bottom"],A5=["bottom","top"];function z5(e,t,n,o){var i=nv(e),a=function(s,l,c){switch(s){case"top":case"bottom":return c?l?Vm:Wm:l?Wm:Vm;case"left":case"right":return l?$5:A5;default:return[]}}(Is(e),n==="start",o);return i&&(a=a.map(s=>s+"-"+i),t&&(a=a.concat(a.map(Gf)))),a}function zu(e){var t=Is(e);return M5[t]+e.slice(t.length)}function P5(e){return typeof e!="number"?function(t){return De({top:0,right:0,bottom:0,left:0},t)}(e):{top:e,right:e,bottom:e,left:e}}function kd(e){var{x:t,y:n,width:o,height:i}=e;return{width:o,height:i,top:n,left:t,right:t+o,bottom:n+i,x:t,y:n}}function Jm(e,t,n){var o,{reference:i,floating:a}=e,s=Ui(t),l=Gy(t),c=Ky(l),u=Is(t),d=s==="y",v=i.x+i.width/2-a.width/2,f=i.y+i.height/2-a.height/2,h=i[c]/2-a[c]/2;switch(u){case"top":o={x:v,y:i.y-a.height};break;case"bottom":o={x:v,y:i.y+i.height};break;case"right":o={x:i.x+i.width,y:f};break;case"left":o={x:i.x-a.width,y:f};break;default:o={x:i.x,y:i.y}}switch(nv(t)){case"start":o[l]-=h*(n&&d?-1:1);break;case"end":o[l]+=h*(n&&d?-1:1)}return o}function N5(e,t){return Yf.apply(this,arguments)}function Yf(){return Yf=Pt(function*(e,t){var n;t===void 0&&(t={});var{x:o,y:i,platform:a,rects:s,elements:l,strategy:c}=e,{boundary:u="clippingAncestors",rootBoundary:d="viewport",elementContext:v="floating",altBoundary:f=!1,padding:h=0}=tv(t,e),p=P5(h),y=l[f?v==="floating"?"reference":"floating":v],j=kd(yield a.getClippingRect({element:(n=yield a.isElement==null?void 0:a.isElement(y))==null||n?y:y.contextElement||(yield a.getDocumentElement==null?void 0:a.getDocumentElement(l.floating)),boundary:u,rootBoundary:d,strategy:c})),b=v==="floating"?{x:o,y:i,width:s.floating.width,height:s.floating.height}:s.reference,k=yield a.getOffsetParent==null?void 0:a.getOffsetParent(l.floating),E=(yield a.isElement==null?void 0:a.isElement(k))&&(yield a.getScale==null?void 0:a.getScale(k))||{x:1,y:1},O=kd(a.convertOffsetParentRelativeRectToViewportRelativeRect?yield a.convertOffsetParentRelativeRectToViewportRelativeRect({elements:l,rect:b,offsetParent:k,strategy:c}):b);return{top:(j.top-O.top+p.top)/E.y,bottom:(O.bottom-j.bottom+p.bottom)/E.y,left:(j.left-O.left+p.left)/E.x,right:(O.right-j.right+p.right)/E.x}}),Yf.apply(this,arguments)}var R5=function(){var e=Pt(function*(t,n,o){for(var{placement:i="bottom",strategy:a="absolute",middleware:s=[],platform:l}=o,c=l.detectOverflow?l:De(De({},l),{},{detectOverflow:N5}),u=yield l.isRTL==null?void 0:l.isRTL(n),d=yield l.getElementRects({reference:t,floating:n,strategy:a}),{x:v,y:f}=Jm(d,i,u),h=i,p=0,y={},j=0;j<s.length;j++){var b=s[j];if(b){var{name:k,fn:E}=b,{x:O,y:w,data:_,reset:A}=yield E({x:v,y:f,initialPlacement:i,placement:h,strategy:a,middlewareData:y,rects:d,platform:c,elements:{reference:t,floating:n}});v=O??v,f=w??f,y[k]=De(De({},y[k]),_),A&&p<50&&(p++,typeof A=="object"&&(A.placement&&(h=A.placement),A.rects&&(d=A.rects===!0?yield l.getElementRects({reference:t,floating:n,strategy:a}):A.rects),{x:v,y:f}=Jm(d,h,u)),j=-1)}}return{x:v,y:f,placement:h,strategy:a,middlewareData:y}});return function(t,n,o){return e.apply(this,arguments)}}(),I5=new Set(["left","top"]);function Xf(){return Xf=Pt(function*(e,t){var{placement:n,platform:o,elements:i}=e,a=yield o.isRTL==null?void 0:o.isRTL(i.floating),s=Is(n),l=nv(n),c=Ui(n)==="y",u=I5.has(s)?-1:1,d=a&&c?-1:1,v=tv(t,e),{mainAxis:f,crossAxis:h,alignmentAxis:p}=typeof v=="number"?{mainAxis:v,crossAxis:0,alignmentAxis:null}:{mainAxis:v.mainAxis||0,crossAxis:v.crossAxis||0,alignmentAxis:v.alignmentAxis};return l&&typeof p=="number"&&(h=l==="end"?-1*p:p),c?{x:h*d,y:f*u}:{x:f*u,y:h*d}}),Xf.apply(this,arguments)}function rv(){return typeof window<"u"}function Rl(e){return Yy(e)?(e.nodeName||"").toLowerCase():"#document"}function Bo(e){var t;return(e==null||(t=e.ownerDocument)==null?void 0:t.defaultView)||window}function qa(e){var t;return(t=(Yy(e)?e.ownerDocument:e.document)||window.document)==null?void 0:t.documentElement}function Yy(e){return!!rv()&&(e instanceof Node||e instanceof Bo(e).Node)}function ja(e){return!!rv()&&(e instanceof Element||e instanceof Bo(e).Element)}function bi(e){return!!rv()&&(e instanceof HTMLElement||e instanceof Bo(e).HTMLElement)}function Hm(e){return!(!rv()||typeof ShadowRoot>"u")&&(e instanceof ShadowRoot||e instanceof Bo(e).ShadowRoot)}function Ic(e){var{overflow:t,overflowX:n,overflowY:o,display:i}=xa(e);return/auto|scroll|overlay|hidden|clip/.test(t+o+n)&&i!=="inline"&&i!=="contents"}function q5(e){return/^(table|td|th)$/.test(Rl(e))}function Sd(e){try{if(e.matches(":popover-open"))return!0}catch{}try{return e.matches(":modal")}catch{return!1}}var Gv,D5=/transform|translate|scale|rotate|perspective|filter/,L5=/paint|layout|strict|content/,fs=e=>!!e&&e!=="none";function Zf(e){var t=ja(e)?xa(e):e;return fs(t.transform)||fs(t.translate)||fs(t.scale)||fs(t.rotate)||fs(t.perspective)||!ch()&&(fs(t.backdropFilter)||fs(t.filter))||D5.test(t.willChange||"")||L5.test(t.contain||"")}function ch(){return Gv==null&&(Gv=typeof CSS<"u"&&CSS.supports&&CSS.supports("-webkit-backdrop-filter","none")),Gv}function yl(e){return/^(html|body|#document)$/.test(Rl(e))}function xa(e){return Bo(e).getComputedStyle(e)}function ov(e){return ja(e)?{scrollLeft:e.scrollLeft,scrollTop:e.scrollTop}:{scrollLeft:e.scrollX,scrollTop:e.scrollY}}function Bi(e){if(Rl(e)==="html")return e;var t=e.assignedSlot||e.parentNode||Hm(e)&&e.host||qa(e);return Hm(t)?t.host:t}function Xy(e){var t=Bi(e);return yl(t)?e.ownerDocument?e.ownerDocument.body:e.body:bi(t)&&Ic(t)?t:Xy(t)}function qc(e,t,n){var o;t===void 0&&(t=[]),n===void 0&&(n=!0);var i=Xy(e),a=i===((o=e.ownerDocument)==null?void 0:o.body),s=Bo(i);if(a){var l=ep(s);return t.concat(s,s.visualViewport||[],Ic(i)?i:[],l&&n?qc(l):[])}return t.concat(i,qc(i,[],n))}function ep(e){return e.parent&&Object.getPrototypeOf(e.parent)?e.frameElement:null}function Zy(e){var t=xa(e),n=parseFloat(t.width)||0,o=parseFloat(t.height)||0,i=bi(e),a=i?e.offsetWidth:n,s=i?e.offsetHeight:o,l=wd(n)!==a||wd(o)!==s;return l&&(n=a,o=s),{width:n,height:o,$:l}}function uh(e){return ja(e)?e:e.contextElement}function jl(e){var t=uh(e);if(!bi(t))return Ia(1);var n=t.getBoundingClientRect(),{width:o,height:i,$:a}=Zy(t),s=(a?wd(n.width):n.width)/o,l=(a?wd(n.height):n.height)/i;return s&&Number.isFinite(s)||(s=1),l&&Number.isFinite(l)||(l=1),{x:s,y:l}}var U5=Ia(0);function ej(e){var t=Bo(e);return ch()&&t.visualViewport?{x:t.visualViewport.offsetLeft,y:t.visualViewport.offsetTop}:U5}function qs(e,t,n,o){t===void 0&&(t=!1),n===void 0&&(n=!1);var i=e.getBoundingClientRect(),a=uh(e),s=Ia(1);t&&(o?ja(o)&&(s=jl(o)):s=jl(e));var l=function(w,_,A){return _===void 0&&(_=!1),!(!A||_&&A!==Bo(w))&&_}(a,n,o)?ej(a):Ia(0),c=(i.left+l.x)/s.x,u=(i.top+l.y)/s.y,d=i.width/s.x,v=i.height/s.y;if(a)for(var f=Bo(a),h=o&&ja(o)?Bo(o):o,p=f,y=ep(p);y&&o&&h!==p;){var j=jl(y),b=y.getBoundingClientRect(),k=xa(y),E=b.left+(y.clientLeft+parseFloat(k.paddingLeft))*j.x,O=b.top+(y.clientTop+parseFloat(k.paddingTop))*j.y;c*=j.x,u*=j.y,d*=j.x,v*=j.y,c+=E,u+=O,y=ep(p=Bo(y))}return kd({width:d,height:v,x:c,y:u})}function Cd(e,t){var n=ov(e).scrollLeft;return t?t.left+n:qs(qa(e)).left+n}function tj(e,t){var n=e.getBoundingClientRect();return{x:n.left+t.scrollLeft-Cd(e,n),y:n.top+t.scrollTop}}function Qm(e,t,n){var o;if(t==="viewport")o=function(a,s){var l=Bo(a),c=qa(a),u=l.visualViewport,d=c.clientWidth,v=c.clientHeight,f=0,h=0;if(u){d=u.width,v=u.height;var p=ch();(!p||p&&s==="fixed")&&(f=u.offsetLeft,h=u.offsetTop)}var y=Cd(c);if(y<=0){var j=c.ownerDocument,b=j.body,k=getComputedStyle(b),E=j.compatMode==="CSS1Compat"&&parseFloat(k.marginLeft)+parseFloat(k.marginRight)||0,O=Math.abs(c.clientWidth-b.clientWidth-E);O<=25&&(d-=O)}else y<=25&&(d+=y);return{width:d,height:v,x:f,y:h}}(e,n);else if(t==="document")o=function(a){var s=qa(a),l=ov(a),c=a.ownerDocument.body,u=Es(s.scrollWidth,s.clientWidth,c.scrollWidth,c.clientWidth),d=Es(s.scrollHeight,s.clientHeight,c.scrollHeight,c.clientHeight),v=-l.scrollLeft+Cd(a),f=-l.scrollTop;return xa(c).direction==="rtl"&&(v+=Es(s.clientWidth,c.clientWidth)-u),{width:u,height:d,x:v,y:f}}(qa(e));else if(ja(t))o=function(a,s){var l=qs(a,!0,s==="fixed"),c=l.top+a.clientTop,u=l.left+a.clientLeft,d=bi(a)?jl(a):Ia(1);return{width:a.clientWidth*d.x,height:a.clientHeight*d.y,x:u*d.x,y:c*d.y}}(t,n);else{var i=ej(e);o={x:t.x-i.x,y:t.y-i.y,width:t.width,height:t.height}}return kd(o)}function nj(e,t){var n=Bi(e);return!(n===t||!ja(n)||yl(n))&&(xa(n).position==="fixed"||nj(n,t))}function B5(e,t,n){var o=bi(t),i=qa(t),a=n==="fixed",s=qs(e,!0,a,t),l={scrollLeft:0,scrollTop:0},c=Ia(0);function u(){c.x=Cd(i)}if(o||!o&&!a)if((Rl(t)!=="body"||Ic(i))&&(l=ov(t)),o){var d=qs(t,!0,a,t);c.x=d.x+t.clientLeft,c.y=d.y+t.clientTop}else i&&u();a&&!o&&i&&u();var v=!i||o||a?Ia(0):tj(i,l);return{x:s.left+l.scrollLeft-c.x-v.x,y:s.top+l.scrollTop-c.y-v.y,width:s.width,height:s.height}}function Yv(e){return xa(e).position==="static"}function Km(e,t){if(!bi(e)||xa(e).position==="fixed")return null;if(t)return t(e);var n=e.offsetParent;return qa(e)===n&&(n=n.ownerDocument.body),n}function Gm(e,t){var n=Bo(e);if(Sd(e))return n;if(!bi(e)){for(var o=Bi(e);o&&!yl(o);){if(ja(o)&&!Yv(o))return o;o=Bi(o)}return n}for(var i=Km(e,t);i&&q5(i)&&Yv(i);)i=Km(i,t);return i&&yl(i)&&Yv(i)&&!Zf(i)?n:i||function(a){for(var s=Bi(a);bi(s)&&!yl(s);){if(Zf(s))return s;if(Sd(s))return null;s=Bi(s)}return null}(e)||n}var F5={convertOffsetParentRelativeRectToViewportRelativeRect:function(e){var{elements:t,rect:n,offsetParent:o,strategy:i}=e,a=i==="fixed",s=qa(o),l=!!t&&Sd(t.floating);if(o===s||l&&a)return n;var c={scrollLeft:0,scrollTop:0},u=Ia(1),d=Ia(0),v=bi(o);if((v||!v&&!a)&&((Rl(o)!=="body"||Ic(s))&&(c=ov(o)),v)){var f=qs(o);u=jl(o),d.x=f.x+o.clientLeft,d.y=f.y+o.clientTop}var h=!s||v||a?Ia(0):tj(s,c);return{width:n.width*u.x,height:n.height*u.y,x:n.x*u.x-c.scrollLeft*u.x+d.x+h.x,y:n.y*u.y-c.scrollTop*u.y+d.y+h.y}},getDocumentElement:qa,getClippingRect:function(e){for(var{element:t,boundary:n,rootBoundary:o,strategy:i}=e,a=n==="clippingAncestors"?Sd(t)?[]:function(p,y){var j=y.get(p);if(j)return j;for(var b=qc(p,[],!1).filter(A=>ja(A)&&Rl(A)!=="body"),k=null,E=xa(p).position==="fixed",O=E?Bi(p):p;ja(O)&&!yl(O);){var w=xa(O),_=Zf(O);_||w.position!=="fixed"||(k=null),(E?!_&&!k:!_&&w.position==="static"&&k&&(k.position==="absolute"||k.position==="fixed")||Ic(O)&&!_&&nj(p,O))?b=b.filter(A=>A!==O):k=w,O=Bi(O)}return y.set(p,b),b}(t,this._c):[].concat(n),s=[...a,o],l=Qm(t,s[0],i),c=l.top,u=l.right,d=l.bottom,v=l.left,f=1;f<s.length;f++){var h=Qm(t,s[f],i);c=Es(h.top,c),u=xd(h.right,u),d=xd(h.bottom,d),v=Es(h.left,v)}return{width:u-v,height:d-c,x:v,y:c}},getOffsetParent:Gm,getElementRects:function(){var e=Pt(function*(t){var n=this.getOffsetParent||Gm,o=this.getDimensions,i=yield o(t.floating);return{reference:B5(t.reference,yield n(t.floating),t.strategy),floating:{x:0,y:0,width:i.width,height:i.height}}});return function(t){return e.apply(this,arguments)}}(),getClientRects:function(e){return Array.from(e.getClientRects())},getDimensions:function(e){var{width:t,height:n}=Zy(e);return{width:t,height:n}},getScale:jl,isElement:ja,isRTL:function(e){return xa(e).direction==="rtl"}};function Ym(e,t){return e.x===t.x&&e.y===t.y&&e.width===t.width&&e.height===t.height}function W5(e,t,n,o){o===void 0&&(o={});var{ancestorScroll:i=!0,ancestorResize:a=!0,elementResize:s=typeof ResizeObserver=="function",layoutShift:l=typeof IntersectionObserver=="function",animationFrame:c=!1}=o,u=uh(e),d=i||a?[...u?qc(u):[],...t?qc(t):[]]:[];d.forEach(j=>{i&&j.addEventListener("scroll",n,{passive:!0}),a&&j.addEventListener("resize",n)});var v,f=u&&l?function(j,b){var k,E=null,O=qa(j);function w(){var _;clearTimeout(k),(_=E)==null||_.disconnect(),E=null}return function _(A,q){A===void 0&&(A=!1),q===void 0&&(q=1),w();var C=j.getBoundingClientRect(),{left:z,top:D,width:H,height:Q}=C;if(A||b(),H&&Q){var fe={rootMargin:-Au(D)+"px "+-Au(O.clientWidth-(z+H))+"px "+-Au(O.clientHeight-(D+Q))+"px "+-Au(z)+"px",threshold:Es(0,xd(1,q))||1},Ie=!0;try{E=new IntersectionObserver(ge,De(De({},fe),{},{root:O.ownerDocument}))}catch{E=new IntersectionObserver(ge,fe)}E.observe(j)}function ge(qe){var ce=qe[0].intersectionRatio;if(ce!==q){if(!Ie)return _();ce?_(!1,ce):k=setTimeout(()=>{_(!1,1e-7)},1e3)}ce!==1||Ym(C,j.getBoundingClientRect())||_(),Ie=!1}}(!0),w}(u,n):null,h=-1,p=null;s&&(p=new ResizeObserver(j=>{var[b]=j;b&&b.target===u&&p&&t&&(p.unobserve(t),cancelAnimationFrame(h),h=requestAnimationFrame(()=>{var k;(k=p)==null||k.observe(t)})),n()}),u&&!c&&p.observe(u),t&&p.observe(t));var y=c?qs(e):null;return c&&function j(){var b=qs(e);y&&!Ym(y,b)&&n(),y=b,v=requestAnimationFrame(j)}(),n(),()=>{var j;d.forEach(b=>{i&&b.removeEventListener("scroll",n),a&&b.removeEventListener("resize",n)}),f==null||f(),(j=p)==null||j.disconnect(),p=null,c&&cancelAnimationFrame(v)}}var V5=function(e){return e===void 0&&(e=0),{name:"offset",options:e,fn:t=>Pt(function*(){var n,o,{x:i,y:a,placement:s,middlewareData:l}=t,c=yield function(u,d){return Xf.apply(this,arguments)}(t,e);return s===((n=l.offset)==null?void 0:n.placement)&&(o=l.arrow)!=null&&o.alignmentOffset?{}:{x:i+c.x,y:a+c.y,data:De(De({},c),{},{placement:s})}})()}},J5=function(e){return e===void 0&&(e={}),{name:"shift",options:e,fn:t=>Pt(function*(){var{x:n,y:o,placement:i,platform:a}=t,s=tv(e,t),{mainAxis:l=!0,crossAxis:c=!1,limiter:u={fn:O=>{var{x:w,y:_}=O;return{x:w,y:_}}}}=s,d=lb(s,qC),v={x:n,y:o},f=yield a.detectOverflow(t,d),h=Ui(Is(i)),p=Qy(h),y=v[p],j=v[h];if(l){var b=p==="y"?"bottom":"right";y=Fm(y+f[p==="y"?"top":"left"],y,y-f[b])}if(c){var k=h==="y"?"bottom":"right";j=Fm(j+f[h==="y"?"top":"left"],j,j-f[k])}var E=u.fn(De(De({},t),{},{[p]:y,[h]:j}));return De(De({},E),{},{data:{x:E.x-n,y:E.y-o,enabled:{[p]:l,[h]:c}}})})()}},H5=function(e){return e===void 0&&(e={}),{name:"flip",options:e,fn:t=>Pt(function*(){var n,o,{placement:i,middlewareData:a,rects:s,initialPlacement:l,platform:c,elements:u}=t,d=tv(e,t),{mainAxis:v=!0,crossAxis:f=!0,fallbackPlacements:h,fallbackStrategy:p="bestFit",fallbackAxisSideDirection:y="none",flipAlignment:j=!0}=d,b=lb(d,IC);if((n=a.arrow)!=null&&n.alignmentOffset)return{};var k=Is(i),E=Ui(l),O=Is(l)===l,w=yield c.isRTL==null?void 0:c.isRTL(u.floating),_=h||(O||!j?[zu(l)]:function(he){var Ue=zu(he);return[Gf(he),Ue,Gf(Ue)]}(l)),A=y!=="none";!h&&A&&_.push(...z5(l,j,y,w));var q=[l,..._],C=yield c.detectOverflow(t,b),z=[],D=((o=a.flip)==null?void 0:o.overflows)||[];if(v&&z.push(C[k]),f){var H=function(he,Ue,Re){Re===void 0&&(Re=!1);var we=nv(he),ue=Gy(he),ie=Ky(ue),vt=ue==="x"?we===(Re?"end":"start")?"right":"left":we==="start"?"bottom":"top";return Ue.reference[ie]>Ue.floating[ie]&&(vt=zu(vt)),[vt,zu(vt)]}(i,s,w);z.push(C[H[0]],C[H[1]])}if(D=[...D,{placement:i,overflows:z}],!z.every(he=>he<=0)){var Q,fe,Ie=(((Q=a.flip)==null?void 0:Q.index)||0)+1,ge=q[Ie];if(ge&&(!(f==="alignment"&&E!==Ui(ge))||D.every(he=>Ui(he.placement)!==E||he.overflows[0]>0)))return{data:{index:Ie,overflows:D},reset:{placement:ge}};var qe=(fe=D.filter(he=>he.overflows[0]<=0).sort((he,Ue)=>he.overflows[1]-Ue.overflows[1])[0])==null?void 0:fe.placement;if(!qe)switch(p){case"bestFit":var ce,ve=(ce=D.filter(he=>{if(A){var Ue=Ui(he.placement);return Ue===E||Ue==="y"}return!0}).map(he=>[he.placement,he.overflows.filter(Ue=>Ue>0).reduce((Ue,Re)=>Ue+Re,0)]).sort((he,Ue)=>he[1]-Ue[1])[0])==null?void 0:ce[0];ve&&(qe=ve);break;case"initialPlacement":qe=l}if(i!==qe)return{reset:{placement:qe}}}return{}})()}};function Q5(e){var t,n,o={autoUpdate:!0},i=e,a=c=>De(De(De({},o),e||{}),c||{}),s=c=>{t&&n&&(i=a(c),((u,d,v)=>{var f=new Map,h=De({platform:F5},v),p=De(De({},h.platform),{},{_c:f});return R5(u,d,De(De({},h),{},{platform:p}))})(t,n,i).then(u=>{var d;Object.assign(n.style,{position:u.strategy,left:"".concat(u.x,"px"),top:"".concat(u.y,"px")}),!((d=i)===null||d===void 0)&&d.onComputed&&i.onComputed(u)}))},l=c=>{ra(c.subscribe(u=>{t===void 0?(t=u,s()):(Object.assign(t,u),s())}))};return[c=>{if("subscribe"in c)return l(c),{};t=c,s()},(c,u)=>{var d;n=c,i=a(u),setTimeout(()=>s(u),0),s(u);var v=()=>{d&&(d(),d=void 0)},f=function(){var{autoUpdate:h}=arguments.length>0&&arguments[0]!==void 0?arguments[0]:i||{};v(),h!==!1&&ty().then(()=>W5(t,n,()=>s(i),h===!0?{}:h))};return d=f(),{update(h){s(h),d=f(h)},destroy(){v()}}},s]}function K5(e){var{loadOptions:t,filterText:n,items:o,multiple:i,value:a,itemId:s,groupBy:l,filterSelectedItems:c,itemFilter:u,convertStringItemsToObjects:d,filterGroupedItems:v,label:f}=e;if(o&&t)return o;if(!o)return[];o&&o.length>0&&typeof o[0]!="object"&&(o=d(o));var h=o.filter(p=>{var y=u(p[f],n,p);return y&&i&&a!=null&&a.length&&(y=!a.some(j=>!!c&&j[s]===p[s])),y});return l&&(h=v(h)),h}function G5(e){return rj.apply(this,arguments)}function rj(){return(rj=Pt(function*(e){var{dispatch:t,loadOptions:n,convertStringItemsToObjects:o,filterText:i}=e,a=yield n(i).catch(s=>{console.warn("svelte-select loadOptions error :>> ",s),t("error",{type:"loadOptions",details:s})});if(a&&!a.cancelled)return a?(a&&a.length>0&&typeof a[0]!="object"&&(a=o(a)),t("loaded",{items:a})):a=[],{filteredItems:a,loading:!1,focused:!0,listOpen:!0}})).apply(this,arguments)}It(`
  svg.svelte-1kxu7be {
      width: var(--chevron-icon-width, 20px);
      height: var(--chevron-icon-width, 20px);
      color: var(--chevron-icon-colour, currentColor);
  }
`);var Y5=os(`<svg width="100%" height="100%" viewBox="0 0 20 20" focusable="false" aria-hidden="true" class="svelte-1kxu7be"><path fill="currentColor" d="M4.516 7.548c0.436-0.446 1.043-0.481 1.576 0l3.908 3.747
          3.908-3.747c0.533-0.481 1.141-0.446 1.574 0 0.436 0.445 0.408 1.197 0
          1.615-0.406 0.418-4.695 4.502-4.695 4.502-0.217 0.223-0.502
          0.335-0.787 0.335s-0.57-0.112-0.789-0.335c0
          0-4.287-4.084-4.695-4.502s-0.436-1.17 0-1.615z"></path></svg>`);It(`
    svg.svelte-1hraxrc {
        width: var(--clear-icon-width, 20px);
        height: var(--clear-icon-width, 20px);
        color: var(--clear-icon-color, currentColor);
    }
`);var X5=os(`<svg width="100%" height="100%" viewBox="-2 -2 50 50" focusable="false" aria-hidden="true" role="presentation" class="svelte-1hraxrc"><path fill="currentColor" d="M34.923,37.251L24,26.328L13.077,37.251L9.436,33.61l10.923-10.923L9.436,11.765l3.641-3.641L24,19.047L34.923,8.124
    l3.641,3.641L27.641,22.688L38.564,33.61L34.923,37.251z"></path></svg>`);function Xv(e){U(e,X5())}It(`
    .loading.svelte-y9fi5p {
        width: var(--spinner-width, 20px);
        height: var(--spinner-height, 20px);
        color: var(--spinner-color, var(--icons-color));
        animation: svelte-y9fi5p-rotate 0.75s linear infinite;
        transform-origin: center center;
        transform: none;
    }

    .circle_path.svelte-y9fi5p {
        stroke-dasharray: 90;
        stroke-linecap: round;
    }

    @keyframes svelte-y9fi5p-rotate {
        100% {
            transform: rotate(360deg);
        }
    }
`);var Z5=os('<svg class="loading svelte-y9fi5p" viewBox="25 25 50 50"><circle class="circle_path svelte-y9fi5p" cx="50" cy="50" r="20" fill="none" stroke="currentColor" stroke-width="5" stroke-miterlimit="10"></circle></svg>');It(`
    .svelte-select.svelte-1ul7oo4 {
        /* deprecating camelCase custom props in favour of kebab-case for v5 */
        --borderRadius: var(--border-radius);
        --clearSelectColor: var(--clear-select-color);
        --clearSelectWidth: var(--clear-select-width);
        --disabledBackground: var(--disabled-background);
        --disabledBorderColor: var(--disabled-border-color);
        --disabledColor: var(--disabled-color);
        --disabledPlaceholderColor: var(--disabled-placeholder-color);
        --disabledPlaceholderOpacity: var(--disabled-placeholder-opacity);
        --errorBackground: var(--error-background);
        --errorBorder: var(--error-border);
        --groupItemPaddingLeft: var(--group-item-padding-left);
        --groupTitleColor: var(--group-title-color);
        --groupTitleFontSize: var(--group-title-font-size);
        --groupTitleFontWeight: var(--group-title-font-weight);
        --groupTitlePadding: var(--group-title-padding);
        --groupTitleTextTransform: var(--group-title-text-transform);
        --groupTitleBorderColor: var(--group-title-border-color);
        --groupTitleBorderWidth: var(--group-title-border-width);
        --groupTitleBorderStyle: var(--group-title-border-style);
        --indicatorColor: var(--chevron-color);
        --indicatorHeight: var(--chevron-height);
        --indicatorWidth: var(--chevron-width);
        --inputColor: var(--input-color);
        --inputLeft: var(--input-left);
        --inputLetterSpacing: var(--input-letter-spacing);
        --inputMargin: var(--input-margin);
        --inputPadding: var(--input-padding);
        --itemActiveBackground: var(--item-active-background);
        --itemColor: var(--item-color);
        --itemFirstBorderRadius: var(--item-first-border-radius);
        --itemHoverBG: var(--item-hover-bg);
        --itemHoverColor: var(--item-hover-color);
        --itemIsActiveBG: var(--item-is-active-bg);
        --itemIsActiveColor: var(--item-is-active-color);
        --itemIsNotSelectableColor: var(--item-is-not-selectable-color);
        --itemPadding: var(--item-padding);
        --listBackground: var(--list-background);
        --listBorder: var(--list-border);
        --listBorderRadius: var(--list-border-radius);
        --listEmptyColor: var(--list-empty-color);
        --listEmptyPadding: var(--list-empty-padding);
        --listEmptyTextAlign: var(--list-empty-text-align);
        --listMaxHeight: var(--list-max-height);
        --listPosition: var(--list-position);
        --listShadow: var(--list-shadow);
        --listZIndex: var(--list-z-index);
        --multiItemBG: var(--multi-item-bg);
        --multiItemBorderRadius: var(--multi-item-border-radius);
        --multiItemDisabledHoverBg: var(--multi-item-disabled-hover-bg);
        --multiItemDisabledHoverColor: var(--multi-item-disabled-hover-color);
        --multiItemHeight: var(--multi-item-height);
        --multiItemMargin: var(--multi-item-margin);
        --multiItemPadding: var(--multi-item-padding);
        --multiSelectInputMargin: var(--multi-select-input-margin);
        --multiSelectInputPadding: var(--multi-select-input-padding);
        --multiSelectPadding: var(--multi-select-padding);
        --placeholderColor: var(--placeholder-color);
        --placeholderOpacity: var(--placeholder-opacity);
        --selectedItemPadding: var(--selected-item-padding);
        --spinnerColor: var(--spinner-color);
        --spinnerHeight: var(--spinner-height);
        --spinnerWidth: var(--spinner-width);

        --internal-padding: 0 0 0 16px;

        border: var(--border, 1px solid #d8dbdf);
        border-radius: var(--border-radius, 6px);
        min-height: var(--height, 42px);
        position: relative;
        display: flex;
        align-items: stretch;
        padding: var(--padding, var(--internal-padding));
        background: var(--background, #fff);
        margin: var(--margin, 0);
        width: var(--width, 100%);
        font-size: var(--font-size, 16px);
        max-height: var(--max-height);
    }

    .svelte-1ul7oo4 {
        box-sizing: var(--box-sizing, border-box);
    }

    .svelte-select.svelte-1ul7oo4:hover {
        border: var(--border-hover, 1px solid #b2b8bf);
    }

    .value-container.svelte-1ul7oo4 {
        display: flex;
        flex: 1 1 0%;
        flex-wrap: wrap;
        align-items: center;
        gap: 5px 10px;
        padding: var(--value-container-padding, 5px 0);
        position: relative;
        overflow: var(--value-container-overflow, hidden);
        align-self: stretch;
    }

    .prepend.svelte-1ul7oo4,
    .indicators.svelte-1ul7oo4 {
        display: flex;
        flex-shrink: 0;
        align-items: center;
    }

    .indicators.svelte-1ul7oo4 {
        position: var(--indicators-position);
        top: var(--indicators-top);
        right: var(--indicators-right);
        bottom: var(--indicators-bottom);
    }

    input.svelte-1ul7oo4 {
        position: absolute;
        cursor: default;
        border: none;
        color: var(--input-color, var(--item-color));
        padding: var(--input-padding, 0);
        letter-spacing: var(--input-letter-spacing, inherit);
        margin: var(--input-margin, 0);
        min-width: 10px;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background: transparent;
        font-size: var(--font-size, 16px);
    }

    .svelte-1ul7oo4:not(.multi) > .value-container:where(.svelte-1ul7oo4) > input:where(.svelte-1ul7oo4) {
        width: 100%;
        height: 100%;
    }

    input.svelte-1ul7oo4::placeholder {
        color: var(--placeholder-color, #78848f);
        opacity: var(--placeholder-opacity, 1);
    }

    input.svelte-1ul7oo4:focus {
        outline: none;
    }

    .svelte-select.focused.svelte-1ul7oo4 {
        border: var(--border-focused, 1px solid #006fe8);
        border-radius: var(--border-radius-focused, var(--border-radius, 6px));
    }

    .disabled.svelte-1ul7oo4 {
        background: var(--disabled-background, #ebedef);
        border-color: var(--disabled-border-color, #ebedef);
        color: var(--disabled-color, #c1c6cc);
    }

    .disabled.svelte-1ul7oo4 input:where(.svelte-1ul7oo4)::placeholder {
        color: var(--disabled-placeholder-color, #c1c6cc);
        opacity: var(--disabled-placeholder-opacity, 1);
    }

    .selected-item.svelte-1ul7oo4 {
        position: relative;
        overflow: var(--selected-item-overflow, hidden);
        padding: var(--selected-item-padding, 0 20px 0 0);
        text-overflow: ellipsis;
        white-space: nowrap;
        color: var(--selected-item-color, inherit);
        font-size: var(--font-size, 16px);
    }

    .multi.svelte-1ul7oo4 .selected-item:where(.svelte-1ul7oo4) {
        position: absolute;
        line-height: var(--height, 42px);
        height: var(--height, 42px);
    }

    .selected-item.svelte-1ul7oo4:focus {
        outline: none;
    }

    .hide-selected-item.svelte-1ul7oo4 {
        opacity: 0;
    }

    .icon.svelte-1ul7oo4 {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .clear-select.svelte-1ul7oo4 {
        all: unset;
        display: flex;
        align-items: center;
        justify-content: center;
        width: var(--clear-select-width, 40px);
        height: var(--clear-select-height, 100%);
        color: var(--clear-select-color, var(--icons-color));
        margin: var(--clear-select-margin, 0);
        pointer-events: all;
        flex-shrink: 0;
    }

    .clear-select.svelte-1ul7oo4:focus {
        outline: var(--clear-select-focus-outline, 1px solid #006fe8);
    }

    .loading.svelte-1ul7oo4 {
        width: var(--loading-width, 40px);
        height: var(--loading-height);
        color: var(--loading-color, var(--icons-color));
        margin: var(--loading--margin, 0);
        flex-shrink: 0;
    }

    .chevron.svelte-1ul7oo4 {
        width: var(--chevron-width, 40px);
        height: var(--chevron-height, 40px);
        background: var(--chevron-background, transparent);
        pointer-events: var(--chevron-pointer-events, none);
        color: var(--chevron-color, var(--icons-color));
        border: var(--chevron-border, 0 0 0 1px solid #d8dbdf);
        flex-shrink: 0;
    }

    .multi.svelte-1ul7oo4 {
        padding: var(--multi-select-padding, var(--internal-padding));
    }

    .multi.svelte-1ul7oo4 input:where(.svelte-1ul7oo4) {
        padding: var(--multi-select-input-padding, 0);
        position: relative;
        margin: var(--multi-select-input-margin, 5px 0);
        flex: 1 1 40px;
    }

    .svelte-select.error.svelte-1ul7oo4 {
        border: var(--error-border, 1px solid #ff2d55);
        background: var(--error-background, #fff);
    }

    .a11y-text.svelte-1ul7oo4 {
        z-index: 9999;
        border: 0px;
        clip: rect(1px, 1px, 1px, 1px);
        height: 1px;
        width: 1px;
        position: absolute;
        overflow: hidden;
        padding: 0px;
        white-space: nowrap;
    }

    .multi-item.svelte-1ul7oo4 {
        background: var(--multi-item-bg, #ebedef);
        margin: var(--multi-item-margin, 0);
        outline: var(--multi-item-outline, 1px solid #ddd);
        border-radius: var(--multi-item-border-radius, 4px);
        height: var(--multi-item-height, 25px);
        line-height: var(--multi-item-height, 25px);
        display: flex;
        cursor: default;
        padding: var(--multi-item-padding, 0 5px);
        overflow: hidden;
        gap: var(--multi-item-gap, 4px);
        outline-offset: -1px;
        max-width: var(--multi-max-width, none);
        color: var(--multi-item-color, var(--item-color));
    }

    .multi-item.disabled.svelte-1ul7oo4:hover {
        background: var(--multi-item-disabled-hover-bg, #ebedef);
        color: var(--multi-item-disabled-hover-color, #c1c6cc);
    }

    .multi-item-text.svelte-1ul7oo4 {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .multi-item-clear.svelte-1ul7oo4 {
        display: flex;
        align-items: center;
        justify-content: center;
        --clear-icon-color: var(--multi-item-clear-icon-color, #000);
    }

    .multi-item.active.svelte-1ul7oo4 {
        outline: var(--multi-item-active-outline, 1px solid #006fe8);
    }

    .svelte-select-list.svelte-1ul7oo4 {
        box-shadow: var(--list-shadow, 0 2px 3px 0 rgba(44, 62, 80, 0.24));
        border-radius: var(--list-border-radius, 4px);
        max-height: var(--list-max-height, 252px);
        overflow-y: auto;
        background: var(--list-background, #fff);
        position: var(--list-position, absolute);
        z-index: var(--list-z-index, 2);
        border: var(--list-border);
    }

    .prefloat.svelte-1ul7oo4 {
        opacity: 0;
        pointer-events: none;
    }

    .list-group-title.svelte-1ul7oo4 {
        color: var(--group-title-color, #8f8f8f);
        cursor: default;
        font-size: var(--group-title-font-size, 16px);
        font-weight: var(--group-title-font-weight, 600);
        height: var(--height, 42px);
        line-height: var(--height, 42px);
        padding: var(--group-title-padding, 0 20px);
        text-overflow: ellipsis;
        overflow-x: hidden;
        white-space: nowrap;
        text-transform: var(--group-title-text-transform, uppercase);
        border-width: var(--group-title-border-width, medium);
        border-style: var(--group-title-border-style, none);
        border-color: var(--group-title-border-color, color);
    }

    .empty.svelte-1ul7oo4 {
        text-align: var(--list-empty-text-align, center);
        padding: var(--list-empty-padding, 20px 0);
        color: var(--list-empty-color, #78848f);
    }

    .item.svelte-1ul7oo4 {
        cursor: default;
        height: var(--item-height, var(--height, 42px));
        line-height: var(--item-line-height, var(--height, 42px));
        padding: var(--item-padding, 0 20px);
        color: var(--item-color, inherit);
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
        transition: var(--item-transition, all 0.2s);
        align-items: center;
        width: 100%;
    }

    .item.group-item.svelte-1ul7oo4 {
        padding-left: var(--group-item-padding-left, 40px);
    }

    .item.svelte-1ul7oo4:active {
        background: var(--item-active-background, #b9daff);
    }

    .item.active.svelte-1ul7oo4 {
        background: var(--item-is-active-bg, #007aff);
        color: var(--item-is-active-color, #fff);
    }

    .item.first.svelte-1ul7oo4 {
        border-radius: var(--item-first-border-radius, 4px 4px 0 0);
    }

    .item.hover.svelte-1ul7oo4:not(.active) {
        background: var(--item-hover-bg, #e7f2ff);
        color: var(--item-hover-color, inherit);
    }

    .item.not-selectable.svelte-1ul7oo4,
    .item.hover.item.not-selectable.svelte-1ul7oo4,
    .item.active.item.not-selectable.svelte-1ul7oo4,
    .item.not-selectable.svelte-1ul7oo4:active {
        color: var(--item-is-not-selectable-color, #999);
        background: transparent;
    }

    .required.svelte-1ul7oo4 {
        opacity: 0;
        z-index: -1;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
    }
`);var eO=re('<div class="list-item svelte-1ul7oo4" tabindex="-1" role="none"><div><!></div></div>'),tO=re('<div class="empty svelte-1ul7oo4">No options</div>'),nO=re('<div role="none"><!> <!> <!></div>'),rO=re('<span id="aria-selection" class="svelte-1ul7oo4"> </span> <span id="aria-context" class="svelte-1ul7oo4"> </span>',1),oO=re('<div class="multi-item-clear svelte-1ul7oo4"><!></div>'),aO=re('<div role="none"><span class="multi-item-text svelte-1ul7oo4"><!></span> <!></div>'),iO=re("<div><!></div>"),sO=re('<div class="icon loading svelte-1ul7oo4" aria-hidden="true"><!></div>'),lO=re('<button type="button" class="icon clear-select svelte-1ul7oo4"><!></button>'),cO=re('<div class="icon chevron svelte-1ul7oo4" aria-hidden="true"><!></div>'),uO=re('<input type="hidden" class="svelte-1ul7oo4"/>'),dO=re('<select class="required svelte-1ul7oo4" required="" tabindex="-1" aria-hidden="true"></select>'),vO=re('<div role="none"><!> <span aria-live="polite" aria-atomic="false" aria-relevant="additions text" class="a11y-text svelte-1ul7oo4"><!></span> <div class="prepend svelte-1ul7oo4"><!></div> <div class="value-container svelte-1ul7oo4"><!> <input/></div> <div class="indicators svelte-1ul7oo4"><!> <!> <!></div> <!> <!></div>');function ys(e,t){var n=function(P){var Z={};for(var xe in P.children&&(Z.default=!0),P.$$slots)Z[xe]=!0;return Z}(t);yt(t,!1);var o,i=R(),a=R(),s=R(),l=R(),c=R(),u=R(),d=R(),v=R(),f=R(),h=c9(),p=m(t,"justValue",12,null),y=m(t,"filter",8,K5),j=m(t,"getItems",8,G5),b=m(t,"id",8,null),k=m(t,"name",8,null),E=m(t,"container",12,void 0),O=m(t,"input",12,void 0),w=m(t,"multiple",8,!1),_=m(t,"multiFullItemClearable",8,!1),A=m(t,"disabled",8,!1),q=m(t,"focused",12,!1),C=m(t,"value",12,null),z=m(t,"filterText",12,""),D=m(t,"placeholder",8,"Please select"),H=m(t,"placeholderAlwaysShow",8,!1),Q=m(t,"items",12,null),fe=m(t,"label",8,"label"),Ie=m(t,"itemFilter",8,(P,Z,xe)=>"".concat(P).toLowerCase().includes(Z.toLowerCase())),ge=m(t,"groupBy",8,void 0),qe=m(t,"groupFilter",8,P=>P),ce=m(t,"groupHeaderSelectable",8,!1),ve=m(t,"itemId",8,"value"),he=m(t,"loadOptions",8,void 0),Ue=m(t,"containerStyles",8,""),Re=m(t,"hasError",8,!1),we=m(t,"filterSelectedItems",8,!0),ue=m(t,"required",8,!1),ie=m(t,"closeListOnChange",8,!0),vt=m(t,"clearFilterTextOnBlur",8,!0),ft=m(t,"createGroupHeaderItem",8,(P,Z)=>({value:P,[fe()]:P})),kt=()=>r(d),oe=m(t,"searchable",8,!0),Ze=m(t,"inputStyles",8,""),te=m(t,"clearable",8,!0),X=m(t,"loading",12,!1),B=m(t,"listOpen",12,!1),Ne=m(t,"debounce",8,function(P){var Z=arguments.length>1&&arguments[1]!==void 0?arguments[1]:1;clearTimeout(o),o=setTimeout(P,Z)}),ee=m(t,"debounceWait",8,300),L=m(t,"hideEmptyState",8,!1),pt=m(t,"inputAttributes",24,()=>({})),ht=m(t,"listAutoWidth",8,!0),_e=m(t,"showChevron",8,!1),at=m(t,"listOffset",8,5),We=m(t,"hoverItemIndex",12,0),Ye=m(t,"floatingConfig",24,()=>({})),Tt=m(t,"class",8,""),He=R(),qt=R(),S=R(),$=R(),N=R();function G(P){return P.map((Z,xe)=>({index:xe,value:Z,label:"".concat(Z)}))}function W(P){var Z=[],xe={};P.forEach(Qe=>{var Je=ge()(Qe);Z.includes(Je)||(Z.push(Je),xe[Je]=[],Je&&xe[Je].push(Object.assign(ft()(Je,Qe),{id:Je,groupHeader:!0,selectable:ce()}))),xe[Je].push(Object.assign({groupItem:!!Je},Qe))});var ot=[];return qe()(Z).forEach(Qe=>{xe[Qe]&&ot.push(...xe[Qe])}),ot}function de(){var P=arguments.length>0&&arguments[0]!==void 0?arguments[0]:0,Z=arguments.length>1?arguments[1]:void 0;We(P<0?0:P),!Z&&ge()&&r(d)[We()]&&!r(d)[We()].selectable&&dt(1)}function Me(){var P=!0;if(C()){var Z=[],xe=[];C().forEach(ot=>{Z.includes(ot[ve()])?P=!1:(Z.push(ot[ve()]),xe.push(ot))}),P||C(xe)}return P}function pe(P){var Z=P?P[ve()]:C()[ve()];return Q().find(xe=>xe[ve()]===Z)}function le(P){return St.apply(this,arguments)}function St(){return(St=Pt(function*(P){var Z=C()[P];C().length===1?C(void 0):C(C().filter(xe=>xe!==Z)),h("clear",Z)})).apply(this,arguments)}function lt(P){if(q())switch(P.stopPropagation(),P.key){case"Escape":P.preventDefault(),Yt();break;case"Enter":if(P.preventDefault(),B()){if(r(d).length===0)break;var Z=r(d)[We()];if(C()&&!w()&&C()[ve()]===Z[ve()]){Yt();break}ye(r(d)[We()])}break;case"ArrowDown":P.preventDefault(),B()?dt(1):(B(!0),g(He,void 0));break;case"ArrowUp":P.preventDefault(),B()?dt(-1):(B(!0),g(He,void 0));break;case"Tab":if(B()&&q()){if(r(d).length===0||C()&&C()[ve()]===r(d)[We()][ve()])return Yt();P.preventDefault(),ye(r(d)[We()]),Yt()}break;case"Backspace":if(!w()||z().length>0)return;if(w()&&C()&&C().length>0){if(le(r(He)!==void 0?r(He):C().length-1),r(He)===0||r(He)===void 0)break;g(He,C().length>r(He)?r(He)-1:void 0)}break;case"ArrowLeft":if(!C()||!w()||z().length>0)return;r(He)===void 0?g(He,C().length-1):C().length>r(He)&&r(He)!==0&&g(He,r(He)-1);break;case"ArrowRight":if(!C()||!w()||z().length>0||r(He)===void 0)return;r(He)===C().length-1?g(He,void 0):r(He)<C().length-1&&g(He,r(He)+1)}}function Xe(P){var Z,xe;q()&&O()===((Z=document)===null||Z===void 0?void 0:Z.activeElement)||(P&&h("focus",P),(xe=O())===null||xe===void 0||xe.focus(),q(!0))}function Ae(P){return $t.apply(this,arguments)}function $t(){return($t=Pt(function*(P){var Z;Ve||(B()||q())&&(h("blur",P),Yt(),q(!1),g(He,void 0),(Z=O())===null||Z===void 0||Z.blur())})).apply(this,arguments)}function sn(){if(!A())return z().length>0?B(!0):void B(!B())}function Un(){h("clear",C()),C(void 0),Yt(),Xe()}function Yt(){vt()&&z(""),B(!1)}u9(Pt(function*(){g(qt,C()),g(S,z()),g($,w())})),vo(()=>{B()&&q(!0),q()&&O()&&O().focus()});var Zt=m(t,"ariaValues",8,P=>"Option ".concat(P,", selected.")),Dt=m(t,"ariaListOpen",8,(P,Z)=>"You are currently focused on option ".concat(P,". There are ").concat(Z," results available.")),hn=m(t,"ariaFocused",8,()=>"Select is focused, type to refine list, press down to open the menu."),Hn,J=R(null);function V(){clearTimeout(Hn),Hn=setTimeout(()=>{Ve=!1},100)}ra(()=>{var P;(P=r(J))===null||P===void 0||P.remove()});var Ve=!1;function ye(P){P&&P.selectable!==!1&&function(Z){if(Z){z("");var xe=Object.assign({},Z);if(xe.groupHeader&&!xe.selectable)return;C(w()?C()?C().concat([xe]):[xe]:C(xe)),setTimeout(()=>{ie()&&Yt(),g(He,void 0),h("change",C()),h("select",Z)})}}(P)}function rt(P){Ve||We(P)}function dt(P){if(r(d).filter(xe=>!Object.hasOwn(xe,"selectable")||xe.selectable===!0).length===0)return We(0);P>0&&We()===r(d).length-1?We(0):P<0&&We()===0?We(r(d).length-1):We(We()+P);var Z=r(d)[We()];Z&&Z.selectable===!1&&(P!==1&&P!==-1||dt(P))}function At(P,Z,xe){if(!w())return Z&&Z[xe]===P[xe]}var en=Ht,Vt=Ht;function Ht(P){return{update(Z){Z.scroll&&(V(),P.scrollIntoView({behavior:"auto",block:"nearest"}))}}}var On=R({strategy:"absolute",placement:"bottom-start",middleware:[V5(at()),H5(),J5()],autoUpdate:!1}),[dn,Qn,Kn]=Q5(r(On)),Bn=R(!0);ne(()=>(x(Q()),x(C())),()=>{Q(),C()&&function(){if(typeof C()=="string"){var P=(Q()||[]).find(Z=>Z[ve()]===C());C(P||{[ve()]:C(),label:C()})}else w()&&Array.isArray(C())&&C().length>0&&C(C().map(Z=>typeof Z=="string"?{value:Z,label:Z}:Z))}()}),ne(()=>(x(pt()),x(oe())),()=>{!pt()&&oe()||(g(N,Object.assign({autocapitalize:"none",autocomplete:"off",autocorrect:"off",spellcheck:!1,tabindex:0,type:"text","aria-autocomplete":"list"},pt())),b()&&Lo(N,r(N).id=b()),oe()||Lo(N,r(N).readonly=!0))}),ne(()=>x(w()),()=>{w()&&C()&&(Array.isArray(C())?C([...C()]):C([C()]))}),ne(()=>(r($),x(w())),()=>{r($)&&!w()&&C()&&C(null)}),ne(()=>(x(w()),x(C())),()=>{w()&&C()&&C().length>1&&Me()}),ne(()=>x(C()),()=>{C()&&(w()?JSON.stringify(C())!==JSON.stringify(r(qt))&&Me()&&h("input",C()):r(qt)&&JSON.stringify(C()[ve()])===JSON.stringify(r(qt)[ve()])||h("input",C()))}),ne(()=>(x(C()),x(w()),r(qt)),()=>{!C()&&w()&&r(qt)&&h("input",C())}),ne(()=>(x(q()),x(O())),()=>{!q()&&O()&&Yt()}),ne(()=>(x(z()),r(S)),()=>{z()!==r(S)&&(he()||z().length!==0)&&(he()?Ne()(Pt(function*(){X(!0);var P=yield j()({dispatch:h,loadOptions:he(),convertStringItemsToObjects:G,filterText:z()});P?(X(P.loading),B(B()?P.listOpen:z().length>0),q(B()&&P.focused),Q(ge()?W(P.filteredItems):P.filteredItems)):(X(!1),q(!0),B(!0))}),ee()):(B(!0),w()&&g(He,void 0)))}),ne(()=>(x(y()),x(he()),x(z()),x(Q()),x(w()),x(C()),x(ve()),x(ge()),x(fe()),x(we()),x(Ie())),()=>{g(d,y()({loadOptions:he(),filterText:z(),items:Q(),multiple:w(),value:C(),itemId:ve(),groupBy:ge(),label:fe(),filterSelectedItems:we(),itemFilter:Ie(),convertStringItemsToObjects:G,filterGroupedItems:W}))}),ne(()=>(x(w()),x(B()),x(C()),r(d)),()=>{!w()&&B()&&C()&&r(d)&&de(r(d).findIndex(P=>P[ve()]===C()[ve()]),!0)}),ne(()=>(x(B()),x(w())),()=>{B()&&w()&&We(0)}),ne(()=>x(z()),()=>{z()&&We(0)}),ne(()=>x(We()),()=>{var P;P=We(),h("hoverItem",P)}),ne(()=>(x(w()),x(C())),()=>{g(i,w()?C()&&C().length>0:C())}),ne(()=>(r(i),x(z())),()=>{g(a,r(i)&&z().length>0)}),ne(()=>(r(i),x(te()),x(A()),x(X())),()=>{g(s,r(i)&&te()&&!A()&&!X())}),ne(()=>(x(H()),x(w()),x(D()),x(C())),()=>{var P;g(l,H()&&w()||w()&&((P=C())===null||P===void 0?void 0:P.length)===0?D():C()?"":D())}),ne(()=>(x(C()),x(w())),()=>{var P,Z;g(c,C()?(P=w(),Z=void 0,Z=P&&C().length>0?C().map(xe=>xe[fe()]).join(", "):C()[fe()],Zt()(Z)):"")}),ne(()=>(r(d),x(We()),x(q()),x(B())),()=>{g(u,function(){if(!r(d)||r(d).length===0)return"";var P=r(d)[We()];if(B()&&P){var Z=r(d)?r(d).length:0;return Dt()(P[fe()],Z)}return hn()()}((r(d),We(),q(),B())))}),ne(()=>x(Q()),()=>{(function(P){P&&P.length!==0&&!P.some(Z=>typeof Z!="object")&&C()&&(w()?!C().some(Z=>!Z||!Z[ve()]):C()[ve()])&&(Array.isArray(C())?C(C().map(Z=>pe(Z)||Z)):C(pe()||C()))})(Q())}),ne(()=>(x(w()),x(C()),x(ve())),()=>{p((w(),C(),ve(),w()?C()?C().map(P=>P[ve()]):null:C()?C()[ve()]:C()))}),ne(()=>(x(w()),r(qt),x(C())),()=>{w()||!r(qt)||C()||h("input",C())}),ne(()=>(x(B()),r(d),x(w()),x(C())),()=>{B()&&r(d)&&!w()&&!C()&&de()}),ne(()=>r(d),()=>{(function(P){B()&&h("filter",P)})(r(d))}),ne(()=>(x(E()),x(Ye()),r(On)),()=>{E()&&Ye()&&Kn(Object.assign(r(On),Ye()))}),ne(()=>r(J),()=>{g(v,!!r(J))}),ne(()=>(r(J),x(B())),()=>{(function(P,Z){if(!P||!Z)return g(Bn,!0);setTimeout(()=>{g(Bn,!1)},0)})(r(J),B())}),ne(()=>(x(B()),x(E()),r(J)),()=>{B()&&E()&&r(J)&&function(){var{width:P}=E().getBoundingClientRect();Lo(J,r(J).style.width=ht()?P+"px":"auto")}()}),ne(()=>x(We()),()=>{g(f,We())}),ne(()=>(x(O()),x(B()),x(q())),()=>{O()&&B()&&!q()&&Xe()}),ne(()=>(x(E()),x(Ye())),()=>{var P;E()&&((P=Ye())===null||P===void 0?void 0:P.autoUpdate)===void 0&&Lo(On,r(On).autoUpdate=!0)}),Mn();var Zn={getFilteredItems:kt,handleClear:Un};Ft();var yr,Fn=vO();ze("click",li,function(P){var Z;B()||q()||!E()||E().contains(P.target)||(Z=r(J))!==null&&Z!==void 0&&Z.contains(P.target)||Ae()}),ze("keydown",li,lt);var $n=I(Fn),ar=P=>{var Z,xe=nO(),ot=I(xe),Qe=Ot=>{var an=br();Sr(Mt(an),t,"list-prepend",{},null),U(Ot,an)};be(ot,Ot=>{F(()=>n["list-prepend"])&&Ot(Qe)});var Je=Y(ot,2),Lt=Ot=>{var an=br();Sr(Mt(an),t,"list",{get filteredItems(){return r(d)}},null),U(Ot,an)},Ct=Ot=>{var an=br();Or(Mt(an),1,()=>r(d),Pr,(fr,Gn,Nn)=>{var Ke,zn=eO(),sr=I(zn);Sr(I(sr),t,"item",{get item(){return r(Gn)},index:Nn},_t=>{var _n=oo();Le(()=>xt(_n,(r(Gn),x(fe()),F(()=>{var lr;return(lr=r(Gn))===null||lr===void 0?void 0:lr[fe()]})))),U(_t,_n)}),go(sr,(_t,_n)=>en==null?void 0:en(_t),()=>({scroll:At(r(Gn),C(),ve()),listDom:r(v)})),go(sr,(_t,_n)=>Vt==null?void 0:Vt(_t),()=>({scroll:r(f)===Nn,listDom:r(v)})),Le(_t=>Ke=Bt(sr,1,"item svelte-1ul7oo4",null,Ke,_t),[()=>{var _t,_n;return{"list-group-title":r(Gn).groupHeader,active:At(r(Gn),C(),ve()),first:(_n=Nn,_n===0),hover:We()===Nn,"group-item":r(Gn).groupItem,"not-selectable":((_t=r(Gn))===null||_t===void 0?void 0:_t.selectable)===!1}}]),ze("mouseover",zn,()=>rt(Nn)),ze("focus",zn,()=>rt(Nn)),ze("click",zn,Za(()=>function(_t){var{item:_n,i:lr}=_t;if((_n==null?void 0:_n.selectable)!==!1)return C()&&!w()&&C()[ve()]===_n[ve()]?Yt():void(function(Nr){return Nr.groupHeader&&Nr.selectable||Nr.selectable||!Nr.hasOwnProperty("selectable")}(_n)&&(We(lr),ye(_n)))}({item:r(Gn),i:Nn}))),ze("keydown",zn,Ti(Za(function(_t){dc.call(this,t,_t)}))),U(fr,zn)}),U(Ot,an)},jn=Ot=>{var an=br();Sr(Mt(an),t,"empty",{},fr=>{U(fr,tO())}),U(Ot,an)};be(Je,Ot=>{F(()=>n.list)?Ot(Lt):(r(d),F(()=>r(d).length>0)?Ot(Ct,1):L()||Ot(jn,2))});var vn=Y(Je,2),er=Ot=>{var an=br();Sr(Mt(an),t,"list-append",{},null),U(Ot,an)};be(vn,Ot=>{F(()=>n["list-append"])&&Ot(er)}),go(xe,Ot=>Qn==null?void 0:Qn(Ot)),or(xe,Ot=>g(J,Ot),()=>r(J)),so(()=>ze("scroll",xe,V)),so(()=>ze("pointerup",xe,Ti(Za(function(Ot){dc.call(this,t,Ot)})))),so(()=>ze("mousedown",xe,Ti(Za(function(Ot){dc.call(this,t,Ot)})))),Le(()=>Z=Bt(xe,1,"svelte-select-list svelte-1ul7oo4",null,Z,{prefloat:r(Bn)})),U(P,xe)};be($n,P=>{B()&&P(ar)});var Se=Y($n,2),Ee=I(Se),tn=P=>{var Z=rO(),xe=Mt(Z),ot=I(xe),Qe=I(Y(xe,2));Le(()=>{xt(ot,r(c)),xt(Qe,r(u))}),U(P,Z)};be(Ee,P=>{q()&&P(tn)});var Ar=Y(Se,2);Sr(I(Ar),t,"prepend",{},null);var jr=Y(Ar,2),on=I(jr),dr=P=>{var Z=br(),xe=Mt(Z),ot=Je=>{var Lt=br();Or(Mt(Lt),1,C,Pr,(Ct,jn,vn)=>{var er,Ot=aO(),an=I(Ot);Sr(I(an),t,"selection",{get selection(){return r(jn)},index:vn},Nn=>{var Ke=oo();Le(()=>xt(Ke,(r(jn),x(fe()),F(()=>r(jn)[fe()])))),U(Nn,Ke)});var fr=Y(an,2),Gn=Nn=>{var Ke=oO();Sr(I(Ke),t,"multi-clear-icon",{},zn=>{Xv(zn)}),ze("pointerup",Ke,Ti(Za(()=>le(vn)))),U(Nn,Ke)};be(fr,Nn=>{A()||_()||!Xv||Nn(Gn)}),Le(()=>er=Bt(Ot,1,"multi-item svelte-1ul7oo4",null,er,{active:r(He)===vn,disabled:A()})),ze("click",Ot,Ti(()=>_()?le(vn):{})),ze("keydown",Ot,Ti(Za(function(Nn){dc.call(this,t,Nn)}))),U(Ct,Ot)}),U(Je,Lt)},Qe=Je=>{var Lt,Ct=iO();Sr(I(Ct),t,"selection",{get selection(){return C()}},jn=>{var vn=oo();Le(()=>xt(vn,(x(C()),x(fe()),F(()=>C()[fe()])))),U(jn,vn)}),Le(()=>Lt=Bt(Ct,1,"selected-item svelte-1ul7oo4",null,Lt,{"hide-selected-item":r(a)})),U(Je,Ct)};be(xe,Je=>{w()?Je(ot):Je(Qe,-1)}),U(P,Z)};be(on,P=>{r(i)&&P(dr)});var vr=Y(on,2);Vu(vr,()=>De(De({readOnly:!oe()},r(N)),{},{placeholder:r(l),style:Ze(),disabled:A()}),void 0,void 0,void 0,"svelte-1ul7oo4",!0),or(vr,P=>O(P),()=>O());var Br=Y(jr,2),eo=I(Br),zr=P=>{var Z=sO();Sr(I(Z),t,"loading-icon",{},xe=>{(function(ot){U(ot,Z5())})(xe)}),U(P,Z)};be(eo,P=>{X()&&P(zr)});var Pn=Y(eo,2),yn=P=>{var Z=lO();Sr(I(Z),t,"clear-icon",{},xe=>{Xv(xe)}),ze("click",Z,Un),U(P,Z)};be(Pn,P=>{r(s)&&P(yn)});var Wt=Y(Pn,2),Wn=P=>{var Z=cO();Sr(I(Z),t,"chevron-icon",{get listOpen(){return B()}},xe=>{(function(ot){U(ot,Y5())})(xe)}),U(P,Z)};be(Wt,P=>{_e()&&P(Wn)});var ir=Y(Br,2);Sr(ir,t,"input-hidden",{get value(){return C()}},P=>{var Z=uO();Le(xe=>{Tn(Z,"name",k()),Ps(Z,xe)},[()=>(x(C()),F(()=>C()?JSON.stringify(C()):null))]),U(P,Z)});var K=Y(ir,2),Ce=P=>{var Z=br();Sr(Mt(Z),t,"required",{get value(){return C()}},xe=>{U(xe,dO())}),U(P,Z)};return be(K,P=>{x(ue()),x(C()),F(()=>ue()&&(!C()||C().length===0))&&P(Ce)}),so(()=>ze("pointerup",Fn,Ti(sn))),or(Fn,P=>E(P),()=>E()),go(Fn,P=>dn==null?void 0:dn(P)),Le(()=>{var P;yr=Bt(Fn,1,"svelte-select ".concat((P=Tt())!==null&&P!==void 0?P:""),"svelte-1ul7oo4",yr,{multi:w(),disabled:A(),focused:q(),"list-open":B(),"show-chevron":_e(),error:Re()}),ea(Fn,Ue())}),ze("keydown",vr,lt),ze("blur",vr,Ae),ze("focus",vr,Xe),vd(vr,z),U(e,Fn),Rt(t,"getFilteredItems",kt),Rt(t,"handleClear",Un),jt(Zn)}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
table.jse-transform-wizard.svelte-9wqi8y {
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
}
table.jse-transform-wizard.svelte-9wqi8y input:where(.svelte-9wqi8y) {
  font-family: inherit;
  font-size: inherit;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) th:where(.svelte-9wqi8y) {
  font-weight: normal;
  text-align: left;
  width: 60px;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) {
  width: 100%;
  display: flex;
  flex-direction: row;
  margin-bottom: calc(0.5 * var(--jse-padding, 10px));
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select .multi-item {
  align-items: center;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select .value-container {
  gap: 0 !important;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select.jse-filter-path {
  flex: 4;
  margin-right: calc(0.5 * var(--jse-padding, 10px));
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select.jse-filter-relation {
  flex: 1.5;
  margin-right: calc(0.5 * var(--jse-padding, 10px));
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select.jse-sort-path {
  flex: 3;
  margin-right: calc(0.5 * var(--jse-padding, 10px));
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select.jse-sort-direction {
  flex: 1;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select.jse-projection-paths {
  flex: 1;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .svelte-select input {
  box-sizing: border-box;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .jse-filter-value:where(.svelte-9wqi8y) {
  flex: 4;
  padding: 4px 8px;
  border: var(--jse-input-border, 1px solid #d8dbdf);
  border-radius: var(--jse-input-radius, 3px);
  outline: none;
  background: var(--jse-input-background, var(--jse-background-color, #fff));
  color: inherit;
}
table.jse-transform-wizard.svelte-9wqi8y tr:where(.svelte-9wqi8y) td:where(.svelte-9wqi8y) .jse-horizontal:where(.svelte-9wqi8y) .jse-filter-value:where(.svelte-9wqi8y):focus {
  border: var(--jse-input-border-focus, 1px solid var(--jse-input-border-focus, var(--jse-theme-color, #3883fa)));
}`);var fO=re('<table class="jse-transform-wizard svelte-9wqi8y"><tbody><tr class="svelte-9wqi8y"><th class="svelte-9wqi8y">Filter</th><td class="svelte-9wqi8y"><div class="jse-horizontal svelte-9wqi8y"><!> <!> <input class="jse-filter-value svelte-9wqi8y"/></div></td></tr><tr class="svelte-9wqi8y"><th class="svelte-9wqi8y">Sort</th><td class="svelte-9wqi8y"><div class="jse-horizontal svelte-9wqi8y"><!> <!></div></td></tr><tr class="svelte-9wqi8y"><th class="svelte-9wqi8y">Pick</th><td class="svelte-9wqi8y"><div class="jse-horizontal svelte-9wqi8y"><!></div></td></tr></tbody></table>');function pO(e,t){var n,o,i,a,s;yt(t,!1);var l=R(void 0,!0),c=R(void 0,!0),u=R(void 0,!0),d=R(void 0,!0),v=R(void 0,!0),f=R(void 0,!0),h=Zr("jsoneditor:TransformWizard"),p=m(t,"json",9),y=m(t,"queryOptions",29,()=>({})),j=m(t,"onChange",9),b=["==","!=","<","<=",">",">="].map(we=>({value:we,label:we})),k=[{value:"asc",label:"ascending"},{value:"desc",label:"descending"}],E=R((n=y())!==null&&n!==void 0&&(n=n.filter)!==null&&n!==void 0&&n.path?Pi(y().filter.path):void 0,!0),O=R((o=b.find(we=>{var ue;return we.value===((ue=y().filter)===null||ue===void 0?void 0:ue.relation)}))!==null&&o!==void 0?o:b[0],!0),w=R(((i=y())===null||i===void 0||(i=i.filter)===null||i===void 0?void 0:i.value)||"",!0),_=R((a=y())!==null&&a!==void 0&&(a=a.sort)!==null&&a!==void 0&&a.path?Pi(y().sort.path):void 0,!0),A=R((s=k.find(we=>{var ue;return we.value===((ue=y().sort)===null||ue===void 0?void 0:ue.direction)}))!==null&&s!==void 0?s:k[0],!0);ne(()=>x(p()),()=>{g(l,Array.isArray(p()))}),ne(()=>(r(l),x(p())),()=>{g(c,r(l)?Lf(p()):[])}),ne(()=>(r(l),x(p())),()=>{g(u,r(l)?Lf(p(),!0):[])}),ne(()=>(r(c),Pi),()=>{g(d,r(c).map(Pi))}),ne(()=>(r(u),Pi),()=>{g(v,r(u)?r(u).map(Pi):[])}),ne(()=>(x(y()),r(v),Gt),()=>{var we;g(f,(we=y())!==null&&we!==void 0&&(we=we.projection)!==null&&we!==void 0&&we.paths&&r(v)?y().projection.paths.map(ue=>r(v).find(ie=>Gt(ie.value,ue))).filter(ue=>!!ue):void 0)}),ne(()=>r(E),()=>{var we,ue,ie;ue=(we=r(E))===null||we===void 0?void 0:we.value,Gt((ie=y())===null||ie===void 0||(ie=ie.filter)===null||ie===void 0?void 0:ie.path,ue)||(h("changeFilterPath",ue),y(Co(y(),["filter","path"],ue,!0)),j()(y()))}),ne(()=>r(O),()=>{var we,ue,ie;ue=(we=r(O))===null||we===void 0?void 0:we.value,Gt((ie=y())===null||ie===void 0||(ie=ie.filter)===null||ie===void 0?void 0:ie.relation,ue)||(h("changeFilterRelation",ue),y(Co(y(),["filter","relation"],ue,!0)),j()(y()))}),ne(()=>r(w),()=>{var we,ue;we=r(w),Gt((ue=y())===null||ue===void 0||(ue=ue.filter)===null||ue===void 0?void 0:ue.value,we)||(h("changeFilterValue",we),y(Co(y(),["filter","value"],we,!0)),j()(y()))}),ne(()=>r(_),()=>{var we,ue,ie;ue=(we=r(_))===null||we===void 0?void 0:we.value,Gt((ie=y())===null||ie===void 0||(ie=ie.sort)===null||ie===void 0?void 0:ie.path,ue)||(h("changeSortPath",ue),y(Co(y(),["sort","path"],ue,!0)),j()(y()))}),ne(()=>r(A),()=>{var we,ue,ie;ue=(we=r(A))===null||we===void 0?void 0:we.value,Gt((ie=y())===null||ie===void 0||(ie=ie.sort)===null||ie===void 0?void 0:ie.direction,ue)||(h("changeSortDirection",ue),y(Co(y(),["sort","direction"],ue,!0)),j()(y()))}),ne(()=>r(f),()=>{(function(we){var ue;Gt((ue=y())===null||ue===void 0||(ue=ue.projection)===null||ue===void 0?void 0:ue.paths,we)||(h("changeProjectionPaths",we),y(Co(y(),["projection","paths"],we,!0)),j()(y()))})(r(f)?r(f).map(we=>we.value):void 0)}),Mn(),Ft(!0);var q=fO(),C=I(q),z=I(C),D=Y(I(z)),H=I(D),Q=I(H);ys(Q,{class:"jse-filter-path",showChevron:!0,get items(){return r(d)},get value(){return r(E)},set value(we){g(E,we)},$$legacy:!0});var fe=Y(Q,2);ys(fe,{class:"jse-filter-relation",showChevron:!0,clearable:!1,get items(){return b},get value(){return r(O)},set value(we){g(O,we)},$$legacy:!0});var Ie=Y(fe,2),ge=Y(z),qe=Y(I(ge)),ce=I(qe),ve=I(ce);ys(ve,{class:"jse-sort-path",showChevron:!0,get items(){return r(d)},get value(){return r(_)},set value(we){g(_,we)},$$legacy:!0}),ys(Y(ve,2),{class:"jse-sort-direction",showChevron:!0,clearable:!1,get items(){return k},get value(){return r(A)},set value(we){g(A,we)},$$legacy:!0});var he=Y(ge),Ue=Y(I(he)),Re=I(Ue);ys(I(Re),{class:"jse-projection-paths",multiple:!0,showChevron:!0,get items(){return r(v)},get value(){return r(f)},set value(we){g(f,we)},$$legacy:!0}),vd(Ie,()=>r(w),we=>g(w,we)),U(e,q),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-select-query-language.svelte-jrd4q2 {
  position: relative;
  width: 32px;
}
.jse-select-query-language.svelte-jrd4q2 .jse-select-query-language-container:where(.svelte-jrd4q2) {
  position: absolute;
  top: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  box-shadow: var(--jse-controls-box-shadow, 0 2px 6px 0 rgba(0, 0, 0, 0.24));
}
.jse-select-query-language.svelte-jrd4q2 .jse-select-query-language-container:where(.svelte-jrd4q2) .jse-query-language:where(.svelte-jrd4q2) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  text-align: left;
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  white-space: nowrap;
  color: var(--jse-context-menu-color, var(--jse-text-color-inverse, #fff));
  background: var(--jse-context-menu-background, #656565);
}
.jse-select-query-language.svelte-jrd4q2 .jse-select-query-language-container:where(.svelte-jrd4q2) .jse-query-language:where(.svelte-jrd4q2):hover {
  background: var(--jse-context-menu-background-highlight, #7a7a7a);
}`);var hO=re('<button type="button"><!> </button>'),gO=re('<div class="jse-select-query-language svelte-jrd4q2"><div class="jse-select-query-language-container svelte-jrd4q2"></div></div>');function mO(e,t){yt(t,!1);var n=m(t,"queryLanguages",8),o=m(t,"queryLanguageId",12),i=m(t,"onChangeQueryLanguage",8);Ft();var a=gO();Or(I(a),5,n,Pr,(s,l)=>{var c,u=hO(),d=I(u),v=p=>{un(p,{get data(){return Y1}})},f=p=>{un(p,{get data(){return X1}})};be(d,p=>{r(l),x(o()),F(()=>r(l).id===o())?p(v):p(f,-1)});var h=Y(d);Le(()=>{var p;c=Bt(u,1,"jse-query-language svelte-jrd4q2",null,c,{selected:r(l).id===o()}),Tn(u,"title",(r(l),F(()=>"Select ".concat(r(l).name," as query language")))),xt(h," ".concat((r(l),(p=F(()=>r(l).name))!==null&&p!==void 0?p:"")))}),ze("click",u,()=>{return p=r(l).id,o(p),void i()(p);var p}),U(s,u)}),U(e,a),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-header.svelte-1k211ye {
  display: flex;
  background: var(--jse-theme-color, #3883fa);
  color: var(--jse-menu-color, var(--jse-text-color-inverse, #fff));
}
.jse-header.svelte-1k211ye .jse-title:where(.svelte-1k211ye) {
  flex: 1;
  padding: 5px;
  vertical-align: middle;
}
.jse-header.svelte-1k211ye button:where(.svelte-1k211ye) {
  border: none;
  background: transparent;
  min-width: 32px;
  color: inherit;
  cursor: pointer;
}
.jse-header.svelte-1k211ye button:where(.svelte-1k211ye):hover {
  background: rgba(255, 255, 255, 0.1);
}`);var bO=re('<button type="button" class="jse-fullscreen svelte-1k211ye" title="Toggle full screen"><!></button>'),yO=re('<div class="jse-header svelte-1k211ye"><div class="jse-title svelte-1k211ye"> </div> <!> <!> <button type="button" class="jse-close svelte-1k211ye"><!></button></div>');function Od(e,t){yt(t,!1);var n=m(t,"title",9,"Modal"),o=m(t,"fullScreenButton",9,!1),i=m(t,"fullscreen",13,!1),a=m(t,"onClose",9,void 0);Ft(!0);var s=yO(),l=I(s),c=I(l),u=Y(l,2);Sr(u,t,"actions",{},null);var d=Y(u,2),v=h=>{var p=bO(),y=I(p),j=nt(()=>i()?uC:rC);un(y,{get data(){return r(j)}}),ze("click",p,()=>i(!i())),U(h,p)};be(d,h=>{o()&&h(v)});var f=Y(d,2);un(I(f),{get data(){return Hd}}),Le(()=>xt(c,n())),ze("click",f,()=>{var h;return(h=a())===null||h===void 0?void 0:h()}),U(e,s),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-config.svelte-5gkegr {
  border: none;
  background: transparent;
  min-width: 32px;
  color: inherit;
  cursor: pointer;
}
.jse-config.svelte-5gkegr:hover {
  background: rgba(255, 255, 255, 0.1);
}
.jse-config.hide.svelte-5gkegr {
  display: none;
}`);var jO=re('<button slot="actions" type="button" title="Select a query language"><!></button>'),Zv=Zr("jsoneditor:AutoScrollHandler");function Xm(e){var t,n;function o(l){return l<20?200:l<50?400:1200}function i(){if(e){var l=.05*(t||0);e.scrollTop+=l}}function a(l){n&&l===t||(s(),Zv("startAutoScroll",l),t=l,n=setInterval(i,50))}function s(){n&&(Zv("stopAutoScroll"),clearInterval(n),n=void 0,t=void 0)}return Zv("createAutoScrollHandler",e),{onDrag:function(l){if(e){var c=l.clientY,{top:u,bottom:d}=e.getBoundingClientRect();c<u?a(-o(u-c)):c>d?a(o(c-d)):s()}},onDragEnd:function(){s()}}}var xO=(e,t,n,o)=>(e/=o/2)<1?n/2*e*e+t:-n/2*(--e*(e-2)-1)+t,oj=()=>{var e,t,n,o,i,a,s,l,c,u,d,v,f;function h(j){return j.getBoundingClientRect().top-(e.getBoundingClientRect?e.getBoundingClientRect().top:0)+n}function p(j){e.scrollTo?e.scrollTo(e.scrollLeft,j):e.scrollTop=j}function y(j){u||(u=j),p(a(d=j-u,n,l,c)),f=!0,d<c?requestAnimationFrame(y):function(){p(n+l),t&&s&&(t.setAttribute("tabindex","-1"),t.focus()),typeof v=="function"&&v(),u=0,f=!1}()}return function(j){var b=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};switch(c=1e3,i=b.offset||0,v=b.callback,a=b.easing||xO,s=b.a11y||!1,typeof b.container){case"object":e=b.container;break;case"string":e=document.querySelector(b.container);break;default:e=window.document.documentElement}switch(n=e.scrollTop,typeof j){case"number":t=void 0,s=!1,o=n+j;break;case"object":o=h(t=j);break;case"string":t=document.querySelector(j),o=h(t)}switch(l=o-n+i,typeof b.duration){case"number":c=b.duration;break;case"function":c=b.duration(l)}f?u=0:requestAnimationFrame(y)}};function fl(e,t){var n=Date.now(),o=e();return t(Date.now()-n),o}var al=Zr("validation"),wO={createObjectDocumentState:()=>({type:"object",properties:{}}),createArrayDocumentState:()=>({type:"array",items:[]}),createValueDocumentState:()=>({type:"value"})};function Zm(e,t,n,o){return ah(e,t,n,o,wO)}function aj(e,t,n,o){if(al("validateJSON"),!t)return[];if(n!==o){var i=n.stringify(e);return t(i!==void 0?o.parse(i):void 0)}return t(e)}function kO(e,t,n,o){if(al("validateText"),e.length>104857600)return{validationErrors:[{path:[],message:"Validation turned off: the document is too large",severity:ba.info}]};if(e.length!==0)try{var i=fl(()=>n.parse(e),c=>al("validate: parsed json in ".concat(c," ms")));if(!t)return;var a=n===o?i:fl(()=>o.parse(e),c=>al("validate: parsed json with the validationParser in ".concat(c," ms"))),s=fl(()=>t(a),c=>al("validate: validated json in ".concat(c," ms")));return gn(s)?void 0:{validationErrors:s}}catch(c){var l=fl(()=>function(u,d){if(u.length>i5)return!1;try{return d.parse(Aa(u)),!0}catch{return!1}}(e,n),u=>al("validate: checked whether repairable in ".concat(u," ms")));return{parseError:$l(e,c.message||c.toString()),isRepairable:l}}}var Pu=Zr("jsoneditor:FocusTracker");function dh(e){var t,{onMount:n,onDestroy:o,getWindow:i,hasFocus:a,onFocus:s,onBlur:l}=e,c=!1;function u(){var v=a();v&&(clearTimeout(t),c||(Pu("focus"),s(),c=v))}function d(){c&&(clearTimeout(t),t=setTimeout(()=>{a()||(Pu("blur"),c=!1,l())}))}n(()=>{Pu("mount FocusTracker");var v=i();v&&(v.addEventListener("focusin",u,!0),v.addEventListener("focusout",d,!0))}),o(()=>{Pu("destroy FocusTracker");var v=i();v&&(v.removeEventListener("focusin",u,!0),v.removeEventListener("focusout",d,!0))})}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-message.svelte-cbvd26 {
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  padding: var(--jse-padding, 10px);
  display: flex;
  gap: var(--jse-padding, 10px);
  flex-wrap: wrap;
  align-items: stretch;
}
.jse-message.jse-success.svelte-cbvd26 {
  background: var(--message-success-background, #9ac45d);
  color: var(--jse-message-success-color, #fff);
}
.jse-message.svelte-cbvd26 .jse-text:where(.svelte-cbvd26) {
  display: flex;
  flex: 1;
  min-width: 60%;
  align-items: center;
}
.jse-message.svelte-cbvd26 .jse-text.jse-clickable:where(.svelte-cbvd26) {
  cursor: pointer;
}
.jse-message.svelte-cbvd26 .jse-text.jse-clickable:where(.svelte-cbvd26):hover {
  background-color: rgba(255, 255, 255, 0.1);
}
.jse-message.jse-error.svelte-cbvd26 {
  background: var(--jse-message-error-background, var(--jse-error-color, #ee5341));
  color: var(--jse-message-error-color, #fff);
}
.jse-message.jse-warning.svelte-cbvd26 {
  background: var(--jse-message-warning-background, #ffde5c);
  color: var(--jse-message-warning-color, #4d4d4d);
}
.jse-message.jse-info.svelte-cbvd26 {
  background: var(--jse-message-info-background, #4f91ff);
  color: var(--jse-message-info-color, #fff);
}
.jse-message.svelte-cbvd26 .jse-actions:where(.svelte-cbvd26) {
  display: flex;
  gap: var(--jse-padding, 10px);
}
.jse-message.svelte-cbvd26 .jse-actions:where(.svelte-cbvd26) button.jse-action:where(.svelte-cbvd26) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-message-action-background, rgba(255, 255, 255, 0.2));
  color: inherit;
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px);
}
.jse-message.svelte-cbvd26 .jse-actions:where(.svelte-cbvd26) button.jse-action:where(.svelte-cbvd26):hover {
  background: var(--jse-message-action-background-highlight, rgba(255, 255, 255, 0.3));
}`);var SO=re('<button type="button" class="jse-button jse-action jse-primary svelte-cbvd26"><!> </button>'),CO=re('<div><div role="button" tabindex="-1"><div class="jse-text-centered"><!> </div></div> <div class="jse-actions svelte-cbvd26"></div></div>');function Fo(e,t){yt(t,!1);var n=m(t,"type",9,"success"),o=m(t,"icon",9,void 0),i=m(t,"message",9,void 0),a=m(t,"actions",25,()=>[]),s=m(t,"onClick",9,void 0),l=m(t,"onClose",9,void 0);l()&&ra(l()),Ft(!0);var c,u=CO(),d=I(u),v=I(d),f=I(v),h=y=>{un(y,{get data(){return o()}})};be(f,y=>{o()&&y(h)});var p=Y(f);Or(Y(d,2),5,a,Pr,(y,j)=>{var b=SO(),k=I(b),E=w=>{un(w,{get data(){return r(j),F(()=>r(j).icon)}})};be(k,w=>{r(j),F(()=>r(j).icon)&&w(E)});var O=Y(k);Le(()=>{var w;Tn(b,"title",(r(j),F(()=>r(j).title))),b.disabled=(r(j),F(()=>r(j).disabled)),xt(O," ".concat((r(j),(w=F(()=>r(j).text))!==null&&w!==void 0?w:"")))}),ze("click",b,()=>{r(j).onClick&&r(j).onClick()}),ze("mousedown",b,()=>{r(j).onMouseDown&&r(j).onMouseDown()}),U(y,b)}),Le(()=>{var y,j;Bt(u,1,"jse-message jse-".concat((y=n())!==null&&y!==void 0?y:""),"svelte-cbvd26"),c=Bt(d,1,"jse-text svelte-cbvd26",null,c,{"jse-clickable":!!s()}),xt(p," ".concat((j=i())!==null&&j!==void 0?j:""))}),ze("click",d,function(){s()&&s()()}),U(e,u),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-validation-errors-overview.svelte-1342rh4 {
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  overflow: auto;
  max-height: 25%;
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) {
  border-collapse: collapse;
  width: 100%;
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4) {
  cursor: pointer;
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr.jse-validation-error:where(.svelte-1342rh4) {
  background: var(--jse-message-error-background, var(--jse-error-color, #ee5341));
  color: var(--jse-message-error-color, #fff);
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr.jse-validation-warning:where(.svelte-1342rh4) {
  background: var(--jse-message-warning-background, #ffde5c);
  color: var(--jse-message-warning-color, #4d4d4d);
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr.jse-validation-warning:where(.svelte-1342rh4):hover {
  filter: brightness(105%);
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr.jse-validation-info:where(.svelte-1342rh4) {
  background: var(--jse-message-info-background, #4f91ff);
  color: var(--jse-message-info-color, #fff);
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4):hover {
  filter: brightness(110%);
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4) td:where(.svelte-1342rh4) {
  padding: 4px var(--jse-padding, 10px);
  vertical-align: middle;
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4) td.jse-validation-error-icon:where(.svelte-1342rh4) {
  width: 36px;
  box-sizing: border-box;
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4) td.jse-validation-error-action:where(.svelte-1342rh4) {
  width: 36px;
  box-sizing: border-box;
  padding: 0;
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4) td.jse-validation-error-action:where(.svelte-1342rh4) button.jse-validation-errors-collapse:where(.svelte-1342rh4) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  width: 36px;
  height: 26px;
  cursor: pointer;
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4) td.jse-validation-error-action:where(.svelte-1342rh4) button.jse-validation-errors-collapse:where(.svelte-1342rh4):hover {
  background-color: rgba(255, 255, 255, 0.2);
}
.jse-validation-errors-overview.svelte-1342rh4 table:where(.svelte-1342rh4) tr:where(.svelte-1342rh4) td:where(.svelte-1342rh4) div.jse-validation-errors-expand:where(.svelte-1342rh4) {
  display: inline-block;
  position: relative;
  top: 3px;
}`);var OO=re('<button type="button" class="jse-validation-errors-collapse svelte-1342rh4" title="Collapse validation errors"><!></button>'),_O=re('<tr tabindex="0"><td class="jse-validation-error-icon svelte-1342rh4"><!></td><td class="jse-validation-error-path svelte-1342rh4"> </td><td class="jse-validation-error-message svelte-1342rh4"> </td><td class="jse-validation-error-action svelte-1342rh4"><!></td></tr>'),EO=re('<tr class="jse-validation-error svelte-1342rh4"><td class="svelte-1342rh4"></td><td class="svelte-1342rh4"></td><td class="svelte-1342rh4"> </td><td class="svelte-1342rh4"></td></tr>'),TO=re('<table class="jse-validation-errors-overview-expanded svelte-1342rh4"><tbody><!><!></tbody></table>'),MO=re('<table class="jse-validation-errors-overview-collapsed svelte-1342rh4"><tbody><tr><td class="jse-validation-error-icon svelte-1342rh4"><!></td><td class="jse-validation-error-count svelte-1342rh4"> <div class="jse-validation-errors-expand svelte-1342rh4"><!></div></td></tr></tbody></table>'),$O=re('<div class="jse-validation-errors-overview svelte-1342rh4"><!></div>');function vh(e,t){yt(t,!1);var n=R(void 0,!0),o=m(t,"validationErrors",9),i=m(t,"selectError",9),a=R(!0,!0);function s(){g(a,!1)}function l(){g(a,!0)}ne(()=>x(o()),()=>{g(n,o().length)}),Mn(),Ft(!0);var c=br(),u=Mt(c),d=f=>{var h=$O(),p=I(h),y=b=>{var k=TO(),E=I(k),O=I(E);Or(O,1,()=>(x(fd),x(o()),x(Eu),F(()=>fd(o(),Eu))),Pr,(A,q,C)=>{var z=_O(),D=I(z);un(I(D),{get data(){return $s}});var H=Y(D),Q=I(H),fe=Y(H),Ie=I(fe),ge=I(Y(fe)),qe=ce=>{var ve=OO();un(I(ve),{get data(){return iC}}),ze("click",ve,Za(s)),U(ce,ve)};be(ge,ce=>{x(o()),F(()=>C===0&&o().length>1)&&ce(qe)}),Le(ce=>{var ve;Bt(z,1,"jse-validation-".concat((r(q),(ve=F(()=>r(q).severity))!==null&&ve!==void 0?ve:"")),"svelte-1342rh4"),xt(Q,ce),xt(Ie,(r(q),F(()=>r(q).message)))},[()=>(x(Eo),r(q),F(()=>Eo(r(q).path)))]),ze("click",z,()=>{setTimeout(()=>i()(r(q)))}),U(A,z)});var w=Y(O),_=A=>{var q=EO(),C=Y(I(q),2),z=I(C);Le(()=>xt(z,"(and ".concat(r(n)-Eu," more errors)"))),U(A,q)};be(w,A=>{r(n)>Eu&&A(_)}),U(b,k)},j=b=>{var k=MO(),E=I(k),O=I(E),w=I(O);un(I(w),{get data(){return $s}});var _=I(Y(w));un(I(Y(_)),{get data(){return rb}}),Le(A=>{var q;Bt(O,1,"jse-validation-".concat(A??""),"svelte-1342rh4"),xt(_,"".concat((q=r(n))!==null&&q!==void 0?q:""," validation errors "))},[()=>(x(o()),F(()=>{return A=o(),[ba.error,ba.warning,ba.info].find(q=>A.some(C=>C.severity===q));var A}))]),ze("click",O,l),U(b,k)};be(p,b=>{r(a)||r(n)===1?b(y):b(j,-1)}),U(f,h)},v=Kt(()=>(x(gn),x(o()),F(()=>!gn(o()))));be(u,f=>{r(v)&&f(d)}),U(e,c),jt()}function _d(e,t){if(e)return e.addEventListener("keydown",n),{destroy(){e.removeEventListener("keydown",n)}};function n(o){o.key==="Escape"&&(o.preventDefault(),o.stopPropagation(),t())}}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
dialog.jse-modal.svelte-2aoco4 {
  border-radius: 3px;
  font-size: var(--jse-padding, 10px);
  border: none;
  padding: 0;
  display: flex;
  min-width: 0;
  margin: auto;
  overflow: visible;
  transition: width 0.1s ease-in-out, height 0.1s ease-in-out;
}
dialog.jse-modal.jse-sort-modal.svelte-2aoco4 {
  width: 400px;
}
dialog.jse-modal.jse-repair-modal.svelte-2aoco4 {
  width: 600px;
  height: 500px;
}
dialog.jse-modal.jse-jsoneditor-modal.svelte-2aoco4 {
  width: 800px;
  height: 600px;
}
dialog.jse-modal.jse-transform-modal.svelte-2aoco4 {
  width: 1200px;
  height: 800px;
}
dialog.jse-modal.jse-fullscreen.svelte-2aoco4 {
  width: 100%;
  height: 100%;
}
dialog.jse-modal.svelte-2aoco4::backdrop {
  background: var(--jse-overlay-background, rgba(0, 0, 0, 0.3));
}
dialog.jse-modal[open].svelte-2aoco4 {
  animation: svelte-2aoco4-zoom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
dialog.jse-modal[open].svelte-2aoco4::backdrop {
  animation: svelte-2aoco4-fade 0.2s ease-out;
}
dialog.jse-modal.svelte-2aoco4 .jse-modal-inner:where(.svelte-2aoco4) {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
  min-height: 0;
  padding: 0;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  line-height: normal;
  background: var(--jse-modal-background, #f5f5f5);
  color: var(--jse-text-color, #4d4d4d);
}
@keyframes svelte-2aoco4-zoom {
  from {
    transform: scale(0.95);
  }
  to {
    transform: scale(1);
  }
}
@keyframes svelte-2aoco4-fade {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
dialog.jse-modal.svelte-2aoco4 .svelte-select {
  --border: var(--jse-svelte-select-border, 1px solid #d8dbdf);
  --item-is-active-bg: var(--jse-item-is-active-bg, #3883fa);
  --border-radius: var(--jse-svelte-select-border-radius, 3px);
  --background: var(--jse-svelte-select-background, #fff);
  --padding: var(--jse-svelte-select-padding, 0 10px);
  --multi-select-padding: var(--jse-svelte-select-multi-select-padding, 0 10px);
  --font-size: var(--jse-svelte-select-font-size, var(--jse-font-size, 16px));
  --height: 36px;
  --multi-item-height: 28px;
  --multi-item-margin: 2px;
  --multi-item-padding: 2px 8px;
  --multi-item-border-radius: 6px;
  --indicator-top: 8px;
}`);var AO=re('<dialog><div class="jse-modal-inner svelte-2aoco4"><!></div></dialog>');function Dc(e,t){yt(t,!1);var n=m(t,"className",8,void 0),o=m(t,"fullscreen",8,!1),i=m(t,"onClose",8),a=R();function s(){i()()}vo(()=>r(a).showModal()),ra(()=>r(a).close()),Ft();var l,c=AO(),u=I(c);Sr(I(u),t,"default",{},null),or(c,d=>g(a,d),()=>r(a)),so(()=>ze("close",c,s)),so(()=>{return ze("pointerdown",c,(d=s,function(){for(var v=arguments.length,f=new Array(v),h=0;h<v;h++)f[h]=arguments[h];f[0].target===this&&(d==null||d.apply(this,f))}));var d}),so(()=>ze("cancel",c,Ti(function(d){dc.call(this,t,d)}))),go(c,(d,v)=>_d==null?void 0:_d(d,v),()=>s),Le(d=>l=Bt(c,1,d,"svelte-2aoco4",l,{"jse-fullscreen":o()}),[()=>es((x(ka),x(n()),F(()=>ka("jse-modal",n()))))]),U(e,c),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-modal-contents.svelte-10a6ob6 {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
  overflow: auto;
  min-width: 0;
  min-height: 0;
}
.jse-modal-contents.svelte-10a6ob6 .jse-actions:where(.svelte-10a6ob6) {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-top: var(--jse-padding, 10px);
}
.jse-modal-contents.svelte-10a6ob6 .jse-actions:where(.svelte-10a6ob6) button.jse-primary:where(.svelte-10a6ob6) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-button-primary-background, var(--jse-theme-color, #3883fa));
  color: var(--jse-button-primary-color, #fff);
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  border-radius: 3px;
}
.jse-modal-contents.svelte-10a6ob6 .jse-actions:where(.svelte-10a6ob6) button.jse-primary:where(.svelte-10a6ob6):hover {
  background: var(--jse-button-primary-background-highlight, var(--jse-theme-color-highlight, #5f9dff));
}
.jse-modal-contents.svelte-10a6ob6 .jse-actions:where(.svelte-10a6ob6) button.jse-primary:where(.svelte-10a6ob6):disabled {
  background: var(--jse-button-primary-background-disabled, #9d9d9d);
}

.jse-shortcuts.svelte-10a6ob6 {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  margin: calc(2 * var(--jse-padding, 10px)) 0;
}
.jse-shortcuts.svelte-10a6ob6 .jse-shortcut:where(.svelte-10a6ob6) .jse-key:where(.svelte-10a6ob6) {
  font-size: 200%;
  color: var(--jse-theme-color, #3883fa);
}`);var zO=re('<!> <div class="jse-modal-contents svelte-10a6ob6"><div>Clipboard permission is disabled by your browser. You can use:</div> <div class="jse-shortcuts svelte-10a6ob6"><div class="jse-shortcut svelte-10a6ob6"><div class="jse-key svelte-10a6ob6"> </div> for copy</div> <div class="jse-shortcut svelte-10a6ob6"><div class="jse-key svelte-10a6ob6"> </div> for cut</div> <div class="jse-shortcut svelte-10a6ob6"><div class="jse-key svelte-10a6ob6"> </div> for paste</div></div> <div class="jse-actions svelte-10a6ob6"><button type="button" class="jse-primary svelte-10a6ob6">Close</button></div></div>',1);function ij(e,t){yt(t,!1);var n=m(t,"onClose",9),o=Yp()?"⌘":"Ctrl";Ft(!0),Dc(e,{get onClose(){return n()},className:"jse-copy-paste",children:(i,a)=>{var s=zO(),l=Mt(s);Od(l,{title:"Copying and pasting",get onClose(){return n()}});var c=Y(l,2),u=Y(I(c),2),d=I(u),v=I(d),f=I(v),h=Y(d,2),p=I(h),y=I(p),j=I(Y(h,2)),b=I(j),k=I(Y(u,2));Le(()=>{xt(f,"".concat(o,"+C")),xt(y,"".concat(o,"+X")),xt(b,"".concat(o,"+V"))}),ze("click",k,function(){for(var E,O=arguments.length,w=new Array(O),_=0;_<O;_++)w[_]=arguments[_];(E=n())===null||E===void 0||E.apply(this,w)}),U(i,s)},$$slots:{default:!0}}),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-menu.svelte-3erbu0 {
  background: var(--jse-theme-color, #3883fa);
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size-main-menu, 14px);
  color: var(--jse-menu-color, var(--jse-text-color-inverse, #fff));
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  position: relative;
}
.jse-menu.svelte-3erbu0 .jse-button:where(.svelte-3erbu0) {
  font-family: inherit;
  font-size: inherit;
  line-height: 1.5em;
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  width: var(--jse-menu-button-size, 32px);
  height: var(--jse-menu-button-size, 32px);
  padding: calc(0.5 * var(--jse-padding, 10px));
  margin: 0;
  border-radius: 0;
  display: inline-flex;
  align-items: center;
  text-align: center;
  justify-content: center;
}
.jse-menu.svelte-3erbu0 .jse-button:where(.svelte-3erbu0):hover, .jse-menu.svelte-3erbu0 .jse-button:where(.svelte-3erbu0):focus {
  background: var(--jse-theme-color-highlight, #5f9dff);
}
.jse-menu.svelte-3erbu0 .jse-button:where(.svelte-3erbu0):disabled {
  color: var(--jse-menu-color, var(--jse-text-color-inverse, #fff));
  opacity: 0.5;
  background: transparent;
}
.jse-menu.svelte-3erbu0 .jse-button.jse-group-button:where(.svelte-3erbu0) {
  width: auto;
  height: calc(var(--jse-menu-button-size, 32px) - var(--jse-padding, 10px));
  margin: calc(0.5 * var(--jse-padding, 10px)) 0;
  padding: 0 calc(0.5 * var(--jse-padding, 10px)) 1px;
  border: 1px solid var(--jse-menu-color, var(--jse-text-color-inverse, #fff));
}
.jse-menu.svelte-3erbu0 .jse-button.jse-group-button:where(.svelte-3erbu0):not(.jse-last) {
  border-right: none;
}
.jse-menu.svelte-3erbu0 .jse-button.jse-group-button.jse-first:where(.svelte-3erbu0) {
  margin-left: calc(0.5 * var(--jse-padding, 10px));
}
.jse-menu.svelte-3erbu0 .jse-button.jse-group-button.jse-last:where(.svelte-3erbu0) {
  margin-right: calc(0.5 * var(--jse-padding, 10px));
}
.jse-menu.svelte-3erbu0 .jse-button.jse-group-button:where(.svelte-3erbu0):hover, .jse-menu.svelte-3erbu0 .jse-button.jse-group-button:where(.svelte-3erbu0):focus {
  background: var(--jse-theme-color-highlight, #5f9dff);
}
.jse-menu.svelte-3erbu0 .jse-button.jse-group-button.jse-selected:where(.svelte-3erbu0) {
  background: var(--jse-menu-color, var(--jse-text-color-inverse, #fff));
  color: var(--jse-theme-color, #3883fa);
}
.jse-menu.svelte-3erbu0 .jse-space:where(.svelte-3erbu0) {
  flex: 1;
}
.jse-menu.svelte-3erbu0 .jse-separator:where(.svelte-3erbu0) {
  background: var(--jse-menu-color, var(--jse-text-color-inverse, #fff));
  opacity: 0.3;
  width: 1px;
  margin: 3px;
}`);var PO=re('<div class="jse-separator svelte-3erbu0"></div>'),NO=re('<div class="jse-space svelte-3erbu0"></div>'),RO=re('<button type="button"><!> <!></button>'),IO=re('<div class="jse-menu svelte-3erbu0"><!> <!> <!></div>');function av(e,t){yt(t,!1);var n=m(t,"items",25,()=>[]);Ft(!0);var o=IO(),i=I(o);Sr(i,t,"left",{},null);var a=Y(i,2);Or(a,1,n,Pr,(s,l)=>{var c=br(),u=Mt(c),d=b=>{U(b,PO())},v=Kt(()=>(x(zi),r(l),F(()=>zi(r(l))))),f=b=>{U(b,NO())},h=Kt(()=>(x(Wf),r(l),F(()=>Wf(r(l))))),p=b=>{var k=RO(),E=I(k),O=A=>{un(A,{get data(){return r(l),F(()=>r(l).icon)}})};be(E,A=>{r(l),F(()=>r(l).icon)&&A(O)});var w=Y(E,2),_=A=>{var q=oo();Le(()=>xt(q,(r(l),F(()=>r(l).text)))),U(A,q)};be(w,A=>{r(l),F(()=>r(l).text)&&A(_)}),Le(()=>{var A;Bt(k,1,"jse-button ".concat((r(l),(A=F(()=>r(l).className))!==null&&A!==void 0?A:"")),"svelte-3erbu0"),Tn(k,"title",(r(l),F(()=>r(l).title))),k.disabled=(r(l),F(()=>r(l).disabled||!1))}),ze("click",k,function(){for(var A,q=arguments.length,C=new Array(q),z=0;z<q;z++)C[z]=arguments[z];(A=r(l).onClick)===null||A===void 0||A.apply(this,C)}),U(b,k)},y=Kt(()=>(x(ei),r(l),F(()=>ei(r(l))))),j=b=>{var k=oo();Le(E=>xt(k,E),[()=>(r(l),F(()=>function(E){return console.error("Unknown type of menu item",E),"???"}(r(l))))]),U(b,k)};be(u,b=>{r(v)?b(d):r(h)?b(f,1):r(y)?b(p,2):b(j,-1)}),U(s,c)}),Sr(Y(a,2),t,"right",{},null),U(e,o),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-json-repair-component.svelte-16jv58j {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: var(--jse-background-color, #fff);
  color: var(--jse-text-color, #4d4d4d);
}
.jse-json-repair-component.svelte-16jv58j .jse-info:where(.svelte-16jv58j) {
  padding: calc(0.5 * var(--jse-padding, 10px));
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  vertical-align: center;
}
.jse-json-repair-component.svelte-16jv58j .jse-json-text:where(.svelte-16jv58j) {
  flex: 1;
  border: none;
  padding: 2px;
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  background: var(--jse-input-background, var(--jse-background-color, #fff));
  color: var(--jse-text-color, #4d4d4d);
  resize: none;
  outline: none;
}`);var qO=re('<div slot="left" class="jse-info svelte-16jv58j">Repair invalid JSON, then click apply</div>'),DO=re('<div class="jse-json-repair-component svelte-16jv58j"><!> <!> <textarea class="jse-json-text svelte-16jv58j" autocomplete="off" autocapitalize="off" spellcheck="false"></textarea></div>');function LO(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),i=R(void 0,!0),a=R(void 0,!0),s=R(void 0,!0),l=R(void 0,!0),c=m(t,"text",13,""),u=m(t,"readOnly",9,!1),d=m(t,"onParse",9),v=m(t,"onRepair",9),f=m(t,"onChange",9,void 0),h=m(t,"onApply",9),p=m(t,"onCancel",9),y=Zr("jsoneditor:JSONRepair"),j=R(void 0,!0);function b(){if(r(j)&&r(n)){var D=r(n).position!==void 0?r(n).position:0;r(j).setSelectionRange(D,D),r(j).focus()}}function k(){h()(c())}function E(){try{c(v()(c())),f()&&f()(c())}catch{}}var O=R(void 0,!0);ne(()=>x(c()),()=>{g(n,function(D){try{return void d()(D)}catch(H){return $l(D,H.message)}}(c()))}),ne(()=>x(c()),()=>{g(o,function(D){try{return v()(D),!0}catch{return!1}}(c()))}),ne(()=>r(n),()=>{y("error",r(n))}),ne(()=>x(p()),()=>{g(O,[{type:"space"},{type:"button",icon:Hd,title:"Cancel repair",className:"jse-cancel",onClick:p()}])}),ne(()=>Pg,()=>{g(i,{icon:Pg,text:"Show me",title:"Scroll to the error location",onClick:b})}),ne(()=>Yi,()=>{g(a,{icon:Yi,text:"Auto repair",title:"Automatically repair JSON",onClick:E})}),ne(()=>(r(o),r(i),r(a)),()=>{g(s,r(o)?[r(i),r(a)]:[r(i)])}),ne(()=>x(u()),()=>{g(l,[{icon:Ap,text:"Apply",title:"Apply fixed JSON",disabled:u(),onClick:k}])}),Mn(),Ft(!0);var w=DO(),_=I(w);av(_,{get items(){return r(O)},$$slots:{left:(D,H)=>{U(D,qO())}}});var A=Y(_,2),q=D=>{var H=nt(()=>(r(n),F(()=>"Cannot parse JSON: ".concat(r(n).message))));Fo(D,{type:"error",get icon(){return $s},get message(){return r(H)},get actions(){return r(s)}})},C=D=>{Fo(D,{type:"success",message:"JSON is valid now and can be parsed.",get actions(){return r(l)}})};be(A,D=>{r(n)?D(q):D(C,-1)});var z=Y(A,2);or(z,D=>g(j,D),()=>r(j)),Le(()=>{z.readOnly=u(),Ps(z,c())}),ze("input",z,function(D){y("handleChange");var H=D.target.value;c()!==H&&(c(H),f()&&f()(c()))}),U(e,w),jt()}function sj(e,t){yt(t,!1);var n=m(t,"text",13),o=m(t,"onParse",9),i=m(t,"onRepair",9),a=m(t,"onApply",9),s=m(t,"onClose",9);function l(u){a()(u),s()()}function c(){s()()}Ft(!0),Dc(e,{get onClose(){return s()},className:"jse-repair-modal",children:(u,d)=>{LO(u,{get onParse(){return o()},get onRepair(){return i()},onApply:l,onCancel:c,get text(){return n()},set text(v){n(v)},$$legacy:!0})},$$slots:{default:!0}}),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
div.jse-collapsed-items.svelte-1v6dhm4 {
  margin-left: calc(var(--level) * var(--jse-indent-size, calc(1em + 4px)));
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  color: var(--jse-collapsed-items-link-color, rgba(0, 0, 0, 0.38));
  padding: calc(0.5 * var(--jse-padding, 10px));
  border: 8px solid transparent;
  border-width: 8px 0;
  background-color: var(--jse-contents-background-color, transparent);
  background-image: linear-gradient(var(--jse-collapsed-items-background-color, #f5f5f5), var(--jse-collapsed-items-background-color, #f5f5f5)), linear-gradient(to bottom right, transparent 50.5%, var(--jse-collapsed-items-background-color, #f5f5f5) 50.5%), linear-gradient(to bottom left, transparent 50.5%, var(--jse-collapsed-items-background-color, #f5f5f5) 50.5%), linear-gradient(to top right, transparent 50.5%, var(--jse-collapsed-items-background-color, #f5f5f5) 50.5%), linear-gradient(to top left, transparent 50.5%, var(--jse-collapsed-items-background-color, #f5f5f5) 50.5%);
  background-repeat: repeat, repeat-x, repeat-x, repeat-x, repeat-x;
  background-position: 0 0, 8px 0, 8px 0, 8px 100%, 8px 100%;
  background-size: auto auto, 16px 16px, 16px 16px, 16px 16px, 16px 16px;
  background-clip: padding-box, border-box, border-box, border-box, border-box;
  background-origin: padding-box, border-box, border-box, border-box, border-box;
  display: flex;
}
div.jse-collapsed-items.jse-selected.svelte-1v6dhm4 {
  background-color: var(--jse-selection-background-color, #d3d3d3);
  --jse-collapsed-items-background-color: var(--jse-collapsed-items-selected-background-color, #c2c2c2);
}
div.jse-collapsed-items.svelte-1v6dhm4 div.jse-text:where(.svelte-1v6dhm4),
div.jse-collapsed-items.svelte-1v6dhm4 button.jse-expand-items:where(.svelte-1v6dhm4) {
  margin: 0 calc(0.5 * var(--jse-padding, 10px));
}
div.jse-collapsed-items.svelte-1v6dhm4 div.jse-text:where(.svelte-1v6dhm4) {
  display: inline;
}
div.jse-collapsed-items.svelte-1v6dhm4 button.jse-expand-items:where(.svelte-1v6dhm4) {
  font-family: inherit;
  font-size: inherit;
  color: var(--jse-collapsed-items-link-color, rgba(0, 0, 0, 0.38));
  background: none;
  border: none;
  padding: 0;
  text-decoration: underline;
  cursor: pointer;
}
div.jse-collapsed-items.svelte-1v6dhm4 button.jse-expand-items:where(.svelte-1v6dhm4):hover, div.jse-collapsed-items.svelte-1v6dhm4 button.jse-expand-items:where(.svelte-1v6dhm4):focus {
  color: var(--jse-collapsed-items-link-color-highlight, #ee5341);
}`);var UO=re('<button type="button" class="jse-expand-items svelte-1v6dhm4"> </button>'),BO=re('<div role="none"><div><div class="jse-text svelte-1v6dhm4"> </div> <!></div></div>');function FO(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),i=R(void 0,!0),a=R(void 0,!0),s=R(void 0,!0),l=m(t,"visibleSections",9),c=m(t,"sectionIndex",9),u=m(t,"total",9),d=m(t,"path",9),v=m(t,"selection",9),f=m(t,"onExpandSection",9),h=m(t,"context",9);ne(()=>(x(l()),x(c())),()=>{g(n,l()[c()])}),ne(()=>r(n),()=>{g(o,r(n).end)}),ne(()=>(x(l()),x(c()),x(u())),()=>{g(i,l()[c()+1]?l()[c()+1].start:u())}),ne(()=>(x(h()),x(v()),x(d()),r(o)),()=>{g(a,Rc(h().getJson(),v(),d().concat(String(r(o)))))}),ne(()=>(r(o),r(i)),()=>{g(s,function(O,w){var _={start:O,end:Math.min(Ff(O),w)},A=Math.max(hd((O+w)/2),O),q={start:A,end:Math.min(Ff(A),w)},C=hd(w),z=C===w?C-Ac:C,D={start:Math.max(z,O),end:w},H=[_],Q=q.start>=_.end&&q.end<=D.start;return Q&&H.push(q),D.start>=(Q?q.end:_.end)&&H.push(D),H}(r(o),r(i)))}),Mn(),Ft(!0);var p,y,j=BO(),b=I(j),k=I(b),E=I(k);Or(Y(k,2),1,()=>r(s),Pr,(O,w)=>{var _=UO(),A=I(_);Le(()=>{var q,C;return xt(A,"show ".concat((r(w),(q=F(()=>r(w).start))!==null&&q!==void 0?q:""),"-").concat((r(w),(C=F(()=>r(w).end))!==null&&C!==void 0?C:"")))}),ze("click",_,()=>f()(d(),r(w))),U(O,_)}),Le(()=>{var O,w;p=Bt(j,1,"jse-collapsed-items svelte-1v6dhm4",null,p,{"jse-selected":r(a)}),y=ea(j,"",y,{"--level":(x(d()),F(()=>d().length+2))}),xt(E,"Items ".concat((O=r(o))!==null&&O!==void 0?O:"","-").concat((w=r(i))!==null&&w!==void 0?w:""))}),ze("mousemove",j,function(O){O.stopPropagation()}),U(e,j),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-context-menu-pointer.svelte-10ijtzr {
  position: absolute;
  top: calc(-0.5 * var(--jse-context-menu-pointer-size, calc(1em + 4px)));
  right: calc(-0.5 * var(--jse-context-menu-pointer-size, calc(1em + 4px)));
  width: var(--jse-context-menu-pointer-size, calc(1em + 4px));
  height: var(--jse-context-menu-pointer-size, calc(1em + 4px));
  padding: 0;
  margin: 0;
  cursor: pointer;
  background: transparent;
  border-radius: 2px;
  background: var(--jse-context-menu-pointer-hover-background, #b2b2b2);
  color: var(--jse-context-menu-pointer-color, var(--jse-context-menu-color, var(--jse-text-color-inverse, #fff)));
  border: none;
  box-shadow: var(--jse-controls-box-shadow, 0 2px 6px 0 rgba(0, 0, 0, 0.24));
}
.jse-context-menu-pointer.jse-root.svelte-10ijtzr {
  top: 0;
  right: calc(-2px - var(--jse-context-menu-pointer-size, calc(1em + 4px)));
}
.jse-context-menu-pointer.jse-insert.svelte-10ijtzr {
  right: -1px;
}
.jse-context-menu-pointer.svelte-10ijtzr:hover {
  background: var(--jse-context-menu-pointer-background-highlight, var(--jse-context-menu-background-highlight, #7a7a7a));
}
.jse-context-menu-pointer.jse-selected.svelte-10ijtzr {
  background: var(--jse-context-menu-pointer-background, var(--jse-context-menu-background, #656565));
}
.jse-context-menu-pointer.jse-selected.svelte-10ijtzr:hover {
  background: var(--jse-context-menu-pointer-background-highlight, var(--jse-context-menu-background-highlight, #7a7a7a));
}`);var WO=re('<button type="button"><!></button>');function Mi(e,t){yt(t,!1);var n=m(t,"root",9,!1),o=m(t,"insert",9,!1),i=m(t,"selected",9),a=m(t,"onContextMenu",9);Ft(!0);var s,l=WO();un(I(l),{get data(){return di}}),Le(()=>{s=Bt(l,1,"jse-context-menu-pointer svelte-10ijtzr",null,s,{"jse-root":n(),"jse-insert":o(),"jse-selected":i()}),Tn(l,"title",Zp)}),ze("click",l,function(c){for(var u=c.target;u&&u.nodeName!=="BUTTON";)u=u.parentNode;u&&a()({anchor:u,left:0,top:0,width:ri,height:ni,offsetTop:2,offsetLeft:0,showTip:!0})}),U(e,l),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-key.svelte-1n4cez4 {
  display: inline-block;
  min-width: 2em;
  padding: 0 5px;
  box-sizing: border-box;
  outline: none;
  border-radius: 1px;
  vertical-align: top;
  color: var(--jse-key-color, #1a1a1a);
  word-break: normal;
  overflow-wrap: normal;
  white-space: pre-wrap;
}
.jse-key.jse-empty.svelte-1n4cez4 {
  min-width: 3em;
  outline: 1px dotted var(--jse-tag-background, rgba(0, 0, 0, 0.2));
  -moz-outline-radius: 2px;
}
.jse-key.jse-empty.svelte-1n4cez4::after {
  pointer-events: none;
  color: var(--jse-tag-background, rgba(0, 0, 0, 0.2));
  content: "key";
}`);var VO=re('<div role="none" data-type="selectable-key"><!></div>'),JO=re("<!> <!>",1),HO=re('<div role="button" tabindex="-1" class="jse-value" data-type="selectable-value"></div>');function lj(e,t){yt(t,!0);var n=Kt(()=>bn(t.selection)&&Kr(t.selection)),o=Kt(()=>t.context.onRenderValue({path:t.path,value:t.value,mode:t.context.mode,truncateTextSize:t.context.truncateTextSize,readOnly:t.context.readOnly,enforceString:t.enforceString,isEditing:r(n),parser:t.context.parser,normalization:t.context.normalization,selection:t.selection,searchResultItems:t.searchResultItems,onPatch:t.context.onPatch,onPasteJson:t.context.onPasteJson,onSelect:t.context.onSelect,onFind:t.context.onFind,findNextInside:t.context.findNextInside,focus:t.context.focus})),i=br();Or(Mt(i),17,()=>r(o),Pr,(a,s)=>{var l=br(),c=Mt(l),u=f=>{var h=Kt(()=>r(s).action),p=HO();go(p,(y,j)=>{var b;return(b=r(h))===null||b===void 0?void 0:b(y,j)},()=>r(s).props),U(f,p)},d=Kt(()=>d5(r(s))),v=f=>{var h=Kt(()=>r(s).component),p=br();dy(Mt(p),()=>r(h),(y,j)=>{j(y,Hi(()=>r(s).props))}),U(f,p)};be(c,f=>{r(d)?f(u):f(v,-1)}),U(a,l)}),U(e,i),jt()}var QO={selecting:!1,selectionAnchor:void 0,selectionAnchorType:void 0,selectionFocus:void 0,dragging:!1};function ef(e){var{json:t,selection:n,deltaY:o,items:i}=e;if(!n)return{operations:void 0,updatedSelection:void 0,offset:0};var a=o<0?function(d){for(var{json:v,items:f,selection:h,deltaY:p}=d,y=oi(v,h),j=f.findIndex(_=>Gt(_.path,y)),b=()=>{var _;return(_=f[k-1])===null||_===void 0?void 0:_.height},k=j,E=0;b()!==void 0&&Math.abs(p)>E+b()/2;)E+=b(),k-=1;var O=f[k].path,w=k-j;return k!==j&&f[k]!==void 0?{beforePath:O,offset:w}:void 0}({json:t,selection:n,deltaY:o,items:i}):function(d){for(var v,{json:f,items:h,selection:p,deltaY:y}=d,j=Ki(f,p),b=h.findIndex(z=>Gt(z.path,j)),k=0,E=b,O=()=>{var z;return(z=h[E+1])===null||z===void 0?void 0:z.height};O()!==void 0&&Math.abs(y)>k+O()/2;)k+=O(),E+=1;var w=cn(j),_=tt(f,w),A=Array.isArray(_)?E:E+1,q=(v=h[A])===null||v===void 0?void 0:v.path,C=E-b;return q?{beforePath:q,offset:C}:{append:!0,offset:C}}({json:t,selection:n,deltaY:o,items:i});if(!a||a.offset===0)return{operations:void 0,updatedSelection:void 0,offset:0};var s=function(d,v,f){if(!v)return[];var h="beforePath"in f?f.beforePath:void 0,p="append"in f?f.append:void 0,y=cn(st(v)),j=tt(d,y);if(!(p||h&&Ra(h,y)&&h.length>y.length))return[];var b=oi(d,v),k=Ki(d,v),E=Xt(b),O=Xt(k),w=h?h[y.length]:void 0;if(!$r(j)){if(Cr(j)){var _=lo(E),A=lo(O),q=w!==void 0?lo(w):j.length;return gS(A-_+1,q<_?Q=>({op:"move",from:wt(y.concat(String(_+Q))),path:wt(y.concat(String(q+Q)))}):()=>({op:"move",from:wt(y.concat(String(_))),path:wt(y.concat(String(q)))}))}throw new Error("Cannot create move operations: parent must be an Object or Array")}var C=Object.keys(j),z=C.indexOf(E),D=C.indexOf(O),H=p?C.length:w!==void 0?C.indexOf(w):-1;return z!==-1&&D!==-1&&H!==-1?H>z?[...C.slice(z,D+1),...C.slice(H,C.length)].map(Q=>ns(y,Q)):[...C.slice(H,z),...C.slice(D+1,C.length)].map(Q=>ns(y,Q)):[]}(t,n,a),l=cn(oi(t,n)),c=tt(t,l);if(Array.isArray(c)){var u=function(d){var v,f,{items:h,json:p,selection:y,offset:j}=d,b=oi(p,y),k=Ki(p,y),E=h.findIndex(A=>Gt(A.path,b)),O=h.findIndex(A=>Gt(A.path,k)),w=(v=h[E+j])===null||v===void 0?void 0:v.path,_=(f=h[O+j])===null||f===void 0?void 0:f.path;return po(w,_)}({items:i,json:t,selection:n,offset:a.offset});return{operations:s,updatedSelection:u,offset:a.offset}}return{operations:s,updatedSelection:void 0,offset:a.offset}}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
button.jse-validation-error.svelte-q6a061 {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  padding: 0;
  margin: 0;
  vertical-align: top;
  display: inline-flex;
  color: var(--jse-error-color, #ee5341);
}

button.jse-validation-info.svelte-q6a061 {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  padding: 0;
  margin: 0;
  vertical-align: top;
  display: inline-flex;
  color: var(--jse-info-color, #4f91ff);
}

button.jse-validation-warning.svelte-q6a061 {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  padding: 0;
  margin: 0;
  vertical-align: top;
  display: inline-flex;
  color: var(--jse-warning-color, #fdc539);
}`);var KO=re('<button type="button"><!></button>');function xl(e,t){yt(t,!1);var n=R(),o=rs("absolute-popup"),i=m(t,"validationError",8),a=m(t,"onExpand",8);ne(()=>x(i()),()=>{g(n,u5(i())&&i().isChildError?"Contains invalid data":i().message)}),Mn(),Ft();var s=KO();un(I(s),{get data(){return $s}}),so(()=>ze("click",s,function(){for(var l,c=arguments.length,u=new Array(c),d=0;d<c;d++)u[d]=arguments[d];(l=a())===null||l===void 0||l.apply(this,u)})),go(s,(l,c)=>Nl==null?void 0:Nl(l,c),()=>De({text:r(n)},o)),Le(()=>{var l;return Bt(s,1,"jse-validation-".concat((x(i()),(l=F(()=>i().severity))!==null&&l!==void 0?l:"")),"svelte-q6a061")}),U(e,s),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-expand.svelte-1qi6rc1 {
  width: var(--jse-indent-size, calc(1em + 4px));
  padding: 0;
  margin: 0;
  border: none;
  cursor: pointer;
  background: transparent;
  color: var(--jse-delimiter-color, rgba(0, 0, 0, 0.38));
  font-size: var(--jse-font-size-mono, 14px);
  height: var(--jse-line-height, calc(1em + 4px));
}
.jse-expand.svelte-1qi6rc1:hover {
  opacity: 0.8;
}

.jse-meta.svelte-1qi6rc1,
.jse-separator.svelte-1qi6rc1,
.jse-index.svelte-1qi6rc1,
.jse-bracket.svelte-1qi6rc1 {
  vertical-align: top;
  color: var(--jse-delimiter-color, rgba(0, 0, 0, 0.38));
}

.jse-index.svelte-1qi6rc1 {
  padding: 0 calc(0.5 * var(--jse-padding, 10px));
}

.jse-bracket.svelte-1qi6rc1 {
  padding: 0 2px;
}
.jse-bracket.jse-expanded.svelte-1qi6rc1 {
  padding-right: var(--jse-padding, 10px);
}

.jse-identifier.svelte-1qi6rc1 {
  vertical-align: top;
  position: relative;
}

.jse-json-node.svelte-1qi6rc1 {
  position: relative;
  color: var(--jse-text-color, #4d4d4d);
}
.jse-json-node.jse-root.svelte-1qi6rc1 {
  min-height: 100%;
  padding-bottom: 2px;
  box-sizing: border-box;
}
.jse-json-node.jse-root.svelte-1qi6rc1 > .jse-contents-outer:where(.svelte-1qi6rc1) > .jse-contents:where(.svelte-1qi6rc1) {
  padding-left: 0;
}
.jse-json-node.svelte-1qi6rc1 .jse-props:where(.svelte-1qi6rc1),
.jse-json-node.svelte-1qi6rc1 .jse-items:where(.svelte-1qi6rc1) {
  position: relative;
}
.jse-json-node.svelte-1qi6rc1 .jse-header-outer:where(.svelte-1qi6rc1),
.jse-json-node.svelte-1qi6rc1 .jse-footer-outer:where(.svelte-1qi6rc1) {
  display: flex;
  margin-left: calc(var(--level) * var(--jse-indent-size, calc(1em + 4px)));
}
.jse-json-node.svelte-1qi6rc1 .jse-header:where(.svelte-1qi6rc1) {
  position: relative;
}
.jse-json-node.svelte-1qi6rc1 .jse-header:where(.svelte-1qi6rc1) .jse-meta:where(.svelte-1qi6rc1) > .jse-meta-inner:where(.svelte-1qi6rc1) {
  display: flex;
  justify-content: center;
}
.jse-json-node.svelte-1qi6rc1 .jse-contents-outer:where(.svelte-1qi6rc1) {
  display: flex;
  margin-left: calc(var(--level) * var(--jse-indent-size, calc(1em + 4px)));
}
.jse-json-node.svelte-1qi6rc1 .jse-header:where(.svelte-1qi6rc1),
.jse-json-node.svelte-1qi6rc1 .jse-contents:where(.svelte-1qi6rc1) {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}
.jse-json-node.svelte-1qi6rc1 .jse-contents:where(.svelte-1qi6rc1) {
  padding-left: var(--jse-indent-size, calc(1em + 4px));
  cursor: var(--jse-contents-cursor, pointer);
}
.jse-json-node.svelte-1qi6rc1 .jse-contents:where(.svelte-1qi6rc1) .jse-value-outer:where(.svelte-1qi6rc1) {
  display: inline-flex;
}
.jse-json-node.svelte-1qi6rc1 .jse-footer:where(.svelte-1qi6rc1) {
  display: inline-flex;
  padding-left: calc(var(--jse-indent-size, calc(1em + 4px)) + 5px);
}
.jse-json-node.svelte-1qi6rc1 .jse-header:where(.svelte-1qi6rc1),
.jse-json-node.svelte-1qi6rc1 .jse-contents:where(.svelte-1qi6rc1),
.jse-json-node.svelte-1qi6rc1 .jse-footer:where(.svelte-1qi6rc1) {
  background: var(--jse-contents-background-color, transparent);
}
.jse-json-node.svelte-1qi6rc1 .jse-insert-selection-area:where(.svelte-1qi6rc1) {
  padding: 0 calc(0.5 * var(--jse-padding, 10px));
  flex: 1;
}
.jse-json-node.svelte-1qi6rc1 .jse-insert-selection-area.jse-inside:where(.svelte-1qi6rc1) {
  display: inline-flex;
  align-items: center;
}
.jse-json-node.svelte-1qi6rc1 .jse-insert-selection-area.jse-after:where(.svelte-1qi6rc1) {
  display: flex;
  align-items: flex-end;
}
.jse-json-node.svelte-1qi6rc1 .jse-context-menu-pointer-anchor:where(.svelte-1qi6rc1) {
  position: relative;
}
.jse-json-node.svelte-1qi6rc1 .jse-insert-area:where(.svelte-1qi6rc1) {
  display: flex;
  position: relative;
  z-index: 1;
  margin-left: calc(var(--level) * var(--jse-indent-size, calc(1em + 4px)));
  max-width: 250px;
  min-width: 100px;
  height: 0;
  margin-right: calc(0.5 * var(--jse-padding, 10px));
  outline: 1px solid;
}
.jse-json-node.svelte-1qi6rc1 .jse-insert-area.jse-hovered:where(.svelte-1qi6rc1) {
  outline-color: var(--jse-context-menu-pointer-hover-background, #b2b2b2);
}
.jse-json-node.svelte-1qi6rc1 .jse-key-outer:where(.svelte-1qi6rc1) {
  position: relative;
}
.jse-json-node.svelte-1qi6rc1 .jse-key-outer:where(.svelte-1qi6rc1):hover,
.jse-json-node.svelte-1qi6rc1 .jse-value-outer:where(.svelte-1qi6rc1):hover,
.jse-json-node.svelte-1qi6rc1 .jse-meta:where(.svelte-1qi6rc1):hover,
.jse-json-node.svelte-1qi6rc1 .jse-footer:where(.svelte-1qi6rc1):hover {
  background: var(--jse-hover-background-color, rgba(0, 0, 0, 0.06));
  cursor: var(--jse-contents-cursor, pointer);
}
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-meta,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-items .jse-header,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-items .jse-contents,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-props .jse-header,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-props .jse-contents,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-footer {
  background: var(--jse-hover-background-color, rgba(0, 0, 0, 0.06));
  cursor: var(--jse-contents-cursor, pointer);
}
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-value-outer .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-value-outer .jse-meta,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-meta .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-meta .jse-meta,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-items .jse-header .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-items .jse-header .jse-meta,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-items .jse-contents .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-items .jse-contents .jse-meta,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-props .jse-header .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-props .jse-header .jse-meta,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-props .jse-contents .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-props .jse-contents .jse-meta,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-footer .jse-value-outer,
.jse-json-node.jse-hovered.svelte-1qi6rc1:not(.jse-selected):not(.jse-selected-value) .jse-footer .jse-meta {
  background: none;
}
.jse-json-node.jse-selected.svelte-1qi6rc1 .jse-header:where(.svelte-1qi6rc1),
.jse-json-node.jse-selected.svelte-1qi6rc1 .jse-contents:where(.svelte-1qi6rc1),
.jse-json-node.jse-selected.svelte-1qi6rc1 .jse-footer:where(.svelte-1qi6rc1) {
  background: var(--jse-selection-background-color, #d3d3d3);
  cursor: var(--jse-contents-selected-cursor, grab);
}
.jse-json-node.jse-selected.svelte-1qi6rc1 .jse-key-outer:where(.svelte-1qi6rc1):hover,
.jse-json-node.jse-selected.svelte-1qi6rc1 .jse-value-outer:where(.svelte-1qi6rc1):hover,
.jse-json-node.jse-selected.svelte-1qi6rc1 .jse-meta:where(.svelte-1qi6rc1):hover,
.jse-json-node.jse-selected.svelte-1qi6rc1 .jse-footer:where(.svelte-1qi6rc1):hover {
  background: inherit;
  cursor: inherit;
}
.jse-json-node.svelte-1qi6rc1 .jse-key-outer.jse-selected-key:where(.svelte-1qi6rc1) {
  background: var(--jse-selection-background-color, #d3d3d3);
  cursor: var(--jse-contents-selected-cursor, grab);
}
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-value-outer,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-meta,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-items .jse-header,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-items .jse-contents,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-props .jse-header,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-props .jse-contents,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-footer {
  background: var(--jse-selection-background-color, #d3d3d3);
  cursor: var(--jse-contents-selected-cursor, grab);
}
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-value-outer .jse-key-outer:hover,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-meta .jse-key-outer:hover,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-items .jse-header .jse-key-outer:hover,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-items .jse-contents .jse-key-outer:hover,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-props .jse-header .jse-key-outer:hover,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-props .jse-contents .jse-key-outer:hover,
.jse-json-node.jse-selected-value.svelte-1qi6rc1 .jse-footer .jse-key-outer:hover {
  background: inherit;
  cursor: inherit;
}
.jse-json-node.jse-readonly.svelte-1qi6rc1 {
  --jse-contents-selected-cursor: pointer;
}
.jse-json-node.svelte-1qi6rc1 .jse-insert-area.jse-selected:where(.svelte-1qi6rc1) {
  outline-color: var(--jse-context-menu-pointer-background, var(--jse-context-menu-background, #656565));
}`);var nr=Yd(()=>QO),GO=re('<div class="jse-separator svelte-1qi6rc1">:</div>'),YO=re('<div class="jse-bracket svelte-1qi6rc1">[</div> <!> &nbsp;',1),XO=re('<div class="jse-bracket svelte-1qi6rc1">[</div> <!> <div class="jse-bracket svelte-1qi6rc1">]</div>',1),ZO=re('<div class="jse-context-menu-pointer-anchor svelte-1qi6rc1"><!></div>'),e_=re('<div role="none" class="jse-insert-selection-area jse-inside svelte-1qi6rc1" data-type="insert-selection-area-inside"></div>'),t_=re('<div role="none" class="jse-insert-selection-area jse-after svelte-1qi6rc1" data-type="insert-selection-area-after"></div>'),n_=re('<div data-type="insert-selection-area-inside"><!></div>'),r_=re('<div slot="identifier" class="jse-identifier svelte-1qi6rc1"><div class="jse-index svelte-1qi6rc1"> </div></div>'),o_=re("<!> <!>",1),a_=re('<div role="none" class="jse-insert-selection-area jse-after svelte-1qi6rc1" data-type="insert-selection-area-after"></div>'),i_=re('<div class="jse-items svelte-1qi6rc1"><!> <!></div> <div class="jse-footer-outer svelte-1qi6rc1"><div data-type="selectable-value" class="jse-footer svelte-1qi6rc1"><span class="jse-bracket svelte-1qi6rc1">]</span></div> <!></div>',1),s_=re('<div class="jse-header-outer svelte-1qi6rc1"><div class="jse-header svelte-1qi6rc1"><button type="button" class="jse-expand svelte-1qi6rc1" title="Expand or collapse this array (Ctrl+Click to expand/collapse recursively)"><!></button> <!> <!> <div class="jse-meta svelte-1qi6rc1"><div class="jse-meta-inner svelte-1qi6rc1" data-type="selectable-value"><!></div></div> <!></div> <!> <!></div> <!>',1),l_=re('<div class="jse-separator svelte-1qi6rc1">:</div>'),c_=re('<div class="jse-bracket jse-expanded svelte-1qi6rc1">&lbrace;</div>'),u_=re('<div class="jse-bracket svelte-1qi6rc1">&lbrace;</div> <!> <div class="jse-bracket svelte-1qi6rc1">&rbrace;</div>',1),d_=re('<div class="jse-context-menu-pointer-anchor svelte-1qi6rc1"><!></div>'),v_=re('<div role="none" class="jse-insert-selection-area jse-inside svelte-1qi6rc1" data-type="insert-selection-area-inside"></div>'),f_=re('<div role="none" class="jse-insert-selection-area jse-after svelte-1qi6rc1" data-type="insert-selection-area-after"></div>'),p_=re('<div data-type="insert-selection-area-inside"><!></div>'),h_=re('<div slot="identifier"><!></div>'),g_=re('<div role="none" class="jse-insert-selection-area jse-after svelte-1qi6rc1" data-type="insert-selection-area-after"></div>'),m_=re('<div class="jse-props svelte-1qi6rc1"><!> <!></div> <div class="jse-footer-outer svelte-1qi6rc1"><div data-type="selectable-value" class="jse-footer svelte-1qi6rc1"><div class="jse-bracket svelte-1qi6rc1">&rbrace;</div></div> <!></div>',1),b_=re('<div class="jse-header-outer svelte-1qi6rc1"><div class="jse-header svelte-1qi6rc1"><button type="button" class="jse-expand svelte-1qi6rc1" title="Expand or collapse this object (Ctrl+Click to expand/collapse recursively)"><!></button> <!> <!> <div class="jse-meta svelte-1qi6rc1" data-type="selectable-value"><div class="jse-meta-inner svelte-1qi6rc1"><!></div></div> <!></div> <!> <!></div> <!>',1),y_=re('<div class="jse-separator svelte-1qi6rc1">:</div>'),j_=re('<div class="jse-context-menu-pointer-anchor svelte-1qi6rc1"><!></div>'),x_=re('<div role="none" class="jse-insert-selection-area jse-after svelte-1qi6rc1" data-type="insert-selection-area-after"></div>'),w_=re('<div class="jse-contents-outer svelte-1qi6rc1"><div class="jse-contents svelte-1qi6rc1"><!> <!> <div class="jse-value-outer svelte-1qi6rc1"><!></div> <!></div> <!> <!></div>'),k_=re('<div data-type="insert-selection-area-after"><!></div>'),S_=re('<div role="treeitem" tabindex="-1"><!> <!></div>');function tp(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),i=m(t,"pointer",9),a=m(t,"value",9),s=m(t,"state",9),l=m(t,"validationErrors",9),c=m(t,"searchResults",9),u=m(t,"selection",9),d=m(t,"context",9),v=m(t,"onDragSelectionStart",9),f=Zr("jsoneditor:JSONNode"),h=R(void 0,!0),p=void 0,y=R(void 0,!0),j=R(void 0,!0),b=R(void 0,!0),k=R(void 0,!0),E=R(void 0,!0),O=R(void 0,!0),w=R(void 0,!0);function _(X){X.stopPropagation();var B=Xp(X);d().onExpand(r(j),!r(b),B)}function A(){d().onExpand(r(j),!0)}function q(X,B){var Ne=au(r(j),Object.keys(a()),X,B);return d().onPatch(Ne),Xt(Mo(Ne[0].path))}function C(X){d().onDrag(X)}function z(X){nr().selecting&&(nr(nr().selecting=!1),X.stopPropagation()),d().onDragEnd(),document.removeEventListener("mousemove",C,!0),document.removeEventListener("mouseup",z)}function D(){var X;return((X=d().findElement([]))===null||X===void 0||(X=X.getBoundingClientRect())===null||X===void 0?void 0:X.top)||0}function H(X,B){var Ne=D()-X.initialContentTop;return B.clientY-X.initialClientY-Ne}function Q(X){if(!d().readOnly&&u()){var B=cn(st(u()));if(Gt(r(j),B)){var Ne=function(_e,at){var We=[];function Ye(de){var Me=r(j).concat(de),pe=d().findElement(Me);pe!==void 0&&We.push({path:Me,height:pe.clientHeight})}if(Array.isArray(a())){var Tt=d().getJson();if(Tt===void 0)return;var He=oi(Tt,_e),qt=Ki(Tt,_e),S=parseInt(Xt(He),10),$=parseInt(Xt(qt),10),N=at.find(de=>S>=de.start&&$<=de.end);if(!N)return;var{start:G,end:W}=N;my(G,Math.min(a().length,W),de=>Ye(String(de)))}else Object.keys(a()).forEach(Ye);return We}(u(),r(E)||bl);if(f("dragSelectionStart",{selection:u(),items:Ne}),Ne){var ee=d().getJson();if(ee!==void 0){var L=oi(ee,u()),pt=Ne.findIndex(_e=>Gt(_e.path,L)),{offset:ht}=ef({json:ee,selection:d().getSelection(),deltaY:0,items:Ne});g(y,{initialTarget:X.target,initialClientY:X.clientY,initialContentTop:D(),selectionStartIndex:pt,selectionItemsCount:ts(ee,u()).length,items:Ne,offset:ht,didMoveItems:!1}),nr(nr().dragging=!0),document.addEventListener("mousemove",fe,!0),document.addEventListener("mouseup",Ie)}}else f("Cannot drag the current selection (probably spread over multiple sections)")}else v()(X)}}function fe(X){if(r(y)){var B=d().getJson();if(B===void 0)return;var Ne=H(r(y),X),{offset:ee}=ef({json:B,selection:d().getSelection(),deltaY:Ne,items:r(y).items});ee!==r(y).offset&&(f("drag selection",ee,Ne),g(y,De(De({},r(y)),{},{offset:ee,didMoveItems:!0})))}}function Ie(X){if(r(y)){var B=d().getJson();if(B===void 0)return;var Ne=H(r(y),X),{operations:ee,updatedSelection:L}=ef({json:B,selection:d().getSelection(),deltaY:Ne,items:r(y).items});if(ee)d().onPatch(ee,(_e,at)=>({state:at,selection:L??u()}));else if(X.target===r(y).initialTarget&&!r(y).didMoveItems){var pt=Uv(X.target),ht=Ty(X.target);ht&&d().onSelect(Pm(pt,ht))}g(y,void 0),nr(nr().dragging=!1),document.removeEventListener("mousemove",fe,!0),document.removeEventListener("mouseup",Ie)}}function ge(X){X.shiftKey||(X.stopPropagation(),X.preventDefault(),d().onSelect(mi(r(j))))}function qe(X){X.shiftKey||(X.stopPropagation(),X.preventDefault(),d().onSelect(ci(r(j))))}function ce(X){d().onSelect(mi(r(j))),Xn(),d().onContextMenu(X)}function ve(X){d().onSelect(ci(r(j))),Xn(),d().onContextMenu(X)}ne(()=>x(i()),()=>{g(j,Mo(i()))}),ne(()=>x(i()),()=>{g(n,encodeURIComponent(i()))}),ne(()=>x(s()),()=>{g(b,!!Ns(s())&&s().expanded)}),ne(()=>(x(a()),x(s())),()=>{g(k,$a(a(),s(),[]))}),ne(()=>x(s()),()=>{g(E,Gr(s())?s().visibleSections:void 0)}),ne(()=>x(l()),()=>{var X;g(O,(X=l())===null||X===void 0?void 0:X.validationError)}),ne(()=>(x(d()),x(u()),r(j)),()=>{g(w,Rc(d().getJson(),u(),r(j)))}),ne(()=>r(j),()=>{g(o,r(j).length===0)}),Mn(),Ft(!0);var he,Ue,Re=S_(),we=I(Re),ue=X=>{var B=s_(),Ne=Mt(B),ee=I(Ne),L=I(ee),pt=I(L),ht=Ae=>{un(Ae,{get data(){return di}})},_e=Ae=>{un(Ae,{get data(){return _c}})};be(pt,Ae=>{r(b)?Ae(ht):Ae(_e,-1)});var at=Y(L,2);Sr(at,t,"identifier",{},null);var We=Y(at,2),Ye=Ae=>{U(Ae,GO())};be(We,Ae=>{r(o)||Ae(Ye)});var Tt=Y(We,2),He=I(Tt),qt=I(He),S=Ae=>{var $t=YO();Ku(Y(Mt($t),2),{children:(sn,Un)=>{var Yt=oo();Le(()=>{var Zt,Dt;return xt(Yt,"".concat((x(a()),(Zt=F(()=>a().length))!==null&&Zt!==void 0?Zt:""),`
                `).concat((x(a()),(Dt=F(()=>a().length===1?"item":"items"))!==null&&Dt!==void 0?Dt:"")))}),U(sn,Yt)},$$slots:{default:!0}}),U(Ae,$t)},$=Ae=>{var $t=XO();Ku(Y(Mt($t),2),{onclick:A,children:(sn,Un)=>{var Yt=oo();Le(()=>{var Zt,Dt;return xt(Yt,"".concat((x(a()),(Zt=F(()=>a().length))!==null&&Zt!==void 0?Zt:""),`
                `).concat((x(a()),(Dt=F(()=>a().length===1?"item":"items"))!==null&&Dt!==void 0?Dt:"")))}),U(sn,Yt)},$$slots:{default:!0}}),U(Ae,$t)};be(qt,Ae=>{r(b)?Ae(S):Ae($,-1)});var N=Y(Tt,2),G=Ae=>{var $t=ZO();Mi(I($t),{get root(){return r(o)},selected:!0,get onContextMenu(){return x(d()),F(()=>d().onContextMenu)}}),U(Ae,$t)},W=Kt(()=>(x(d()),r(w),x(u()),x(bn),x(Jn),x(Kr),x(Gt),x(st),r(j),F(()=>!d().readOnly&&r(w)&&u()&&(bn(u())||Jn(u()))&&!Kr(u())&&Gt(st(u()),r(j)))));be(N,Ae=>{r(W)&&Ae(G)});var de=Y(ee,2),Me=Ae=>{xl(Ae,{get validationError(){return r(O)},onExpand:A})};be(de,Ae=>{r(O),r(b),F(()=>r(O)&&(!r(b)||!r(O).isChildError))&&Ae(Me)});var pe=Y(de,2),le=Ae=>{var $t=e_();ze("click",$t,ge),U(Ae,$t)},St=Ae=>{var $t=t_();ze("click",$t,qe),U(Ae,$t)};be(pe,Ae=>{r(b)?Ae(le):Ae(St,-1)});var lt=Y(Ne,2),Xe=Ae=>{var $t=i_(),sn=Mt($t),Un=I(sn),Yt=J=>{var V,Ve,ye=n_(),rt=I(ye),dt=nt(()=>(r(w),x(Hr),x(u()),F(()=>r(w)&&Hr(u()))));Mi(rt,{insert:!0,get selected(){return r(dt)},onContextMenu:ce}),Le(At=>{V=Bt(ye,1,"jse-insert-area jse-inside svelte-1qi6rc1",null,V,At),Tn(ye,"title",Fv),Ve=ea(ye,"",Ve,{"--level":(r(j),F(()=>r(j).length+1))})},[()=>({"jse-hovered":r(h)===vs,"jse-selected":r(w)&&Hr(u())})]),U(J,ye)},Zt=Kt(()=>(x(d()),r(h),x(vs),r(w),x(Hr),x(u()),F(()=>!d().readOnly&&(r(h)===vs||r(w)&&Hr(u())))));be(Un,J=>{r(Zt)&&J(Yt)}),Or(Y(Un,2),1,()=>r(E)||bl,Pr,(J,V,Ve)=>{var ye=o_(),rt=Mt(ye);Or(rt,1,()=>(x(a()),r(V),r(y),F(()=>function(en,Vt,Ht){var On=Vt.start,dn=Math.min(Vt.end,en.length),Qn=W1(On,dn);return Ht&&Ht.offset!==0?pm(Qn,Ht.selectionStartIndex,Ht.selectionItemsCount,Ht.offset).map((Kn,Bn)=>({index:Kn,gutterIndex:Bn})):Qn.map(Kn=>({index:Kn,gutterIndex:Kn}))}(a(),r(V),r(y)))),en=>en.index,(en,Vt)=>{var Ht=nt(()=>(x(Gr),x(l()),r(Vt),F(()=>Gr(l())?l().items[r(Vt).index]:void 0))),On=nt(()=>(x($u),x(d()),x(u()),r(j),r(Vt),F(()=>$u(d().getJson(),u(),r(j).concat(String(r(Vt).index)))))),dn=br(),Qn=Mt(dn),Kn=nt(()=>(x(uu),x(i()),r(Vt),F(()=>uu(i(),r(Vt).index)))),Bn=nt(()=>(x(Gr),x(s()),r(Vt),F(()=>Gr(s())?s().items[r(Vt).index]:void 0))),Zn=nt(()=>(x(Gr),x(c()),r(Vt),F(()=>Gr(c())?c().items[r(Vt).index]:void 0)));tp(Qn,{get value(){return x(a()),r(Vt),F(()=>a()[r(Vt).index])},get pointer(){return r(Kn)},get state(){return r(Bn)},get validationErrors(){return r(Ht)},get searchResults(){return r(Zn)},get selection(){return r(On)},get context(){return d()},onDragSelectionStart:Q,$$slots:{identifier:(yr,Fn)=>{var $n=r_(),ar=I($n),Se=I(ar);Le(()=>xt(Se,(r(Vt),F(()=>r(Vt).gutterIndex)))),U(yr,$n)}}}),U(en,dn)});var dt=Y(rt,2),At=en=>{var Vt=nt(()=>r(E)||bl);FO(en,{get visibleSections(){return r(Vt)},sectionIndex:Ve,get total(){return x(a()),F(()=>a().length)},get path(){return r(j)},get onExpandSection(){return x(d()),F(()=>d().onExpandSection)},get selection(){return u()},get context(){return d()}})};be(dt,en=>{r(V),x(a()),F(()=>r(V).end<a().length)&&en(At)}),U(J,ye)});var Dt=Y(sn,2),hn=Y(I(Dt),2),Hn=J=>{var V=a_();ze("click",V,qe),U(J,V)};be(hn,J=>{r(o)||J(Hn)}),U(Ae,$t)};be(lt,Ae=>{r(b)&&Ae(Xe)}),ze("click",L,_),U(X,B)},ie=Kt(()=>(x(a()),F(()=>Array.isArray(a())))),vt=X=>{var B=b_(),Ne=Mt(B),ee=I(Ne),L=I(ee),pt=I(L),ht=Ae=>{un(Ae,{get data(){return di}})},_e=Ae=>{un(Ae,{get data(){return _c}})};be(pt,Ae=>{r(b)?Ae(ht):Ae(_e,-1)});var at=Y(L,2);Sr(at,t,"identifier",{},null);var We=Y(at,2),Ye=Ae=>{U(Ae,l_())};be(We,Ae=>{r(o)||Ae(Ye)});var Tt=Y(We,2),He=I(Tt),qt=I(He),S=Ae=>{U(Ae,c_())},$=Ae=>{var $t=u_();Ku(Y(Mt($t),2),{onclick:A,children:(sn,Un)=>{var Yt=oo();Le((Zt,Dt)=>xt(Yt,"".concat(Zt??"",`
                `).concat(Dt??"")),[()=>(x(a()),F(()=>Object.keys(a()).length)),()=>(x(a()),F(()=>Object.keys(a()).length===1?"prop":"props"))]),U(sn,Yt)},$$slots:{default:!0}}),U(Ae,$t)};be(qt,Ae=>{r(b)?Ae(S):Ae($,-1)});var N=Y(Tt,2),G=Ae=>{var $t=d_();Mi(I($t),{get root(){return r(o)},selected:!0,get onContextMenu(){return x(d()),F(()=>d().onContextMenu)}}),U(Ae,$t)},W=Kt(()=>(x(d()),r(w),x(u()),x(bn),x(Jn),x(Kr),x(Gt),x(st),r(j),F(()=>!d().readOnly&&r(w)&&u()&&(bn(u())||Jn(u()))&&!Kr(u())&&Gt(st(u()),r(j)))));be(N,Ae=>{r(W)&&Ae(G)});var de=Y(ee,2),Me=Ae=>{xl(Ae,{get validationError(){return r(O)},onExpand:A})};be(de,Ae=>{r(O),r(b),F(()=>r(O)&&(!r(b)||!r(O).isChildError))&&Ae(Me)});var pe=Y(de,2),le=Ae=>{var $t=v_();ze("click",$t,ge),U(Ae,$t)},St=Ae=>{var $t=f_();ze("click",$t,qe),U(Ae,$t)};be(pe,Ae=>{r(b)?Ae(le):r(o)||Ae(St,1)});var lt=Y(Ne,2),Xe=Ae=>{var $t=m_(),sn=Mt($t),Un=I(sn),Yt=J=>{var V,Ve,ye=p_(),rt=I(ye),dt=nt(()=>(r(w),x(Hr),x(u()),F(()=>r(w)&&Hr(u()))));Mi(rt,{insert:!0,get selected(){return r(dt)},onContextMenu:ce}),Le(At=>{V=Bt(ye,1,"jse-insert-area jse-inside svelte-1qi6rc1",null,V,At),Tn(ye,"title",Fv),Ve=ea(ye,"",Ve,{"--level":(r(j),F(()=>r(j).length+1))})},[()=>({"jse-hovered":r(h)===vs,"jse-selected":r(w)&&Hr(u())})]),U(J,ye)},Zt=Kt(()=>(x(d()),r(h),x(vs),r(w),x(Hr),x(u()),F(()=>!d().readOnly&&(r(h)===vs||r(w)&&Hr(u())))));be(Un,J=>{r(Zt)&&J(Yt)}),Or(Y(Un,2),1,()=>(x(a()),r(y),F(()=>function(J,V){var Ve=Object.keys(J);return V&&V.offset!==0?pm(Ve,V.selectionStartIndex,V.selectionItemsCount,V.offset):Ve}(a(),r(y)))),Pr,(J,V)=>{var Ve=nt(()=>(x(uu),x(i()),r(V),F(()=>uu(i(),r(V))))),ye=nt(()=>(x(Oo),x(c()),r(V),F(()=>Oo(c())?c().properties[r(V)]:void 0))),rt=nt(()=>(x(Oo),x(l()),r(V),F(()=>Oo(l())?l().properties[r(V)]:void 0))),dt=nt(()=>(r(j),r(V),F(()=>r(j).concat(r(V))))),At=nt(()=>(x($u),x(d()),x(u()),x(r(dt)),F(()=>$u(d().getJson(),u(),r(dt))))),en=br(),Vt=Mt(en),Ht=nt(()=>(x(Oo),x(s()),r(V),F(()=>Oo(s())?s().properties[r(V)]:void 0)));tp(Vt,{get value(){return x(a()),r(V),F(()=>a()[r(V)])},get pointer(){return r(Ve)},get state(){return r(Ht)},get validationErrors(){return r(rt)},get searchResults(){return r(ye)},get selection(){return r(At)},get context(){return d()},onDragSelectionStart:Q,$$slots:{identifier:(On,dn)=>{var Qn,Kn=h_(),Bn=I(Kn),Zn=nt(()=>(x(Um),x(r(ye)),F(()=>Um(r(ye)))));(function(yr,Fn){yt(Fn,!1);var $n=R(void 0,!0),ar=R(void 0,!0),Se=m(Fn,"pointer",9),Ee=m(Fn,"key",9),tn=m(Fn,"selection",9),Ar=m(Fn,"searchResultItems",9),jr=m(Fn,"onUpdateKey",9),on=m(Fn,"context",9),dr=R(void 0,!0);function vr(K){r(ar)||on().readOnly||(K.preventDefault(),on().onSelect(lh(r(dr))))}function Br(K,Ce){var P=jr()(Ee(),on().normalization.unescapeValue(K)),Z=cn(r(dr)).concat(P);on().onSelect(Ce===Qi.nextInside?rn(Z):gi(Z)),Ce!==Qi.self&&on().focus()}function eo(){on().onSelect(gi(r(dr))),on().focus()}ne(()=>x(Se()),()=>{g(dr,Mo(Se()))}),ne(()=>(x(tn()),r(dr)),()=>{g($n,Yr(tn())&&Gt(tn().path,r(dr)))}),ne(()=>(r($n),x(tn())),()=>{g(ar,r($n)&&Kr(tn()))}),Mn(),Ft(!0);var zr=JO(),Pn=Mt(zr),yn=K=>{var Ce=nt(()=>(x(on()),x(Ee()),F(()=>on().normalization.escapeValue(Ee())))),P=nt(()=>(x(Kr),x(tn()),F(()=>Kr(tn())?tn().initialValue:void 0)));Ly(K,{get value(){return r(Ce)},get initialValue(){return r(P)},label:"Edit key",shortText:!0,onChange:Br,onCancel:eo,get onFind(){return x(on()),F(()=>on().onFind)}})},Wt=K=>{var Ce,P=VO(),Z=I(P),xe=Qe=>{var Je=nt(()=>(x(on()),x(Ee()),F(()=>on().normalization.escapeValue(Ee()))));Hy(Qe,{get text(){return r(Je)},get searchResultItems(){return Ar()}})},ot=Qe=>{var Je=oo();Le(Lt=>xt(Je,Lt),[()=>(x(Al),x(on()),x(Ee()),F(()=>Al(on().normalization.escapeValue(Ee()))))]),U(Qe,Je)};be(Z,Qe=>{Ar()?Qe(xe):Qe(ot,-1)}),Le(()=>Ce=Bt(P,1,"jse-key svelte-1n4cez4",null,Ce,{"jse-empty":Ee()===""})),ze("dblclick",P,vr),U(K,P)};be(Pn,K=>{x(on()),r(ar),F(()=>!on().readOnly&&r(ar))?K(yn):K(Wt,-1)});var Wn=Y(Pn,2),ir=K=>{Mi(K,{selected:!0,get onContextMenu(){return x(on()),F(()=>on().onContextMenu)}})};be(Wn,K=>{x(on()),r($n),r(ar),F(()=>!on().readOnly&&r($n)&&!r(ar))&&K(ir)}),U(yr,zr),jt()})(Bn,{get pointer(){return r(Ve)},get key(){return r(V)},get selection(){return r(At)},get searchResultItems(){return r(Zn)},get context(){return d()},onUpdateKey:q}),Le(yr=>Qn=Bt(Kn,1,"jse-key-outer svelte-1qi6rc1",null,Qn,yr),[()=>({"jse-selected-key":Yr(r(At))&&Gt(r(At).path,r(dt))})]),U(On,Kn)}}}),U(J,en)});var Dt=Y(sn,2),hn=Y(I(Dt),2),Hn=J=>{var V=g_();ze("click",V,qe),U(J,V)};be(hn,J=>{r(o)||J(Hn)}),U(Ae,$t)};be(lt,Ae=>{r(b)&&Ae(Xe)}),ze("click",L,_),U(X,B)},ft=Kt(()=>(x(Cn),x(a()),F(()=>Cn(a())))),kt=X=>{var B=w_(),Ne=I(B),ee=I(Ne);Sr(ee,t,"identifier",{},null);var L=Y(ee,2),pt=G=>{U(G,y_())};be(L,G=>{r(o)||G(pt)});var ht=Y(L,2),_e=I(ht),at=nt(()=>r(w)?u():void 0),We=nt(()=>(x(Bm),x(c()),F(()=>Bm(c()))));lj(_e,{get path(){return r(j)},get value(){return a()},get enforceString(){return r(k)},get selection(){return r(at)},get searchResultItems(){return r(We)},get context(){return d()}});var Ye=Y(ht,2),Tt=G=>{var W=j_();Mi(I(W),{get root(){return r(o)},selected:!0,get onContextMenu(){return x(d()),F(()=>d().onContextMenu)}}),U(G,W)},He=Kt(()=>(x(d()),r(w),x(u()),x(bn),x(Jn),x(Kr),x(Gt),x(st),r(j),F(()=>!d().readOnly&&r(w)&&u()&&(bn(u())||Jn(u()))&&!Kr(u())&&Gt(st(u()),r(j)))));be(Ye,G=>{r(He)&&G(Tt)});var qt=Y(Ne,2),S=G=>{xl(G,{get validationError(){return r(O)},onExpand:A})};be(qt,G=>{r(O)&&G(S)});var $=Y(qt,2),N=G=>{var W=x_();ze("click",W,qe),U(G,W)};be($,G=>{r(o)||G(N)}),U(X,B)};be(we,X=>{r(ie)?X(ue):r(ft)?X(vt,1):X(kt,-1)});var oe=Y(we,2),Ze=X=>{var B,Ne=k_(),ee=I(Ne),L=nt(()=>(r(w),x(_o),x(u()),F(()=>r(w)&&_o(u()))));Mi(ee,{insert:!0,get selected(){return r(L)},onContextMenu:ve}),Le(pt=>{B=Bt(Ne,1,"jse-insert-area jse-after svelte-1qi6rc1",null,B,pt),Tn(Ne,"title",Fv)},[()=>({"jse-hovered":r(h)===Tu,"jse-selected":r(w)&&_o(u())})]),U(X,Ne)},te=Kt(()=>(x(d()),r(h),x(Tu),r(w),x(_o),x(u()),F(()=>!d().readOnly&&(r(h)===Tu||r(w)&&_o(u())))));be(oe,X=>{r(te)&&X(Ze)}),Le((X,B)=>{he=Bt(Re,1,X,"svelte-1qi6rc1",he,B),Tn(Re,"data-path",r(n)),Tn(Re,"aria-selected",r(w)),Ue=ea(Re,"",Ue,{"--level":(r(j),F(()=>r(j).length))})},[()=>es((x(ka),r(b),x(d()),r(j),x(a()),F(()=>ka("jse-json-node",{"jse-expanded":r(b)},d().onClassName(r(j),a()))))),()=>({"jse-root":r(o),"jse-selected":r(w)&&Jn(u()),"jse-selected-value":r(w)&&bn(u()),"jse-readonly":d().readOnly,"jse-hovered":r(h)===bm})]),ze("mousedown",Re,function(X){if((X.buttons===1||X.buttons===2)&&!((B=X.target).nodeName==="DIV"&&B.contentEditable==="true"||X.buttons===1&&_y(X.target,"BUTTON"))){var B;X.stopPropagation(),X.preventDefault(),d().focus(),document.addEventListener("mousemove",C,!0),document.addEventListener("mouseup",z);var Ne=Uv(X.target),ee=d().getJson(),L=d().getDocumentState();if(!u()||Ne===Dn.after||Ne===Dn.inside||u().type!==Ne&&u().type!==Dn.multi||!Rc(ee,u(),r(j)))if(nr(nr().selecting=!0),nr(nr().selectionAnchor=r(j)),nr(nr().selectionAnchorType=Ne),nr(nr().selectionFocus=r(j)),X.shiftKey){var pt=d().getSelection();pt&&d().onSelect(po(_s(pt),r(j)))}else if(Ne===Dn.multi)if(r(o)&&X.target.hasAttribute("data-path")){var ht=Xt(Ny(a(),L));d().onSelect(Hf(ht))}else d().onSelect(po(r(j),r(j)));else ee!==void 0&&d().onSelect(Pm(Ne,r(j)));else X.button===0&&v()(X)}}),ze("mousemove",Re,function(X){if(nr().selecting){X.preventDefault(),X.stopPropagation(),nr().selectionFocus===void 0&&window.getSelection&&window.getSelection().empty();var B=Uv(X.target);Gt(r(j),nr().selectionFocus)&&B===nr().selectionAnchorType||(nr(nr().selectionFocus=r(j)),nr(nr().selectionAnchorType=B),d().onSelect(po(nr().selectionAnchor||nr().selectionFocus,nr().selectionFocus)))}}),ze("mouseover",Re,function(X){nr().selecting||nr().dragging||(X.stopPropagation(),Li(X.target,"data-type","selectable-value")?g(h,bm):Li(X.target,"data-type","selectable-key")?g(h,void 0):Li(X.target,"data-type","insert-selection-area-inside")?g(h,vs):Li(X.target,"data-type","insert-selection-area-after")&&g(h,Tu),clearTimeout(p))}),ze("mouseout",Re,function(X){X.stopPropagation(),p=window.setTimeout(()=>g(h,void 0))}),U(e,Re),jt()}var cj={prefix:"fas",iconName:"jsoneditor-expand",icon:[512,512,[],"","M 0,448 V 512 h 512 v -64 z M 0,0 V 64 H 512 V 0 Z M 256,96 128,224 h 256 z M 256,416 384,288 H 128 Z"]},uj={prefix:"fas",iconName:"jsoneditor-collapse",icon:[512,512,[],"","m 0,224 v 64 h 512 v -64 z M 256,192 384,64 H 128 Z M 256,320 128,448 h 256 z"]},e0={prefix:"fas",iconName:"jsoneditor-format",icon:[512,512,[],"","M 0,32 v 64 h 416 v -64 z M 160,160 v 64 h 352 v -64 z M 160,288 v 64 h 288 v -64 z M 0,416 v 64 h 320 v -64 z"]},C_={prefix:"fas",iconName:"jsoneditor-compact",icon:[512,512,[],"","M 0,32 v 64 h 512 v -64 z M 0,160 v 64 h 512 v -64 z M 0,288 v 64 h 352 v -64 z"]};It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-welcome.svelte-1lhnan {
  flex: 1;
  overflow: auto;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  display: flex;
  flex-direction: column;
  align-items: center;
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-welcome.svelte-1lhnan:last-child {
  border-bottom: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-welcome.svelte-1lhnan .jse-space.jse-before:where(.svelte-1lhnan) {
  flex: 1;
}
.jse-welcome.svelte-1lhnan .jse-space.jse-after:where(.svelte-1lhnan) {
  flex: 2;
}
.jse-welcome.svelte-1lhnan .jse-contents:where(.svelte-1lhnan) {
  display: flex;
  flex-direction: column;
  max-width: 300px;
  margin: 2em var(--jse-padding, 10px);
  gap: var(--jse-padding, 10px);
}
.jse-welcome.svelte-1lhnan .jse-contents:where(.svelte-1lhnan) .jse-welcome-info:where(.svelte-1lhnan) {
  color: var(--jse-panel-color-readonly, #b2b2b2);
}
.jse-welcome.svelte-1lhnan .jse-contents:where(.svelte-1lhnan) button:where(.svelte-1lhnan) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-button-primary-background, var(--jse-theme-color, #3883fa));
  color: var(--jse-button-primary-color, #fff);
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  border-radius: 3px;
}
.jse-welcome.svelte-1lhnan .jse-contents:where(.svelte-1lhnan) button:where(.svelte-1lhnan):hover {
  background: var(--jse-button-primary-background-highlight, var(--jse-theme-color-highlight, #5f9dff));
}
.jse-welcome.svelte-1lhnan .jse-contents:where(.svelte-1lhnan) button:where(.svelte-1lhnan):disabled {
  background: var(--jse-button-primary-background-disabled, #9d9d9d);
}`);var O_=re('<div class="jse-welcome-info svelte-1lhnan">You can paste clipboard data using <b>Ctrl+V</b>, or use the following options:</div> <button class="svelte-1lhnan">Create object</button> <button class="svelte-1lhnan">Create array</button>',1),__=re('<div class="jse-welcome svelte-1lhnan" role="none"><div class="jse-space jse-before svelte-1lhnan"></div> <div class="jse-contents svelte-1lhnan"><div class="jse-welcome-title">Empty document</div> <!></div> <div class="jse-space jse-after svelte-1lhnan"></div></div>');function np(e,t){var n=typeof e=="string"?e.toLowerCase():e,o=typeof t=="string"?t.toLowerCase():t;return pC(n,o)}function dj(e){var t=arguments.length>1&&arguments[1]!==void 0?arguments[1]:[],n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:[],o=arguments.length>3&&arguments[3]!==void 0?arguments[3]:1,i=tt(e,t);if(Cr(i)){if(n===void 0)throw new Error("Cannot sort: no property selected by which to sort the array");return function(a){var s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:[],l=arguments.length>2&&arguments[2]!==void 0?arguments[2]:[],c=arguments.length>3&&arguments[3]!==void 0?arguments[3]:1,u=function(v,f){var h={boolean:0,number:1,string:2,undefined:4},p=3;return function(y,j){var b=tt(y,v),k=tt(j,v);if(typeof b!=typeof k){var E,O,w=(E=h[typeof b])!==null&&E!==void 0?E:p,_=(O=h[typeof k])!==null&&O!==void 0?O:p;return w>_?f:w<_?-f:0}return typeof b=="number"||typeof b=="boolean"?b>k?f:b<k?-f:0:mr(b)?0:f*np(b,k)}}(l,c),d=tt(a,s);return[{op:"replace",path:wt(s),value:d.slice(0).sort(u)}]}(e,t,n,o)}if(Cn(i))return function(a){var s=arguments.length>1&&arguments[1]!==void 0?arguments[1]:[],l=arguments.length>2&&arguments[2]!==void 0?arguments[2]:1,c=tt(a,s),u=Object.keys(c).slice();u.sort((v,f)=>l*np(v,f));var d={};return u.forEach(v=>d[v]=c[v]),[{op:"replace",path:wt(s),value:d}]}(e,t,o);throw new Error("Cannot sort: no array or object")}Zc(["click"]);It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-navigation-bar-dropdown.svelte-1k47orx {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 3;
  background: var(--jse-navigation-bar-background, var(--jse-background-color, #fff));
  color: var(--jse-navigation-bar-dropdown-color, #656565);
  box-shadow: var(--jse-controls-box-shadow, 0 2px 6px 0 rgba(0, 0, 0, 0.24));
  display: flex;
  flex-direction: column;
  max-height: 300px;
  overflow: auto;
  min-width: 80px;
}
.jse-navigation-bar-dropdown.svelte-1k47orx button.jse-navigation-bar-dropdown-item:where(.svelte-1k47orx) {
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  outline: none;
  text-align: left;
  white-space: nowrap;
  box-sizing: border-box;
  padding: calc(0.5 * var(--jse-padding, 10px)) 36px;
}
.jse-navigation-bar-dropdown.svelte-1k47orx button.jse-navigation-bar-dropdown-item:where(.svelte-1k47orx):focus, .jse-navigation-bar-dropdown.svelte-1k47orx button.jse-navigation-bar-dropdown-item:where(.svelte-1k47orx):hover {
  background: var(--jse-navigation-bar-background-highlight, #e5e5e5);
}
.jse-navigation-bar-dropdown.svelte-1k47orx button.jse-navigation-bar-dropdown-item.jse-selected:where(.svelte-1k47orx) {
  background: var(--jse-navigation-bar-dropdown-color, #656565);
  color: var(--jse-navigation-bar-background, var(--jse-background-color, #fff));
}`);var E_=re('<button type="button"> </button>'),T_=re('<button type="button" class="jse-navigation-bar-dropdown-item svelte-1k47orx">...</button>'),M_=re('<div class="jse-navigation-bar-dropdown svelte-1k47orx"><!> <!></div>');function $_(e,t){yt(t,!1);var n=m(t,"items",9),o=m(t,"selectedItem",9),i=m(t,"onSelect",9);Ft(!0);var a=M_(),s=I(a);Or(s,1,()=>(x(fd),x(n()),F(()=>fd(n(),100))),u=>u,(u,d)=>{var v,f=E_(),h=I(f);Le((p,y)=>{v=Bt(f,1,"jse-navigation-bar-dropdown-item svelte-1k47orx",null,v,{"jse-selected":r(d)===o()}),Tn(f,"title",p),xt(h,y)},[()=>(r(d),F(()=>r(d).toString())),()=>(x(ti),r(d),F(()=>ti(r(d).toString(),30)))]),ze("click",f,Za(()=>i()(r(d)))),U(u,f)});var l=Y(s,2),c=u=>{var d=T_();Tn(d,"title","Limited to 100 items"),U(u,d)};be(l,u=>{x(n()),F(()=>n().length>100)&&u(c)}),U(e,a),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-navigation-bar-item.svelte-13sijxb {
  position: relative;
  display: flex;
}
.jse-navigation-bar-item.svelte-13sijxb button.jse-navigation-bar-button:where(.svelte-13sijxb) {
  font-family: inherit;
  font-size: inherit;
  padding: calc(0.5 * var(--jse-padding, 10px)) 2px;
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  outline: none;
  min-width: 2em;
  white-space: nowrap;
}
.jse-navigation-bar-item.svelte-13sijxb button.jse-navigation-bar-button:where(.svelte-13sijxb):focus, .jse-navigation-bar-item.svelte-13sijxb button.jse-navigation-bar-button:where(.svelte-13sijxb):hover {
  background: var(--jse-panel-button-background-highlight, #e0e0e0);
  color: var(--panel-button-color-highlight, var(--jse-text-color, #4d4d4d));
}
.jse-navigation-bar-item.svelte-13sijxb button.jse-navigation-bar-button.jse-navigation-bar-arrow:where(.svelte-13sijxb) {
  padding: 2px var(--jse-padding, 10px) 0;
}
.jse-navigation-bar-item.svelte-13sijxb button.jse-navigation-bar-button.jse-navigation-bar-arrow.jse-open:where(.svelte-13sijxb) {
  background: var(--jse-navigation-bar-background, var(--jse-background-color, #fff));
  color: var(--jse-navigation-bar-dropdown-color, #656565);
}
.jse-navigation-bar-item.svelte-13sijxb:last-child {
  padding-right: var(--jse-padding, 10px);
}`);var A_=re('<button type="button" class="jse-navigation-bar-button svelte-13sijxb"> </button>'),z_=re('<div class="jse-navigation-bar-item svelte-13sijxb"><button type="button"><!></button> <!></div>');function t0(e,t){yt(t,!1);var n,o=R(void 0,!0),i=R(void 0,!0),{openAbsolutePopup:a,closeAbsolutePopup:s}=rs("absolute-popup"),l=m(t,"path",9),c=m(t,"index",9),u=m(t,"onSelect",9),d=m(t,"getItems",9),v=R(void 0,!0),f=R(!1,!0);function h(E){s(n),u()(r(o).concat(E))}ne(()=>(x(l()),x(c())),()=>{g(o,l().slice(0,c()))}),ne(()=>(x(l()),x(c())),()=>{g(i,l()[c()])}),Mn(),Ft(!0);var p,y=z_(),j=I(y);un(I(j),{get data(){return rb}});var b=Y(j,2),k=E=>{var O=A_(),w=I(O);Le(()=>xt(w,r(i))),ze("click",O,()=>h(r(i))),U(E,O)};be(b,E=>{r(i)!==void 0&&E(k)}),or(y,E=>g(v,E),()=>r(v)),Le(()=>p=Bt(j,1,"jse-navigation-bar-button jse-navigation-bar-arrow svelte-13sijxb",null,p,{"jse-open":r(f)})),ze("click",j,function(){if(r(v)){g(f,!0);var E={items:d()(r(o)),selectedItem:r(i),onSelect:h};n=a($_,E,{anchor:r(v),closeOnOuterClick:!0,onClose:()=>{g(f,!1)}})}}),U(e,y),jt()}function fh(e){var t,n;if(navigator.clipboard)return navigator.clipboard.writeText(e);if((t=(n=document).queryCommandSupported)!==null&&t!==void 0&&t.call(n,"copy")){var o=document.createElement("textarea");o.value=e,o.style.position="fixed",o.style.opacity="0",document.body.appendChild(o),o.select();try{document.execCommand("copy")}catch(i){console.error(i)}finally{document.body.removeChild(o)}return Promise.resolve()}return console.error("Copy failed."),Promise.resolve()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-navigation-bar-path-editor.svelte-uyexy4 {
  flex: 1;
  display: flex;
  border: var(--jse-edit-outline, 2px solid #656565);
  background: var(--jse-background-color, #fff);
}
.jse-navigation-bar-path-editor.svelte-uyexy4 input.jse-navigation-bar-text:where(.svelte-uyexy4) {
  flex: 1;
  font-family: inherit;
  font-size: inherit;
  padding: 0 5px 1px;
  background: var(--jse-background-color, #fff);
  color: var(--jse-text-color, #4d4d4d);
  border: none;
  outline: none;
}
.jse-navigation-bar-path-editor.svelte-uyexy4 button:where(.svelte-uyexy4) {
  border: none;
  background: var(--jse-background-color, #fff);
  cursor: pointer;
  font-family: inherit;
  font-size: 80%;
  color: inherit;
}
.jse-navigation-bar-path-editor.svelte-uyexy4 button.jse-navigation-bar-copy.copied:where(.svelte-uyexy4) {
  color: var(--message-success-background, #9ac45d);
}
.jse-navigation-bar-path-editor.svelte-uyexy4 button.jse-navigation-bar-validation-error:where(.svelte-uyexy4) {
  color: var(--jse-error-color, #ee5341);
}
.jse-navigation-bar-path-editor.error.svelte-uyexy4 {
  border-color: var(--jse-error-color, #ee5341);
}
.jse-navigation-bar-path-editor.error.svelte-uyexy4 input.jse-navigation-bar-text:where(.svelte-uyexy4) {
  color: var(--jse-error-color, #ee5341);
}
.jse-navigation-bar-path-editor.svelte-uyexy4 .jse-copied-text:where(.svelte-uyexy4) {
  background: var(--message-success-background, #9ac45d);
  color: var(--jse-message-success-color, #fff);
  position: relative;
  margin: 2px;
  padding: 0 5px;
  border-radius: 3px;
}`);var P_=re('<button type="button" class="jse-navigation-bar-validation-error svelte-uyexy4"><!></button>'),N_=re('<div class="jse-copied-text svelte-uyexy4">Copied!</div>'),R_=re('<div><input type="text" class="jse-navigation-bar-text svelte-uyexy4"/> <!> <!> <button type="button" title="Copy selected path to the clipboard"><!></button></div>');function I_(e,t){yt(t,!1);var n=R(),o=rs("absolute-popup"),i=m(t,"path",8),a=m(t,"pathParser",8),s=m(t,"onChange",8),l=m(t,"onClose",8),c=m(t,"onError",8),u=m(t,"pathExists",8),d=R(),v=R(),f=R(!1),h=void 0,p=R(!1);function y(){r(d).focus()}function j(z){try{var D=a().parse(z);return function(H){if(!u()(H))throw new Error("Path does not exist in current document")}(D),{path:D,error:void 0}}catch(H){return{path:void 0,error:H}}}vo(()=>{y()}),ra(()=>{clearTimeout(h)}),ne(()=>(x(a()),x(i())),()=>{g(v,a().stringify(i()))}),ne(()=>(r(f),r(v)),()=>{g(n,r(f)?j(r(v)).error:void 0)}),Mn(),Ft();var b,k=R_(),E=I(k);or(E,z=>g(d,z),()=>r(d));var O=Y(E,2),w=z=>{var D=P_();un(I(D),{get data(){return $s}}),go(D,(H,Q)=>Nl==null?void 0:Nl(H,Q),()=>De({text:String(r(n)||"")},o)),U(z,D)};be(O,z=>{r(n)&&z(w)});var _=Y(O,2),A=z=>{U(z,N_())};be(_,z=>{r(p)&&z(A)});var q,C=Y(_,2);un(I(C),{get data(){return Ri}}),Le(()=>{b=Bt(k,1,"jse-navigation-bar-path-editor svelte-uyexy4",null,b,{error:r(n)}),Ps(E,r(v)),q=Bt(C,1,"jse-navigation-bar-copy svelte-uyexy4",null,q,{copied:r(p)})}),ze("keydown",E,Za(function(z){var D=hi(z);if(D==="Escape"&&(z.preventDefault(),l()()),D==="Enter"){z.preventDefault(),g(f,!0);var H=j(r(v));H.path!==void 0?s()(H.path):c()(H.error)}})),ze("input",E,function(z){g(v,z.currentTarget.value)}),ze("click",C,function(){fh(r(v)),g(p,!0),h=window.setTimeout(()=>g(p,!1),1e3),y()}),U(e,k),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-navigation-bar.svelte-hjhal6 {
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  background: var(--jse-panel-background, #ebebeb);
  color: var(--jse-panel-button-color, inherit);
  padding: 0;
  margin: 0;
  display: flex;
  overflow: auto;
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-navigation-bar.svelte-hjhal6 .jse-navigation-bar-edit:where(.svelte-hjhal6) {
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px);
  color: var(--jse-panel-color-readonly, #b2b2b2);
  background: transparent;
  border: none;
  display: flex;
  cursor: pointer;
  outline: none;
  align-items: center;
}
.jse-navigation-bar.svelte-hjhal6 .jse-navigation-bar-edit.flex:where(.svelte-hjhal6) {
  flex: 1;
}
.jse-navigation-bar.svelte-hjhal6 .jse-navigation-bar-edit:where(.svelte-hjhal6):focus, .jse-navigation-bar.svelte-hjhal6 .jse-navigation-bar-edit:where(.svelte-hjhal6):hover, .jse-navigation-bar.svelte-hjhal6 .jse-navigation-bar-edit.editing:where(.svelte-hjhal6) {
  background: var(--jse-panel-button-background-highlight, #e0e0e0);
  color: var(--panel-button-color-highlight, var(--jse-text-color, #4d4d4d));
  transition: color 0.2s ease-in, background 0.2s ease-in;
}
.jse-navigation-bar.svelte-hjhal6 .jse-navigation-bar-edit:where(.svelte-hjhal6) .jse-navigation-bar-space:where(.svelte-hjhal6) {
  flex: 1;
  text-align: left;
}`);var q_=re("<!> <!>",1),D_=re('<div class="jse-navigation-bar svelte-hjhal6"><!> <button type="button"><span class="jse-navigation-bar-space svelte-hjhal6"> </span> <!></button></div>');function L_(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),i=Zr("jsoneditor:NavigationBar"),a=m(t,"json",9),s=m(t,"selection",9),l=m(t,"onSelect",9),c=m(t,"onError",9),u=m(t,"pathParser",9),d=R(void 0,!0),v=R(!1,!0);function f(D){i("get items for path",D);var H=tt(a(),D);if(Array.isArray(H))return W1(0,H.length).map(String);if(Cn(H)){var Q=Object.keys(H).slice(0);return Q.sort(np),Q}return[]}function h(D){return To(a(),D)}function p(D){i("select path",JSON.stringify(D)),l()(po(D,D))}function y(){g(v,!1)}function j(D){y(),p(D)}ne(()=>(x(s()),st),()=>{g(n,s()?st(s()):[])}),ne(()=>(x(a()),r(n)),()=>{g(o,mr(tt(a(),r(n))))}),ne(()=>r(n),()=>{r(n),setTimeout(()=>{if(r(d)&&r(d).scrollTo){var D=r(d).scrollWidth-r(d).clientWidth;D>0&&(i("scrollTo ",D),r(d).scrollTo({left:D,behavior:"smooth"}))}})}),Mn(),Ft(!0);var b=D_(),k=I(b),E=D=>{var H=q_(),Q=Mt(H);Or(Q,1,()=>r(n),Pr,(ge,qe,ce)=>{t0(ge,{getItems:f,get path(){return r(n)},index:ce,onSelect:p})});var fe=Y(Q,2),Ie=ge=>{t0(ge,{getItems:f,get path(){return r(n)},get index(){return r(n),F(()=>r(n).length)},onSelect:p})};be(fe,ge=>{r(o)&&ge(Ie)}),U(D,H)},O=D=>{I_(D,{get path(){return r(n)},onClose:y,onChange:j,get onError(){return c()},pathExists:h,get pathParser(){return u()}})};be(k,D=>{r(v)?D(O,-1):D(E)});var w,_=Y(k,2),A=I(_),q=I(A),C=Y(A,2),z=nt(()=>r(v)?oC:YS);un(C,{get data(){return r(z)}}),or(b,D=>g(d,D),()=>r(d)),Le(D=>{w=Bt(_,1,"jse-navigation-bar-edit svelte-hjhal6",null,w,{flex:!r(v),editing:r(v)}),Tn(_,"title",r(v)?"Cancel editing the selected path":"Edit the selected path"),xt(q,D)},[()=>(x(mr),x(a()),r(v),F(()=>mr(a())||r(v)?" ":"Navigation bar"))]),ze("click",_,function(){g(v,!r(v))}),U(e,b),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-search-box.svelte-1x1x8q0 {
  border: var(--jse-panel-border, var(--jse-main-border, 1px solid #d7d7d7));
  border-radius: 3px;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  background: var(--jse-panel-background, #ebebeb);
  color: var(--jse-panel-color-readonly, #b2b2b2);
  box-shadow: var(--jse-controls-box-shadow, 0 2px 6px 0 rgba(0, 0, 0, 0.24));
  display: inline-block;
  width: 400px;
  max-width: 100%;
  overflow: auto;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) {
  display: flex;
  align-items: stretch;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) button:where(.svelte-1x1x8q0),
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) input:where(.svelte-1x1x8q0) {
  font-family: inherit;
  font-size: inherit;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) button:where(.svelte-1x1x8q0) {
  display: block;
  text-align: center;
  border: none;
  padding: 0 5px;
  margin: 0;
  cursor: pointer;
  color: var(--jse-panel-button-color, inherit);
  background: var(--jse-panel-button-background, transparent);
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) button:where(.svelte-1x1x8q0):hover {
  color: var(--panel-button-color-highlight, var(--jse-text-color, #4d4d4d));
  background: var(--jse-panel-button-background-highlight, #e0e0e0);
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) input:where(.svelte-1x1x8q0) {
  color: var(--jse-panel-color, var(--jse-text-color, #4d4d4d));
  border: var(--jse-input-border, 1px solid #d8dbdf);
  border-radius: 3px;
  background: var(--jse-input-background, var(--jse-background-color, #fff));
  height: 28px;
  padding: 0 5px;
  margin: 0;
  flex: 1;
  width: 0;
  min-width: 50px;
  outline: none;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-replace-toggle:where(.svelte-1x1x8q0) {
  padding: var(--jse-padding, 10px) calc(0.5 * var(--jse-padding, 10px));
  min-width: 20px;
  background: var(--jse-panel-button-background-highlight, #e0e0e0);
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: calc(0.5 * var(--jse-padding, 10px));
  gap: calc(0.5 * var(--jse-padding, 10px));
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) .jse-search-section:where(.svelte-1x1x8q0) {
  flex: 1;
  display: flex;
  align-items: center;
  position: relative;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) .jse-search-section:where(.svelte-1x1x8q0) .jse-search-icon:where(.svelte-1x1x8q0) {
  color: inherit;
  cursor: inherit;
  background: inherit;
  width: 32px;
  text-align: center;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) .jse-search-section:where(.svelte-1x1x8q0) label.jse-search-input-label:where(.svelte-1x1x8q0) {
  flex: 1;
  display: flex;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) .jse-search-section:where(.svelte-1x1x8q0) .jse-search-count:where(.svelte-1x1x8q0) {
  color: inherit;
  font-size: 80%;
  visibility: hidden;
  padding: 0 5px;
  min-width: 36px;
  text-align: center;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) .jse-search-section:where(.svelte-1x1x8q0) .jse-search-count.jse-visible:where(.svelte-1x1x8q0) {
  visibility: visible;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) .jse-replace-section:where(.svelte-1x1x8q0) {
  flex: 1;
  display: flex;
  padding-left: 32px;
}
.jse-search-box.svelte-1x1x8q0 .jse-search-form:where(.svelte-1x1x8q0) .jse-search-contents:where(.svelte-1x1x8q0) .jse-replace-section:where(.svelte-1x1x8q0) button:where(.svelte-1x1x8q0) {
  width: auto;
}`);var U_=re('<button type="button" class="jse-replace-toggle svelte-1x1x8q0" title="Toggle visibility of replace options (Ctrl+H)"><!></button>'),B_=re('<div class="jse-replace-section svelte-1x1x8q0"><input class="jse-replace-input svelte-1x1x8q0" title="Enter replacement text" type="text" placeholder="Replace"/> <button type="button" title="Replace current occurrence (Ctrl+Enter)" class="svelte-1x1x8q0">Replace</button> <button type="button" title="Replace all occurrences" class="svelte-1x1x8q0">All</button></div>'),F_=re('<div class="jse-search-box svelte-1x1x8q0"><form class="jse-search-form svelte-1x1x8q0"><!> <div class="jse-search-contents svelte-1x1x8q0"><div class="jse-search-section svelte-1x1x8q0"><div class="jse-search-icon svelte-1x1x8q0"><!></div> <label class="jse-search-input-label svelte-1x1x8q0" about="jse-search input"><input class="jse-search-input svelte-1x1x8q0" title="Enter text to search" type="text" placeholder="Find"/></label> <div> </div> <button type="button" class="jse-search-next svelte-1x1x8q0" title="Go to next search result (Enter)"><!></button> <button type="button" class="jse-search-previous svelte-1x1x8q0" title="Go to previous search result (Shift+Enter)"><!></button> <button type="button" class="jse-search-clear svelte-1x1x8q0" title="Close search box (Esc)"><!></button></div> <!></div></form></div>');function vj(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),i=R(void 0,!0),a=Zr("jsoneditor:SearchBox"),s=m(t,"json",9),l=m(t,"documentState",9),c=m(t,"parser",9),u=m(t,"showSearch",9),d=m(t,"showReplace",13),v=m(t,"readOnly",9),f=m(t,"columns",9),h=m(t,"onSearch",9),p=m(t,"onFocus",9),y=m(t,"onPatch",9),j=m(t,"onClose",9),b=R("",!0),k="",E=R("",!0),O=R(!1,!0),w=R(void 0,!0),_=od(function(B){return ie.apply(this,arguments)},300),A=od(function(B){return vt.apply(this,arguments)},300);function q(){d(!d()&&!v())}function C(B){B.stopPropagation();var Ne=hi(B);Ne==="Enter"&&(B.preventDefault(),r(b)!==k?_.flush():ce()),Ne==="Shift+Enter"&&(B.preventDefault(),he()),Ne==="Ctrl+Enter"&&(B.preventDefault(),d()?Q():ce()),Ne==="Ctrl+H"&&(B.preventDefault(),q()),Ne==="Escape"&&(B.preventDefault(),oe())}function z(B){hi(B)==="Enter"&&(B.preventDefault(),B.stopPropagation(),Q())}function D(){return H.apply(this,arguments)}function H(){return(H=Pt(function*(){Xn(),yield _.flush()})).apply(this,arguments)}function Q(){return fe.apply(this,arguments)}function fe(){return(fe=Pt(function*(){var B;if(!v()){var Ne=(B=r(w))===null||B===void 0?void 0:B.activeItem;if(a("handleReplace",{replaceText:r(E),activeItem:Ne}),r(w)&&Ne&&s()!==void 0){g(w,De(De({},Rm(r(w))),{},{activeIndex:r(o)}));var{operations:ee,newSelection:L}=h5(s(),l(),r(E),Ne,c());y()(ee,(pt,ht)=>({state:ht,selection:L})),Xn(),yield A.flush(),yield Re()}}})).apply(this,arguments)}function Ie(){return ge.apply(this,arguments)}function ge(){return(ge=Pt(function*(){if(!v()){a("handleReplaceAll",{text:r(b),replaceText:r(E)});var{operations:B,newSelection:Ne}=function(ee,L,pt,ht,_e){for(var at=Im(pt,ee,{maxResults:1/0}),We=[],Ye=0;Ye<at.length;Ye++){var Tt=at[Ye-1],He=at[Ye];Ye!==0&&He.field===Tt.field&&Gt(He.path,Tt.path)?Xt(We).items.push(He):We.push({path:He.path,field:He.field,items:[He]})}We.sort(($,N)=>$.field!==N.field?$.field===ya.key?1:-1:N.path.length-$.path.length);var qt,S=[];return We.forEach($=>{var{field:N,path:G,items:W}=$;if(N===ya.key){var de=cn(G),Me=tt(ee,de),pe=Xt(G),le=au(de,Object.keys(Me),pe,Dm(pe,ht,W));S=S.concat(le),qt=Pl(ee,le)}else{if(N!==ya.value)throw new Error("Cannot replace: unknown type of search result field ".concat(N));var St=tt(ee,G);if(St===void 0)throw new Error("Cannot replace: path not found ".concat(wt(G)));var lt=typeof St=="string"?St:String(St),Xe=$a(ee,L,G),Ae=Dm(lt,ht,W),$t=[{op:"replace",path:wt(G),value:Xe?Ae:Ql(Ae,_e)}];S=S.concat($t),qt=Pl(ee,$t)}}),{operations:S,newSelection:qt}}(s(),l(),r(b),r(E),c());y()(B,(ee,L)=>({state:L,selection:Ne})),yield Re()}})).apply(this,arguments)}function qe(B){B.select()}function ce(){return ve.apply(this,arguments)}function ve(){return(ve=Pt(function*(){g(w,r(w)?Rm(r(w)):void 0),yield Re()})).apply(this,arguments)}function he(){return Ue.apply(this,arguments)}function Ue(){return Ue=Pt(function*(){g(w,r(w)?function(B){var Ne=B.activeIndex>0?B.activeIndex-1:B.items.length-1,ee=B.items[Ne],L=B.items.map((pt,ht)=>De(De({},pt),{},{active:ht===Ne}));return De(De({},B),{},{items:L,activeItem:ee,activeIndex:Ne})}(r(w)):void 0),yield Re()}),Ue.apply(this,arguments)}function Re(){return we.apply(this,arguments)}function we(){return(we=Pt(function*(){var B;a("handleFocus",r(w));var Ne=(B=r(w))===null||B===void 0?void 0:B.activeItem;Ne&&s()!==void 0&&(yield p()(Ne.path,Ne.resultIndex))})).apply(this,arguments)}function ue(){return ue=Pt(function*(B){yield ft(B,r(b),s())}),ue.apply(this,arguments)}function ie(){return ie=Pt(function*(B){yield ft(u(),B,s()),yield Re()}),ie.apply(this,arguments)}function vt(){return vt=Pt(function*(B){yield ft(u(),r(b),B)}),vt.apply(this,arguments)}function ft(B,Ne,ee){return kt.apply(this,arguments)}function kt(){return kt=Pt(function*(B,Ne,ee){return B?(a("applySearch",{showSearch:B,text:Ne}),Ne===""?(a("clearing search result"),r(w)!==void 0&&g(w,void 0),Promise.resolve()):(k=Ne,g(O,!0),new Promise(L=>{setTimeout(()=>{var pt=Im(Ne,ee,{maxResults:Bv,columns:f()});g(w,function(ht,_e){var at=_e!=null&&_e.activeItem?Lm(_e.activeItem):void 0,We=ht.findIndex(He=>Gt(at,Lm(He))),Ye=We!==-1?We:(_e==null?void 0:_e.activeIndex)!==void 0&&(_e==null?void 0:_e.activeIndex)<ht.length?_e==null?void 0:_e.activeIndex:ht.length>0?0:-1,Tt=ht.map((He,qt)=>De(De({resultIndex:qt},He),{},{active:qt===Ye}));return{items:Tt,activeItem:Tt[Ye],activeIndex:Ye}}(pt,r(w))),g(O,!1),L()})}))):(r(w)&&g(w,void 0),Promise.resolve())}),kt.apply(this,arguments)}function oe(){a("handleClose"),_.cancel(),A.cancel(),ft(!1,r(b),s()),j()()}ne(()=>r(w),()=>{var B;g(n,((B=r(w))===null||B===void 0||(B=B.items)===null||B===void 0?void 0:B.length)||0)}),ne(()=>r(w),()=>{var B;g(o,((B=r(w))===null||B===void 0?void 0:B.activeIndex)||0)}),ne(()=>(r(n),Bv),()=>{g(i,r(n)>=Bv?"".concat(999,"+"):String(r(n)))}),ne(()=>(x(h()),r(w)),()=>{h()(r(w))}),ne(()=>x(u()),()=>{(function(B){ue.apply(this,arguments)})(u())}),ne(()=>r(b),()=>{_(r(b))}),ne(()=>x(s()),()=>{A(s())}),Mn(),Ft(!0);var Ze=br(),te=Mt(Ze),X=B=>{var Ne=F_(),ee=I(Ne),L=I(ee),pt=pe=>{var le=U_(),St=I(le),lt=nt(()=>d()?di:_c);un(St,{get data(){return r(lt)}}),ze("click",le,q),U(pe,le)};be(L,pe=>{v()||pe(pt)});var ht=I(Y(L,2)),_e=I(ht),at=I(_e),We=pe=>{un(pe,{get data(){return QS},spin:!0})},Ye=pe=>{un(pe,{get data(){return Jd}})};be(at,pe=>{r(O)?pe(We):pe(Ye,-1)});var Tt=Y(_e,2),He=I(Tt);so(()=>vd(He,()=>r(b),pe=>g(b,pe))),go(He,pe=>qe==null?void 0:qe(pe)),so(()=>ze("paste",He,D));var qt,S=Y(Tt,2),$=I(S),N=Y(S,2);un(I(N),{get data(){return aC}});var G=Y(N,2);un(I(G),{get data(){return HS}});var W=Y(G,2);un(I(W),{get data(){return Hd}});var de=Y(ht,2),Me=pe=>{var le=B_(),St=I(le),lt=Y(St,2),Xe=Y(lt,2);vd(St,()=>r(E),Ae=>g(E,Ae)),ze("keydown",St,z),ze("click",lt,Q),ze("click",Xe,Ie),U(pe,le)};be(de,pe=>{d()&&!v()&&pe(Me)}),Le(()=>{var pe;qt=Bt(S,1,"jse-search-count svelte-1x1x8q0",null,qt,{"jse-visible":r(b)!==""}),xt($,"".concat(r(o)!==-1&&r(o)<r(n)?"".concat(r(o)+1,"/"):"").concat((pe=r(i))!==null&&pe!==void 0?pe:""))}),ze("click",N,ce),ze("click",G,he),ze("click",W,oe),ze("keydown",ee,C),U(B,Ne)};be(te,B=>{u()&&B(X)}),U(e,Ze),jt()}var Lc=Symbol("path");function W_(e,t){var n=arguments.length>2&&arguments[2]!==void 0?arguments[2]:1/0,o={};Array.isArray(e)&&function(a,s,l){if(a.length<s)a.forEach(l);else for(var c=s>1?(a.length-1)/(s-1):a.length,u=0;u<s;u++){var d=Math.floor(u*c);l(a[d],d,a)}}(e,n,a=>{Cn(a)?fj(a,o,t):o[Lc]=!0});var i=[];return Lc in o&&i.push([]),pj(o,[],i,t),i}function fj(e,t,n){for(var o in e){var i=e[o],a=t[o]||(t[o]={});Cn(i)&&n?fj(i,a,n):a[Lc]===void 0&&(a[Lc]=!0)}}function pj(e,t,n,o){for(var i in e){var a=t.concat(i),s=e[i];s&&s[Lc]===!0&&n.push(a),$r(s)&&o&&pj(s,a,n,o)}}function V_(e,t,n,o,i,a){for(var s=arguments.length>6&&arguments[6]!==void 0?arguments[6]:80,l=Cr(n)?n.length:0,c=function(k,E){var O=Object.values(k);if(gn(O))return E;var w=(_,A)=>_+A;return O.reduce(w)/O.length}(o,i),u=e-s,d=t+2*s,v=k=>o[k]||i,f=0,h=a;h<u&&f<l;)h+=v(f),f++;f>0&&(h-=v(--f));for(var p=f,y=0;y<d&&p<l;)y+=v(p),p++;for(var j=0,b=p;b<l;b++)j+=v(b);return{startIndex:f,endIndex:p,startHeight:h,endHeight:j,averageItemHeight:c,visibleHeight:y,visibleItems:Cr(n)?n.slice(f,p):[]}}function n0(e,t,n,o){for(var{rowIndex:i}=Qo(e,t),a=0,s=0;s<i;s++)a+=n[s]||o;return a}function Qo(e,t){var[n,...o]=e,i=parseInt(n,10);return{rowIndex:isNaN(i)?-1:i,columnIndex:t.findIndex(a=>Ra(o,a))}}function ps(e,t){var{rowIndex:n,columnIndex:o}=e;return[String(n),...t[o]]}function J_(e,t){var[n,o]=iS(e,s=>Jp(s.path[0])),i=H8(n,H_),a=Z8(i,s=>{var l={row:[],columns:{}};return s.forEach(c=>{var u=function(d,v){var f=Qo(d.path,v);return f.columnIndex!==-1?f.columnIndex:-1}(c,t);u!==-1?(l.columns[u]===void 0&&(l.columns[u]=[]),l.columns[u].push(c)):l.row.push(c)}),l});return{root:o,rows:a}}function Xs(e,t){if(t&&t.length!==0)return t.length===1?t[0]:{path:e,message:"Multiple validation issues: "+t.map(n=>Eo(n.path)+" "+n.message).join(", "),severity:ba.warning}}function H_(e){return parseInt(e.path[0],10)}function Q_(e,t,n){var o=t.some(i=>function(a,s,l){if(!a)return!1;if(s.op==="replace"){var c=Mo(s.path),{rowIndex:u,columnIndex:d}=Qo(c,l),v=l.findIndex(f=>Gt(f,a.path));if(u!==-1&&d!==-1&&d!==v)return!1}return!0}(e,i,n));return o?void 0:e}var ho=Zr("jsoneditor:actions");function hj(e){return rp.apply(this,arguments)}function rp(){return rp=Pt(function*(e){var{json:t,selection:n,indentation:o,readOnly:i,parser:a,onPatch:s}=e;if(!i&&t!==void 0&&n&&dl(n)){var l=qy(t,n,o,a);if(l!==void 0){ho("cut",{selection:n,clipboard:l,indentation:o}),yield fh(l);var{operations:c,newSelection:u}=Wy(t,n);s(c,(d,v)=>({state:v,selection:u}))}}}),rp.apply(this,arguments)}function gj(e){return op.apply(this,arguments)}function op(){return op=Pt(function*(e){var{json:t,selection:n,indentation:o,parser:i}=e,a=qy(t,n,o,i);a!==void 0&&(ho("copy",{clipboard:a,indentation:o}),yield fh(a))}),op.apply(this,arguments)}function mj(e){var{clipboardText:t,json:n,selection:o,readOnly:i,parser:a,onPatch:s,onChangeText:l,onPasteMultilineText:c,openRepairModal:u}=e;if(!i)try{d(t)}catch{u(t,f=>{ho("repaired pasted text: ",f),d(f)})}function d(v){if(n!==void 0){var f=o||rn([]),h=Fy(n,f,v,a),p=function(y,j,b){var k=arguments.length>3&&arguments[3]!==void 0?arguments[3]:s5;if(y.length>k)return!1;var E=/\n/.test(y);if(!E)return!1;var O=j.some(_=>_.op==="replace"&&Array.isArray(_.value)),w=j.filter(_=>_.op==="add").length>1;if(!O&&!w)return!1;try{return tu(y,b.parse),!1}catch{return!0}}(t,h,a);ho("paste",{pastedText:v,operations:h,ensureSelection:f,pasteMultilineText:p}),s(h,(y,j)=>{var b=j;return h.filter(k=>(X0(k)||gp(k))&&mr(k.value)).forEach(k=>{var E=ma(n,k.path);b=Rs(y,b,E)}),{state:b}}),p&&c(v)}else ho("paste text",{pastedText:v}),l(t,(y,j)=>{if(y)return{state:Rs(y,j,[])}})}}function bj(e){var{json:t,text:n,selection:o,keepSelection:i,readOnly:a,onChange:s,onPatch:l}=e;if(!a&&o){var c=t!==void 0&&(Yr(o)||bn(o))?po(o.path,o.path):o;if(gn(st(o)))ho("remove root",{selection:o}),s&&s({text:"",json:void 0},t!==void 0?{text:void 0,json:t}:{text:n||"",json:t},{contentErrors:void 0,patchResult:void 0});else if(t!==void 0){var{operations:u,newSelection:d}=Wy(t,c);ho("remove",{operations:u,selection:o,newSelection:d}),l(u,(v,f)=>({state:f,selection:i?o:d}))}}}function Ed(e){var{insertType:t,selectInside:n,initialValue:o,json:i,selection:a,readOnly:s,parser:l,onPatch:c,onReplaceJson:u}=e;if(!s){var d=function(y,j,b){if(b==="object")return{};if(b==="array")return[];if(b==="structure"&&y!==void 0){var k=j?Ry(j):[],E=tt(y,k);if(Array.isArray(E)&&!gn(E)){var O=ai(E);return mr(O)?R6(O,w=>Array.isArray(w)?[]:Cn(w)?void 0:""):""}}return""}(i,a,t);if(i!==void 0){var v=l.stringify(d),f=Fy(i,a,v,l);ho("onInsert",{insertType:t,operations:f,newValue:d,data:v});var h=Xt(f.filter(y=>y.op==="add"||y.op==="replace"));c(f,(y,j,b)=>{if(h){var k=ma(y,h.path);if(mr(d))return{state:la(y,j,k,sh),selection:n?mi(k):b};if(d===""){var E=gn(k)?void 0:tt(y,cn(k));return{state:la(y,j,k,Hu),selection:Cn(E)?lh(k,o):bd(k,o)}}}}),ho("after patch")}else{ho("onInsert",{insertType:t,newValue:d});var p=[];u(d,(y,j)=>({state:Rs(y,j,p),selection:mr(d)?mi(p):bd(p)}))}}}function yj(e){return ap.apply(this,arguments)}function ap(){return ap=Pt(function*(e){var{char:t,selectInside:n,json:o,selection:i,readOnly:a,parser:s,onPatch:l,onReplaceJson:c,onSelect:u}=e;a||(Yr(i)?u(De(De({},i),{},{edit:!0,initialValue:t})):t==="{"?Ed({insertType:"object",selectInside:n,initialValue:void 0,json:o,selection:i,readOnly:a,parser:s,onPatch:l,onReplaceJson:c}):t==="["?Ed({insertType:"array",selectInside:n,initialValue:void 0,json:o,selection:i,readOnly:a,parser:s,onPatch:l,onReplaceJson:c}):bn(i)&&o!==void 0?mr(tt(o,i.path))||u(De(De({},i),{},{edit:!0,initialValue:t})):(ho("onInsertValueWithCharacter",{char:t}),yield function(d){return ip.apply(this,arguments)}({char:t,json:o,selection:i,readOnly:a,parser:s,onPatch:l,onReplaceJson:c})))}),ap.apply(this,arguments)}function ip(){return ip=Pt(function*(e){var{char:t,json:n,selection:o,readOnly:i,parser:a,onPatch:s,onReplaceJson:l}=e;i||Ed({insertType:"value",selectInside:!1,initialValue:t,json:n,selection:o,readOnly:i,parser:a,onPatch:s,onReplaceJson:l})}),ip.apply(this,arguments)}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-json-preview.svelte-25xmyd {
  flex: 1;
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  color: var(--jse-panel-color-readonly, #b2b2b2);
  overflow: auto;
  white-space: pre-wrap;
  padding: 2px;
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
  border-bottom: var(--jse-main-border, 1px solid #d7d7d7);
}`);var K_=re('<div class="jse-json-preview svelte-25xmyd"> </div>');function jj(e,t){yt(t,!1);var n=R(),o=R(),i=m(t,"text",8),a=m(t,"json",8),s=m(t,"indentation",8),l=m(t,"parser",8);ne(()=>(x(a()),x(i())),()=>{g(n,a()!==void 0?{json:a()}:{text:i()||""})}),ne(()=>(r(n),x(s()),x(l()),pd),()=>{g(o,ti(Uf(r(n),s(),l()),pd))}),Mn(),Ft();var c=K_(),u=I(c);Le(()=>xt(u,r(o))),U(e,c),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
button.jse-context-menu-button.svelte-16jz6ui {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  flex: 1;
  white-space: nowrap;
  padding: var(--jse-padding, 10px);
  color: inherit;
}
button.jse-context-menu-button.svelte-16jz6ui:hover {
  background: var(--jse-context-menu-background-highlight, #7a7a7a);
}
button.jse-context-menu-button.svelte-16jz6ui:focus {
  background: var(--jse-context-menu-background-highlight, #7a7a7a);
  z-index: 1;
}
button.jse-context-menu-button.svelte-16jz6ui:disabled {
  color: var(--jse-context-menu-color-disabled, #9d9d9d);
  background: unset;
}
button.jse-context-menu-button.left.svelte-16jz6ui {
  text-align: left;
}
button.jse-context-menu-button.svelte-16jz6ui svg {
  width: 16px;
}`);var G_=re('<button type="button"><!> <!></button>');function tf(e,t){yt(t,!1);var n=m(t,"item",8),o=m(t,"className",8,void 0),i=m(t,"onRequestClose",8);Ft();var a=G_(),s=I(a),l=d=>{un(d,{get data(){return x(n()),F(()=>n().icon)}})};be(s,d=>{x(n()),F(()=>n().icon)&&d(l)});var c=Y(s,2),u=d=>{var v=oo();Le(()=>xt(v,(x(n()),F(()=>n().text)))),U(d,v)};be(c,d=>{x(n()),F(()=>n().text)&&d(u)}),Le(d=>{Bt(a,1,d,"svelte-16jz6ui"),Tn(a,"title",(x(n()),F(()=>n().title))),a.disabled=(x(n()),F(()=>n().disabled||!1))},[()=>es((x(ka),x(o()),x(n()),F(()=>ka("jse-context-menu-button",o(),n().className))))]),ze("click",a,d=>{i()(),n().onClick(d)}),U(e,a),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-dropdown-button.svelte-bov1j6 {
  flex: 1;
  line-height: normal;
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  position: relative;
  padding: 0;
  display: flex;
}
.jse-dropdown-button.svelte-bov1j6 ul:where(.svelte-bov1j6) {
  margin: 0;
  padding: 0;
}
.jse-dropdown-button.svelte-bov1j6 ul:where(.svelte-bov1j6) li:where(.svelte-bov1j6) {
  margin: 0;
  padding: 0;
  list-style-type: none;
}
.jse-dropdown-button.svelte-bov1j6 button.jse-open-dropdown:where(.svelte-bov1j6) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  width: 2em;
  background: var(--jse-context-menu-background, #656565);
  color: var(--jse-context-menu-color, var(--jse-text-color-inverse, #fff));
  border-radius: 0;
}
.jse-dropdown-button.svelte-bov1j6 button.jse-open-dropdown.jse-visible:where(.svelte-bov1j6) {
  background: var(--jse-context-menu-background, #656565);
}
.jse-dropdown-button.svelte-bov1j6 button.jse-open-dropdown:where(.svelte-bov1j6):hover {
  background: var(--jse-context-menu-background-highlight, #7a7a7a);
}
.jse-dropdown-button.svelte-bov1j6 button.jse-open-dropdown:where(.svelte-bov1j6):focus {
  z-index: 1;
}
.jse-dropdown-button.svelte-bov1j6 button.jse-open-dropdown:where(.svelte-bov1j6):disabled {
  color: var(--jse-context-menu-color-disabled, #9d9d9d);
  background: unset;
}
.jse-dropdown-button.svelte-bov1j6 .jse-dropdown-items:where(.svelte-bov1j6) {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1;
  background: var(--jse-context-menu-background, #656565);
  color: var(--jse-context-menu-color, var(--jse-text-color-inverse, #fff));
  box-shadow: var(--jse-controls-box-shadow, 0 2px 6px 0 rgba(0, 0, 0, 0.24));
}
.jse-dropdown-button.svelte-bov1j6 .jse-dropdown-items.jse-visible:where(.svelte-bov1j6) {
  display: block;
}
.jse-dropdown-button.svelte-bov1j6 .jse-dropdown-items:where(.svelte-bov1j6) button:where(.svelte-bov1j6) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  width: 100%;
  text-align: left;
  padding: var(--jse-padding, 10px);
  margin: 0;
}
.jse-dropdown-button.svelte-bov1j6 .jse-dropdown-items:where(.svelte-bov1j6) button:where(.svelte-bov1j6):hover {
  background: var(--jse-context-menu-background-highlight, #7a7a7a);
}
.jse-dropdown-button.svelte-bov1j6 .jse-dropdown-items:where(.svelte-bov1j6) button:where(.svelte-bov1j6):disabled {
  color: var(--jse-context-menu-color-disabled, #9d9d9d);
  background: unset;
}`);var Y_=re('<li class="svelte-bov1j6"><button type="button"><!> </button></li>'),X_=re('<div role="button" tabindex="0" class="jse-dropdown-button svelte-bov1j6"><!> <button type="button" data-type="jse-open-dropdown"><!></button> <div><ul class="svelte-bov1j6"></ul></div></div>');It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
button.jse-context-menu-button.svelte-1y5l9l1 {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  flex: 1;
  white-space: nowrap;
  padding: var(--jse-padding, 10px);
  color: inherit;
}
button.jse-context-menu-button.svelte-1y5l9l1:hover {
  background: var(--jse-context-menu-background-highlight, #7a7a7a);
}
button.jse-context-menu-button.svelte-1y5l9l1:focus {
  background: var(--jse-context-menu-background-highlight, #7a7a7a);
  z-index: 1;
}
button.jse-context-menu-button.svelte-1y5l9l1:disabled {
  color: var(--jse-context-menu-color-disabled, #9d9d9d);
  background: unset;
}
button.jse-context-menu-button.left.svelte-1y5l9l1 {
  text-align: left;
}
button.jse-context-menu-button.svelte-1y5l9l1 svg {
  width: 16px;
}`);var Z_=re('<button type="button" slot="defaultItem"><!> </button>');function nf(e,t){yt(t,!1);var n=R(),o=m(t,"item",8),i=m(t,"className",8,void 0),a=m(t,"onRequestClose",8);ne(()=>(x(o()),x(a())),()=>{g(n,o().items.map(s=>De(De({},s),{},{onClick:l=>{a()(),s.onClick(l)}})))}),Mn(),Ft(),function(s,l){yt(l,!1);var c=R(void 0,!0),u=m(l,"items",25,()=>[]),d=m(l,"title",9,void 0),v=m(l,"width",9,"120px"),f=R(!1,!0);function h(){g(f,!1)}function p(w){hi(w)==="Escape"&&(w.preventDefault(),g(f,!1))}vo(()=>{document.addEventListener("click",h),document.addEventListener("keydown",p)}),ra(()=>{document.removeEventListener("click",h),document.removeEventListener("keydown",p)}),ne(()=>x(u()),()=>{g(c,u().every(w=>w.disabled===!0))}),Mn(),Ft(!0);var y=X_(),j=I(y);Sr(j,l,"defaultItem",{},null);var b,k=Y(j,2);un(I(k),{get data(){return di}});var E,O=Y(k,2);Or(I(O),5,u,Pr,(w,_)=>{var A=Y_(),q=I(A),C=I(q),z=H=>{un(H,{get data(){return r(_),F(()=>r(_).icon)}})};be(C,H=>{r(_),F(()=>r(_).icon)&&H(z)});var D=Y(C);Le(()=>{var H;Tn(q,"title",(r(_),F(()=>r(_).title))),q.disabled=(r(_),F(()=>r(_).disabled)),Bt(q,1,es((r(_),F(()=>r(_).className))),"svelte-bov1j6"),xt(D," ".concat((r(_),(H=F(()=>r(_).text))!==null&&H!==void 0?H:"")))}),ze("click",q,H=>r(_).onClick(H)),U(w,A)}),Le(()=>{var w;Tn(y,"title",d()),b=Bt(k,1,"jse-open-dropdown svelte-bov1j6",null,b,{"jse-visible":r(f)}),k.disabled=r(c),E=Bt(O,1,"jse-dropdown-items svelte-bov1j6",null,E,{"jse-visible":r(f)}),ea(O,"width: ".concat((w=v())!==null&&w!==void 0?w:"",";"))}),ze("click",k,function(){var w=r(f);setTimeout(()=>g(f,!w))}),ze("click",y,h),U(s,y),jt()}(e,{get width(){return x(o()),F(()=>o().width)},get items(){return r(n)},$$slots:{defaultItem:(s,l)=>{var c=Z_(),u=I(c),d=f=>{un(f,{get data(){return x(o()),F(()=>o().main.icon)}})};be(u,f=>{x(o()),F(()=>o().main.icon)&&f(d)});var v=Y(u);Le(f=>{var h;Bt(c,1,f,"svelte-1y5l9l1"),Tn(c,"title",(x(o()),F(()=>o().main.title))),c.disabled=(x(o()),F(()=>o().main.disabled||!1)),xt(v," ".concat((x(o()),(h=F(()=>o().main.text))!==null&&h!==void 0?h:"")))},[()=>es((x(ka),x(i()),x(o()),F(()=>ka("jse-context-menu-button",i(),o().main.className))))]),ze("click",c,f=>{a()(),o().main.onClick(f)}),U(s,c)}}}),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-contextmenu.svelte-1shjn02 {
  box-shadow: var(--jse-controls-box-shadow, 0 2px 6px 0 rgba(0, 0, 0, 0.24));
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  background: var(--jse-context-menu-background, #656565);
  color: var(--jse-context-menu-color, var(--jse-text-color-inverse, #fff));
}
.jse-contextmenu.svelte-1shjn02 .jse-row:where(.svelte-1shjn02) {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: stretch;
}
.jse-contextmenu.svelte-1shjn02 .jse-row:where(.svelte-1shjn02) div.jse-label:where(.svelte-1shjn02) {
  flex: 1;
  white-space: nowrap;
  padding: var(--jse-padding, 10px);
  color: var(--jse-context-menu-color-disabled, #9d9d9d);
  line-height: normal;
}
.jse-contextmenu.svelte-1shjn02 .jse-row:where(.svelte-1shjn02) div.jse-tip:where(.svelte-1shjn02) {
  flex: 1;
  background: var(--jse-context-menu-tip-background, rgba(255, 255, 255, 0.2));
  color: var(--context-menu-tip-color, inherit);
  margin: calc(0.5 * var(--jse-padding, 10px));
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px);
  font-size: 80%;
  line-height: 1.3em;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: var(--jse-padding, 10px);
  border-radius: 3px;
}
.jse-contextmenu.svelte-1shjn02 .jse-row:where(.svelte-1shjn02) div.jse-tip:where(.svelte-1shjn02) div.jse-tip-icon:where(.svelte-1shjn02) {
  padding-top: calc(0.5 * var(--jse-padding, 10px));
}
.jse-contextmenu.svelte-1shjn02 .jse-column:where(.svelte-1shjn02) {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.jse-contextmenu.svelte-1shjn02 .jse-column:where(.svelte-1shjn02):not(:last-child) {
  border-right: 1px solid var(--jse-context-menu-separator-color, #7a7a7a);
}
.jse-contextmenu.svelte-1shjn02 .jse-separator:where(.svelte-1shjn02) {
  width: 100%;
  height: 1px;
  background: var(--jse-context-menu-separator-color, #7a7a7a);
}`);var eE=re('<div class="jse-separator svelte-1shjn02"></div>'),tE=re('<div class="jse-label svelte-1shjn02"> </div>'),nE=re('<div class="jse-column svelte-1shjn02"></div>'),rE=re('<div class="jse-separator svelte-1shjn02"></div>'),oE=re('<div class="jse-row svelte-1shjn02"></div>'),aE=re('<div class="jse-separator svelte-1shjn02"></div>'),iE=re('<div class="jse-row svelte-1shjn02"><div class="jse-tip svelte-1shjn02"><div class="jse-tip-icon svelte-1shjn02"><!></div> <div class="jse-tip-text"> </div></div></div>'),sE=re('<div role="menu" tabindex="-1" class="jse-contextmenu svelte-1shjn02"><!> <!></div>');function xj(e,t){yt(t,!1);var n=m(t,"items",9),o=m(t,"onRequestClose",9),i=m(t,"tip",9),a=R(void 0,!0);vo(()=>{var f=Array.from(r(a).querySelectorAll("button")).find(h=>!h.disabled);f&&f.focus()});var s={ArrowUp:"Up",ArrowDown:"Down",ArrowLeft:"Left",ArrowRight:"Right"};function l(f){return console.error("Unknown type of context menu item",f),"???"}Ft(!0);var c=sE(),u=I(c);Or(u,1,n,Pr,(f,h)=>{var p=br(),y=Mt(p),j=C=>{tf(C,{get item(){return r(h)},get onRequestClose(){return o()}})},b=Kt(()=>(x(ei),r(h),F(()=>ei(r(h))))),k=C=>{nf(C,{get item(){return r(h)},get onRequestClose(){return o()}})},E=Kt(()=>(x(Gs),r(h),F(()=>Gs(r(h))))),O=C=>{var z=oE();Or(z,5,()=>(r(h),F(()=>r(h).items)),Pr,(D,H)=>{var Q=br(),fe=Mt(Q),Ie=ue=>{tf(ue,{get item(){return r(H)},get onRequestClose(){return o()}})},ge=Kt(()=>(x(ei),r(H),F(()=>ei(r(H))))),qe=ue=>{nf(ue,{get item(){return r(H)},get onRequestClose(){return o()}})},ce=Kt(()=>(x(Gs),r(H),F(()=>Gs(r(H))))),ve=ue=>{var ie=nE();Or(ie,5,()=>(r(H),F(()=>r(H).items)),Pr,(vt,ft)=>{var kt=br(),oe=Mt(kt),Ze=_e=>{tf(_e,{className:"left",get item(){return r(ft)},get onRequestClose(){return o()}})},te=Kt(()=>(x(ei),r(ft),F(()=>ei(r(ft))))),X=_e=>{nf(_e,{className:"left",get item(){return r(ft)},get onRequestClose(){return o()}})},B=Kt(()=>(x(Gs),r(ft),F(()=>Gs(r(ft))))),Ne=_e=>{U(_e,eE())},ee=Kt(()=>(x(zi),r(ft),F(()=>zi(r(ft))))),L=_e=>{var at=tE(),We=I(at);Le(()=>xt(We,(r(ft),F(()=>r(ft).text)))),U(_e,at)},pt=Kt(()=>(x(xm),r(ft),F(()=>xm(r(ft))))),ht=_e=>{var at=oo();Le(We=>xt(at,We),[()=>(r(ft),F(()=>l(r(ft))))]),U(_e,at)};be(oe,_e=>{r(te)?_e(Ze):r(B)?_e(X,1):r(ee)?_e(Ne,2):r(pt)?_e(L,3):_e(ht,-1)}),U(vt,kt)}),U(ue,ie)},he=Kt(()=>(x(km),r(H),F(()=>km(r(H))))),Ue=ue=>{U(ue,rE())},Re=Kt(()=>(x(zi),r(H),F(()=>zi(r(H))))),we=ue=>{var ie=oo();Le(vt=>xt(ie,vt),[()=>(r(H),F(()=>l(r(H))))]),U(ue,ie)};be(fe,ue=>{r(ge)?ue(Ie):r(ce)?ue(qe,1):r(he)?ue(ve,2):r(Re)?ue(Ue,3):ue(we,-1)}),U(D,Q)}),U(C,z)},w=Kt(()=>(x(wm),r(h),F(()=>wm(r(h))))),_=C=>{U(C,aE())},A=Kt(()=>(x(zi),r(h),F(()=>zi(r(h))))),q=C=>{var z=oo();Le(D=>xt(z,D),[()=>(r(h),F(()=>l(r(h))))]),U(C,z)};be(y,C=>{r(b)?C(j):r(E)?C(k,1):r(w)?C(O,2):r(A)?C(_,3):C(q,-1)}),U(f,p)});var d=Y(u,2),v=f=>{var h=iE(),p=I(h),y=I(p);un(I(y),{get data(){return qS}});var j=I(Y(y,2));Le(()=>xt(j,i())),U(f,h)};be(d,f=>{i()&&f(v)}),or(c,f=>g(a,f),()=>r(a)),ze("keydown",c,function(f){var h=hi(f),p=s[h];if(p&&f.target){f.preventDefault();var y=L9({allElements:Array.from(r(a).querySelectorAll("button:not([disabled])")),currentElement:f.target,direction:p,hasPrio:j=>j.getAttribute("data-type")!=="jse-open-dropdown"});y&&y.focus()}}),U(e,c),jt()}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-value.jse-string.svelte-1htmvf1 {
  color: var(--jse-value-color-string, #008000);
}
.jse-value.jse-object.svelte-1htmvf1, .jse-value.jse-array.svelte-1htmvf1 {
  min-width: 16px;
  color: var(--jse-delimiter-color, rgba(0, 0, 0, 0.38));
}
.jse-value.jse-number.svelte-1htmvf1 {
  color: var(--jse-value-color-number, #ee422e);
}
.jse-value.jse-boolean.svelte-1htmvf1 {
  color: var(--jse-value-color-boolean, #ff8c00);
}
.jse-value.jse-null.svelte-1htmvf1 {
  color: var(--jse-value-color-null, #004ed0);
}
.jse-value.jse-invalid.svelte-1htmvf1 {
  color: var(--jse-text-color, #4d4d4d);
}
.jse-value.jse-url.svelte-1htmvf1 {
  color: var(--jse-value-color-url, #008000);
  text-decoration: underline;
}

.jse-enum-value.svelte-1htmvf1 {
  background: var(--jse-hover-background-color, rgba(0, 0, 0, 0.06));
  border: none;
  padding: 0;
  font-family: inherit;
  font-size: inherit;
  cursor: pointer;
  outline: none;
}
.jse-enum-value.jse-selected.svelte-1htmvf1 {
  background: var(--jse-selection-background-color, #d3d3d3);
  color: inherit;
}
.jse-enum-value.jse-value.svelte-1htmvf1:focus {
  color: var(--jse-text-color, #4d4d4d);
}`);re("<option> </option>");re("<select></select>");var Nu,Ru;function Iu(e,t){return Nu||(Ru=new WeakMap,Nu=new ResizeObserver(n=>{for(var o of n){var i=Ru.get(o.target);i&&i(o.target)}})),Ru.set(e,t),Nu.observe(e),{destroy:()=>{Ru.delete(e),Nu.unobserve(e)}}}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-tree-mode.svelte-10mlrw4 {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  background: var(--jse-background-color, #fff);
  min-width: 0;
  min-height: 0;
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  color: var(--jse-text-color, #4d4d4d);
  line-height: var(--jse-line-height, calc(1em + 4px));
}
.jse-tree-mode.svelte-10mlrw4 .jse-hidden-input-label:where(.svelte-10mlrw4) .jse-hidden-input:where(.svelte-10mlrw4) {
  position: fixed;
  top: -10px;
  left: -10px;
  width: 1px;
  height: 1px;
  padding: 0;
  border: 0;
  outline: none;
}
.jse-tree-mode.no-main-menu.svelte-10mlrw4 {
  border-top: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-tree-mode.svelte-10mlrw4 .jse-search-box-container:where(.svelte-10mlrw4) {
  position: relative;
  height: 0;
  top: var(--jse-padding, 10px);
  margin-right: calc(var(--jse-padding, 10px) + 20px);
  margin-left: var(--jse-padding, 10px);
  text-align: right;
  z-index: 3;
}
.jse-tree-mode.svelte-10mlrw4 .jse-contents:where(.svelte-10mlrw4) {
  flex: 1;
  overflow: auto;
  position: relative;
  padding: 2px;
  display: flex;
  flex-direction: column;
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-tree-mode.svelte-10mlrw4 .jse-contents:where(.svelte-10mlrw4):last-child {
  border-bottom: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-tree-mode.svelte-10mlrw4 .jse-contents:where(.svelte-10mlrw4) .jse-loading-space:where(.svelte-10mlrw4) {
  flex: 1;
}
.jse-tree-mode.svelte-10mlrw4 .jse-contents:where(.svelte-10mlrw4) .jse-loading:where(.svelte-10mlrw4) {
  flex: 2;
  text-align: center;
  color: var(--jse-panel-color-readonly, #b2b2b2);
  box-sizing: border-box;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
}
.jse-tree-mode.svelte-10mlrw4 .jse-contents:where(.svelte-10mlrw4) .jse-search-box-background:where(.svelte-10mlrw4) {
  border: 50px solid var(--jse-modal-background, #f5f5f5);
  margin: -2px;
  margin-bottom: 2px;
  display: inline-block;
}`);var lE=re("<!> <!>",1),cE=re('<div class="jse-search-box-background svelte-10mlrw4"></div>'),uE=re('<div class="jse-search-box-container svelte-10mlrw4"><!></div> <div class="jse-contents svelte-10mlrw4"><!> <!></div> <!> <!> <!> <!>',1),dE=re('<label class="jse-hidden-input-label svelte-10mlrw4"><input type="text" tabindex="-1" class="jse-hidden-input svelte-10mlrw4"/></label> <!>',1),vE=re('<div class="jse-contents svelte-10mlrw4"><div class="jse-loading-space svelte-10mlrw4"></div> <div class="jse-loading svelte-10mlrw4">loading...</div></div>'),fE=re('<div role="tree" tabindex="-1"><!> <!> <!></div> <!> <!>',1);function sp(e,t){yt(t,!1);var n=R(void 0,!0),o=Zr("jsoneditor:TreeMode"),i=typeof window>"u";o("isSSR:",i);var a=Sl(),s=Sl(),{openAbsolutePopup:l,closeAbsolutePopup:c}=rs("absolute-popup"),u=R(void 0,!0),d=R(void 0,!0),v=R(void 0,!0),f=!1,h=oj(),p=m(t,"readOnly",9),y=m(t,"externalContent",9),j=m(t,"externalSelection",9),b=m(t,"history",9),k=m(t,"truncateTextSize",9),E=m(t,"mainMenuBar",9),O=m(t,"navigationBar",9),w=m(t,"escapeControlCharacters",9),_=m(t,"escapeUnicodeCharacters",9),A=m(t,"parser",9),q=m(t,"parseMemoizeOne",9),C=m(t,"validator",9),z=m(t,"validationParser",9),D=m(t,"pathParser",9),H=m(t,"indentation",9),Q=m(t,"onError",9),fe=m(t,"onChange",9),Ie=m(t,"onChangeMode",9),ge=m(t,"onSelect",9),qe=m(t,"onUndo",9),ce=m(t,"onRedo",9),ve=m(t,"onRenderValue",9),he=m(t,"onRenderMenu",9),Ue=m(t,"onRenderContextMenu",9),Re=m(t,"onClassName",9),we=m(t,"onFocus",9),ue=m(t,"onBlur",9),ie=m(t,"onSortModal",9),vt=m(t,"onTransformModal",9),ft=m(t,"onJSONEditorModal",9),kt=!1,oe=R(!1,!0),Ze=R(void 0,!0);dh({onMount:vo,onDestroy:ra,getWindow:()=>nu(r(v)),hasFocus:()=>kt&&document.hasFocus()||Gp(r(v)),onFocus:()=>{f=!0,we()&&we()()},onBlur:()=>{f=!1,ue()&&ue()()}});var te=R(void 0,!0),X=R(void 0,!0),B=void 0,Ne=!1,ee=R(Vf({json:r(te)}),!0),L=R(Nc(j())?j():void 0,!0);function pt(T){g(L,T)}vo(()=>{if(r(L)){var T=st(r(L));g(ee,la(r(te),r(ee),T,Hu)),setTimeout(()=>Wn(T))}});var ht,_e=R(void 0,!0),at=R(void 0,!0),We=R(void 0,!0),Ye=R(void 0,!0),Tt=R(!1,!0),He=R(!1,!0);function qt(T){g(Ye,(ht=T)?Jy(r(te),ht.items):void 0)}function S(T,ae){return $.apply(this,arguments)}function $(){return($=Pt(function*(T,ae){g(ee,la(r(te),r(ee),T,Hu));var $e=Wt(ae);yield zr(T,{element:$e})})).apply(this,arguments)}function N(){g(Tt,!1),g(He,!1),_t()}function G(T){o("select validation error",T),g(L,rn(T.path)),zr(T.path)}function W(T){var ae=arguments.length>1&&arguments[1]!==void 0?arguments[1]:Jf;o("expand"),g(ee,la(r(te),r(ee),T,ae))}function de(T,ae){g(ee,_m(r(te),r(ee),T,ae)),r(L)&&function($e,et){return Ra(st($e),et)&&(st($e).length>et.length||Hr($e))}(r(L),T)&&g(L,void 0)}var Me=R(!1,!0),pe=R([],!0),le=R(void 0,!0),St=Ec(aj);function lt(T,ae,$e,et){fl(()=>{var ke;try{ke=St(T,ae,$e,et)}catch(Pe){ke=[{path:[],message:"Failed to validate: "+Pe.message,severity:ba.warning}]}Gt(ke,r(pe))||(o("validationErrors changed:",ke),g(pe,ke),g(le,function(Pe,bt){var Nt;return bt.forEach(Qt=>{Nt=Zm(Pe,Nt,Qt.path,(xn,nn)=>De(De({},nn),{},{validationError:Qt}))}),bt.forEach(Qt=>{for(var xn=Qt.path;xn.length>0;)xn=cn(xn),Nt=Zm(Pe,Nt,xn,(nn,Yn)=>Yn.validationError?Yn:De(De({},Yn),{},{validationError:{isChildError:!0,path:xn,message:"Contains invalid data",severity:ba.warning}}))}),Nt}(T,r(pe))))},ke=>o("validationErrors updated in ".concat(ke," ms")))}function Xe(){return o("validate"),B?{parseError:B,isRepairable:!1}:(lt(r(te),C(),A(),z()),gn(r(pe))?void 0:{validationErrors:r(pe)})}function Ae(){return r(te)}function $t(){return r(ee)}function sn(){return r(L)}function Un(T){o("applyExternalContent",{updatedContent:T}),$c(T)?function(ae){if(ae!==void 0){var $e=!Gt(r(te),ae);if(o("update external json",{isChanged:$e,currentlyText:r(te)===void 0}),!!$e){var et={documentState:r(ee),selection:r(L),json:r(te),text:r(X),textIsRepaired:r(Me)};g(te,ae),g(ee,Do(ae,r(ee))),Yt(r(te)),g(X,void 0),g(Me,!1),B=void 0,Zt(r(te)),Dt(et)}}}(T.json):Mc(T)&&function(ae){if(!(ae===void 0||$c(y()))){var $e=ae!==r(X);if(o("update external text",{isChanged:$e}),!!$e){var et={documentState:r(ee),selection:r(L),json:r(te),text:r(X),textIsRepaired:r(Me)};try{g(te,q()(ae)),g(ee,Do(r(te),r(ee))),Yt(r(te)),g(X,ae),g(Me,!1),B=void 0}catch(ke){try{g(te,q()(Aa(ae))),g(ee,Do(r(te),r(ee))),Yt(r(te)),g(X,ae),g(Me,!0),B=void 0,Zt(r(te))}catch{g(te,void 0),g(ee,void 0),g(X,y().text),g(Me,!1),B=r(X)!==void 0&&r(X)!==""?$l(r(X),ke.message||String(ke)):void 0}}Zt(r(te)),Dt(et)}}}(T.text)}function Yt(T){Ne||(Ne=!0,g(ee,Rs(T,r(ee),[])))}function Zt(T){r(L)&&(To(T,_s(r(L)))&&To(T,st(r(L)))||(o("clearing selection: path does not exist anymore",r(L)),g(L,Ys(T,r(ee)))))}function Dt(T){if(T.json!==void 0||T.text!==void 0){var ae=r(te)!==void 0&&T.json!==void 0;b().add({type:"tree",undo:{patch:ae?[{op:"replace",path:"",value:T.json}]:void 0,json:T.json,text:T.text,documentState:T.documentState,textIsRepaired:T.textIsRepaired,selection:Ma(T.selection),sortedColumn:void 0},redo:{patch:ae?[{op:"replace",path:"",value:r(te)}]:void 0,json:r(te),text:r(X),documentState:r(ee),textIsRepaired:r(Me),selection:Ma(r(L)),sortedColumn:void 0}})}}function hn(T,ae){var $e;if(o("patch",T,ae),r(te)===void 0)throw new Error("Cannot apply patch: no JSON");var et=r(te),ke={json:void 0,text:r(X),documentState:r(ee),selection:Ma(r(L)),textIsRepaired:r(Me),sortedColumn:void 0},Pe=Vy(r(te),T),bt=zy(r(te),r(ee),T),Nt=($e=Pl(r(te),T))!==null&&$e!==void 0?$e:r(L),Qt=typeof ae=="function"?ae(bt.json,bt.documentState,Nt):void 0;return g(te,(Qt==null?void 0:Qt.json)!==void 0?Qt.json:bt.json),g(ee,(Qt==null?void 0:Qt.state)!==void 0?Qt.state:bt.documentState),g(L,(Qt==null?void 0:Qt.selection)!==void 0?Qt.selection:Nt),g(X,void 0),g(Me,!1),g(at,void 0),g(We,void 0),B=void 0,Zt(r(te)),b().add({type:"tree",undo:De({patch:Pe},ke),redo:{patch:T,json:void 0,text:r(X),documentState:r(ee),selection:Ma(r(L)),sortedColumn:void 0,textIsRepaired:r(Me)}}),{json:r(te),previousJson:et,undo:Pe,redo:T}}function Hn(){!p()&&r(L)&&g(L,lh(st(r(L))))}function J(){if(!p()&&r(L)){var T=st(r(L)),ae=tt(r(te),T);mr(ae)?function($e,et){o("openJSONEditorModal",{path:$e,value:et}),kt=!0,ft()({content:{json:et},path:$e,onPatch:r(to).onPatch,onClose:()=>{kt=!1,setTimeout(_t)}})}(T,ae):g(L,bd(T))}}function V(){if(!p()&&bn(r(L))){var T=st(r(L)),ae=wt(T),$e=tt(r(te),T),et=!$a(r(te),r(ee),T),ke=et?String($e):Ql(String($e),A());o("handleToggleEnforceString",{enforceString:et,value:$e,updatedValue:ke}),K([{op:"replace",path:ae,value:ke}],(Pe,bt)=>({state:Zd(r(te),bt,T,{type:"value",enforceString:et})}))}}function Ve(){return r(Me)&&r(te)!==void 0&&Ce(r(te)),r(te)!==void 0?{json:r(te)}:{text:r(X)||""}}function ye(){return rt.apply(this,arguments)}function rt(){return rt=Pt(function*(){var T=!(arguments.length>0&&arguments[0]!==void 0)||arguments[0];yield hj({json:r(te),selection:r(L),indentation:T?H():void 0,readOnly:p(),parser:A(),onPatch:K})}),rt.apply(this,arguments)}function dt(){return At.apply(this,arguments)}function At(){return At=Pt(function*(){var T=!(arguments.length>0&&arguments[0]!==void 0)||arguments[0];r(te)!==void 0&&(yield gj({json:r(te),selection:r(L),indentation:T?H():void 0,parser:A()}))}),At.apply(this,arguments)}function en(T){var ae;T.preventDefault(),On((ae=T.clipboardData)===null||ae===void 0?void 0:ae.getData("text/plain"))}function Vt(){return Ht.apply(this,arguments)}function Ht(){return(Ht=Pt(function*(){try{On(yield navigator.clipboard.readText())}catch(T){console.error(T),g(oe,!0)}})).apply(this,arguments)}function On(T){T!==void 0&&mj({clipboardText:T,json:r(te),selection:r(L),readOnly:p(),parser:A(),onPatch:K,onChangeText:P,onPasteMultilineText:Ct,openRepairModal:dn})}function dn(T,ae){g(Ze,{text:T,onParse:$e=>tu($e,et=>eu(et,A())),onRepair:yy,onApply:ae,onClose:_t})}function Qn(){bj({json:r(te),text:r(X),selection:r(L),keepSelection:!1,readOnly:p(),onChange:fe(),onPatch:K})}function Kn(){!p()&&r(te)!==void 0&&r(L)&&dl&&!gn(st(r(L)))&&(o("duplicate",{selection:r(L)}),K(Uy(r(te),ts(r(te),r(L)))))}function Bn(){p()||!r(L)||!Jn(r(L))&&!bn(r(L))||gn(st(r(L)))||(o("extract",{selection:r(L)}),K(By(r(te),r(L)),(T,ae)=>{if(mr(T))return{state:Jv(T,ae,[])}}))}function Zn(T){Ed({insertType:T,selectInside:!0,initialValue:void 0,json:r(te),selection:r(L),readOnly:p(),parser:A(),onPatch:K,onReplaceJson:Ce})}function yr(T){Yr(r(L))&&g(L,rn(r(L).path)),r(L)||g(L,Ys(r(te),r(ee))),Zn(T)}function Fn(T){if(!p()&&r(L))if(Mu(r(L)))try{var ae=_s(r(L)),$e=tt(r(te),ae),et=function(Pe,bt,Nt){if(bt==="array"){if(Array.isArray(Pe))return Pe;if(Cn(Pe))return fm(Pe);if(typeof Pe=="string")try{var Qt=Nt.parse(Pe);if(Array.isArray(Qt))return Qt;if(Cn(Qt))return fm(Qt)}catch{return[Pe]}return[Pe]}if(bt==="object"){if(Array.isArray(Pe))return vm(Pe);if(Cn(Pe))return Pe;if(typeof Pe=="string")try{var xn=Nt.parse(Pe);if(Cn(xn))return xn;if(Array.isArray(xn))return vm(xn)}catch{return{value:Pe}}return{value:Pe}}if(bt==="value")return mr(Pe)?Nt.stringify(Pe):Pe;throw new Error("Cannot convert ".concat(Hp(Pe,Nt)," to ").concat(bt))}($e,T,A());if(et===$e)return;var ke=[{op:"replace",path:wt(ae),value:et}];o("handleConvert",{selection:r(L),path:ae,type:T,operations:ke}),K(ke,(Pe,bt)=>({state:r(L)?Rs(Pe,bt,st(r(L))):r(ee)}))}catch(Pe){Q()(Pe)}else Q()(new Error("Cannot convert current selection to ".concat(T)))}function $n(){if(r(L)){var T=$m(r(te),r(ee),r(L),!1),ae=cn(st(r(L)));T&&!gn(st(T))&&Gt(ae,cn(st(T)))?g(L,ci(st(T))):g(L,mi(ae)),o("insert before",{selection:r(L),selectionBefore:T,parentPath:ae}),Xn(),vn()}}function ar(){if(r(L)){var T=Ki(r(te),r(L));o("insert after",T),g(L,ci(T)),Xn(),vn()}}function Se(T){return Ee.apply(this,arguments)}function Ee(){return(Ee=Pt(function*(T){yield yj({char:T,selectInside:!0,json:r(te),selection:r(L),readOnly:p(),parser:A(),onPatch:K,onReplaceJson:Ce,onSelect:pt})})).apply(this,arguments)}function tn(){if(!p()&&b().canUndo){var T=b().undo();if(gd(T)){var ae={json:r(te),text:r(X)};g(te,T.undo.patch?ga(r(te),T.undo.patch):T.undo.json),g(ee,T.undo.documentState),g(L,T.undo.selection),g(X,T.undo.text),g(Me,T.undo.textIsRepaired),B=void 0,o("undo",{item:T,json:r(te),documentState:r(ee),selection:r(L)}),ir(ae,T.undo.patch&&T.redo.patch?{json:r(te),previousJson:ae.json,redo:T.undo.patch,undo:T.redo.patch}:void 0),_t(),r(L)&&zr(st(r(L)),{scrollToWhenVisible:!1})}else qe()(T)}}function Ar(){if(!p()&&b().canRedo){var T=b().redo();if(gd(T)){var ae={json:r(te),text:r(X)};g(te,T.redo.patch?ga(r(te),T.redo.patch):T.redo.json),g(ee,T.redo.documentState),g(L,T.redo.selection),g(X,T.redo.text),g(Me,T.redo.textIsRepaired),B=void 0,o("redo",{item:T,json:r(te),documentState:r(ee),selection:r(L)}),ir(ae,T.undo.patch&&T.redo.patch?{json:r(te),previousJson:ae.json,redo:T.redo.patch,undo:T.undo.patch}:void 0),_t(),r(L)&&zr(st(r(L)),{scrollToWhenVisible:!1})}else ce()(T)}}function jr(T){var ae;p()||r(te)===void 0||(kt=!0,ie()({id:a,json:r(te),rootPath:T,onSort:(ae=Pt(function*($e){var{operations:et}=$e;o("onSort",T,et),K(et,(ke,Pe)=>({state:Jv(ke,Pe,T),selection:rn(T)}))}),function($e){return ae.apply(this,arguments)}),onClose:()=>{kt=!1,setTimeout(_t)}}))}function on(){r(L)&&jr(zm(r(te),r(L)))}function dr(){jr([])}function vr(T){if(r(te)!==void 0){var{id:ae,onTransform:$e,onClose:et}=T,ke=T.rootPath||[];kt=!0,vt()({id:ae||s,json:r(te),rootPath:ke,onTransform:Pe=>{$e?$e({operations:Pe,json:r(te),transformedJson:ga(r(te),Pe)}):(o("onTransform",ke,Pe),K(Pe,(bt,Nt)=>({state:Jv(bt,Nt,ke),selection:rn(ke)})))},onClose:()=>{kt=!1,setTimeout(_t),et&&et()}})}}function Br(){r(L)&&vr({rootPath:zm(r(te),r(L))})}function eo(){vr({rootPath:[]})}function zr(T){return Pn.apply(this,arguments)}function Pn(){return Pn=Pt(function*(T){var{scrollToWhenVisible:ae=!0,element:$e}=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{};g(ee,la(r(te),r(ee),T,Hu));var et=$e??yn(T);if(o("scrollTo",{path:T,elem:et,refContents:r(u)}),!et||!r(u))return Promise.resolve();var ke=r(u).getBoundingClientRect(),Pe=et.getBoundingClientRect();if(!ae&&Pe.bottom>ke.top&&Pe.top<ke.bottom)return Promise.resolve();var bt=-ke.height/4;return new Promise(Nt=>{h(et,{container:r(u),offset:bt,duration:300,callback:()=>Nt()})})}),Pn.apply(this,arguments)}function yn(T){var ae,$e;return Xn(),(ae=($e=r(u))===null||$e===void 0?void 0:$e.querySelector('div[data-path="'.concat(Ju(T),'"]')))!==null&&ae!==void 0?ae:void 0}function Wt(T){var ae,$e;return Xn(),(ae=($e=r(u))===null||$e===void 0?void 0:$e.querySelector('span[data-search-result-index="'.concat(T,'"]')))!==null&&ae!==void 0?ae:void 0}function Wn(T){var ae=yn(T);if(ae&&r(u)){var $e=r(u).getBoundingClientRect(),et=ae.getBoundingClientRect(),ke=mr(tt(r(te),T))?20:et.height;et.top<$e.top+20?h(ae,{container:r(u),offset:-20,duration:0}):et.top+ke>$e.bottom-20&&h(ae,{container:r(u),offset:-($e.height-ke-20),duration:0})}}function ir(T,ae){if(T.json!==void 0||(T==null?void 0:T.text)!==void 0){if(r(X)!==void 0){var $e,et={text:r(X),json:void 0};($e=fe())===null||$e===void 0||$e(et,T,{contentErrors:Xe(),patchResult:ae})}else if(r(te)!==void 0){var ke,Pe={text:void 0,json:r(te)};(ke=fe())===null||ke===void 0||ke(Pe,T,{contentErrors:Xe(),patchResult:ae})}}}function K(T,ae){o("handlePatch",T,ae);var $e={json:r(te),text:r(X)},et=hn(T,ae);return ir($e,et),et}function Ce(T,ae){var $e={json:r(te),text:r(X)},et={documentState:r(ee),selection:r(L),json:r(te),text:r(X),textIsRepaired:r(Me)},ke=la(r(te),Do(T,r(ee)),[],fc),Pe=typeof ae=="function"?ae(T,ke,r(L)):void 0;g(te,(Pe==null?void 0:Pe.json)!==void 0?Pe.json:T),g(ee,(Pe==null?void 0:Pe.state)!==void 0?Pe.state:ke),g(L,(Pe==null?void 0:Pe.selection)!==void 0?Pe.selection:r(L)),g(X,void 0),g(Me,!1),B=void 0,Zt(r(te)),Dt(et),ir($e,void 0)}function P(T,ae){o("handleChangeText");var $e={json:r(te),text:r(X)},et={documentState:r(ee),selection:r(L),json:r(te),text:r(X),textIsRepaired:r(Me)};try{g(te,q()(T)),g(ee,la(r(te),Do(r(te),r(ee)),[],fc)),g(X,void 0),g(Me,!1),B=void 0}catch(Pe){try{g(te,q()(Aa(T))),g(ee,la(r(te),Do(r(te),r(ee)),[],fc)),g(X,T),g(Me,!0),B=void 0}catch{g(te,void 0),g(ee,Vf({json:r(te),expand:fc})),g(X,T),g(Me,!1),B=r(X)!==""?$l(r(X),Pe.message||String(Pe)):void 0}}if(typeof ae=="function"){var ke=ae(r(te),r(ee),r(L));g(te,(ke==null?void 0:ke.json)!==void 0?ke.json:r(te)),g(ee,(ke==null?void 0:ke.state)!==void 0?ke.state:r(ee)),g(L,(ke==null?void 0:ke.selection)!==void 0?ke.selection:r(L))}Zt(r(te)),Dt(et),ir($e,void 0)}function Z(T,ae){var $e=arguments.length>2&&arguments[2]!==void 0&&arguments[2];o("handleExpand",{path:T,expanded:ae,recursive:$e}),ae?W(T,$e?sh:Jf):de(T,$e),_t()}function xe(){Z([],!0,!0)}function ot(){Z([],!1,!0)}function Qe(T){o("openFind",{findAndReplace:T}),g(Tt,!1),g(He,!1),Xn(),g(Tt,!0),g(He,T)}function Je(T,ae){o("handleExpandSection",T,ae),g(ee,function($e,et,ke,Pe){return zl($e,et,ke,(bt,Nt)=>{if(!Gr(Nt))return Nt;var Qt=My(Nt.visibleSections.concat(Pe));return De(De({},Nt),{},{visibleSections:Qt})})}(r(te),r(ee),T,ae))}function Lt(T){o("pasted json as text",T),g(at,T)}function Ct(T){o("pasted multiline text",{pastedText:T}),g(We,T)}function jn(T){var ae,{anchor:$e,left:et,top:ke,width:Pe,height:bt,offsetTop:Nt,offsetLeft:Qt,showTip:xn}=T,nn=function(Rn){var{json:tr,documentState:wn,selection:Et,readOnly:fn,onEditKey:In,onEditValue:xr,onToggleEnforceString:_r,onCut:ct,onCopy:Jt,onPaste:ur,onRemove:no,onDuplicate:fo,onExtract:Er,onInsertBefore:ao,onInsert:Va,onConvert:zo,onInsertAfter:aa,onSort:Oa,onTransform:ia}=Rn,Qr=tr!==void 0,Fr=!!Et,wo=!!Et&&gn(st(Et)),Wo=Et?tt(tr,st(Et)):void 0,Ja=Array.isArray(Wo)?"Edit array":Cn(Wo)?"Edit object":"Edit value",mn=Qr&&(Jn(Et)||Yr(Et)||bn(Et)),Rr=Et&&!wo?tt(tr,cn(st(Et))):void 0,Po=!fn&&Qr&&md(Et)&&!wo&&!Array.isArray(Rr),ki=!fn&&Qr&&Et!==void 0&&md(Et),Js=ki&&!mr(Wo),as=!fn&&mn,is=mn,su=!fn&&Fr,dv=!fn&&Qr&&mn&&!wo,vv=!fn&&Qr&&Et!==void 0&&(Jn(Et)||bn(Et))&&!wo,_a=mn,ss=_a?"Convert to:":"Insert:",fv=!fn&&(Hr(Et)&&Array.isArray(Wo)||_o(Et)&&Array.isArray(Rr)),pv=!fn&&(_a?Mu(Et)&&!Cn(Wo):Fr),hv=!fn&&(_a?Mu(Et)&&!Array.isArray(Wo):Fr),gv=!fn&&(_a?Mu(Et)&&mr(Wo):Fr),Ir=Et!==void 0&&$a(tr,wn,st(Et));function yo(ls){mn?ls!=="structure"&&zo(ls):Va(ls)}return[{type:"row",items:[{type:"button",onClick:()=>In(),icon:pl,text:"Edit key",title:"Edit the key (Double-click on the key)",disabled:!Po},{type:"dropdown-button",main:{type:"button",onClick:()=>xr(),icon:pl,text:Ja,title:"Edit the value (Double-click on the value)",disabled:!ki},width:"11em",items:[{type:"button",icon:pl,text:Ja,title:"Edit the value (Double-click on the value)",onClick:()=>xr(),disabled:!ki},{type:"button",icon:Ir?nb:ab,text:"Enforce string",title:"Enforce keeping the value as string when it contains a numeric value",onClick:()=>_r(),disabled:!Js}]}]},{type:"separator"},{type:"row",items:[{type:"dropdown-button",main:{type:"button",onClick:()=>ct(!0),icon:hl,text:"Cut",title:"Cut selected contents, formatted with indentation (Ctrl+X)",disabled:!as},width:"10em",items:[{type:"button",icon:hl,text:"Cut formatted",title:"Cut selected contents, formatted with indentation (Ctrl+X)",onClick:()=>ct(!0),disabled:!as},{type:"button",icon:hl,text:"Cut compacted",title:"Cut selected contents, without indentation (Ctrl+Shift+X)",onClick:()=>ct(!1),disabled:!as}]},{type:"dropdown-button",main:{type:"button",onClick:()=>Jt(!0),icon:Ri,text:"Copy",title:"Copy selected contents, formatted with indentation (Ctrl+C)",disabled:!is},width:"12em",items:[{type:"button",icon:Ri,text:"Copy formatted",title:"Copy selected contents, formatted with indentation (Ctrl+C)",onClick:()=>Jt(!0),disabled:!is},{type:"button",icon:Ri,text:"Copy compacted",title:"Copy selected contents, without indentation (Ctrl+Shift+C)",onClick:()=>Jt(!1),disabled:!is}]},{type:"button",onClick:()=>ur(),icon:Z1,text:"Paste",title:"Paste clipboard contents (Ctrl+V)",disabled:!su}]},{type:"separator"},{type:"row",items:[{type:"column",items:[{type:"button",onClick:()=>fo(),icon:tb,text:"Duplicate",title:"Duplicate selected contents (Ctrl+D)",disabled:!dv},{type:"button",onClick:()=>Er(),icon:US,text:"Extract",title:"Extract selected contents",disabled:!vv},{type:"button",onClick:()=>Oa(),icon:sd,text:"Sort",title:"Sort array or object contents",disabled:fn||!mn},{type:"button",onClick:()=>ia(),icon:ad,text:"Transform",title:"Transform array or object contents (filter, sort, project)",disabled:fn||!mn},{type:"button",onClick:()=>no(),icon:xf,text:"Remove",title:"Remove selected contents (Delete)",disabled:fn||!mn}]},{type:"column",items:[{type:"label",text:ss},{type:"button",onClick:()=>yo("structure"),icon:_a?mu:il,text:"Structure",title:ss+" structure like the first item in the array",disabled:!fv},{type:"button",onClick:()=>yo("object"),icon:_a?mu:il,text:"Object",title:ss+" object",disabled:!pv},{type:"button",onClick:()=>yo("array"),icon:_a?mu:il,text:"Array",title:ss+" array",disabled:!hv},{type:"button",onClick:()=>yo("value"),icon:_a?mu:il,text:"Value",title:ss+" value",disabled:!gv}]}]},{type:"separator"},{type:"row",items:[{type:"button",onClick:()=>ao(),icon:eC,text:"Insert before",title:"Select area before current entry to insert or paste contents",disabled:fn||!mn||wo},{type:"button",onClick:()=>aa(),icon:FS,text:"Insert after",title:"Select area after current entry to insert or paste contents",disabled:fn||!mn||wo}]}]}({json:r(te),documentState:r(ee),selection:r(L),readOnly:p(),onEditKey:Hn,onEditValue:J,onToggleEnforceString:V,onCut:ye,onCopy:dt,onPaste:Vt,onRemove:Qn,onDuplicate:Kn,onExtract:Bn,onInsertBefore:$n,onInsert:yr,onInsertAfter:ar,onConvert:Fn,onSort:on,onTransform:Br}),Yn=(ae=Ue()(nn))!==null&&ae!==void 0?ae:nn;if(Yn!==!1){var Ut={left:et,top:ke,offsetTop:Nt,offsetLeft:Qt,width:Pe,height:bt,anchor:$e,closeOnOuterClick:!0,onClose:()=>{kt=!1,_t()}};kt=!0;var cr=l(xj,{tip:xn?"Tip: you can open this context menu via right-click or with Ctrl+Q":void 0,items:Yn,onRequestClose:()=>c(cr)},Ut)}}function vn(T){if(!Kr(r(L)))if(T&&(T.stopPropagation(),T.preventDefault()),T&&T.type==="contextmenu"&&T.target!==r(d))jn({left:T.clientX,top:T.clientY,width:ri,height:ni,showTip:!1});else{var ae,$e=(ae=r(u))===null||ae===void 0?void 0:ae.querySelector(".jse-context-menu-pointer.jse-selected");if($e)jn({anchor:$e,offsetTop:2,width:ri,height:ni,showTip:!1});else{var et,ke=(et=r(u))===null||et===void 0?void 0:et.getBoundingClientRect();ke&&jn({top:ke.top+2,left:ke.left+2,width:ri,height:ni,showTip:!1})}}}function er(T){jn({anchor:Ey(T.target,"BUTTON"),offsetTop:0,width:ri,height:ni,showTip:!0})}function Ot(){return an.apply(this,arguments)}function an(){return(an=Pt(function*(){if(o("apply pasted json",r(at)),r(at)){var{onPasteAsJson:T}=r(at);g(at,void 0),T(),setTimeout(_t)}})).apply(this,arguments)}function fr(){return Gn.apply(this,arguments)}function Gn(){return(Gn=Pt(function*(){o("apply pasted multiline text",r(We)),r(We)&&(On(JSON.stringify(r(We))),setTimeout(_t))})).apply(this,arguments)}function Nn(){o("clear pasted json"),g(at,void 0),_t()}function Ke(){o("clear pasted multiline text"),g(We,void 0),_t()}function zn(){Ie()(Mr.text)}function sr(T){g(L,T),_t(),zr(st(T))}function _t(){o("focus"),r(d)&&(r(d).focus(),r(d).select())}function _n(T){return function(ae,$e,et){var ke=cn(et),Pe=[Xt(et)],bt=tt(ae,ke),Nt=bt?Vv(bt,$e,Pe):void 0;return Nt?rn(ke.concat(Nt)):ci(et)}(r(te),r(ee),T)}function lr(T){r(n)&&r(n).onDrag(T)}function Nr(){r(n)&&r(n).onDragEnd()}var to=R(void 0,!0);ne(()=>r(L),()=>{var T;T=r(L),Gt(T,j())||(o("onSelect",T),ge()(T))}),ne(()=>(x(w()),x(_())),()=>{g(_e,Qp({escapeControlCharacters:w(),escapeUnicodeCharacters:_()}))}),ne(()=>r(Tt),()=>{(function(T){r(u)&&T&&r(u).scrollTop===0&&(Lo(u,r(u).style.overflowAnchor="none"),Lo(u,r(u).scrollTop+=vc),setTimeout(()=>{r(u)&&Lo(u,r(u).style.overflowAnchor="")}))})(r(Tt))}),ne(()=>x(y()),()=>{Un(y())}),ne(()=>x(j()),()=>{(function(T){Gt(r(L),T)||(o("applyExternalSelection",{selection:r(L),externalSelection:T}),Nc(T)&&g(L,T))})(j())}),ne(()=>(r(te),x(C()),x(A()),x(z())),()=>{lt(r(te),C(),A(),z())}),ne(()=>(r(u),Xm),()=>{g(n,r(u)?Xm(r(u)):void 0)}),ne(()=>(x(p()),x(k()),x(A()),r(_e),x(ve()),x(Re())),()=>{g(to,{mode:Mr.tree,readOnly:p(),truncateTextSize:k(),parser:A(),normalization:r(_e),getJson:Ae,getDocumentState:$t,getSelection:sn,findElement:yn,findNextInside:_n,focus:_t,onPatch:K,onInsert:Zn,onExpand:Z,onSelect:pt,onFind:Qe,onExpandSection:Je,onPasteJson:Lt,onRenderValue:ve(),onContextMenu:jn,onClassName:Re()||(()=>{}),onDrag:lr,onDragEnd:Nr})}),ne(()=>r(to),()=>{o("context changed",r(to))}),Mn();var bo={expand:W,collapse:de,validate:Xe,getJson:Ae,patch:hn,acceptAutoRepair:Ve,openTransformModal:vr,scrollTo:zr,findElement:yn,findSearchResult:Wt,focus:_t};Ft(!0);var jo=fE();ze("mousedown",li,function(T){!Kl(T.target,ae=>ae===r(v))&&Kr(r(L))&&(o("click outside the editor, exit edit mode"),g(L,Ma(r(L))),f&&r(d)&&(r(d).focus(),r(d).blur()),o("blur (outside editor)"),r(d)&&r(d).blur())});var M,se=Mt(jo),Te=I(se),Be=T=>{(function(ae,$e){yt($e,!1);var et=R(void 0,!0),ke=R(void 0,!0),Pe=R(void 0,!0),bt=m($e,"json",9),Nt=m($e,"selection",9),Qt=m($e,"readOnly",9),xn=m($e,"showSearch",13,!1),nn=m($e,"history",9),Yn=m($e,"onExpandAll",9),Ut=m($e,"onCollapseAll",9),cr=m($e,"onUndo",9),Rn=m($e,"onRedo",9),tr=m($e,"onSort",9),wn=m($e,"onTransform",9),Et=m($e,"onContextMenu",9),fn=m($e,"onCopy",9),In=m($e,"onRenderMenu",9);function xr(){xn(!xn())}var _r=R(void 0,!0),ct=R(void 0,!0),Jt=R(void 0,!0),ur=R(void 0,!0);ne(()=>x(bt()),()=>{g(et,bt()!==void 0)}),ne(()=>(r(et),x(Nt()),bn),()=>{g(ke,r(et)&&(Jn(Nt())||Yr(Nt())||bn(Nt())))}),ne(()=>(x(Yn()),x(bt())),()=>{g(_r,{type:"button",icon:cj,title:"Expand all",className:"jse-expand-all",onClick:Yn(),disabled:!mr(bt())})}),ne(()=>(x(Ut()),x(bt())),()=>{g(ct,{type:"button",icon:uj,title:"Collapse all",className:"jse-collapse-all",onClick:Ut(),disabled:!mr(bt())})}),ne(()=>x(bt()),()=>{g(Jt,{type:"button",icon:Jd,title:"Search (Ctrl+F)",className:"jse-search",onClick:xr,disabled:bt()===void 0})}),ne(()=>(x(Qt()),r(_r),r(ct),x(tr()),x(bt()),x(wn()),r(Jt),x(Et()),x(cr()),x(nn()),x(Rn()),x(fn()),r(ke)),()=>{g(ur,Qt()?[r(_r),r(ct),{type:"separator"},{type:"button",icon:Ri,title:"Copy (Ctrl+C)",className:"jse-copy",onClick:fn(),disabled:!r(ke)},{type:"separator"},r(Jt),{type:"space"}]:[r(_r),r(ct),{type:"separator"},{type:"button",icon:sd,title:"Sort",className:"jse-sort",onClick:tr(),disabled:Qt()||bt()===void 0},{type:"button",icon:ad,title:"Transform contents (filter, sort, project)",className:"jse-transform",onClick:wn(),disabled:Qt()||bt()===void 0},r(Jt),{type:"button",icon:eb,title:Zp,className:"jse-contextmenu",onClick:Et()},{type:"separator"},{type:"button",icon:Pp,title:"Undo (Ctrl+Z)",className:"jse-undo",onClick:cr(),disabled:!nn().canUndo},{type:"button",icon:zp,title:"Redo (Ctrl+Shift+Z)",className:"jse-redo",onClick:Rn(),disabled:!nn().canRedo},{type:"space"}])}),ne(()=>(x(In()),r(ur)),()=>{g(Pe,In()(r(ur))||r(ur))}),Mn(),Ft(!0),av(ae,{get items(){return r(Pe)}}),jt()})(T,{get json(){return r(te)},get selection(){return r(L)},get readOnly(){return p()},get history(){return b()},onExpandAll:xe,onCollapseAll:ot,onUndo:tn,onRedo:Ar,onSort:dr,onTransform:eo,onContextMenu:er,onCopy:dt,get onRenderMenu(){return he()},get showSearch(){return r(Tt)},set showSearch(ae){g(Tt,ae)},$$legacy:!0})};be(Te,T=>{E()&&T(Be)});var Oe=Y(Te,2),Ge=T=>{L_(T,{get json(){return r(te)},get selection(){return r(L)},onSelect:sr,get onError(){return Q()},get pathParser(){return D()}})};be(Oe,T=>{O()&&T(Ge)});var Fe=Y(Oe,2),mt=T=>{var ae=dE(),$e=Mt(ae),et=I($e);et.readOnly=!0,or(et,Nt=>g(d,Nt),()=>r(d));var ke=Y($e,2),Pe=Nt=>{var Qt=br(),xn=Mt(Qt),nn=Ut=>{(function(cr,Rn){function tr(_r){_r.stopPropagation(),Rn.onCreateObject()}function wn(_r){_r.stopPropagation(),Rn.onCreateArray()}yt(Rn,!0);var Et=__(),fn=Y(I(Et),2),In=Y(I(fn),2),xr=_r=>{var ct=O_(),Jt=Y(Mt(ct),2);Tn(Jt,"title","Create an empty JSON object (press '{')");var ur=Y(Jt,2);Tn(ur,"title","Create an empty JSON array (press '[')"),ha("click",Jt,tr),ha("click",ur,wn),U(_r,ct)};be(In,_r=>{Rn.readOnly||_r(xr)}),ha("click",Et,()=>Rn.onClick()),U(cr,Et),jt()})(Ut,{get readOnly(){return p()},onCreateObject:()=>{_t(),Se("{")},onCreateArray:()=>{_t(),Se("[")},onClick:()=>{_t()}})},Yn=Ut=>{var cr=lE(),Rn=Mt(cr),tr=nt(()=>p()?[]:[{icon:id,text:"Repair manually",title:'Open the document in "code" mode and repair it manually',onClick:zn}]);Fo(Rn,{type:"error",message:"The loaded JSON document is invalid and could not be repaired automatically.",get actions(){return r(tr)}}),jj(Y(Rn,2),{get text(){return r(X)},get json(){return r(te)},get indentation(){return H()},get parser(){return A()}}),U(Ut,cr)};be(xn,Ut=>{r(X)===""||r(X)===void 0?Ut(nn):Ut(Yn,-1)}),U(Nt,Qt)},bt=Nt=>{var Qt=uE(),xn=Mt(Qt);vj(I(xn),{get json(){return r(te)},get documentState(){return r(ee)},get parser(){return A()},get showSearch(){return r(Tt)},get showReplace(){return r(He)},get readOnly(){return p()},columns:void 0,onSearch:qt,onFocus:S,onPatch:K,onClose:N});var nn=Y(xn,2);Tn(nn,"data-jsoneditor-scrollable-contents",!0);var Yn=I(nn),Ut=In=>{U(In,cE())};be(Yn,In=>{r(Tt)&&In(Ut)}),tp(Y(Yn,2),{get value(){return r(te)},pointer:"",get state(){return r(ee)},get validationErrors(){return r(le)},get searchResults(){return r(Ye)},get selection(){return r(L)},get context(){return r(to)},get onDragSelectionStart(){return Dr}}),or(nn,In=>g(u,In),()=>r(u));var cr=Y(nn,2),Rn=In=>{var xr=nt(()=>(r(at),F(()=>"You pasted a JSON ".concat(Array.isArray(r(at).contents)?"array":"object"," as text")))),_r=nt(()=>[{icon:Yi,text:"Paste as JSON instead",title:"Replace the value with the pasted JSON",onMouseDown:Ot},{text:"Leave as is",title:"Keep the JSON embedded in the value",onClick:Nn}]);Fo(In,{type:"info",get message(){return r(xr)},get actions(){return r(_r)}})};be(cr,In=>{r(at)&&In(Rn)});var tr=Y(cr,2),wn=In=>{var xr=nt(()=>[{icon:Yi,text:"Paste as string instead",title:"Paste the clipboard data as a single string value instead of an array",onClick:fr},{text:"Leave as is",title:"Keep the pasted array",onClick:Ke}]);Fo(In,{type:"info",message:"Multiline text was pasted as array",get actions(){return r(xr)}})};be(tr,In=>{r(We)&&In(wn)});var Et=Y(tr,2),fn=In=>{var xr=nt(()=>p()?[]:[{icon:Ap,text:"Ok",title:"Accept the repaired document",onClick:Ve},{icon:id,text:"Repair manually instead",title:"Leave the document unchanged and repair it manually instead",onClick:zn}]);Fo(In,{type:"success",message:"The loaded JSON document was invalid but is successfully repaired.",get actions(){return r(xr)},onClose:_t})};be(Et,In=>{r(Me)&&In(fn)}),vh(Y(Et,2),{get validationErrors(){return r(pe)},selectError:G}),U(Nt,Qt)};be(ke,Nt=>{r(te)===void 0?Nt(Pe):Nt(bt,-1)}),ze("paste",et,en),U(T,ae)},it=T=>{U(T,vE())};be(Fe,T=>{i?T(it,-1):T(mt)}),or(se,T=>g(v,T),()=>r(v));var ut=Y(se,2),ln=T=>{ij(T,{onClose:()=>g(oe,!1)})};be(ut,T=>{r(oe)&&T(ln)});var An=Y(ut,2),xo=T=>{sj(T,Hi(()=>r(Ze),{onClose:()=>{var ae;(ae=r(Ze))===null||ae===void 0||ae.onClose(),g(Ze,void 0)}}))};return be(An,T=>{r(Ze)&&T(xo)}),Le(()=>M=Bt(se,1,"jse-tree-mode svelte-10mlrw4",null,M,{"no-main-menu":!E()})),ze("keydown",se,function(T){var ae=hi(T),$e=T.shiftKey;if(o("keydown",{combo:ae,key:T.key}),ae==="Ctrl+X"&&(T.preventDefault(),ye(!0)),ae==="Ctrl+Shift+X"&&(T.preventDefault(),ye(!1)),ae==="Ctrl+C"&&(T.preventDefault(),dt(!0)),ae==="Ctrl+Shift+C"&&(T.preventDefault(),dt(!1)),ae==="Ctrl+D"&&(T.preventDefault(),Kn()),ae!=="Delete"&&ae!=="Backspace"||(T.preventDefault(),Qn()),ae==="Insert"&&(T.preventDefault(),Zn("structure")),ae==="Ctrl+A"&&(T.preventDefault(),g(L,rn([]))),ae==="Ctrl+Q"&&vn(T),ae==="ArrowUp"||ae==="Shift+ArrowUp"){T.preventDefault();var et=r(L)?$m(r(te),r(ee),r(L),$e)||r(L):Ys(r(te),r(ee));g(L,et),Wn(st(et))}if(ae==="ArrowDown"||ae==="Shift+ArrowDown"){T.preventDefault();var ke=r(L)?function(nn,Yn,Ut){var cr=arguments.length>3&&arguments[3]!==void 0&&arguments[3];if(Ut){var Rn=cr?st(Ut):Ki(nn,Ut),tr=mr(tt(nn,Rn))?_m(nn,Yn,Rn,!0):Yn,wn=Vv(nn,Yn,Rn),Et=Vv(nn,tr,Rn);if(cr)return Hr(Ut)?wn!==void 0?po(wn,wn):void 0:_o(Ut)?Et!==void 0?po(Et,Et):void 0:Et!==void 0?po(_s(Ut),Et):void 0;if(_o(Ut))return Et!==void 0?rn(Et):void 0;if(Hr(Ut)||bn(Ut))return wn!==void 0?rn(wn):void 0;if(Yr(Ut)){if(wn===void 0||wn.length===0)return;var fn=cn(wn),In=tt(nn,fn);return Array.isArray(In)?rn(wn):gi(wn)}return Jn(Ut)?Et!==void 0?rn(Et):wn!==void 0?rn(wn):void 0:void 0}}(r(te),r(ee),r(L),$e)||r(L):Ys(r(te),r(ee));g(L,ke),Wn(st(ke))}if(ae==="ArrowLeft"||ae==="Shift+ArrowLeft"){T.preventDefault();var Pe=r(L)?function(nn,Yn,Ut){var cr=arguments.length>3&&arguments[3]!==void 0&&arguments[3],Rn=!(arguments.length>4&&arguments[4]!==void 0)||arguments[4];if(Ut){var{caret:tr,previous:wn}=Am(nn,Yn,Ut,Rn);if(cr)return Jn(Ut)?void 0:po(Ut.path,Ut.path);if(tr&&wn)return Hf(wn);var Et=cn(st(Ut)),fn=tt(nn,Et);return bn(Ut)&&Array.isArray(fn)?po(Ut.path,Ut.path):Jn(Ut)&&!Array.isArray(fn)?gi(Ut.focusPath):void 0}}(r(te),r(ee),r(L),$e,!p())||r(L):Ys(r(te),r(ee));g(L,Pe),Wn(st(Pe))}if(ae==="ArrowRight"||ae==="Shift+ArrowRight"){T.preventDefault();var bt=r(L)&&r(te)!==void 0?function(nn,Yn,Ut){var cr=arguments.length>3&&arguments[3]!==void 0&&arguments[3],Rn=!(arguments.length>4&&arguments[4]!==void 0)||arguments[4];if(Ut){var{caret:tr,next:wn}=Am(nn,Yn,Ut,Rn);return cr?Jn(Ut)?void 0:po(Ut.path,Ut.path):tr&&wn?Hf(wn):Jn(Ut)?rn(Ut.focusPath):void 0}}(r(te),r(ee),r(L),$e,!p())||r(L):Ys(r(te),r(ee));g(L,bt),Wn(st(bt))}if(ae==="Enter"&&r(L)){if(ev(r(L))){var Nt=r(L).focusPath,Qt=tt(r(te),cn(Nt));Array.isArray(Qt)&&(T.preventDefault(),g(L,rn(Nt)))}Yr(r(L))&&(T.preventDefault(),g(L,De(De({},r(L)),{},{edit:!0}))),bn(r(L))&&(T.preventDefault(),mr(tt(r(te),r(L).path))?Z(r(L).path,!0):g(L,De(De({},r(L)),{},{edit:!0})))}if(ae.replace(/^Shift\+/,"").length===1&&r(L))return T.preventDefault(),void Se(T.key);if(ae==="Enter"&&(_o(r(L))||Hr(r(L))))return T.preventDefault(),void Se("");if(ae==="Ctrl+Enter"&&bn(r(L))){var xn=tt(r(te),r(L).path);Xd(xn)&&window.open(String(xn),"_blank")}ae==="Escape"&&r(L)&&(T.preventDefault(),g(L,void 0)),ae==="Ctrl+F"&&(T.preventDefault(),Qe(!1)),ae==="Ctrl+H"&&(T.preventDefault(),Qe(!0)),ae==="Ctrl+Z"&&(T.preventDefault(),tn()),ae==="Ctrl+Shift+Z"&&(T.preventDefault(),Ar())}),ze("mousedown",se,function(T){o("handleMouseDown",T);var ae=T.target;_y(ae,"BUTTON")||ae.isContentEditable||(_t(),r(L)||r(te)!==void 0||r(X)!==""&&r(X)!==void 0||(o("createDefaultSelection"),g(L,rn([]))))}),ze("contextmenu",se,vn),U(e,jo),Rt(t,"expand",W),Rt(t,"collapse",de),Rt(t,"validate",Xe),Rt(t,"getJson",Ae),Rt(t,"patch",hn),Rt(t,"acceptAutoRepair",Ve),Rt(t,"openTransformModal",vr),Rt(t,"scrollTo",zr),Rt(t,"findElement",yn),Rt(t,"findSearchResult",Wt),Rt(t,"focus",_t),jt(bo)}function wj(e){return typeof(t=e)!="object"||t===null?e:new Proxy(e,{get:(n,o,i)=>wj(Reflect.get(n,o,i)),set:()=>!1,deleteProperty:()=>!1});var t}var qu=Zr("jsoneditor:History");function kj(){var e=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{},t=e.maxItems||1e3,n=[],o=0;function i(){return o<n.length}function a(){return o>0}function s(){return{canUndo:i(),canRedo:a(),items:()=>n.slice().reverse(),add:c,undo:d,redo:v,clear:u}}function l(){e.onChange&&e.onChange(s())}function c(f){qu("add",f),n=[f].concat(n.slice(o)).slice(0,t),o=0,l()}function u(){qu("clear"),n=[],o=0,l()}function d(){if(i()){var f=n[o];return o+=1,qu("undo",f),l(),f}}function v(){if(a())return qu("redo",n[o-=1]),l(),n[o]}return{get:s}}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-transform-modal-inner.svelte-lta8xm {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
  min-height: 0;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) {
  color: inherit;
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 0;
  overflow: auto;
  min-width: 0;
  min-height: 0;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-actions:where(.svelte-lta8xm) {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-top: var(--jse-padding, 10px);
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-actions:where(.svelte-lta8xm) button.jse-primary:where(.svelte-lta8xm) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-button-primary-background, var(--jse-theme-color, #3883fa));
  color: var(--jse-button-primary-color, #fff);
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  border-radius: 3px;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-actions:where(.svelte-lta8xm) button.jse-primary:where(.svelte-lta8xm):hover {
  background: var(--jse-button-primary-background-highlight, var(--jse-theme-color-highlight, #5f9dff));
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-actions:where(.svelte-lta8xm) button.jse-primary:where(.svelte-lta8xm):disabled {
  background: var(--jse-button-primary-background-disabled, #9d9d9d);
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) {
  flex: 1;
  display: flex;
  gap: calc(2 * var(--jse-padding, 10px));
  min-height: 0;
  box-sizing: border-box;
  padding: 0 calc(2 * var(--jse-padding, 10px)) var(--jse-padding, 10px);
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) {
  flex: 1;
  display: flex;
  flex-direction: column;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) .jse-description:where(.svelte-lta8xm) p {
  margin: var(--jse-padding, 10px) 0;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) .jse-description:where(.svelte-lta8xm) p:first-child {
  margin-top: 0;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) .jse-description:where(.svelte-lta8xm) p:last-child {
  margin-bottom: 0;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) .jse-description:where(.svelte-lta8xm) code {
  background: var(--jse-modal-code-background, rgba(0, 0, 0, 0.05));
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) .query-error:where(.svelte-lta8xm) {
  color: var(--jse-error-color, #ee5341);
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) textarea.jse-query:where(.svelte-lta8xm) {
  flex: 1;
  outline: none;
  resize: vertical;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents:where(.svelte-lta8xm) {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: calc(2 * var(--jse-padding, 10px));
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents:where(.svelte-lta8xm) .jse-original-data:where(.svelte-lta8xm) {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
  box-sizing: border-box;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents:where(.svelte-lta8xm) .jse-original-data.jse-hide:where(.svelte-lta8xm) {
  flex: none;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents:where(.svelte-lta8xm) .jse-preview-data:where(.svelte-lta8xm) {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-height: 0;
  box-sizing: border-box;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents.jse-hide-original-data:where(.svelte-lta8xm) {
  flex-direction: column;
  gap: 0;
  margin-bottom: 0;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-actions:where(.svelte-lta8xm) {
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px)) calc(2 * var(--jse-padding, 10px));
}
@media screen and (max-width: 1200px) {
  .jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) {
    flex-direction: column;
    overflow: auto;
  }
  .jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-query-contents:where(.svelte-lta8xm) textarea.jse-query:where(.svelte-lta8xm) {
    min-height: 150px;
    flex: none;
  }
  .jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents:where(.svelte-lta8xm) .jse-tree-mode {
    height: 300px;
    flex: none;
  }
  .jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents:where(.svelte-lta8xm) .jse-original-data:where(.svelte-lta8xm),
  .jse-transform-modal-inner.svelte-lta8xm .jse-modal-contents:where(.svelte-lta8xm) .jse-main-contents:where(.svelte-lta8xm) .jse-data-contents:where(.svelte-lta8xm) .jse-preview-data:where(.svelte-lta8xm) {
    flex: unset;
  }
}
.jse-transform-modal-inner.svelte-lta8xm .jse-label:where(.svelte-lta8xm) {
  font-weight: bold;
  display: block;
  box-sizing: border-box;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-label:where(.svelte-lta8xm) .jse-label-inner:where(.svelte-lta8xm) {
  margin-top: calc(2 * var(--jse-padding, 10px));
  margin-bottom: calc(0.5 * var(--jse-padding, 10px));
  box-sizing: border-box;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-label:where(.svelte-lta8xm) .jse-label-inner:where(.svelte-lta8xm) button:where(.svelte-lta8xm) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  font-weight: bold;
  padding: 0;
}
.jse-transform-modal-inner.svelte-lta8xm .jse-tree-mode {
  flex: 1;
  background: var(--jse-input-background-readonly, transparent);
  box-shadow: none;
  box-sizing: border-box;
  --jse-main-border: var(--jse-input-border, 1px solid #d8dbdf);
}
.jse-transform-modal-inner.svelte-lta8xm input:where(.svelte-lta8xm),
.jse-transform-modal-inner.svelte-lta8xm textarea:where(.svelte-lta8xm) {
  border: var(--jse-input-border, 1px solid #d8dbdf);
  outline: none;
  box-sizing: border-box;
  padding: calc(0.5 * var(--jse-padding, 10px));
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  color: inherit;
  background: var(--jse-input-background, var(--jse-background-color, #fff));
}
.jse-transform-modal-inner.svelte-lta8xm input:where(.svelte-lta8xm):focus,
.jse-transform-modal-inner.svelte-lta8xm textarea:where(.svelte-lta8xm):focus {
  border: var(--jse-input-border-focus, 1px solid var(--jse-input-border-focus, var(--jse-theme-color, #3883fa)));
}
.jse-transform-modal-inner.svelte-lta8xm input:where(.svelte-lta8xm):read-only,
.jse-transform-modal-inner.svelte-lta8xm textarea:where(.svelte-lta8xm):read-only {
  background: var(--jse-input-background-readonly, transparent);
}
.jse-transform-modal-inner.svelte-lta8xm .jse-preview.jse-error:where(.svelte-lta8xm) {
  flex: 1;
  background: var(--jse-input-background-readonly, transparent);
  border: var(--jse-input-border, 1px solid #d8dbdf);
  color: var(--jse-error-color, #ee5341);
  padding: calc(0.5 * var(--jse-padding, 10px));
}
.jse-transform-modal-inner.svelte-lta8xm a {
  color: var(--jse-a-color, #156fc5);
}
.jse-transform-modal-inner.svelte-lta8xm a:hover {
  color: var(--jse-a-color-highlight, #0f508d);
}`);var sc=Yd(()=>E5),Zs=Yd(()=>T5),pE=re('<div class="query-error svelte-lta8xm"> </div>'),hE=re("<!> <!>",1),gE=re('<div class="jse-preview jse-error svelte-lta8xm"> </div>'),mE=re('<!> <div class="jse-modal-contents svelte-lta8xm"><div class="jse-main-contents svelte-lta8xm"><div class="jse-query-contents svelte-lta8xm"><div class="jse-label svelte-lta8xm"><div class="jse-label-inner svelte-lta8xm">Language</div></div> <div class="jse-description svelte-lta8xm"></div> <div class="jse-label svelte-lta8xm"><div class="jse-label-inner svelte-lta8xm">Path</div></div> <input class="jse-path svelte-lta8xm" type="text" readonly="" title="Selected path"/> <div class="jse-label svelte-lta8xm"><div class="jse-label-inner svelte-lta8xm"><button type="button" class="svelte-lta8xm"><!> Wizard</button></div></div> <!> <div class="jse-label svelte-lta8xm"><div class="jse-label-inner svelte-lta8xm">Query</div></div> <textarea class="jse-query svelte-lta8xm" spellcheck="false"></textarea></div> <div><div><div class="jse-label svelte-lta8xm"><div class="jse-label-inner svelte-lta8xm"><button type="button" class="svelte-lta8xm"><!> Original</button></div></div> <!></div> <div class="jse-preview-data svelte-lta8xm"><div class="jse-label svelte-lta8xm"><div class="jse-label-inner svelte-lta8xm">Preview</div></div> <!></div></div></div> <div class="jse-actions svelte-lta8xm"><button type="button" class="jse-primary svelte-lta8xm">Transform</button></div></div>',1),bE=re('<div class="jse-transform-modal-inner svelte-lta8xm"><!></div>');function yE(e,t){var n,o,i;yt(t,!1);var a=Zr("jsoneditor:TransformModal"),s=m(t,"id",25,()=>"transform-modal-"+ul()),l=m(t,"json",9),c=m(t,"rootPath",25,()=>[]),u=m(t,"indentation",9),d=m(t,"truncateTextSize",9),v=m(t,"escapeControlCharacters",9),f=m(t,"escapeUnicodeCharacters",9),h=m(t,"parser",9),p=m(t,"parseMemoizeOne",9),y=m(t,"validationParser",9),j=m(t,"pathParser",9),b=m(t,"queryLanguages",9),k=m(t,"queryLanguageId",13),E=m(t,"onChangeQueryLanguage",9),O=m(t,"onRenderValue",9),w=m(t,"onRenderMenu",9),_=m(t,"onRenderContextMenu",9),A=m(t,"onClassName",9),q=m(t,"onTransform",9),C=m(t,"onClose",9),z=R(void 0,!0),D=R(kj({onChange:ee=>g(D,ee)}).get(),!0),H=R(void 0,!0),Q=R(void 0,!0),fe=R(!1,!0),Ie="".concat(s(),":").concat(wt(c())),ge=(n=sc()[Ie])!==null&&n!==void 0?n:{},qe=R(Zs().showWizard!==!1,!0),ce=R(Zs().showOriginal!==!1,!0),ve=R((o=ge.queryOptions)!==null&&o!==void 0?o:{},!0),he=R(k()===ge.queryLanguageId&&ge.query?ge.query:"",!0),Ue=R((i=ge.isManual)!==null&&i!==void 0&&i,!0),Re=R(void 0,!0),we=R(void 0,!0),ue=R({text:""},!0);function ie(ee){var L;return(L=b().find(pt=>pt.id===ee))!==null&&L!==void 0?L:b()[0]}function vt(ee){try{g(ve,ee),g(he,ie(k()).createQuery(r(H),ee)),g(Re,void 0),g(Ue,!1),a("updateQueryByWizard",{queryOptions:r(ve),query:r(he),isManual:r(Ue)})}catch(L){g(Re,String(L))}}function ft(ee){g(he,ee.target.value),g(Ue,!0),a("handleChangeQuery",{query:r(he),isManual:r(Ue)})}r(Ue)||vt(r(ve)),vo(()=>{var ee;(ee=r(z))===null||ee===void 0||ee.focus()});var kt=od(function(ee,L){if(ee===void 0)return g(ue,{text:""}),void g(we,"Error: No JSON");if(L.trim()!=="")try{a("previewTransform",{query:L});var pt=ie(k()).executeQuery(ee,L,h());g(ue,{json:pt}),g(we,void 0)}catch(ht){g(ue,{text:""}),g(we,String(ht))}else g(ue,{json:ee})},300);function oe(){if(r(H)===void 0)return g(ue,{text:""}),void g(we,"Error: No JSON");try{a("handleTransform",{query:r(he)});var ee=ie(k()).executeQuery(r(H),r(he),h());q()([{op:"replace",path:wt(c()),value:ee}]),C()()}catch(L){console.error(L),g(ue,{text:""}),g(we,String(L))}}function Ze(){g(qe,!r(qe)),Zs(Zs().showWizard=r(qe))}function te(){g(ce,!r(ce)),Zs(Zs().showOriginal=r(ce))}function X(ee){ee.focus()}function B(ee){a("handleChangeQueryLanguage",ee),k(ee),E()(ee),vt(r(ve))}function Ne(){r(fe)?g(fe,!r(fe)):C()()}ne(()=>(x(l()),x(c())),()=>{g(H,wj(tt(l(),c())))}),ne(()=>r(H),()=>{g(Q,r(H)?{json:r(H)}:{text:""})}),ne(()=>(r(H),r(he)),()=>{kt(r(H),r(he))}),ne(()=>(sc(),r(ve),r(he),x(k()),r(Ue)),()=>{sc(sc()[Ie]={queryOptions:r(ve),query:r(he),queryLanguageId:k(),isManual:r(Ue)}),a("store state in memory",Ie,sc()[Ie])}),Mn(),Ft(!0),Dc(e,{get onClose(){return C()},className:"jse-transform-modal",get fullscreen(){return r(fe)},children:(ee,L)=>{var pt=bE();Bf(I(pt),{children:(ht,_e)=>{var at=mE(),We=Mt(at);(function(ye,rt){yt(rt,!1);var dt,At=m(rt,"queryLanguages",9),en=m(rt,"queryLanguageId",9),Vt=m(rt,"fullscreen",13),Ht=m(rt,"onChangeQueryLanguage",9),On=m(rt,"onClose",9),dn=R(void 0,!0),{openAbsolutePopup:Qn,closeAbsolutePopup:Kn}=rs("absolute-popup");function Bn(){var Zn={queryLanguages:At(),queryLanguageId:en(),onChangeQueryLanguage:yr=>{Kn(dt),Ht()(yr)}};dt=Qn(mO,Zn,{offsetTop:-2,offsetLeft:0,anchor:r(dn),closeOnOuterClick:!0})}Ft(!0),Od(ye,{title:"Transform",fullScreenButton:!0,get onClose(){return On()},get fullscreen(){return Vt()},set fullscreen(Zn){Vt(Zn)},$$slots:{actions:(Zn,yr)=>{var Fn,$n=jO();un(I($n),{get data(){return nC}}),or($n,ar=>g(dn,ar),()=>r(dn)),Le(()=>Fn=Bt($n,1,"jse-config svelte-5gkegr",null,Fn,{hide:At().length<=1})),ze("click",$n,Bn),U(Zn,$n)}},$$legacy:!0}),jt()})(We,{get queryLanguages(){return b()},get queryLanguageId(){return k()},onChangeQueryLanguage:B,get onClose(){return C()},get fullscreen(){return r(fe)},set fullscreen(ye){g(fe,ye)},$$legacy:!0});var Ye=I(Y(We,2)),Tt=I(Ye),He=Y(I(Tt),2);uy(He,()=>(x(k()),F(()=>ie(k()).description)),!0);var qt=Y(He,4),S=Y(qt,2),$=I(S),N=I($),G=I(N),W=nt(()=>r(qe)?di:_c);un(G,{get data(){return r(W)}});var de=Y(S,2),Me=ye=>{var rt=br(),dt=Mt(rt),At=Ht=>{var On=hE(),dn=Mt(On);pO(dn,{get queryOptions(){return r(ve)},get json(){return r(H)},onChange:vt});var Qn=Y(dn,2),Kn=Bn=>{var Zn=pE(),yr=I(Zn);Le(()=>xt(yr,r(Re))),U(Bn,Zn)};be(Qn,Bn=>{r(Re)&&Bn(Kn)}),U(Ht,On)},en=Kt(()=>(r(H),F(()=>Array.isArray(r(H))))),Vt=Ht=>{U(Ht,oo("(Only available for arrays, not for objects)"))};be(dt,Ht=>{r(en)?Ht(At):Ht(Vt,-1)}),U(ye,rt)};be(de,ye=>{r(qe)&&ye(Me)});var pe=Y(de,4);or(pe,ye=>g(z,ye),()=>r(z));var le,St,lt=Y(Tt,2),Xe=I(lt),Ae=I(Xe),$t=I(Ae),sn=I($t),Un=I(sn),Yt=nt(()=>r(ce)?di:_c);un(Un,{get data(){return r(Yt)}});var Zt=Y(Ae,2),Dt=ye=>{sp(ye,{get externalContent(){return r(Q)},externalSelection:void 0,get history(){return r(D)},readOnly:!0,get truncateTextSize(){return d()},mainMenuBar:!1,navigationBar:!1,get indentation(){return u()},get escapeControlCharacters(){return v()},get escapeUnicodeCharacters(){return f()},get parser(){return h()},get parseMemoizeOne(){return p()},get onRenderValue(){return O()},get onRenderMenu(){return w()},get onRenderContextMenu(){return _()},onError:F(()=>console.error),get onChange(){return Dr},get onChangeMode(){return Dr},get onSelect(){return Dr},get onUndo(){return Dr},get onRedo(){return Dr},get onFocus(){return Dr},get onBlur(){return Dr},get onSortModal(){return Dr},get onTransformModal(){return Dr},get onJSONEditorModal(){return Dr},get onClassName(){return A()},validator:void 0,get validationParser(){return y()},get pathParser(){return j()}})};be(Zt,ye=>{r(ce)&&ye(Dt)});var hn=Y(Xe,2),Hn=Y(I(hn),2),J=ye=>{sp(ye,{get externalContent(){return r(ue)},externalSelection:void 0,get history(){return r(D)},readOnly:!0,get truncateTextSize(){return d()},mainMenuBar:!1,navigationBar:!1,get indentation(){return u()},get escapeControlCharacters(){return v()},get escapeUnicodeCharacters(){return f()},get parser(){return h()},get parseMemoizeOne(){return p()},get onRenderValue(){return O()},get onRenderMenu(){return w()},get onRenderContextMenu(){return _()},onError:F(()=>console.error),get onChange(){return Dr},get onChangeMode(){return Dr},get onSelect(){return Dr},get onUndo(){return Dr},get onRedo(){return Dr},get onFocus(){return Dr},get onBlur(){return Dr},get onSortModal(){return Dr},get onTransformModal(){return Dr},get onJSONEditorModal(){return Dr},get onClassName(){return A()},validator:void 0,get validationParser(){return y()},get pathParser(){return j()}})},V=ye=>{var rt=gE(),dt=I(rt);Le(()=>xt(dt,r(we))),U(ye,rt)};be(Hn,ye=>{r(we)?ye(V,-1):ye(J)});var Ve=I(Y(Ye,2));so(()=>ze("click",Ve,oe)),go(Ve,ye=>X==null?void 0:X(ye)),Le(ye=>{Ps(qt,ye),Ps(pe,r(he)),le=Bt(lt,1,"jse-data-contents svelte-lta8xm",null,le,{"jse-hide-original-data":!r(ce)}),St=Bt(Xe,1,"jse-original-data svelte-lta8xm",null,St,{"jse-hide":!r(ce)}),Ve.disabled=!!r(we)},[()=>(x(gn),x(c()),x(Eo),F(()=>gn(c())?"(document root)":Eo(c())))]),ze("click",N,Ze),ze("input",pe,ft),ze("click",sn,te),U(ht,at)},$$slots:{default:!0}}),go(pt,(ht,_e)=>_d==null?void 0:_d(ht,_e),()=>Ne),U(ee,pt)},$$slots:{default:!0}}),jt()}function Ko(){}var jE=0;class co{constructor(){var t=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{};this.id=jE++,this.perNode=!!t.perNode,this.deserialize=t.deserialize||(()=>{throw new Error("This node type doesn't define a deserialize function")}),this.combine=t.combine||null}add(t){if(this.perNode)throw new RangeError("Can't add per-node props to node types");return typeof t!="function"&&(t=Uc.match(t)),n=>{var o=t(n);return o===void 0?null:[this,o]}}}co.closedBy=new co({deserialize:e=>e.split(" ")}),co.openedBy=new co({deserialize:e=>e.split(" ")}),co.group=new co({deserialize:e=>e.split(" ")}),co.isolate=new co({deserialize:e=>{if(e&&e!="rtl"&&e!="ltr"&&e!="auto")throw new RangeError("Invalid value for isolate: "+e);return e||"auto"}}),co.contextHash=new co({perNode:!0}),co.lookAhead=new co({perNode:!0}),co.mounted=new co({perNode:!0});var r0,xE=Object.create(null);class Uc{constructor(t,n,o){var i=arguments.length>3&&arguments[3]!==void 0?arguments[3]:0;this.name=t,this.props=n,this.id=o,this.flags=i}static define(t){var n=t.props&&t.props.length?Object.create(null):xE,o=(t.top?1:0)|(t.skipped?2:0)|(t.error?4:0)|(t.name==null?8:0),i=new Uc(t.name||"",n,t.id,o);if(t.props){for(var a of t.props)if(Array.isArray(a)||(a=a(i)),a){if(a[0].perNode)throw new RangeError("Can't store a per-node prop on a node type");n[a[0].id]=a[1]}}return i}prop(t){return this.props[t.id]}get isTop(){return(1&this.flags)>0}get isSkipped(){return(2&this.flags)>0}get isError(){return(4&this.flags)>0}get isAnonymous(){return(8&this.flags)>0}is(t){if(typeof t=="string"){if(this.name==t)return!0;var n=this.prop(co.group);return!!n&&n.indexOf(t)>-1}return this.id==t}static match(t){var n=Object.create(null);for(var o in t)for(var i of o.split(" "))n[i]=t[o];return a=>{for(var s=a.prop(co.group),l=-1;l<(s?s.length:0);l++){var c=n[l<0?a.name:s[l]];if(c)return c}}}}Uc.none=new Uc("",Object.create(null),0,8),function(e){e[e.ExcludeBuffers=1]="ExcludeBuffers",e[e.IncludeAnonymous=2]="IncludeAnonymous",e[e.IgnoreMounts=4]="IgnoreMounts",e[e.IgnoreOverlays=8]="IgnoreOverlays",e[e.EnterBracketed=16]="EnterBracketed"}(r0||(r0={})),new co({perNode:!0});It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-status-bar.svelte-1pmgv9j {
  background: var(--jse-panel-background, #ebebeb);
  color: var(--jse-panel-color-readonly, #b2b2b2);
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  margin: 0;
  border-top: var(--jse-panel-border, var(--jse-main-border, 1px solid #d7d7d7));
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
  display: flex;
  gap: var(--jse-padding, 10px);
}
.jse-status-bar.svelte-1pmgv9j:last-child {
  border-bottom: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-status-bar.svelte-1pmgv9j .jse-status-bar-info:where(.svelte-1pmgv9j) {
  padding: 2px;
}`);var wE=re('<div class="jse-status-bar-info svelte-1pmgv9j"> </div>'),kE=re('<div class="jse-status-bar-info svelte-1pmgv9j"> </div>'),SE=re('<div class="jse-status-bar-info svelte-1pmgv9j"> </div>'),CE=re('<div class="jse-status-bar svelte-1pmgv9j"><!> <!> <!></div>'),ph=Ox.define([{tag:Io.propertyName,color:"var(--internal-key-color)"},{tag:Io.number,color:"var(--internal-value-color-number)"},{tag:Io.bool,color:"var(--internal-value-color-boolean)"},{tag:Io.string,color:"var(--internal-value-color-string)"},{tag:Io.keyword,color:"var(--internal-value-color-null)"}]),OE=Y0(ph),_E=ph.style;ph.style=e=>_E(e||[]);var EE=[Q0.fromClass(class{constructor(e){this.view=e,this.indentUnit=ed(e.state),this.initialPaddingLeft=null,this.isChrome=window==null?void 0:window.navigator.userAgent.includes("Chrome"),this.generate(e.state)}update(e){var t=ed(e.state);(t!==this.indentUnit||e.docChanged||e.viewportChanged)&&(this.indentUnit=t,this.generate(e.state))}generate(e){var t=new G0;this.initialPaddingLeft?this.addStyleToBuilder(t,e,this.initialPaddingLeft):this.view.requestMeasure({read:n=>{var o=n.contentDOM.querySelector(".cm-line");o&&(this.initialPaddingLeft=window.getComputedStyle(o).getPropertyValue("padding-left"),this.addStyleToBuilder(t,n.state,this.initialPaddingLeft)),this.decorations=t.finish()}}),this.decorations=t.finish()}addStyleToBuilder(e,t,n){var o=this.getVisibleLines(t);for(var i of o){var{numColumns:a,containsTab:s}=this.numColumns(i.text,t.tabSize),l="calc(".concat(a+this.indentUnit,"ch + ").concat(n,")"),c=this.isChrome?"calc(-".concat(a+this.indentUnit,"ch - ").concat(s?1:0,"px)"):"-".concat(a+this.indentUnit,"ch");e.add(i.from,i.from,K0.line({attributes:{style:"padding-left: ".concat(l,"; text-indent: ").concat(c,";")}}))}}getVisibleLines(e){var t=new Set,n=null;for(var{from:o,to:i}of this.view.visibleRanges)for(var a=o;a<=i;){var s=e.doc.lineAt(a);n!==s&&(t.add(s),n=s),a=s.to+1}return t}numColumns(e,t){var n=0,o=!1;e:for(var i=0;i<e.length;i++)switch(e[i]){case" ":n+=1;continue e;case"	":n+=t-n%t,o=!0;continue e;case"\r":continue e;default:break e}return{numColumns:n,containsTab:o}}},{decorations:e=>e.decorations})];It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-text-mode.svelte-k2b9e6 {
  --internal-key-color: var(--jse-key-color, #1a1a1a);
  --internal-value-color-number: var(--jse-value-color-number, #ee422e);
  --internal-value-color-boolean: var(--jse-value-color-boolean, #ff8c00);
  --internal-value-color-string: var(--jse-value-color-string, #008000);
  --internal-value-color-null: var(--jse-value-color-null, #004ed0);
  flex: 1;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  background: var(--jse-background-color, #fff);
}
.jse-text-mode.no-main-menu.svelte-k2b9e6 {
  border-top: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) {
  flex: 1;
  display: flex;
  position: relative;
  flex-direction: column;
  overflow: hidden;
  min-width: 0;
  min-height: 0;
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6):last-child {
  border-bottom: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents.jse-hidden:where(.svelte-k2b9e6) {
  visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor {
  flex: 1;
  overflow: hidden;
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-scroller {
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  line-height: var(--jse-line-height, calc(1em + 4px));
  color: var(--jse-delimiter-color, rgba(0, 0, 0, 0.38));
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-gutters {
  background: var(--jse-panel-background, #ebebeb);
  color: var(--jse-panel-color-readonly, #b2b2b2);
  border-right: var(--jse-panel-border, var(--jse-main-border, 1px solid #d7d7d7));
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-activeLine,
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-activeLineGutter {
  background: var(--jse-active-line-background-color, rgba(0, 0, 0, 0.06));
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-selectionBackground {
  background: var(--jse-selection-background-color, #d3d3d3);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-searchMatch {
  background-color: var(--jse-search-match-color, #ffe665);
  outline: var(--jse-search-match-outline, none);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-searchMatch.cm-searchMatch-selected {
  background-color: var(--jse-search-match-active-color, var(--jse-search-match-color, #ffe665));
  outline: var(--jse-search-match-outline, 2px solid #e0be00);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-selectionMatch {
  background-color: var(--jse-search-match-background-color, rgba(153, 255, 119, 0.5019607843));
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-foldPlaceholder {
  background: var(--jse-tag-background, rgba(0, 0, 0, 0.2));
  color: var(--jse-tag-color, var(--jse-text-color-inverse, #fff));
  border: none;
  padding: 0 var(--jse-padding, 10px);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-tooltip {
  font-size: var(--jse-font-size, 16px);
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  color: var(--jse-tooltip-color, var(--jse-text-color, #4d4d4d));
  background: var(--jse-tooltip-background, var(--jse-modal-background, #f5f5f5));
  border: var(--jse-tooltip-border, var(--jse-main-border, 1px solid #d7d7d7));
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-diagnosticAction {
  background: var(--jse-tooltip-action-button-color, var(--jse-text-color-inverse, #fff));
  background: var(--jse-tooltip-action-button-background, #4d4d4d);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-panels {
  border-bottom: var(--jse-panel-border, var(--jse-main-border, 1px solid #d7d7d7));
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-search {
  background: var(--jse-panel-background, #ebebeb);
  color: var(--jse-panel-color, var(--jse-text-color, #4d4d4d));
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-search input {
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size-text-mode-search, 80%);
  color: var(--jse-input-color, var(--jse-text-color, #4d4d4d));
  border: var(--jse-input-border, 1px solid #d8dbdf);
  background: var(--jse-input-background, var(--jse-background-color, #fff));
  margin-right: 2px;
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-search button {
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size-text-mode-search, 80%);
  color: var(--jse-panel-button-color, inherit);
  background: var(--jse-panel-button-background, transparent);
  border: none;
  cursor: pointer;
  text-transform: capitalize;
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px);
  margin: 0;
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-search button:hover {
  color: var(--panel-button-color-highlight, var(--jse-text-color, #4d4d4d));
  background: var(--jse-panel-button-background-highlight, #e0e0e0);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-search label {
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size-text-mode-search, 80%);
  padding-left: var(--jse-padding, 10px);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-search label input {
  margin-right: 2px;
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-search button[name='close'] {
  width: 32px;
  height: 32px;
  font-size: 24px;
  line-height: 24px;
  padding: 0;
  right: 0;
  top: -4px;
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .cm-editor .cm-cursor-primary {
  border-color: var(--jse-text-color, #4d4d4d);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .jse-loading-space:where(.svelte-k2b9e6) {
  flex: 1;
}
.jse-text-mode.svelte-k2b9e6 .jse-contents:where(.svelte-k2b9e6) .jse-loading:where(.svelte-k2b9e6) {
  flex: 2;
  text-align: center;
  color: var(--jse-panel-color-readonly, #b2b2b2);
  box-sizing: border-box;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
}
.jse-text-mode.svelte-k2b9e6 .jse-contents.jse-preview:where(.svelte-k2b9e6) {
  flex: 1;
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  color: var(--jse-panel-color-readonly, #b2b2b2);
  overflow: auto;
  white-space: pre-wrap;
  word-break: break-word;
  padding: 2px;
}
.jse-text-mode.svelte-k2b9e6 .jse-fold-progress:where(.svelte-k2b9e6) {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: var(--jse-background-color, #fff);
  border-top: var(--jse-panel-border, var(--jse-main-border, 1px solid #d7d7d7));
  border-bottom: var(--jse-panel-border, var(--jse-main-border, 1px solid #d7d7d7));
}
.jse-text-mode.svelte-k2b9e6 .jse-fold-progress:where(.svelte-k2b9e6) .jse-fold-tip:where(.svelte-k2b9e6) {
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size-mono, 14px);
  color: var(--jse-panel-color-readonly, #b2b2b2);
}
.jse-text-mode.svelte-k2b9e6 .jse-fold-progress:where(.svelte-k2b9e6) .jse-fold-progress-track:where(.svelte-k2b9e6) {
  flex: 1;
  height: 6px;
  background: var(--jse-panel-background, #ebebeb);
  border-radius: 3px;
  overflow: hidden;
  border: 1px solid var(--jse-panel-border, var(--jse-main-border, 1px solid #d7d7d7));
}
.jse-text-mode.svelte-k2b9e6 .jse-fold-progress:where(.svelte-k2b9e6) .jse-fold-progress-fill:where(.svelte-k2b9e6) {
  height: 100%;
  background: linear-gradient(90deg, var(--jse-theme-color, #3883fa), var(--jse-theme-color-highlight, #5f9dff));
  border-radius: 2px;
  transition: width 0.1s ease;
  min-width: 2px;
}
.jse-text-mode.svelte-k2b9e6 .jse-fold-progress:where(.svelte-k2b9e6) .jse-fold-cancel-button:where(.svelte-k2b9e6) {
  padding: 4px 12px;
  font-size: 12px;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  background: var(--jse-theme-color, #3883fa);
  color: #fff;
  border-radius: 3px;
  cursor: pointer;
  transition: background-color 0.2s ease;
  flex-shrink: 0;
  border: 1px solid var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-text-mode.svelte-k2b9e6 .jse-fold-progress:where(.svelte-k2b9e6) .jse-fold-cancel-button:where(.svelte-k2b9e6):hover {
  background: var(--jse-theme-color-highlight, #5f9dff);
  color: #fff;
}`);var TE=re('<div class="jse-fold-progress svelte-k2b9e6"><span class="jse-fold-tip svelte-k2b9e6">Collapsing</span> <div class="jse-fold-progress-track svelte-k2b9e6"><div class="jse-fold-progress-fill svelte-k2b9e6"></div></div> <button class="jse-fold-cancel-button svelte-k2b9e6" type="button" title="Cancel folding">Cancel</button></div>'),ME=re('<!> <div class="jse-contents jse-preview svelte-k2b9e6"> </div>',1),$E=re("<!> <!> <!> <!>",1),AE=re("<div></div> <!> <!>",1),zE=re('<div class="jse-contents svelte-k2b9e6"><div class="jse-loading-space svelte-k2b9e6"></div> <div class="jse-loading svelte-k2b9e6">loading...</div></div>'),PE=re("<div><!> <!> <!></div>");function NE(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),i=m(t,"readOnly",9),a=m(t,"mainMenuBar",9),s=m(t,"statusBar",9),l=m(t,"askToFormat",9),c=m(t,"externalContent",9),u=m(t,"externalSelection",9),d=m(t,"history",9),v=m(t,"indentation",9),f=m(t,"tabSize",9),h=m(t,"escapeUnicodeCharacters",9),p=m(t,"maxDocumentSize",9),y=m(t,"parser",9),j=m(t,"validator",9),b=m(t,"validationParser",9),k=m(t,"onChange",9),E=m(t,"onChangeMode",9),O=m(t,"onSelect",9),w=m(t,"onUndo",9),_=m(t,"onRedo",9),A=m(t,"onError",9),q=m(t,"onFocus",9),C=m(t,"onBlur",9),z=m(t,"onRenderMenu",9),D=m(t,"onSortModal",9),H=m(t,"onTransformModal",9),Q=Zr("jsoneditor:TextMode"),fe={key:"Mod-i",run:pe,shift:le,preventDefault:!0},Ie=typeof window>"u";Q("isSSR:",Ie);var ge,qe=R(void 0,!0),ce=R(void 0,!0),ve=R(void 0,!0),he=R(!1,!0),Ue=R(l(),!0),Re=R([],!0),we=R(!1,!0),ue=R(0,!0),ie=R(0,!0),vt=null,ft=new Xl,kt=new Xl,oe=new Xl,Ze=new Xl,te=new Xl,X=c(),B=R(Uf(X,v(),y()),!0),Ne=ew.define(),ee=null;function L(){if(!ee||ee.length===0)return!1;var K=ee[0].startState,Ce=ee[ee.length-1].state,P=ee.map(xe=>xe.changes).reduce((xe,ot)=>xe.compose(ot)),Z={type:"text",undo:{changes:P.invert(K.doc).toJSON(),selection:Fn(K.selection)},redo:{changes:P.toJSON(),selection:Fn(Ce.selection)}};return Q("add history item",Z),d().add(Z),ee=null,!0}var pt=R(h(),!0);vo(Pt(function*(){if(!Ie)try{ge=function(K){var{target:Ce,initialText:P,readOnly:Z,indentation:xe}=K;Q("Create CodeMirror editor",{readOnly:Z,indentation:xe});var ot=function(Je,Lt){return Hv(Je)?Je.ranges.every(Ct=>Ct.anchor<Lt.length&&Ct.head<Lt.length):!1}(u(),P)?en(u()):void 0,Qe=Hs.create({doc:P,selection:ot,extensions:[Lh.of([_x,fe]),ft.of(V()),Ex(),Tx(),Mx(),$x(),Ax(),Ye(),zx(),Px(),Hs.allowMultipleSelections.of(!0),Nx(),Y0(Rx,{fallback:!0}),Ix(),qx(),Dx(),Lx(),Ux(),Bx(),Fx(),Lh.of([...Wx,...Vx,...Jx,{key:"Mod-z",run:sn,preventDefault:!0},{key:"Mod-y",mac:"Mod-Shift-z",run:Un,preventDefault:!0},{key:"Ctrl-Shift-z",run:Un,preventDefault:!0},...Hx,...Qx,...Kx]),OE,RC({hideFirstIndent:!0}),hs.domEventHandlers({dblclick:J}),hs.updateListener.of(Je=>{g(ve,Je.state),Je.docChanged&&(Je.transactions.some(Lt=>!!Lt.annotation(Ne))||(ee=[...ee??[],Je]),Kn()),Je.selectionSet&&yr()}),MC(),Gx({top:!0}),hs.lineWrapping,kt.of(Hs.readOnly.of(Z)),Ze.of(Hs.tabSize.of(f())),oe.of(Qn(xe)),te.of(hs.theme({},{dark:Ve()}))]});return ge=new hs({state:Qe,parent:Ce}),ot&&ge.dispatch(ge.state.update({selection:ot.main,scrollIntoView:!0})),ge}({target:r(qe),initialText:$n(r(B),p(),r(he))?"":r(n).escapeValue(r(B)),readOnly:i(),indentation:v()})}catch(K){console.error(K)}})),ra(()=>{Bn(),ge&&(Q("Destroy CodeMirror editor"),ge.destroy()),S()});var ht=Sl(),_e=Sl();function at(){ge&&(Q("focus"),ge.focus())}function We(K,Ce){if(ge)try{(function(){var P=arguments.length>0&&arguments[0]!==void 0?arguments[0]:[],Z=!(arguments.length>1&&arguments[1]!==void 0)||arguments[1],xe=ge.state,ot=xe.doc.length,Qe=Uh(xe,ot,1/0);if(Qe){var Je=[];if(P.length===0)Je=He(Qe,xe,void 0,Z);else{var{from:Lt}=Dv(r(n).escapeValue(r(B)),P);Lt!==void 0&&Lt!==0&&(Je=He(Qe,xe,Lt,Z))}Je.length>0&&function(Ct){qt.apply(this,arguments)}(Je)}})(K,Ce)}catch(P){A()(P)}}function Ye(){return Yx.of((K,Ce,P)=>{var Z=Uh(K,K.doc.length,1/0);if(!Z||Z.length<P)return null;for(var xe=null,ot=Z.resolveStack(P,1);ot;ot=ot.next){var Qe=ot.node;if(!(Qe.to<=P||Qe.from>P)){if(xe&&Qe.from<Ce)break;var Je=Qe.type.prop(H0);if(Je&&(Qe.to<Z.length-50||Z.length==K.doc.length||!Tt(Qe))){var Lt=Je(Qe,K);Lt&&Lt.from<=P&&Lt.from>=Ce&&Lt.to>P&&(xe=Lt)}}}return xe})}function Tt(K){var Ce=K.lastChild;return Ce&&Ce.to==K.to&&Ce.type.isError}function He(K,Ce,P){var Z=!(arguments.length>3&&arguments[3]!==void 0)||arguments[3],xe=[],ot=new Set;return K.iterate({enter(Qe){if(P===void 0||Qe.from>=P){var Je=tw(Ce,Qe.from,Qe.to);if(Je){var Lt="".concat(Je.from,"-").concat(Je.to);if(!ot.has(Lt))if(Z)xe.push({from:Je.from,to:Je.to}),ot.add(Lt);else{var Ct=xe.some(jn=>jn.from<=Je.from&&jn.to>=Je.to);Ct||(xe.push({from:Je.from,to:Je.to}),ot.add(Lt))}}}}}),xe}function qt(){return qt=Pt(function*(K){if(K.length!==0){var Ce=K.length>5e3;Ce&&(g(we,!0),g(ue,0),g(ie,K.length),vt=new AbortController);var P=Z=>new Promise(xe=>{var ot;Ce&&(ot=vt)!==null&&ot!==void 0&&ot.signal.aborted?xe():requestAnimationFrame(()=>{var Qe=Math.min(Z+100,K.length),Je=K.slice(Z,Qe);ge.dispatch({effects:Je.map(Lt=>ow.of({from:Lt.from,to:Lt.to}))}),Ce&&g(ue,Qe),Qe<K.length?P(Qe).then(xe):xe()})});yield P(0),Ce&&(g(we,!1),g(ue,0),g(ie,0),vt=null)}}),qt.apply(this,arguments)}function S(){vt&&vt.abort()}function $(K){var Ce=arguments.length>1&&arguments[1]!==void 0?arguments[1]:Jf;if(ge)try{if(K&&K.length>0){var{from:P}=Dv(r(n).escapeValue(r(B)),K);P!==void 0&&(ge.dispatch({selection:{anchor:P,head:P}}),nw(ge))}else rw(ge);Ce==null||Ce(K)}catch(Z){A()(Z)}}function N(){$([],()=>!0)}function G(){We([],!0)}var W=!1;function de(K){return Me(K,!1)}function Me(K,Ce){Q("handlePatch",K,Ce);var P=y().parse(r(B)),Z=ga(P,K),xe=r1(P,K);return At({text:y().stringify(Z,null,v())},Ce,!1),{json:Z,previousJson:P,undo:xe,redo:K}}function pe(){if(Q("format"),i())return!1;try{var K=y().parse(r(B));return At({text:y().stringify(K,null,v())},!0,!1),g(Ue,l()),!0}catch(Ce){A()(Ce)}return!1}function le(){if(Q("compact"),i())return!1;try{var K=y().parse(r(B));return At({text:y().stringify(K)},!0,!1),g(Ue,!1),!0}catch(Ce){A()(Ce)}return!1}function St(){if(Q("repair"),!i())try{At({text:Aa(r(B))},!0,!1),g(ar,Wv),g(Se,void 0)}catch(K){A()(K)}}function lt(){var K;if(!i())try{var Ce=y().parse(r(B));W=!0,D()({id:ht,json:Ce,rootPath:[],onSort:(K=Pt(function*(P){var{operations:Z}=P;Q("onSort",Z),Me(Z,!0)}),function(P){return K.apply(this,arguments)}),onClose:()=>{W=!1,at()}})}catch(P){A()(P)}}function Xe(K){var{id:Ce,rootPath:P,onTransform:Z,onClose:xe}=K;try{var ot=y().parse(r(B));W=!0,H()({id:Ce||_e,json:ot,rootPath:P||[],onTransform:Qe=>{Z?Z({operations:Qe,json:ot,transformedJson:ga(ot,Qe)}):(Q("onTransform",Qe),Me(Qe,!0))},onClose:()=>{W=!1,at(),xe&&xe()}})}catch(Qe){A()(Qe)}}function Ae(){i()||Xe({rootPath:[]})}function $t(){ge&&(r(qe)&&r(qe).querySelector(".cm-search")?aw(ge):iw(ge))}function sn(){if(i())return!1;Bn();var K=d().undo();return Q("undo",K),Cm(K)?(ge.dispatch({annotations:Ne.of("undo"),changes:Bh.fromJSON(K.undo.changes),selection:yv.fromJSON(K.undo.selection),scrollIntoView:!0}),!0):(w()(K),!1)}function Un(){if(i())return!1;Bn();var K=d().redo();return Q("redo",K),Cm(K)?(ge.dispatch({annotations:Ne.of("redo"),changes:Bh.fromJSON(K.redo.changes),selection:yv.fromJSON(K.redo.selection),scrollIntoView:!0}),!0):(_()(K),!1)}function Yt(){g(he,!0),At(c(),!0,!0)}function Zt(){E()(Mr.tree)}function Dt(){On()}function hn(K){Q("select validation error",K);var{from:Ce,to:P}=ye(K);Ce!==void 0&&P!==void 0&&(Hn(Ce,P),at())}function Hn(K,Ce){Q("setSelection",{anchor:K,head:Ce}),ge&&ge.dispatch(ge.state.update({selection:{anchor:K,head:Ce},scrollIntoView:!0}))}function J(K,Ce){if(Ce.state.selection.ranges.length===1){var P=Ce.state.selection.ranges[0],Z=r(B).slice(P.from,P.to);if(Z==="{"||Z==="["){var xe=Nd.parse(r(B)),ot=Object.keys(xe.pointers).find(Je=>{var Lt;return((Lt=xe.pointers[Je].value)===null||Lt===void 0?void 0:Lt.pos)===P.from}),Qe=xe.pointers[ot];ot&&Qe&&Qe.value&&Qe.valueEnd&&(Q("pointer found, selecting inner contents of path:",ot,Qe),Hn(Qe.value.pos+1,Qe.valueEnd.pos-1))}}}function V(){return Xx(Ee,{delay:300})}function Ve(){return!!r(qe)&&getComputedStyle(r(qe)).getPropertyValue("--jse-theme").includes("dark")}function ye(K){var{path:Ce,message:P,severity:Z}=K,{line:xe,column:ot,from:Qe,to:Je}=Dv(r(n).escapeValue(r(B)),Ce);return{path:Ce,line:xe,column:ot,from:Qe,to:Je,message:P,severity:Z,actions:[]}}function rt(K,Ce){var{line:P,column:Z,position:xe,message:ot}=K;return{path:[],line:P,column:Z,from:xe,to:xe,severity:ba.error,message:ot,actions:Ce&&!i()?[{name:"Auto repair",apply:()=>St()}]:void 0}}function dt(K){return{from:K.from||0,to:K.to||0,message:K.message||"",actions:K.actions,severity:K.severity}}function At(K,Ce,P){var Z=Uf(K,v(),y()),xe=!Gt(K,X),ot=X;Q("setCodeMirrorContent",{isChanged:xe,emitChange:Ce,forceUpdate:P}),ge&&(xe||P)&&(X=K,g(B,Z),$n(r(B),p(),r(he))||ge.dispatch({changes:{from:0,to:ge.state.doc.length,insert:r(n).escapeValue(r(B))}}),L(),xe&&Ce&&Zn(X,ot))}function en(K){return Hv(K)?yv.fromJSON(K):void 0}function Vt(){return Ht.apply(this,arguments)}function Ht(){return Ht=Pt(function*(){Q("refresh"),yield function(){return dn.apply(this,arguments)}()}),Ht.apply(this,arguments)}function On(){if(ge){var K=ge?r(n).unescapeValue(ge.state.doc.toString()):"",Ce=K!==r(B);if(Q("onChangeCodeMirrorValue",{isChanged:Ce}),Ce){var P=X;g(B,K),X={text:r(B)},L(),Zn(X,P),Xn(),yr()}}}function dn(){return(dn=Pt(function*(){if(Xn(),ge){var K=Ve();return Q("updateTheme",{dark:K}),ge.dispatch({effects:[te.reconfigure(hs.theme({},{dark:K}))]}),new Promise(Ce=>setTimeout(Ce))}return Promise.resolve()})).apply(this,arguments)}function Qn(K){var Ce=Zx.of(typeof K=="number"?" ".repeat(K):K);return K==="	"?[Ce]:[Ce,EE]}dh({onMount:vo,onDestroy:ra,getWindow:()=>nu(r(ce)),hasFocus:()=>W&&document.hasFocus()||Gp(r(ce)),onFocus:q(),onBlur:()=>{Bn(),C()()}});var Kn=od(On,300);function Bn(){Kn.flush()}function Zn(K,Ce){k()&&k()(K,Ce,{contentErrors:tn(),patchResult:void 0})}function yr(){O()(Fn(r(ve).selection))}function Fn(K){return De({type:Dn.text},K.toJSON())}function $n(K,Ce,P){return!!K&&K.length>Ce&&!P}var ar=R(Wv,!0),Se=R(void 0,!0);function Ee(){if($n(r(B),p(),r(he)))return[];var K=tn();if(Sm(K)){var{parseError:Ce,isRepairable:P}=K;return[dt(rt(Ce,P))]}return l5(K)?K.validationErrors.map(ye).map(dt):[]}function tn(){Q("validate:start"),Bn();var K=Ar(r(n).escapeValue(r(B)),j(),y(),b());return Sm(K)?(g(ar,K.isRepairable?ym:"invalid"),g(Se,K.parseError),g(Re,[])):(g(ar,Wv),g(Se,void 0),g(Re,(K==null?void 0:K.validationErrors)||[])),Q("validate:end"),K}var Ar=Ec(kO);function jr(){r(Se)&&function(K){Q("select parse error",K);var Ce=rt(K,!1);Hn(Ce.from!=null?Ce.from:0,Ce.to!=null?Ce.to:0),at()}(r(Se))}var on={icon:VS,text:"Show me",title:"Move to the parse error location",onClick:jr};ne(()=>x(h()),()=>{g(n,Qp({escapeControlCharacters:!1,escapeUnicodeCharacters:h()}))}),ne(()=>x(c()),()=>{At(c(),!1,!1)}),ne(()=>x(u()),()=>{(function(K){if(Hv(K)){var Ce=en(K);!ge||!Ce||r(ve)&&r(ve).selection.eq(Ce)||(Q("applyExternalSelection",Ce),ge.dispatch({selection:Ce}))}})(u())}),ne(()=>x(j()),()=>{(function(K){Q("updateLinter",K),ge&&ge.dispatch({effects:ft.reconfigure(V())})})(j())}),ne(()=>x(v()),()=>{(function(K){ge&&(Q("updateIndentation",K),ge.dispatch({effects:oe.reconfigure(Qn(K))}))})(v())}),ne(()=>x(f()),()=>{(function(K){ge&&(Q("updateTabSize",K),ge.dispatch({effects:Ze.reconfigure(Hs.tabSize.of(K))}))})(f())}),ne(()=>x(i()),()=>{(function(K){ge&&(Q("updateReadOnly",K),ge.dispatch({effects:[kt.reconfigure(Hs.readOnly.of(K))]}))})(i())}),ne(()=>(r(pt),x(h())),()=>{r(pt)!==h()&&(g(pt,h()),Q("forceUpdateText",{escapeUnicodeCharacters:h()}),ge&&ge.dispatch({changes:{from:0,to:ge.state.doc.length,insert:r(n).escapeValue(r(B))}}))}),ne(()=>(r(ar),x(i()),Yi),()=>{g(o,r(ar)!==ym||i()?[on]:[{icon:Yi,text:"Auto repair",title:"Automatically repair JSON",onClick:St},on])}),Mn();var dr={focus:at,collapse:We,expand:$,patch:de,handlePatch:Me,openTransformModal:Xe,refresh:Vt,flush:Bn,validate:tn};Ft(!0);var vr,Br=PE(),eo=I(Br),zr=K=>{var Ce=nt(()=>(r(B),F(()=>r(B).length===0))),P=nt(()=>!r(Ce)),Z=nt(()=>!r(Ce)),xe=nt(()=>!r(Ce)),ot=nt(()=>!r(Ce)),Qe=nt(()=>!r(Ce)),Je=nt(()=>!r(Ce));(function(Lt,Ct){yt(Ct,!1);var jn=R(void 0,!0),vn=m(Ct,"readOnly",9,!1),er=m(Ct,"onExpandAll",9),Ot=m(Ct,"onCollapseAll",9),an=m(Ct,"onFormat",9),fr=m(Ct,"onCompact",9),Gn=m(Ct,"onSort",9),Nn=m(Ct,"onTransform",9),Ke=m(Ct,"onToggleSearch",9),zn=m(Ct,"onUndo",9),sr=m(Ct,"onRedo",9),_t=m(Ct,"canExpandAll",9),_n=m(Ct,"canCollapseAll",9),lr=m(Ct,"canUndo",9),Nr=m(Ct,"canRedo",9),to=m(Ct,"canFormat",9),bo=m(Ct,"canCompact",9),jo=m(Ct,"canSort",9),M=m(Ct,"canTransform",9),se=m(Ct,"onRenderMenu",9),Te=R(void 0,!0),Be=R(void 0,!0),Oe={type:"button",icon:Jd,title:"Search (Ctrl+F)",className:"jse-search",onClick:Ke()},Ge=R(void 0,!0);ne(()=>(x(er()),x(_t())),()=>{g(Te,{type:"button",icon:cj,title:"Expand all",className:"jse-expand-all",onClick:er(),disabled:!_t()})}),ne(()=>(x(Ot()),x(_n())),()=>{g(Be,{type:"button",icon:uj,title:"Collapse all",className:"jse-collapse-all",onClick:Ot(),disabled:!_n()})}),ne(()=>(x(vn()),r(Te),r(Be),x(an()),x(to()),x(fr()),x(bo()),x(Gn()),x(jo()),x(Nn()),x(M()),x(zn()),x(lr()),x(sr()),x(Nr())),()=>{g(Ge,vn()?[r(Te),r(Be),{type:"separator"},Oe,{type:"space"}]:[r(Te),r(Be),{type:"separator"},{type:"button",icon:e0,title:"Format JSON: add proper indentation and new lines (Ctrl+I)",className:"jse-format",onClick:an(),disabled:vn()||!to()},{type:"button",icon:C_,title:"Compact JSON: remove all white spacing and new lines (Ctrl+Shift+I)",className:"jse-compact",onClick:fr(),disabled:vn()||!bo()},{type:"separator"},{type:"button",icon:sd,title:"Sort",className:"jse-sort",onClick:Gn(),disabled:vn()||!jo()},{type:"button",icon:ad,title:"Transform contents (filter, sort, project)",className:"jse-transform",onClick:Nn(),disabled:vn()||!M()},Oe,{type:"separator"},{type:"button",icon:Pp,title:"Undo (Ctrl+Z)",className:"jse-undo",onClick:zn(),disabled:!lr()},{type:"button",icon:zp,title:"Redo (Ctrl+Shift+Z)",className:"jse-redo",onClick:sr(),disabled:!Nr()},{type:"space"}])}),ne(()=>(x(se()),r(Ge)),()=>{g(jn,se()(r(Ge))||r(Ge))}),Mn(),Ft(!0),av(Lt,{get items(){return r(jn)}}),jt()})(K,{get readOnly(){return i()},onExpandAll:N,onCollapseAll:G,onFormat:pe,onCompact:le,onSort:lt,onTransform:Ae,onToggleSearch:$t,onUndo:sn,onRedo:Un,get canExpandAll(){return r(P)},get canCollapseAll(){return r(Z)},get canFormat(){return r(xe)},get canCompact(){return r(ot)},get canSort(){return r(Qe)},get canTransform(){return r(Je)},get canUndo(){return x(d()),F(()=>d().canUndo)},get canRedo(){return x(d()),F(()=>d().canRedo)},get onRenderMenu(){return z()}})};be(eo,K=>{a()&&K(zr)});var Pn=Y(eo,2),yn=K=>{var Ce=TE(),P=Y(I(Ce),2),Z=I(P),xe=Y(P,2);Le(()=>ea(Z,"width: ".concat(r(ie)>0?r(ue)/r(ie)*100:0,"%"))),ze("click",xe,S),U(K,Ce)};be(Pn,K=>{r(we)&&K(yn)});var Wt=Y(Pn,2),Wn=K=>{var Ce,P=nt(()=>(r(B),x(p()),r(he),F(()=>$n(r(B),p(),r(he))))),Z=AE(),xe=Mt(Z);or(xe,Ct=>g(qe,Ct),()=>r(qe));var ot=Y(xe,2),Qe=Ct=>{var jn=ME(),vn=Mt(jn),er=nt(()=>(x(Qu),x(p()),r(B),F(()=>"The JSON document is larger than ".concat(Qu(p()),", ")+"and may crash your browser when loading it in text mode. Actual size: ".concat(Qu(r(B).length),"."))));Fo(vn,{get icon(){return $s},type:"error",get message(){return r(er)},actions:[{text:"Open anyway",title:"Open the document in text mode. This may freeze or crash your browser.",onClick:Yt},{text:"Open in tree mode",title:"Open the document in tree mode. Tree mode can handle large documents.",onClick:Zt},{text:"Cancel",title:"Cancel opening this large document.",onClick:Dt}],onClose:at});var Ot=I(Y(vn,2));Le(an=>xt(Ot,an),[()=>(x(ti),r(B),x(pd),F(()=>ti(r(B)||"",pd)))]),U(Ct,jn)};be(ot,Ct=>{r(P)&&Ct(Qe)});var Je=Y(ot,2),Lt=Ct=>{var jn=$E(),vn=Mt(jn),er=Ke=>{(function(zn,sr){yt(sr,!1);var _t=m(sr,"editorState",8),_n=R(),lr=R(),Nr=R(),to=R(),bo=R();ne(()=>x(_t()),()=>{var Fe;g(_n,(Fe=_t())===null||Fe===void 0||(Fe=Fe.selection)===null||Fe===void 0||(Fe=Fe.main)===null||Fe===void 0?void 0:Fe.head)}),ne(()=>(r(_n),x(_t())),()=>{var Fe;g(lr,r(_n)!==void 0?(Fe=_t())===null||Fe===void 0||(Fe=Fe.doc)===null||Fe===void 0?void 0:Fe.lineAt(r(_n)):void 0)}),ne(()=>r(lr),()=>{g(Nr,r(lr)!==void 0?r(lr).number:void 0)}),ne(()=>(r(lr),r(_n)),()=>{g(to,r(lr)!==void 0&&r(_n)!==void 0?r(_n)-r(lr).from+1:void 0)}),ne(()=>x(_t()),()=>{var Fe;g(bo,(Fe=_t())===null||Fe===void 0||(Fe=Fe.selection)===null||Fe===void 0||(Fe=Fe.ranges)===null||Fe===void 0?void 0:Fe.reduce((mt,it)=>mt+it.to-it.from,0))}),Mn(),Ft();var jo=CE(),M=I(jo),se=Fe=>{var mt=wE(),it=I(mt);Le(()=>{var ut;return xt(it,"Line: ".concat((ut=r(Nr))!==null&&ut!==void 0?ut:""))}),U(Fe,mt)};be(M,Fe=>{r(Nr)!==void 0&&Fe(se)});var Te=Y(M,2),Be=Fe=>{var mt=kE(),it=I(mt);Le(()=>{var ut;return xt(it,"Column: ".concat((ut=r(to))!==null&&ut!==void 0?ut:""))}),U(Fe,mt)};be(Te,Fe=>{r(to)!==void 0&&Fe(Be)});var Oe=Y(Te,2),Ge=Fe=>{var mt=SE(),it=I(mt);Le(()=>{var ut;return xt(it,"Selection: ".concat((ut=r(bo))!==null&&ut!==void 0?ut:""," characters"))}),U(Fe,mt)};be(Oe,Fe=>{r(bo)!==void 0&&r(bo)>0&&Fe(Ge)}),U(zn,jo),jt()})(Ke,{get editorState(){return r(ve)}})};be(vn,Ke=>{s()&&Ke(er)});var Ot=Y(vn,2),an=Ke=>{Fo(Ke,{type:"error",get icon(){return $s},get message(){return r(Se),F(()=>r(Se).message)},get actions(){return r(o)},onClick:jr,onClose:at})};be(Ot,Ke=>{r(Se)&&Ke(an)});var fr=Y(Ot,2),Gn=Ke=>{var zn=nt(()=>[{icon:e0,text:"Format",title:"Format JSON: add proper indentation and new lines (Ctrl+I)",onClick:pe},{icon:Hd,text:"No thanks",title:"Close this message",onClick:()=>g(Ue,!1)}]);Fo(Ke,{type:"success",message:"Do you want to format the JSON?",get actions(){return r(zn)},onClose:at})},Nn=Kt(()=>(r(Se),r(Ue),x(mm),r(B),F(()=>!r(Se)&&r(Ue)&&mm(r(B)))));be(fr,Ke=>{r(Nn)&&Ke(Gn)}),vh(Y(fr,2),{get validationErrors(){return r(Re)},selectError:hn}),U(Ct,jn)};be(Je,Ct=>{r(P)||Ct(Lt)}),Le(()=>Ce=Bt(xe,1,"jse-contents svelte-k2b9e6",null,Ce,{"jse-hidden":r(P)})),U(K,Z)},ir=K=>{U(K,zE())};return be(Wt,K=>{Ie?K(ir,-1):K(Wn)}),or(Br,K=>g(ce,K),()=>r(ce)),Le(()=>vr=Bt(Br,1,"jse-text-mode svelte-k2b9e6",null,vr,{"no-main-menu":!a()})),U(e,Br),Rt(t,"focus",at),Rt(t,"collapse",We),Rt(t,"expand",$),Rt(t,"patch",de),Rt(t,"handlePatch",Me),Rt(t,"openTransformModal",Xe),Rt(t,"refresh",Vt),Rt(t,"flush",Bn),Rt(t,"validate",tn),jt(dr)}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-inline-value.svelte-1jv89ui {
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  line-height: var(--jse-line-height, calc(1em + 4px));
  border: none;
  padding: 0 calc(0.5 * var(--jse-padding, 10px));
  background: transparent;
  color: inherit;
  cursor: inherit;
}
.jse-inline-value.jse-highlight.svelte-1jv89ui {
  background-color: var(--jse-search-match-color, #ffe665);
  outline: var(--jse-search-match-outline, none);
}
.jse-inline-value.jse-highlight.jse-active.svelte-1jv89ui {
  background-color: var(--jse-search-match-active-color, var(--jse-search-match-color, #ffe665));
  outline: var(--jse-search-match-outline, 2px solid #e0be00);
}`);var RE=re('<button type="button"> </button>');It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-column-header.svelte-5pxwfq {
  background: none;
  border: none;
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  display: flex;
  gap: var(--jse-padding, 10px);
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px) calc(0.5 * var(--jse-padding, 10px)) calc(0.5 * var(--jse-padding, 10px));
  width: 100%;
}
.jse-column-header.svelte-5pxwfq:hover {
  background: var(--jse-table-header-background-highlight, #e8e8e8);
}
.jse-column-header.svelte-5pxwfq:not(.jse-column-header.jse-readonly) {
  cursor: pointer;
}
.jse-column-header.svelte-5pxwfq span.jse-column-sort-icon:where(.svelte-5pxwfq) {
  height: 1em;
}`);var IE=re('<span class="jse-column-sort-icon svelte-5pxwfq"><!></span>'),qE=re('<button type="button"><span class="jse-column-name"> </span> <!></button>');It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-table-mode-welcome.svelte-1b9gnk8 {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: auto;
  align-items: center;
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-table-mode-welcome.svelte-1b9gnk8:last-child {
  border-bottom: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-space.jse-before:where(.svelte-1b9gnk8) {
  flex: 1;
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) {
  display: flex;
  flex-direction: column;
  gap: var(--jse-padding, 10px);
  max-width: 400px;
  margin: 2em var(--jse-padding, 10px);
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) .jse-nested-arrays-info:where(.svelte-1b9gnk8) {
  color: var(--jse-panel-color-readonly, #b2b2b2);
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) .jse-nested-property:where(.svelte-1b9gnk8) {
  display: flex;
  align-items: center;
  gap: var(--jse-padding, 10px);
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) .jse-nested-property:where(.svelte-1b9gnk8) .jse-nested-property-path:where(.svelte-1b9gnk8) {
  flex: 1;
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) .jse-nested-property:where(.svelte-1b9gnk8) .jse-nested-property-path:where(.svelte-1b9gnk8) .jse-nested-property-count:where(.svelte-1b9gnk8) {
  opacity: 0.5;
  white-space: nowrap;
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) button.jse-nested-array-action:where(.svelte-1b9gnk8) {
  text-align: left;
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-button-primary-background, var(--jse-theme-color, #3883fa));
  color: var(--jse-button-primary-color, #fff);
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  border-radius: 3px;
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) button.jse-nested-array-action:where(.svelte-1b9gnk8):hover {
  background: var(--jse-button-primary-background-highlight, var(--jse-theme-color-highlight, #5f9dff));
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-nested-arrays:where(.svelte-1b9gnk8) button.jse-nested-array-action:where(.svelte-1b9gnk8):disabled {
  background: var(--jse-button-primary-background-disabled, #9d9d9d);
}
.jse-table-mode-welcome.svelte-1b9gnk8 .jse-space.jse-after:where(.svelte-1b9gnk8) {
  flex: 2;
}`);var DE=re(`An empty document cannot be opened in table mode. You can go to tree mode instead, or paste
        a JSON Array using <b>Ctrl+V</b>.`,1),LE=re('<button type="button" class="jse-nested-array-action svelte-1b9gnk8">Extract</button>'),UE=re('<div class="jse-nested-property svelte-1b9gnk8"><div class="jse-nested-property-path svelte-1b9gnk8"> <span class="jse-nested-property-count svelte-1b9gnk8"> </span></div> <button type="button" class="jse-nested-array-action svelte-1b9gnk8"> </button> <!></div>'),BE=re('<div class="jse-table-mode-welcome svelte-1b9gnk8" role="none"><div class="jse-space jse-before svelte-1b9gnk8"></div> <div class="jse-nested-arrays svelte-1b9gnk8"><div class="jse-nested-arrays-title"> </div> <div class="jse-nested-arrays-info svelte-1b9gnk8"><!></div> <!> <button type="button" class="jse-nested-array-action svelte-1b9gnk8">Switch to tree mode</button></div> <div class="jse-space jse-after svelte-1b9gnk8"></div></div>');function FE(e,t){yt(t,!0);var n=Kt(()=>t.json?function(b){var k=arguments.length>1&&arguments[1]!==void 0?arguments[1]:2,E=[];return function O(w,_){$r(w)&&_.length<k&&Object.keys(w).forEach(A=>{O(w[A],_.concat(A))}),Cr(w)&&E.push(_)}(b,[]),E}(t.json).slice(0,99).filter(b=>b.length>0):[]),o=Kt(()=>!gn(r(n))),i=Kt(()=>t.json===void 0&&(t.text===""||t.text===void 0)),a=Kt(()=>r(o)?"Object with nested arrays":r(i)?"An empty document":$r(t.json)?"An object":Cr(t.json)?"An empty array":"A ".concat(Hp(t.json,t.parser))),s=BE(),l=Y(I(s),2),c=I(l),u=I(c),d=Y(c,2),v=I(d),f=b=>{U(b,oo(`An object cannot be opened in table mode. You can open a nested array instead, or open the
        document in tree mode.`))},h=b=>{U(b,DE())},p=b=>{var k=oo();Le(()=>{var E;return xt(k,"".concat((E=r(a))!==null&&E!==void 0?E:""," cannot be opened in table mode. You can open the document in tree mode instead."))}),U(b,k)};be(v,b=>{r(o)?b(f):r(i)&&!t.readOnly?b(h,1):b(p,-1)});var y=Y(d,2);Or(y,17,()=>r(n),Pr,(b,k)=>{var E=Kt(()=>function(H){return tt(t.json,H).length}(r(k))),O=UE(),w=I(O),_=I(w),A=I(Y(_)),q=Y(w,2),C=I(q),z=Y(q,2),D=H=>{var Q=LE();ha("click",Q,()=>t.extractPath(r(k))),U(H,Q)};be(z,H=>{t.readOnly||H(D)}),Le(H=>{var Q;xt(_,'"'.concat(H??"",'" ')),xt(A,"(".concat((Q=r(E))!==null&&Q!==void 0?Q:""," ").concat(r(E)!==1?"items":"item",")")),xt(C,t.readOnly?"View":"Edit")},[()=>Eo(r(k))]),ha("click",q,()=>t.openJSONEditorModal(r(k))),U(b,O)});var j=Y(y,2);Le(()=>xt(u,r(a))),ha("click",s,()=>t.onClick()),ha("click",j,()=>t.onChangeMode(Mr.tree)),U(e,s),jt()}Zc(["click"]);It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-column-header.svelte-1wgrwv3 {
  background: none;
  border: none;
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  display: flex;
  gap: var(--jse-padding, 10px);
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px) calc(0.5 * var(--jse-padding, 10px)) calc(0.5 * var(--jse-padding, 10px));
  width: 100%;
}
.jse-column-header.svelte-1wgrwv3:hover {
  background: var(--jse-table-header-background-highlight, #e8e8e8);
}
.jse-column-header.svelte-1wgrwv3:not(.jse-column-header.jse-readonly) {
  cursor: pointer;
}`);var WE=re('<button type="button"><!></button>');It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-table-mode.svelte-1p86y3c {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  background: var(--jse-background-color, #fff);
  min-width: 0;
  min-height: 0;
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  color: var(--jse-text-color, #4d4d4d);
  line-height: var(--jse-line-height, calc(1em + 4px));
}
.jse-table-mode.no-main-menu.svelte-1p86y3c {
  border-top: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-table-mode.svelte-1p86y3c .jse-search-box-container:where(.svelte-1p86y3c) {
  position: relative;
  height: 0;
  top: calc(var(--jse-line-height, calc(1em + 4px)) + 2 * var(--jse-padding, 10px));
  margin-right: calc(var(--jse-padding, 10px) + 20px);
  margin-left: var(--jse-padding, 10px);
  text-align: right;
  z-index: 3;
}
.jse-table-mode.svelte-1p86y3c .jse-hidden-input-label:where(.svelte-1p86y3c) {
  position: fixed;
  right: 0;
  top: 0;
  width: 0;
  height: 0;
}
.jse-table-mode.svelte-1p86y3c .jse-hidden-input-label:where(.svelte-1p86y3c) .jse-hidden-input:where(.svelte-1p86y3c) {
  width: 0;
  height: 0;
  padding: 0;
  border: 0;
  outline: none;
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) {
  flex: 1;
  align-items: flex-start;
  flex-direction: column;
  display: flex;
  overflow: auto;
  overflow-anchor: none;
  scrollbar-gutter: stable;
  border-left: var(--jse-main-border, 1px solid #d7d7d7);
  border-right: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c):last-child {
  border-bottom: var(--jse-main-border, 1px solid #d7d7d7);
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) {
  border-collapse: collapse;
  border-spacing: 0;
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-invisible-start-section:where(.svelte-1p86y3c) td:where(.svelte-1p86y3c),
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-invisible-end-section:where(.svelte-1p86y3c) td:where(.svelte-1p86y3c) {
  margin: 0;
  padding: 0;
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-search-box-background:where(.svelte-1p86y3c) {
  background: var(--jse-table-header-background, #f5f5f5);
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-invisible-end-section:where(.svelte-1p86y3c) td:where(.svelte-1p86y3c) {
  padding-bottom: var(--jse-padding, 10px);
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c):hover {
  background-color: var(--jse-table-row-odd-background, rgba(0, 0, 0, 0.05));
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell:where(.svelte-1p86y3c) {
  padding: 0 var(--jse-padding, 10px) 0 0;
  vertical-align: top;
  white-space: nowrap;
  height: var(--jse-line-height, calc(1em + 4px));
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell.jse-table-cell-header:where(.svelte-1p86y3c), .jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell.jse-table-cell-gutter:where(.svelte-1p86y3c) {
  font-weight: normal;
  text-align: left;
  color: var(--jse-text-readonly, #8d8d8d);
  background: var(--jse-table-header-background, #f5f5f5);
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell.jse-table-cell-header:where(.svelte-1p86y3c) {
  padding: 0;
  position: sticky;
  top: 0;
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell.jse-table-cell-header:where(.svelte-1p86y3c) .jse-table-root-error:where(.svelte-1p86y3c) {
  padding: calc(0.5 * var(--jse-padding, 10px)) var(--jse-padding, 10px) calc(0.5 * var(--jse-padding, 10px)) calc(0.5 * var(--jse-padding, 10px));
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell.jse-table-cell-gutter:where(.svelte-1p86y3c) {
  padding: 0 var(--jse-padding, 10px) 0 calc(0.5 * var(--jse-padding, 10px));
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell:where(.svelte-1p86y3c) .jse-value-outer:where(.svelte-1p86y3c) {
  display: inline-block;
  cursor: var(--jse-contents-cursor, pointer);
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell:where(.svelte-1p86y3c) .jse-value-outer:where(.svelte-1p86y3c):hover {
  background: var(--jse-hover-background-color, rgba(0, 0, 0, 0.06));
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell:where(.svelte-1p86y3c) .jse-value-outer.jse-selected-value:where(.svelte-1p86y3c) {
  background: var(--jse-selection-background-color, #d3d3d3);
}
.jse-table-mode.svelte-1p86y3c .jse-contents:where(.svelte-1p86y3c) table.jse-table-main:where(.svelte-1p86y3c) .jse-table-row:where(.svelte-1p86y3c) .jse-table-cell:where(.svelte-1p86y3c) .jse-context-menu-anchor:where(.svelte-1p86y3c) {
  display: inline-flex;
  position: relative;
  vertical-align: top;
}
.jse-table-mode.svelte-1p86y3c .jse-contents.jse-contents-loading:where(.svelte-1p86y3c) {
  align-items: unset;
}
.jse-table-mode.svelte-1p86y3c .jse-contents.jse-contents-loading:where(.svelte-1p86y3c) .jse-loading-space:where(.svelte-1p86y3c) {
  flex: 1;
}
.jse-table-mode.svelte-1p86y3c .jse-contents.jse-contents-loading:where(.svelte-1p86y3c) .jse-loading:where(.svelte-1p86y3c) {
  flex: 2;
  text-align: center;
  color: var(--jse-panel-color-readonly, #b2b2b2);
  box-sizing: border-box;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
}`);var VE=re('<div class="jse-table-root-error svelte-1p86y3c"><!></div>'),JE=re('<th class="jse-table-cell jse-table-cell-header svelte-1p86y3c"><!></th>'),HE=re('<th class="jse-table-cell jse-table-cell-header svelte-1p86y3c"><!></th>'),QE=re('<th class="jse-table-cell jse-table-cell-gutter svelte-1p86y3c"> <!></th>'),KE=re('<div class="jse-context-menu-anchor svelte-1p86y3c"><!></div>'),GE=re('<td class="jse-table-cell svelte-1p86y3c"><div><!><!></div> <!></td>'),YE=re('<td class="jse-table-cell svelte-1p86y3c"></td>'),XE=re('<tr class="jse-table-row svelte-1p86y3c"><!><!><!></tr>'),ZE=re('<div class="jse-search-box-container svelte-1p86y3c"><!></div> <div class="jse-contents svelte-1p86y3c"><table class="jse-table-main svelte-1p86y3c"><tbody><tr class="jse-table-row jse-table-row-header svelte-1p86y3c"><th class="jse-table-cell jse-table-cell-header svelte-1p86y3c"><!></th><!><!></tr><tr><td class="svelte-1p86y3c"></td></tr><!><tr class="jse-table-invisible-end-section svelte-1p86y3c"><td class="svelte-1p86y3c"></td></tr></tbody></table></div> <!> <!> <!> <!>',1),e7=re("<!> <!>",1),t7=re('<label class="jse-hidden-input-label svelte-1p86y3c"><input type="text" tabindex="-1" class="jse-hidden-input svelte-1p86y3c"/></label> <!>',1),n7=re('<div class="jse-contents jse-contents-loading svelte-1p86y3c"><div class="jse-loading-space svelte-1p86y3c"></div> <div class="jse-loading svelte-1p86y3c">loading...</div></div>'),r7=re('<div role="table"><!> <!></div> <!> <!>',1);function o7(e,t){yt(t,!1);var n=R(void 0,!0),o=R(void 0,!0),i=R(void 0,!0),a=Zr("jsoneditor:TableMode"),{openAbsolutePopup:s,closeAbsolutePopup:l}=rs("absolute-popup"),c=oj(),u=Sl(),d=Sl(),v=typeof window>"u";a("isSSR:",v);var f=m(t,"readOnly",9),h=m(t,"externalContent",9),p=m(t,"externalSelection",9),y=m(t,"history",9),j=m(t,"truncateTextSize",9),b=m(t,"mainMenuBar",9),k=m(t,"escapeControlCharacters",9),E=m(t,"escapeUnicodeCharacters",9),O=m(t,"flattenColumns",9),w=m(t,"parser",9),_=m(t,"parseMemoizeOne",9),A=m(t,"validator",9),q=m(t,"validationParser",9),C=m(t,"indentation",9),z=m(t,"onChange",9),D=m(t,"onChangeMode",9),H=m(t,"onSelect",9),Q=m(t,"onUndo",9),fe=m(t,"onRedo",9),Ie=m(t,"onRenderValue",9),ge=m(t,"onRenderMenu",9),qe=m(t,"onRenderContextMenu",9),ce=m(t,"onFocus",9),ve=m(t,"onBlur",9),he=m(t,"onSortModal",9),Ue=m(t,"onTransformModal",9),Re=m(t,"onJSONEditorModal",9),we=R(void 0,!0),ue=R(void 0,!0),ie=R(void 0,!0),vt=R(void 0,!0),ft=R(void 0,!0);dh({onMount:vo,onDestroy:ra,getWindow:()=>nu(r(ue)),hasFocus:()=>He&&document.hasFocus()||Gp(r(ue)),onFocus:()=>{qt=!0,ce()&&ce()()},onBlur:()=>{qt=!1,ve()&&ve()()}});var kt,oe=R(void 0,!0),Ze=R(void 0,!0),te=R(void 0,!0),X=R(void 0,!0),B=R(void 0,!0),Ne=R(void 0,!0),ee=R(!1,!0),L=R(!1,!0);function pt(M){g(Ne,(kt=M)?Jy(r(oe),kt.items):void 0)}function ht(M){return _e.apply(this,arguments)}function _e(){return(_e=Pt(function*(M){g(le,void 0),yield en(M)})).apply(this,arguments)}function at(){g(ee,!1),g(L,!1),ye()}var We=R(1e4,!0),Ye=R([],!0),Tt=R(void 0,!0),He=!1,qt=!1,S=R(!1,!0),$=R({},!0),N=R(600,!0),G=R(0,!0),W=18;function de(M){g(le,M)}function Me(M){r(le)&&M!==void 0&&(To(M,_s(r(le)))&&To(M,st(r(le)))||(a("clearing selection: path does not exist anymore",r(le)),g(le,void 0)))}var pe=R(r(oe)!==void 0?Vf({json:r(oe)}):void 0,!0),le=R(Nc(p())?p():void 0,!0),St=R(void 0,!0),lt=R(!1,!0);function Xe(M){if(!f()){a("onSortByHeader",M);var se=M.sortDirection===Yo.desc?-1:1;hn(dj(r(oe),[],M.path,se),(Te,Be)=>({state:Be,sortedColumn:M}))}}vo(()=>{r(le)&&Ht(st(r(le)))});var Ae=R(void 0,!0);function $t(M){if(M.json!==void 0||M.text!==void 0){var se=r(oe)!==void 0&&M.json!==void 0;y().add({type:"tree",undo:{patch:se?[{op:"replace",path:"",value:M.json}]:void 0,json:M.json,text:M.text,documentState:M.documentState,textIsRepaired:M.textIsRepaired,selection:Ma(M.selection),sortedColumn:M.sortedColumn},redo:{patch:se?[{op:"replace",path:"",value:r(oe)}]:void 0,json:r(oe),text:r(Ze),documentState:r(pe),textIsRepaired:r(lt),selection:Ma(r(le)),sortedColumn:r(St)}})}}var sn=R([],!0),Un=Ec(aj);function Yt(M,se,Te,Be){fl(()=>{var Oe;try{Oe=Un(M,se,Te,Be)}catch(Ge){Oe=[{path:[],message:"Failed to validate: "+Ge.message,severity:ba.warning}]}Gt(Oe,r(sn))||(a("validationErrors changed:",Oe),g(sn,Oe))},Oe=>a("validationErrors updated in ".concat(Oe," ms")))}function Zt(){return a("validate"),r(te)?{parseError:r(te),isRepairable:!1}:(Yt(r(oe),A(),w(),q()),gn(r(sn))?void 0:{validationErrors:r(sn)})}function Dt(M,se){if(a("patch",M,se),r(oe)===void 0)throw new Error("Cannot apply patch: no JSON");var Te=r(oe),Be={json:void 0,text:r(Ze),documentState:r(pe),selection:Ma(r(le)),sortedColumn:r(St),textIsRepaired:r(lt)},Oe=Vy(r(oe),M),Ge=zy(r(oe),r(pe),M),Fe=Q_(r(St),M,r(Ye)),mt=typeof se=="function"?se(Ge.json,Ge.documentState,r(le)):void 0;return g(oe,(mt==null?void 0:mt.json)!==void 0?mt.json:Ge.json),g(pe,(mt==null?void 0:mt.state)!==void 0?mt.state:Ge.documentState),g(le,(mt==null?void 0:mt.selection)!==void 0?mt.selection:r(le)),g(St,(mt==null?void 0:mt.sortedColumn)!==void 0?mt.sortedColumn:Fe),g(Ze,void 0),g(lt,!1),g(X,void 0),g(B,void 0),g(te,void 0),y().add({type:"tree",undo:De({patch:Oe},Be),redo:{patch:M,json:void 0,text:void 0,documentState:r(pe),selection:Ma(r(le)),sortedColumn:r(St),textIsRepaired:r(lt)}}),{json:r(oe),previousJson:Te,undo:Oe,redo:M}}function hn(M,se){a("handlePatch",M,se);var Te={json:r(oe),text:r(Ze)},Be=Dt(M,se);return Hn(Te,Be),Be}function Hn(M,se){if((M.json!==void 0||(M==null?void 0:M.text)!==void 0)&&z()){if(r(Ze)!==void 0){var Te={text:r(Ze),json:void 0};z()(Te,M,{contentErrors:Zt(),patchResult:se})}else if(r(oe)!==void 0){var Be={text:void 0,json:r(oe)};z()(Be,M,{contentErrors:Zt(),patchResult:se})}}}function J(M){a("pasted json as text",M),g(X,M)}function V(M){a("pasted multiline text",{pastedText:M}),g(B,M)}function Ve(M){var se=parseInt(M[0],10),Te=[String(se+1),...M.slice(1)];return To(r(oe),Te)?rn(Te):rn(M)}function ye(){a("focus"),r(vt)&&(r(vt).focus(),r(vt).select())}function rt(M){g(G,M.target.scrollTop)}function dt(){r(le)||g(le,function(){if(Cr(r(oe))&&!gn(r(oe))&&!gn(r(Ye)))return rn(["0",...r(Ye)[0]])}())}function At(){if(r(lt)&&r(oe)!==void 0){var M={json:r(oe),text:r(Ze)},se={json:r(oe),documentState:r(pe),selection:r(le),sortedColumn:r(St),text:r(Ze),textIsRepaired:r(lt)};g(Ze,void 0),g(lt,!1),Me(r(oe)),$t(se),Hn(M,void 0)}return{json:r(oe),text:r(Ze)}}function en(M){var{scrollToWhenVisible:se=!0}=arguments.length>1&&arguments[1]!==void 0?arguments[1]:{},Te=r(ee)?vc:0,Be=n0(M,r(Ye),$,W),Oe=Be-r(G)+Te+W,Ge=On(M);if(a("scrollTo",{path:M,top:Be,scrollTop:r(G),elem:Ge}),!r(ie))return Promise.resolve();var Fe=r(ie).getBoundingClientRect();if(Ge&&!se){var mt=Ge.getBoundingClientRect();if(mt.bottom>Fe.top&&mt.top<Fe.bottom)return Promise.resolve()}var it=-Math.max(Te+2*W,Fe.height/4);return new Promise(Ge?ut=>{c(Ge,{container:r(ie),offset:it,duration:300,callback:()=>{Vt(M),ut()}})}:ut=>{c(Oe,{container:r(ie),offset:it,duration:300,callback:()=>{Xn(),Vt(M),ut()}})})}function Vt(M){var se=On(M);if(se&&r(ie)){var Te=r(ie).getBoundingClientRect(),Be=se.getBoundingClientRect();if(Be.right>Te.right){var Oe=Be.right-Te.right;Lo(ie,r(ie).scrollLeft+=Oe)}if(Be.left<Te.left){var Ge=Te.left-Be.left;Lo(ie,r(ie).scrollLeft-=Ge)}}}function Ht(M){(function(se){if(r(ie)){var{rowIndex:Te}=Qo(se,r(Ye)),Be=n0(se,r(Ye),$,W),Oe=Be+($[Te]||W),Ge=W,Fe=r(ie).getBoundingClientRect(),mt=r(G),it=r(G)+Fe.height-Ge;if(Oe>it){var ut=Oe-it;Lo(ie,r(ie).scrollTop+=ut)}if(Be<mt){var ln=mt-Be;Lo(ie,r(ie).scrollTop-=ln)}}})(M),Vt(M)}function On(M){var se,Te,Be=r(Ye).find(Ge=>Ra(M.slice(1),Ge)),Oe=Be?M.slice(0,1).concat(Be):M;return(se=(Te=r(ie))===null||Te===void 0?void 0:Te.querySelector('td[data-path="'.concat(Ju(Oe),'"]')))!==null&&se!==void 0?se:void 0}function dn(M){var se,{anchor:Te,left:Be,top:Oe,width:Ge,height:Fe,offsetTop:mt,offsetLeft:it,showTip:ut}=M,ln=function(ae){var{json:$e,documentState:et,selection:ke,readOnly:Pe,onEditValue:bt,onEditRow:Nt,onToggleEnforceString:Qt,onCut:xn,onCopy:nn,onPaste:Yn,onRemove:Ut,onDuplicateRow:cr,onInsertBeforeRow:Rn,onInsertAfterRow:tr,onRemoveRow:wn}=ae,Et=$e!==void 0,fn=!!ke,In=$e!==void 0&&ke?tt($e,st(ke)):void 0,xr=Et&&(Jn(ke)||Yr(ke)||bn(ke)),_r=!Pe&&Et&&ke!==void 0&&md(ke),ct=_r&&!mr(In),Jt=!Pe&&xr,ur=ke!==void 0&&$a($e,et,st(ke));return[{type:"separator"},{type:"row",items:[{type:"column",items:[{type:"label",text:"Table cell:"},{type:"dropdown-button",main:{type:"button",onClick:()=>bt(),icon:pl,text:"Edit",title:"Edit the value (Double-click on the value)",disabled:!_r},width:"11em",items:[{type:"button",icon:pl,text:"Edit",title:"Edit the value (Double-click on the value)",onClick:()=>bt(),disabled:!_r},{type:"button",icon:ur?nb:ab,text:"Enforce string",title:"Enforce keeping the value as string when it contains a numeric value",onClick:()=>Qt(),disabled:!ct}]},{type:"dropdown-button",main:{type:"button",onClick:()=>xn(!0),icon:hl,text:"Cut",title:"Cut selected contents, formatted with indentation (Ctrl+X)",disabled:!Jt},width:"10em",items:[{type:"button",icon:hl,text:"Cut formatted",title:"Cut selected contents, formatted with indentation (Ctrl+X)",onClick:()=>xn(!0),disabled:Pe||!xr},{type:"button",icon:hl,text:"Cut compacted",title:"Cut selected contents, without indentation (Ctrl+Shift+X)",onClick:()=>xn(!1),disabled:Pe||!xr}]},{type:"dropdown-button",main:{type:"button",onClick:()=>nn(!0),icon:Ri,text:"Copy",title:"Copy selected contents, formatted with indentation (Ctrl+C)",disabled:!xr},width:"12em",items:[{type:"button",icon:Ri,text:"Copy formatted",title:"Copy selected contents, formatted with indentation (Ctrl+C)",onClick:()=>nn(!1),disabled:!xr},{type:"button",icon:Ri,text:"Copy compacted",title:"Copy selected contents, without indentation (Ctrl+Shift+C)",onClick:()=>nn(!1),disabled:!xr}]},{type:"button",onClick:()=>Yn(),icon:Z1,text:"Paste",title:"Paste clipboard contents (Ctrl+V)",disabled:Pe||!fn},{type:"button",onClick:()=>Ut(),icon:xf,text:"Remove",title:"Remove selected contents (Delete)",disabled:Pe||!xr}]},{type:"column",items:[{type:"label",text:"Table row:"},{type:"button",onClick:()=>Nt(),icon:pl,text:"Edit row",title:"Edit the current row",disabled:Pe||!fn||!Et},{type:"button",onClick:()=>cr(),icon:tb,text:"Duplicate row",title:"Duplicate the current row (Ctrl+D)",disabled:Pe||!fn||!Et},{type:"button",onClick:()=>Rn(),icon:il,text:"Insert before",title:"Insert a row before the current row",disabled:Pe||!fn||!Et},{type:"button",onClick:()=>tr(),icon:il,text:"Insert after",title:"Insert a row after the current row",disabled:Pe||!fn||!Et},{type:"button",onClick:()=>wn(),icon:xf,text:"Remove row",title:"Remove current row",disabled:Pe||!fn||!Et}]}]}]}({json:r(oe),documentState:r(pe),selection:r(le),readOnly:f(),onEditValue:Bn,onEditRow:Zn,onToggleEnforceString:yr,onCut:dr,onCopy:Br,onPaste:ar,onRemove:zr,onDuplicateRow:yn,onInsertBeforeRow:Wt,onInsertAfterRow:Wn,onRemoveRow:ir}),An=(se=qe()(ln))!==null&&se!==void 0?se:ln;if(An!==!1){var xo={left:Be,top:Oe,offsetTop:mt,offsetLeft:it,width:Ge,height:Fe,anchor:Te,closeOnOuterClick:!0,onClose:()=>{He=!1,ye()}};He=!0;var T=s(xj,{tip:ut?"Tip: you can open this context menu via right-click or with Ctrl+Q":void 0,items:An,onRequestClose(){l(T),ye()}},xo)}}function Qn(M){if(!Kr(r(le)))if(M&&(M.stopPropagation(),M.preventDefault()),M&&M.type==="contextmenu"&&M.target!==r(vt))dn({left:M.clientX,top:M.clientY,width:ri,height:ni,showTip:!1});else{var se,Te=(se=r(ie))===null||se===void 0?void 0:se.querySelector(".jse-table-cell.jse-selected-value");if(Te)dn({anchor:Te,offsetTop:2,width:ri,height:ni,showTip:!1});else{var Be,Oe=(Be=r(ie))===null||Be===void 0?void 0:Be.getBoundingClientRect();Oe&&dn({top:Oe.top+2,left:Oe.left+2,width:ri,height:ni,showTip:!1})}}}function Kn(M){dn({anchor:Ey(M.target,"BUTTON"),offsetTop:0,width:ri,height:ni,showTip:!0})}function Bn(){if(!f()&&r(le)){var M=st(r(le));mr(tt(r(oe),M))?Je(M):g(le,rn(M))}}function Zn(){!f()&&r(le)&&Je(st(r(le)).slice(0,1))}function yr(){if(!f()&&bn(r(le))){var M=r(le).path,se=wt(M),Te=tt(r(oe),M),Be=!$a(r(oe),r(pe),M),Oe=Be?String(Te):Ql(String(Te),w());a("handleToggleEnforceString",{enforceString:Be,value:Te,updatedValue:Oe}),hn([{op:"replace",path:se,value:Oe}],(Ge,Fe)=>({state:Zd(r(oe),Fe,M,{type:"value",enforceString:Be})}))}}function Fn(){return $n.apply(this,arguments)}function $n(){return($n=Pt(function*(){if(a("apply pasted json",r(X)),r(X)){var{onPasteAsJson:M}=r(X);M(),setTimeout(ye)}})).apply(this,arguments)}function ar(){return Se.apply(this,arguments)}function Se(){return(Se=Pt(function*(){try{P(yield navigator.clipboard.readText())}catch(M){console.error(M),g(S,!0)}})).apply(this,arguments)}function Ee(){return tn.apply(this,arguments)}function tn(){return(tn=Pt(function*(){a("apply pasted multiline text",r(B)),r(B)&&(P(JSON.stringify(r(B))),setTimeout(ye))})).apply(this,arguments)}function Ar(){a("clear pasted json"),g(X,void 0),ye()}function jr(){a("clear pasted multiline text"),g(B,void 0),ye()}function on(){D()(Mr.text)}function dr(M){return vr.apply(this,arguments)}function vr(){return(vr=Pt(function*(M){yield hj({json:r(oe),selection:r(le),indentation:M?C():void 0,readOnly:f(),parser:w(),onPatch:hn})})).apply(this,arguments)}function Br(){return eo.apply(this,arguments)}function eo(){return eo=Pt(function*(){var M=!(arguments.length>0&&arguments[0]!==void 0)||arguments[0];r(oe)!==void 0&&(yield gj({json:r(oe),selection:r(le),indentation:M?C():void 0,parser:w()}))}),eo.apply(this,arguments)}function zr(){bj({json:r(oe),text:r(Ze),selection:r(le),keepSelection:!0,readOnly:f(),onChange:z(),onPatch:hn})}function Pn(M){f()||(a("extract",{path:M}),hn(By(r(oe),rn(M))))}function yn(){(function(M){var{json:se,selection:Te,columns:Be,readOnly:Oe,onPatch:Ge}=M;if(!Oe&&se!==void 0&&Te&&dl(Te)){var{rowIndex:Fe,columnIndex:mt}=Qo(st(Te),Be);ho("duplicate row",{rowIndex:Fe});var it=[String(Fe)];Ge(Uy(se,[it]),(ut,ln)=>({state:ln,selection:rn(ps({rowIndex:Fe<se.length?Fe+1:Fe,columnIndex:mt},Be))}))}})({json:r(oe),selection:r(le),columns:r(Ye),readOnly:f(),onPatch:hn})}function Wt(){(function(M){var{json:se,selection:Te,columns:Be,readOnly:Oe,onPatch:Ge}=M;if(!Oe&&se!==void 0&&Te&&dl(Te)){var{rowIndex:Fe}=Qo(st(Te),Be);ho("insert before row",{rowIndex:Fe}),Ge(vl(se,[String(Fe)],[{key:"",value:$r(se[0])?{}:""}]))}})({json:r(oe),selection:r(le),columns:r(Ye),readOnly:f(),onPatch:hn})}function Wn(){(function(M){var{json:se,selection:Te,columns:Be,readOnly:Oe,onPatch:Ge}=M;if(!Oe&&se!==void 0&&Te&&dl(Te)){var{rowIndex:Fe,columnIndex:mt}=Qo(st(Te),Be);ho("insert after row",{rowIndex:Fe});var it=Fe+1,ut=[String(it)],ln=[{key:"",value:$r(se[0])?{}:""}];Ge(it<se.length?vl(se,ut,ln):Qf(se,[],ln),(An,xo)=>({state:xo,selection:rn(ps({rowIndex:it,columnIndex:mt},Be))}))}})({json:r(oe),selection:r(le),columns:r(Ye),readOnly:f(),onPatch:hn})}function ir(){(function(M){var{json:se,selection:Te,columns:Be,readOnly:Oe,onPatch:Ge}=M;if(!Oe&&se!==void 0&&Te&&dl(Te)){var{rowIndex:Fe,columnIndex:mt}=Qo(st(Te),Be);ho("remove row",{rowIndex:Fe}),Ge(yd([[String(Fe)]]),(it,ut)=>{var ln=Fe<it.length?Fe:Fe>0?Fe-1:void 0,An=ln!==void 0?rn(ps({rowIndex:ln,columnIndex:mt},Be)):void 0;return ho("remove row new selection",{rowIndex:Fe,newRowIndex:ln,newSelection:An}),{state:ut,selection:An}})}})({json:r(oe),selection:r(le),columns:r(Ye),readOnly:f(),onPatch:hn})}function K(){return(K=Pt(function*(M){yield yj({char:M,selectInside:!1,json:r(oe),selection:r(le),readOnly:f(),parser:w(),onPatch:hn,onReplaceJson:Z,onSelect:de})})).apply(this,arguments)}function Ce(M){var se;M.preventDefault(),P((se=M.clipboardData)===null||se===void 0?void 0:se.getData("text/plain"))}function P(M){M!==void 0&&mj({clipboardText:M,json:r(oe),selection:r(le),readOnly:f(),parser:w(),onPatch:hn,onChangeText:xe,onPasteMultilineText:V,openRepairModal:Lt})}function Z(M,se){var Te={json:r(oe),text:r(Ze)},Be={json:r(oe),documentState:r(pe),selection:r(le),sortedColumn:r(St),text:r(Ze),textIsRepaired:r(lt)},Oe=Do(M,r(pe)),Ge=typeof se=="function"?se(M,Oe,r(le)):void 0;g(oe,(Ge==null?void 0:Ge.json)!==void 0?Ge.json:M),g(pe,(Ge==null?void 0:Ge.state)!==void 0?Ge.state:Oe),g(le,(Ge==null?void 0:Ge.selection)!==void 0?Ge.selection:r(le)),g(St,void 0),g(Ze,void 0),g(lt,!1),g(te,void 0),Me(r(oe)),$t(Be),Hn(Te,void 0)}function xe(M,se){a("handleChangeText");var Te={json:r(oe),text:r(Ze)},Be={json:r(oe),documentState:r(pe),selection:r(le),sortedColumn:r(St),text:r(Ze),textIsRepaired:r(lt)};try{g(oe,_()(M)),g(pe,Do(r(oe),r(pe))),g(Ze,void 0),g(lt,!1),g(te,void 0)}catch(Ge){try{g(oe,_()(Aa(M))),g(pe,Do(r(oe),r(pe))),g(Ze,M),g(lt,!0),g(te,void 0)}catch{g(oe,void 0),g(pe,void 0),g(Ze,M),g(lt,!1),g(te,r(Ze)!==""?$l(r(Ze),Ge.message||String(Ge)):void 0)}}if(typeof se=="function"){var Oe=se(r(oe),r(pe),r(le));g(oe,(Oe==null?void 0:Oe.json)!==void 0?Oe.json:r(oe)),g(pe,(Oe==null?void 0:Oe.state)!==void 0?Oe.state:r(pe)),g(le,(Oe==null?void 0:Oe.selection)!==void 0?Oe.selection:r(le))}Me(r(oe)),$t(Be),Hn(Te,void 0)}function ot(M){a("select validation error",M),g(le,rn(M.path)),en(M.path)}function Qe(M){if(r(oe)!==void 0){var{id:se,onTransform:Te,onClose:Be}=M,Oe=M.rootPath||[];He=!0,Ue()({id:se||d,json:r(oe),rootPath:Oe||[],onTransform:Ge=>{Te?Te({operations:Ge,json:r(oe),transformedJson:ga(r(oe),Ge)}):(a("onTransform",Oe,Ge),hn(Ge))},onClose:()=>{He=!1,setTimeout(ye),Be&&Be()}})}}function Je(M){a("openJSONEditorModal",{path:M}),He=!0,Re()({content:{json:tt(r(oe),M)},path:M,onPatch:hn,onClose:()=>{He=!1,setTimeout(ye)}})}function Lt(M,se){g(ft,{text:M,onParse:Te=>tu(Te,Be=>eu(Be,w())),onRepair:yy,onApply:se,onClose:ye})}function Ct(){(function(M){f()||r(oe)===void 0||(He=!0,he()({id:u,json:r(oe),rootPath:M,onSort:se=>{var{operations:Te,itemPath:Be,direction:Oe}=se;a("onSort",Te,M,Be,Oe),hn(Te,(Ge,Fe)=>({state:Fe,sortedColumn:{path:Be,sortDirection:Oe===-1?Yo.desc:Yo.asc}}))},onClose:()=>{He=!1,setTimeout(ye)}}))})([])}function jn(){Qe({rootPath:[]})}function vn(M){a("openFind",{findAndReplace:M}),g(ee,!1),g(L,!1),Xn(),g(ee,!0),g(L,M)}function er(){if(!f()&&y().canUndo){var M=y().undo();if(gd(M)){var se={json:r(oe),text:r(Ze)};g(oe,M.undo.patch?ga(r(oe),M.undo.patch):M.undo.json),g(pe,M.undo.documentState),g(le,M.undo.selection),g(St,M.undo.sortedColumn),g(Ze,M.undo.text),g(lt,M.undo.textIsRepaired),g(te,void 0),a("undo",{item:M,json:r(oe)}),Hn(se,M.undo.patch&&M.redo.patch?{json:r(oe),previousJson:se.json,redo:M.undo.patch,undo:M.redo.patch}:void 0),ye(),r(le)&&en(st(r(le)),{scrollToWhenVisible:!1})}else Q()(M)}}function Ot(){if(!f()&&y().canRedo){var M=y().redo();if(gd(M)){var se={json:r(oe),text:r(Ze)};g(oe,M.redo.patch?ga(r(oe),M.redo.patch):M.redo.json),g(pe,M.redo.documentState),g(le,M.redo.selection),g(St,M.redo.sortedColumn),g(Ze,M.redo.text),g(lt,M.redo.textIsRepaired),g(te,void 0),a("redo",{item:M,json:r(oe)}),Hn(se,M.undo.patch&&M.redo.patch?{json:r(oe),previousJson:se.json,redo:M.redo.patch,undo:M.undo.patch}:void 0),ye(),r(le)&&en(st(r(le)),{scrollToWhenVisible:!1})}else fe()(M)}}function an(M){g(N,M.getBoundingClientRect().height)}ne(()=>(x(k()),x(E())),()=>{g(we,Qp({escapeControlCharacters:k(),escapeUnicodeCharacters:E()}))}),ne(()=>r(ee),()=>{(function(M){if(r(ie)){var se=M?vc:-100;r(ie).scrollTo({top:Lo(ie,r(ie).scrollTop+=se),left:r(ie).scrollLeft})}})(r(ee))}),ne(()=>x(h()),()=>{(function(M){var se={json:r(oe)},Te=Mc(M)?M.text!==r(Ze):!Gt(se.json,M.json);if(a("update external content",{isChanged:Te}),Te){var Be={json:r(oe),documentState:r(pe),selection:r(le),sortedColumn:r(St),text:r(Ze),textIsRepaired:r(lt)};if(Mc(M))try{g(oe,_()(M.text)),g(pe,Do(r(oe),r(pe))),g(Ze,M.text),g(lt,!1),g(te,void 0)}catch(Oe){try{g(oe,_()(Aa(M.text))),g(pe,Do(r(oe),r(pe))),g(Ze,M.text),g(lt,!0),g(te,void 0)}catch{g(oe,void 0),g(pe,void 0),g(Ze,M.text),g(lt,!1),g(te,r(Ze)!==""?$l(r(Ze),Oe.message||String(Oe)):void 0)}}else g(oe,M.json),g(pe,Do(r(oe),r(pe))),g(Ze,void 0),g(lt,!1),g(te,void 0);Me(r(oe)),g(St,void 0),$t(Be)}})(h())}),ne(()=>x(p()),()=>{(function(M){Gt(r(le),M)||(a("applyExternalSelection",{selection:r(le),externalSelection:M}),Nc(M)&&g(le,M))})(p())}),ne(()=>(r(Ye),r(oe),x(O()),r(We)),()=>{g(Ye,Cr(r(oe))?function(M,se){var Te=new Set(se.map(wt)),Be=new Set(M.map(wt));for(var Oe of Te)Be.has(Oe)||Te.delete(Oe);for(var Ge of Be)Te.has(Ge)||Te.add(Ge);return[...Te].map(Mo)}(W_(r(oe),O(),r(We)),r(Ye)):[])}),ne(()=>(r(oe),r(Ye)),()=>{g(Tt,!(!r(oe)||gn(r(Ye))))}),ne(()=>(r(oe),r(We)),()=>{g(n,Array.isArray(r(oe))&&r(oe).length>r(We))}),ne(()=>(r(G),r(N),r(oe),r(ee),vc),()=>{g(o,V_(r(G),r(N),r(oe),$,W,r(ee)?vc:0))}),ne(()=>r(oe),()=>{r(oe),r(ie)&&r(ie).scrollTo({top:r(ie).scrollTop,left:r(ie).scrollLeft})}),ne(()=>r(le),()=>{var M;M=r(le),Gt(M,p())||(a("onSelect",M),H()(M))}),ne(()=>(x(f()),x(j()),x(w()),r(we),r(oe),r(pe),x(Ie())),()=>{g(Ae,{mode:Mr.table,readOnly:f(),truncateTextSize:j(),parser:w(),normalization:r(we),getJson:()=>r(oe),getDocumentState:()=>r(pe),findElement:On,findNextInside:Ve,focus:ye,onPatch:(M,se)=>hn(function(Te,Be){return Te.flatMap(Oe=>{if(gp(Oe)){var Ge=Mo(Oe.path);if(Ge.length>0){for(var Fe=[Oe],mt=cn(Ge);mt.length>0&&!To(Be,mt);)Fe.unshift({op:"add",path:wt(mt),value:{}}),mt=cn(mt);return Fe}}return Oe})}(M,r(oe)),se),onSelect:de,onFind:vn,onPasteJson:J,onRenderValue:Ie()})}),ne(()=>(r(oe),x(A()),x(w()),x(q())),()=>{Yt(r(oe),A(),w(),q())}),ne(()=>(r(sn),r(Ye)),()=>{g(i,J_(r(sn),r(Ye)))}),Mn();var fr={validate:Zt,patch:Dt,focus:ye,acceptAutoRepair:At,scrollTo:en,findElement:On,openTransformModal:Qe};Ft(!0);var Gn=r7();ze("mousedown",li,function(M){!Kl(M.target,se=>se===r(ue))&&Kr(r(le))&&(a("click outside the editor, exit edit mode"),g(le,Ma(r(le))),qt&&r(vt)&&(r(vt).focus(),r(vt).blur()),a("blur (outside editor)"),r(vt)&&r(vt).blur())});var Nn,Ke=Mt(Gn),zn=I(Ke),sr=M=>{(function(se,Te){yt(Te,!1);var Be=m(Te,"containsValidArray",9),Oe=m(Te,"readOnly",9),Ge=m(Te,"showSearch",13,!1),Fe=m(Te,"history",9),mt=m(Te,"onSort",9),it=m(Te,"onTransform",9),ut=m(Te,"onContextMenu",9),ln=m(Te,"onUndo",9),An=m(Te,"onRedo",9),xo=m(Te,"onRenderMenu",9);function T(){Ge(!Ge())}var ae=R(void 0,!0),$e=R(void 0,!0);ne(()=>(x(Oe()),x(mt()),x(Be()),x(it()),x(ut()),x(ln()),x(Fe()),x(An())),()=>{g(ae,Oe()?[{type:"space"}]:[{type:"button",icon:sd,title:"Sort",className:"jse-sort",onClick:mt(),disabled:Oe()||!Be()},{type:"button",icon:ad,title:"Transform contents (filter, sort, project)",className:"jse-transform",onClick:it(),disabled:Oe()||!Be()},{type:"button",icon:Jd,title:"Search (Ctrl+F)",className:"jse-search",onClick:T,disabled:!Be()},{type:"button",icon:eb,title:Zp,className:"jse-contextmenu",onClick:ut()},{type:"separator"},{type:"button",icon:Pp,title:"Undo (Ctrl+Z)",className:"jse-undo",onClick:ln(),disabled:!Fe().canUndo},{type:"button",icon:zp,title:"Redo (Ctrl+Shift+Z)",className:"jse-redo",onClick:An(),disabled:!Fe().canRedo},{type:"space"}])}),ne(()=>(x(xo()),r(ae)),()=>{g($e,xo()(r(ae))||r(ae))}),Mn(),Ft(!0),av(se,{get items(){return r($e)}}),jt()})(M,{get containsValidArray(){return r(Tt)},get readOnly(){return f()},get history(){return y()},onSort:Ct,onTransform:jn,onUndo:er,onRedo:Ot,onContextMenu:Kn,get onRenderMenu(){return ge()},get showSearch(){return r(ee)},set showSearch(se){g(ee,se)},$$legacy:!0})};be(zn,M=>{b()&&M(sr)});var _t=Y(zn,2),_n=M=>{var se=t7(),Te=Mt(se),Be=I(Te);Be.readOnly=!0,or(Be,it=>g(vt,it),()=>r(vt));var Oe=Y(Te,2),Ge=it=>{var ut=ZE(),ln=Mt(ut);vj(I(ln),{get json(){return r(oe)},get documentState(){return r(pe)},get parser(){return w()},get showSearch(){return r(ee)},get showReplace(){return r(L)},get readOnly(){return f()},get columns(){return r(Ye)},onSearch:pt,onFocus:ht,onPatch:hn,onClose:at});var An=Y(ln,2),xo=I(An),T=I(xo),ae=I(T),$e=I(ae),et=I($e),ke=ct=>{var Jt=nt(()=>(x(Xs),r(i),F(()=>{var Er;return Xs([],(Er=r(i))===null||Er===void 0?void 0:Er.root)}))),ur=br(),no=Mt(ur),fo=Er=>{var ao=VE();xl(I(ao),{get validationError(){return r(Jt)},get onExpand(){return Ko}}),U(Er,ao)};be(no,Er=>{r(Jt)&&Er(fo)}),U(ct,ur)},Pe=Kt(()=>(x(gn),r(i),F(()=>{var ct;return!gn((ct=r(i))===null||ct===void 0?void 0:ct.root)})));be(et,ct=>{r(Pe)&&ct(ke)});var bt=Y($e);Or(bt,1,()=>r(Ye),Pr,(ct,Jt)=>{var ur=JE();(function(no,fo){yt(fo,!1);var Er=R(void 0,!0),ao=R(void 0,!0),Va=R(void 0,!0),zo=m(fo,"path",9),aa=m(fo,"sortedColumn",9),Oa=m(fo,"readOnly",9),ia=m(fo,"onSort",9);ne(()=>(x(zo()),Eo),()=>{g(Er,gn(zo())?"values":Eo(zo()))}),ne(()=>(x(aa()),x(zo())),()=>{var Rr;g(ao,aa()&&Gt(zo(),(Rr=aa())===null||Rr===void 0?void 0:Rr.path)?aa().sortDirection:void 0)}),ne(()=>(r(ao),jm),()=>{g(Va,r(ao)?jm[r(ao)]:void 0)}),Mn(),Ft(!0);var Qr,Fr=qE(),wo=I(Fr),Wo=I(wo),Ja=Y(wo,2),mn=Rr=>{var Po=IE(),ki=I(Po),Js=nt(()=>(r(ao),x(Yo),x(di),x(zg),F(()=>r(ao)===Yo.asc?di:zg)));un(ki,{get data(){return r(Js)}}),Le(()=>Tn(Po,"title","Currently sorted in ".concat(r(Va)," order"))),U(Rr,Po)};be(Ja,Rr=>{r(ao)!==void 0&&Rr(mn)}),Le(Rr=>{Qr=Bt(Fr,1,"jse-column-header svelte-5pxwfq",null,Qr,{"jse-readonly":Oa()}),Tn(Fr,"title",Oa()?r(Er):r(Er)+" (Click to sort the data by this column)"),xt(Wo,Rr)},[()=>(x(ti),r(Er),x(50),F(()=>ti(r(Er),50)))]),ze("click",Fr,function(){Oa()||ia()({path:zo(),sortDirection:r(ao)===Yo.asc?Yo.desc:Yo.asc})}),U(no,Fr),jt()})(I(ur),{get path(){return r(Jt)},get sortedColumn(){return r(St)},get readOnly(){return f()},onSort:Xe}),U(ct,ur)});var Nt=Y(bt),Qt=ct=>{var Jt=HE(),ur=I(Jt),no=nt(()=>(r(oe),F(()=>Array.isArray(r(oe))?r(oe).length:0)));(function(fo,Er){yt(Er,!1);var ao=m(Er,"count",9),Va=m(Er,"maxSampleCount",9),zo=m(Er,"readOnly",9),aa=m(Er,"onRefresh",9);Ft(!0);var Oa,ia=WE();un(I(ia),{get data(){return DS}}),Le(()=>{Oa=Bt(ia,1,"jse-column-header svelte-1wgrwv3",null,Oa,{"jse-readonly":zo()}),Tn(ia,"title","The Columns are created by sampling ".concat(Va()," items out of ").concat(ao(),". ")+"If you're missing a column, click here to sample all of the items instead of a subset. This is slower.")}),ze("click",ia,()=>aa()()),U(fo,ia),jt()})(ur,{get count(){return r(no)},get maxSampleCount(){return r(We)},get readOnly(){return f()},onRefresh:()=>g(We,1/0)}),U(ct,Jt)};be(Nt,ct=>{r(n)&&ct(Qt)});var xn,nn,Yn=Y(ae),Ut=I(Yn),cr=Y(Yn);Or(cr,1,()=>(r(o),F(()=>r(o).visibleItems)),Pr,(ct,Jt,ur)=>{var no=nt(()=>(r(o),F(()=>r(o).startIndex+ur))),fo=nt(()=>(r(i),x(r(no)),F(()=>r(i).rows[r(no)]))),Er=nt(()=>(x(Xs),x(r(no)),x(r(fo)),F(()=>{var Qr;return Xs([String(r(no))],(Qr=r(fo))===null||Qr===void 0?void 0:Qr.row)}))),ao=nt(()=>(x(Ta),r(oe),r(Ne),x(r(no)),F(()=>Ta(r(oe),r(Ne),[String(r(no))])))),Va=XE(),zo=I(Va);cy(zo,()=>r(no),Qr=>{var Fr=QE(),wo=I(Fr),Wo=Y(wo),Ja=mn=>{xl(mn,{get validationError(){return r(Er)},get onExpand(){return Ko}})};be(Wo,mn=>{r(Er)&&mn(Ja)}),go(Fr,(mn,Rr)=>Iu==null?void 0:Iu(mn,Rr),()=>mn=>function(Rr,Po){$[Po]=Rr.getBoundingClientRect().height}(mn,r(no))),Le(()=>{var mn;return xt(wo,"".concat((mn=r(no))!==null&&mn!==void 0?mn:""," "))}),U(Qr,Fr)});var aa=Y(zo);Or(aa,1,()=>r(Ye),Pr,(Qr,Fr,wo,Wo)=>{var Ja,mn=nt(()=>(x(r(no)),r(Fr),F(()=>[String(r(no))].concat(r(Fr))))),Rr=nt(()=>(x(tt),r(Jt),r(Fr),F(()=>tt(r(Jt),r(Fr))))),Po=nt(()=>(x(bn),r(le),x(Ra),x(r(mn)),F(()=>bn(r(le))&&Ra(r(le).path,r(mn))))),ki=nt(()=>(x(r(fo)),F(()=>{var Ir;return(Ir=r(fo))===null||Ir===void 0?void 0:Ir.columns[wo]}))),Js=nt(()=>(x(Xs),x(r(mn)),x(r(ki)),F(()=>Xs(r(mn),r(ki))))),as=GE(),is=I(as),su=I(is),dv=Ir=>{var yo=nt(()=>(x(jd),x(Ta),r(Jt),x(r(ao)),r(Fr),F(()=>jd(Ta(r(Jt),r(ao),r(Fr)))))),ls=nt(()=>(x(r(yo)),F(()=>!!r(yo)&&r(yo).some(Gl=>Gl.active)))),mv=nt(()=>(x(gn),x(r(yo)),F(()=>!gn(r(yo)))));(function(Gl,Vo){yt(Vo,!1);var ex=m(Vo,"path",9),Th=m(Vo,"value",9),Mh=m(Vo,"parser",9),tx=m(Vo,"isSelected",9),nx=m(Vo,"containsSearchResult",9),rx=m(Vo,"containsActiveSearchResult",9),ox=m(Vo,"onEdit",9);Ft(!0);var $h,lu=RE(),ax=I(lu);Le(Yl=>{$h=Bt(lu,1,"jse-inline-value svelte-1jv89ui",null,$h,{"jse-selected":tx(),"jse-highlight":nx(),"jse-active":rx()}),xt(ax,Yl)},[()=>(x(ti),x(Mh()),x(Th()),x(50),F(()=>{var Yl;return ti((Yl=Mh().stringify(Th()))!==null&&Yl!==void 0?Yl:"",50)}))]),ze("dblclick",lu,()=>ox()(ex())),U(Gl,lu),jt()})(Ir,{get path(){return r(mn)},get value(){return r(Rr)},get parser(){return w()},get isSelected(){return r(Po)},get containsSearchResult(){return r(mv)},get containsActiveSearchResult(){return r(ls)},onEdit:Je})},vv=Kt(()=>(x(mr),x(r(Rr)),F(()=>mr(r(Rr))))),_a=Ir=>{var yo=nt(()=>(x(Ta),r(oe),r(Ne),x(r(mn)),F(()=>{var Vo;return(Vo=Ta(r(oe),r(Ne),r(mn)))===null||Vo===void 0?void 0:Vo.searchResults}))),ls=nt(()=>r(Rr)!==void 0?r(Rr):""),mv=nt(()=>(x($a),r(oe),r(pe),x(r(mn)),F(()=>$a(r(oe),r(pe),r(mn))))),Gl=nt(()=>r(Po)?r(le):void 0);lj(Ir,{get path(){return r(mn)},get value(){return r(ls)},get enforceString(){return r(mv)},get selection(){return r(Gl)},get searchResultItems(){return r(yo)},get context(){return r(Ae)}})};be(su,Ir=>{r(vv)?Ir(dv):Ir(_a,-1)});var ss=Y(su),fv=Ir=>{var yo=KE();Mi(I(yo),{selected:!0,onContextMenu:dn}),U(Ir,yo)},pv=Kt(()=>(x(f()),x(r(Po)),x(Kr),r(le),F(()=>!f()&&r(Po)&&!Kr(r(le)))));be(ss,Ir=>{r(pv)&&Ir(fv)});var hv=Y(is,2),gv=Ir=>{xl(Ir,{get validationError(){return r(Js)},get onExpand(){return Ko}})};be(hv,Ir=>{r(Js)&&Ir(gv)}),Le(Ir=>{Tn(as,"data-path",Ir),Ja=Bt(is,1,"jse-value-outer svelte-1p86y3c",null,Ja,{"jse-selected-value":r(Po)})},[()=>(x(Ju),x(r(mn)),F(()=>Ju(r(mn))))]),U(Qr,as)});var Oa=Y(aa),ia=Qr=>{U(Qr,YE())};be(Oa,Qr=>{r(n)&&Qr(ia)}),U(ct,Va)});var Rn,tr=I(Y(cr));or(An,ct=>g(ie,ct),()=>r(ie)),go(An,(ct,Jt)=>Iu==null?void 0:Iu(ct,Jt),()=>an),so(()=>ze("scroll",An,rt));var wn=Y(An,2),Et=ct=>{var Jt=nt(()=>(r(X),F(()=>"You pasted a JSON ".concat(Array.isArray(r(X).contents)?"array":"object"," as text")))),ur=nt(()=>[{icon:Yi,text:"Paste as JSON instead",title:"Paste the text as JSON instead of a single value",onMouseDown:Fn},{text:"Leave as is",title:"Keep the pasted content as a single value",onClick:Ar}]);Fo(ct,{type:"info",get message(){return r(Jt)},get actions(){return r(ur)}})};be(wn,ct=>{r(X)&&ct(Et)});var fn=Y(wn,2),In=ct=>{var Jt=nt(()=>[{icon:Yi,text:"Paste as string instead",title:"Paste the clipboard data as a single string value instead of an array",onClick:Ee},{text:"Leave as is",title:"Keep the pasted array",onClick:jr}]);Fo(ct,{type:"info",message:"Multiline text was pasted as array",get actions(){return r(Jt)}})};be(fn,ct=>{r(B)&&ct(In)});var xr=Y(fn,2),_r=ct=>{var Jt=nt(()=>f()?[]:[{icon:Ap,text:"Ok",title:"Accept the repaired document",onClick:At},{icon:id,text:"Repair manually instead",title:"Leave the document unchanged and repair it manually instead",onClick:on}]);Fo(ct,{type:"success",message:"The loaded JSON document was invalid but is successfully repaired.",get actions(){return r(Jt)},onClose:ye})};be(xr,ct=>{r(lt)&&ct(_r)}),vh(Y(xr,2),{get validationErrors(){return r(sn)},selectError:ot}),Le(()=>{xn=Bt(Yn,1,"jse-table-invisible-start-section svelte-1p86y3c",null,xn,{"jse-search-box-background":r(ee)}),Tn(Ut,"colspan",(r(Ye),F(()=>r(Ye).length))),nn=ea(Ut,"",nn,{height:(r(o),F(()=>r(o).startHeight+"px"))}),Tn(tr,"colspan",(r(Ye),F(()=>r(Ye).length))),Rn=ea(tr,"",Rn,{height:(r(o),F(()=>r(o).endHeight+"px"))})}),U(it,ut)},Fe=it=>{var ut=e7(),ln=Mt(ut),An=nt(()=>f()?[]:[{icon:id,text:"Repair manually",title:'Open the document in "code" mode and repair it manually',onClick:on}]);Fo(ln,{type:"error",message:"The loaded JSON document is invalid and could not be repaired automatically.",get actions(){return r(An)}}),jj(Y(ln,2),{get text(){return r(Ze)},get json(){return r(oe)},get indentation(){return C()},get parser(){return w()}}),U(it,ut)},mt=it=>{FE(it,{get text(){return r(Ze)},get json(){return r(oe)},get readOnly(){return f()},get parser(){return w()},openJSONEditorModal:Je,extractPath:Pn,get onChangeMode(){return D()},onClick:()=>{ye()}})};be(Oe,it=>{r(Tt)?it(Ge):r(te)&&r(Ze)!==void 0&&r(Ze)!==""?it(Fe,1):it(mt,-1)}),ze("paste",Be,Ce),U(M,se)},lr=M=>{U(M,n7())};be(_t,M=>{v?M(lr,-1):M(_n)}),or(Ke,M=>g(ue,M),()=>r(ue));var Nr=Y(Ke,2),to=M=>{ij(M,{onClose:()=>g(S,!1)})};be(Nr,M=>{r(S)&&M(to)});var bo=Y(Nr,2),jo=M=>{sj(M,Hi(()=>r(ft),{onClose:()=>{var se;(se=r(ft))===null||se===void 0||se.onClose(),g(ft,void 0)}}))};return be(bo,M=>{r(ft)&&M(jo)}),Le(()=>Nn=Bt(Ke,1,"jse-table-mode svelte-1p86y3c",null,Nn,{"no-main-menu":!b()})),ze("mousedown",Ke,function(M){if(M.buttons===1||M.buttons===2){var se=M.target;se.isContentEditable||ye();var Te=Ty(se);if(Te){if(Kr(r(le))&&Rc(r(oe),r(le),Te))return;g(le,rn(Te)),M.preventDefault()}}}),ze("keydown",Ke,function(M){var se=hi(M);if(a("keydown",{combo:se,key:M.key}),se==="Ctrl+X"&&(M.preventDefault(),dr(!0)),se==="Ctrl+Shift+X"&&(M.preventDefault(),dr(!1)),se==="Ctrl+C"&&(M.preventDefault(),Br(!0)),se==="Ctrl+Shift+C"&&(M.preventDefault(),Br(!1)),se==="Ctrl+D"&&(M.preventDefault(),yn()),se!=="Delete"&&se!=="Backspace"||(M.preventDefault(),zr()),se==="Insert"&&M.preventDefault(),se==="Ctrl+A"&&M.preventDefault(),se==="Ctrl+Q"&&Qn(M),se==="ArrowLeft"&&(M.preventDefault(),dt(),r(le))){var Te=function(it,ut){var{rowIndex:ln,columnIndex:An}=Qo(st(ut),it);return An>0?rn(ps({rowIndex:ln,columnIndex:An-1},it)):ut}(r(Ye),r(le));g(le,Te),Ht(st(Te))}if(se==="ArrowRight"&&(M.preventDefault(),dt(),r(le))){var Be=function(it,ut){var{rowIndex:ln,columnIndex:An}=Qo(st(ut),it);return An<it.length-1?rn(ps({rowIndex:ln,columnIndex:An+1},it)):ut}(r(Ye),r(le));g(le,Be),Ht(st(Be))}if(se==="ArrowUp"&&(M.preventDefault(),dt(),r(le))){var Oe=function(it,ut){var{rowIndex:ln,columnIndex:An}=Qo(st(ut),it);return ln>0?rn(ps({rowIndex:ln-1,columnIndex:An},it)):ut}(r(Ye),r(le));g(le,Oe),Ht(st(Oe))}if(se==="ArrowDown"&&(M.preventDefault(),dt(),r(le))){var Ge=function(it,ut,ln){var{rowIndex:An,columnIndex:xo}=Qo(st(ln),ut);return An<it.length-1?rn(ps({rowIndex:An+1,columnIndex:xo},ut)):ln}(r(oe),r(Ye),r(le));g(le,Ge),Ht(st(Ge))}if(se==="Enter"&&r(le)&&bn(r(le))){M.preventDefault();var Fe=r(le).path;mr(tt(r(oe),Fe))?Je(Fe):f()||g(le,De(De({},r(le)),{},{edit:!0}))}if(se.replace(/^Shift\+/,"").length===1&&r(le))return M.preventDefault(),void function(it){K.apply(this,arguments)}(M.key);if(se==="Ctrl+Enter"&&bn(r(le))){M.preventDefault();var mt=tt(r(oe),r(le).path);Xd(mt)&&window.open(String(mt),"_blank")}se==="Escape"&&r(le)&&(M.preventDefault(),g(le,void 0)),se==="Ctrl+F"&&(M.preventDefault(),vn(!1)),se==="Ctrl+H"&&(M.preventDefault(),vn(!0)),se==="Ctrl+Z"&&(M.preventDefault(),er()),se==="Ctrl+Shift+Z"&&(M.preventDefault(),Ot())}),ze("contextmenu",Ke,Qn),U(e,Gn),Rt(t,"validate",Zt),Rt(t,"patch",Dt),Rt(t,"focus",ye),Rt(t,"acceptAutoRepair",At),Rt(t,"scrollTo",en),Rt(t,"findElement",On),Rt(t,"openTransformModal",Qe),jt(fr)}function o0(e,t){yt(t,!1);var n=m(t,"content",8),o=m(t,"selection",12),i=m(t,"readOnly",8),a=m(t,"indentation",8),s=m(t,"tabSize",8),l=m(t,"truncateTextSize",8),c=m(t,"externalMode",8),u=m(t,"mainMenuBar",8),d=m(t,"navigationBar",8),v=m(t,"statusBar",8),f=m(t,"askToFormat",8),h=m(t,"escapeControlCharacters",8),p=m(t,"escapeUnicodeCharacters",8),y=m(t,"maxDocumentSizeTextMode",8),j=m(t,"flattenColumns",8),b=m(t,"parser",8),k=m(t,"parseMemoizeOne",8),E=m(t,"validator",8),O=m(t,"validationParser",8),w=m(t,"pathParser",8),_=m(t,"insideModal",8),A=m(t,"onChange",8),q=m(t,"onChangeMode",8),C=m(t,"onSelect",8),z=m(t,"onRenderValue",8),D=m(t,"onClassName",8),H=m(t,"onRenderMenu",8),Q=m(t,"onRenderContextMenu",8),fe=m(t,"onError",8),Ie=m(t,"onFocus",8),ge=m(t,"onBlur",8),qe=m(t,"onSortModal",8),ce=m(t,"onTransformModal",8),ve=m(t,"onJSONEditorModal",8),he=R(),Ue=R(),Re=R(),we=Zr("jsoneditor:JSONEditorRoot"),ue=R(kj({onChange:W=>g(ue,W)}).get()),ie=R(c());function vt(W){if(Om(W)){g(ie,W.undo.mode);var de=r(ue).items(),Me=de.findIndex(le=>le===W),pe=Me!==-1?de[Me-1]:void 0;we("handleUndo",{index:Me,item:W,items:de,prevItem:pe}),pe&&o(pe.redo.selection),q()(r(ie))}}function ft(W){if(Om(W)){g(ie,W.redo.mode);var de=r(ue).items(),Me=de.findIndex(le=>le===W),pe=Me!==-1?de[Me+1]:void 0;we("handleRedo",{index:Me,item:W,items:de,nextItem:pe}),pe&&o(pe.undo.selection),q()(r(ie))}}var kt=R(),oe={type:"separator"},Ze=R(),te=R();function X(W){if(r(he))return r(he).patch(W);if(r(Ue))return r(Ue).patch(W);if(r(Re))return r(Re).patch(W);throw new Error('Method patch is not available in mode "'.concat(r(ie),'"'))}function B(W,de){if(r(he))return r(he).expand(W,de);if(r(Re))return r(Re).expand(W,de);throw new Error('Method expand is not available in mode "'.concat(r(ie),'"'))}function Ne(W,de){if(r(he))return r(he).collapse(W,de);if(r(Re))return r(Re).collapse(W,de);throw new Error('Method collapse is not available in mode "'.concat(r(ie),'"'))}function ee(W){if(r(Re))r(Re).openTransformModal(W);else if(r(he))r(he).openTransformModal(W);else{if(!r(Ue))throw new Error('Method transform is not available in mode "'.concat(r(ie),'"'));r(Ue).openTransformModal(W)}}function L(){if(r(Re))return r(Re).validate();if(r(he))return r(he).validate();if(r(Ue))return r(Ue).validate();throw new Error('Method validate is not available in mode "'.concat(r(ie),'"'))}function pt(){return r(he)?r(he).acceptAutoRepair():n()}function ht(W){if(r(he))return r(he).scrollTo(W);if(r(Ue))return r(Ue).scrollTo(W);throw new Error('Method scrollTo is not available in mode "'.concat(r(ie),'"'))}function _e(W){if(r(he))return r(he).findElement(W);if(r(Ue))return r(Ue).findElement(W);throw new Error('Method findElement is not available in mode "'.concat(r(ie),'"'))}function at(){r(Re)?r(Re).focus():r(he)?r(he).focus():r(Ue)&&r(Ue).focus()}function We(){return Ye.apply(this,arguments)}function Ye(){return(Ye=Pt(function*(){r(Re)&&(yield r(Re).refresh())})).apply(this,arguments)}ne(()=>x(c()),()=>{(function(W){if(W!==r(ie)){var de={type:"mode",undo:{mode:r(ie),selection:void 0},redo:{mode:W,selection:void 0}};r(ie)==="text"&&r(Re)&&r(Re).flush(),we("add history item",de),r(ue).add(de),g(ie,W)}})(c())}),ne(()=>(r(ie),x(q())),()=>{g(kt,[{type:"button",text:"text",title:"Switch to text mode (current mode: ".concat(r(ie),")"),className:"jse-group-button jse-first"+(r(ie)===Mr.text?" jse-selected":""),onClick:()=>q()(Mr.text)},{type:"button",text:"tree",title:"Switch to tree mode (current mode: ".concat(r(ie),")"),className:"jse-group-button "+(r(ie)===Mr.tree?" jse-selected":""),onClick:()=>q()(Mr.tree)},{type:"button",text:"table",title:"Switch to table mode (current mode: ".concat(r(ie),")"),className:"jse-group-button jse-last"+(r(ie)===Mr.table?" jse-selected":""),onClick:()=>q()(Mr.table)}])}),ne(()=>(r(kt),x(H()),r(ie),x(_()),x(i())),()=>{g(Ze,W=>{var de=Wf(W[0])?r(kt).concat(W):r(kt).concat(oe,W),Me=yf(de);return H()(de,{mode:r(ie),modal:_(),readOnly:i()})||Me})}),ne(()=>(x(Q()),r(ie),x(_()),x(i()),x(o())),()=>{g(te,W=>{var de,Me=yf(W);return(de=Q()(W,{mode:r(ie),modal:_(),readOnly:i(),selection:o()}))!==null&&de!==void 0?de:!i()&&Me})}),Mn();var Tt={patch:X,expand:B,collapse:Ne,transform:ee,validate:L,acceptAutoRepair:pt,scrollTo:ht,findElement:_e,focus:at,refresh:We};Ft();var He=br(),qt=Mt(He),S=W=>{or(NE(W,{get externalContent(){return n()},get externalSelection(){return o()},get history(){return r(ue)},get readOnly(){return i()},get indentation(){return a()},get tabSize(){return s()},get mainMenuBar(){return u()},get statusBar(){return v()},get askToFormat(){return f()},get escapeUnicodeCharacters(){return p()},get maxDocumentSize(){return y()},get parser(){return b()},get validator(){return E()},get validationParser(){return O()},get onChange(){return A()},get onChangeMode(){return q()},get onSelect(){return C()},onUndo:vt,onRedo:ft,get onError(){return fe()},get onFocus(){return Ie()},get onBlur(){return ge()},get onRenderMenu(){return r(Ze)},get onSortModal(){return qe()},get onTransformModal(){return ce()},$$legacy:!0}),de=>g(Re,de),()=>r(Re))},$=Kt(()=>(r(ie),x(Mr),F(()=>r(ie)===Mr.text||String(r(ie))==="code"))),N=W=>{or(o7(W,{get externalContent(){return n()},get externalSelection(){return o()},get history(){return r(ue)},get readOnly(){return i()},get truncateTextSize(){return l()},get mainMenuBar(){return u()},get escapeControlCharacters(){return h()},get escapeUnicodeCharacters(){return p()},get flattenColumns(){return j()},get parser(){return b()},get parseMemoizeOne(){return k()},get validator(){return E()},get validationParser(){return O()},get indentation(){return a()},get onChange(){return A()},get onChangeMode(){return q()},get onSelect(){return C()},onUndo:vt,onRedo:ft,get onRenderValue(){return z()},get onFocus(){return Ie()},get onBlur(){return ge()},get onRenderMenu(){return r(Ze)},get onRenderContextMenu(){return r(te)},get onSortModal(){return qe()},get onTransformModal(){return ce()},get onJSONEditorModal(){return ve()},$$legacy:!0}),de=>g(Ue,de),()=>r(Ue))},G=W=>{or(sp(W,{get externalContent(){return n()},get externalSelection(){return o()},get history(){return r(ue)},get readOnly(){return i()},get indentation(){return a()},get truncateTextSize(){return l()},get mainMenuBar(){return u()},get navigationBar(){return d()},get escapeControlCharacters(){return h()},get escapeUnicodeCharacters(){return p()},get parser(){return b()},get parseMemoizeOne(){return k()},get validator(){return E()},get validationParser(){return O()},get pathParser(){return w()},get onError(){return fe()},get onChange(){return A()},get onChangeMode(){return q()},get onSelect(){return C()},onUndo:vt,onRedo:ft,get onRenderValue(){return z()},get onClassName(){return D()},get onFocus(){return Ie()},get onBlur(){return ge()},get onRenderMenu(){return r(Ze)},get onRenderContextMenu(){return r(te)},get onSortModal(){return qe()},get onTransformModal(){return ce()},get onJSONEditorModal(){return ve()},$$legacy:!0}),de=>g(he,de),()=>r(he))};return be(qt,W=>{r($)?W(S):(r(ie),x(Mr),F(()=>r(ie)===Mr.table)?W(N,1):W(G,-1))}),U(e,He),Rt(t,"patch",X),Rt(t,"expand",B),Rt(t,"collapse",Ne),Rt(t,"transform",ee),Rt(t,"validate",L),Rt(t,"acceptAutoRepair",pt),Rt(t,"scrollTo",ht),Rt(t,"findElement",_e),Rt(t,"focus",at),Rt(t,"refresh",We),jt(Tt)}It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-modal-wrapper.svelte-t4zsk3 {
  flex: 1;
  display: flex;
  min-width: 0;
  min-height: 0;
  flex-direction: column;
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
  overflow: auto;
  min-width: 0;
  min-height: 0;
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) .jse-actions:where(.svelte-t4zsk3) {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-top: var(--jse-padding, 10px);
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) .jse-actions:where(.svelte-t4zsk3) button.jse-primary:where(.svelte-t4zsk3) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-button-primary-background, var(--jse-theme-color, #3883fa));
  color: var(--jse-button-primary-color, #fff);
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  border-radius: 3px;
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) .jse-actions:where(.svelte-t4zsk3) button.jse-primary:where(.svelte-t4zsk3):hover {
  background: var(--jse-button-primary-background-highlight, var(--jse-theme-color-highlight, #5f9dff));
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) .jse-actions:where(.svelte-t4zsk3) button.jse-primary:where(.svelte-t4zsk3):disabled {
  background: var(--jse-button-primary-background-disabled, #9d9d9d);
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) .jse-label:where(.svelte-t4zsk3) {
  font-weight: bold;
  display: block;
  box-sizing: border-box;
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) .jse-label:where(.svelte-t4zsk3) .jse-label-inner:where(.svelte-t4zsk3) {
  margin-top: calc(2 * var(--jse-padding, 10px));
  margin-bottom: calc(0.5 * var(--jse-padding, 10px));
  box-sizing: border-box;
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-modal-contents:where(.svelte-t4zsk3) .jse-modal-inline-editor:where(.svelte-t4zsk3) {
  flex: 1;
  min-height: 150px;
  min-width: 0;
  max-width: 100%;
  display: flex;
  --jse-theme-color: var(--jse-modal-editor-theme-color, #707070);
  --jse-theme-color-highlight: var(--jse-modal-editor-theme-color-highlight, #646464);
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-actions:where(.svelte-t4zsk3) {
  gap: var(--jse-padding, 10px);
  align-items: center;
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-actions:where(.svelte-t4zsk3) .jse-error:where(.svelte-t4zsk3) {
  flex: 1;
  color: var(--jse-error-color, #ee5341);
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-actions:where(.svelte-t4zsk3) button.jse-secondary:where(.svelte-t4zsk3) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-button-secondary-background, #d3d3d3);
  color: var(--jse-button-secondary-color, var(--jse-text-color, #4d4d4d));
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  border-radius: 3px;
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-actions:where(.svelte-t4zsk3) button.jse-secondary:where(.svelte-t4zsk3):hover {
  background: var(--jse-button-secondary-background-highlight, #e1e1e1);
}
.jse-modal-wrapper.svelte-t4zsk3 .jse-actions:where(.svelte-t4zsk3) button.jse-secondary:where(.svelte-t4zsk3):disabled {
  background: var(--jse-button-secondary-background-disabled, #9d9d9d);
}
.jse-modal-wrapper.svelte-t4zsk3 input:where(.svelte-t4zsk3) {
  border: var(--jse-input-border, 1px solid #d8dbdf);
  outline: none;
  box-sizing: border-box;
  padding: calc(0.5 * var(--jse-padding, 10px));
  font-family: var(--jse-font-family-mono, consolas, menlo, monaco, "Ubuntu Mono", "source-code-pro", monospace);
  font-size: var(--jse-font-size-mono, 14px);
  color: inherit;
  background: var(--jse-input-background, var(--jse-background-color, #fff));
}
.jse-modal-wrapper.svelte-t4zsk3 input:where(.svelte-t4zsk3):focus {
  border: var(--jse-input-border-focus, 1px solid var(--jse-input-border-focus, var(--jse-theme-color, #3883fa)));
}
.jse-modal-wrapper.svelte-t4zsk3 input:where(.svelte-t4zsk3):read-only {
  background: var(--jse-input-background-readonly, transparent);
}`);var a7=re('<div class="jse-error svelte-t4zsk3"> </div>'),i7=re('<button type="button" class="jse-secondary svelte-t4zsk3"><!> Back</button>'),s7=re('<button type="button" class="jse-primary svelte-t4zsk3">Apply</button>'),l7=re('<button type="button" class="jse-primary svelte-t4zsk3">Close</button>'),c7=re('<!> <div class="jse-modal-contents svelte-t4zsk3"><div class="jse-label svelte-t4zsk3"><div class="jse-label-inner svelte-t4zsk3">Path</div></div> <input class="jse-path svelte-t4zsk3" type="text" readonly="" title="Selected path"/> <div class="jse-label svelte-t4zsk3"><div class="jse-label-inner svelte-t4zsk3">Contents</div></div> <div class="jse-modal-inline-editor svelte-t4zsk3"><!></div> <div class="jse-actions svelte-t4zsk3"><!> <!> <!></div></div>',1),u7=re('<div class="jse-modal-wrapper svelte-t4zsk3"><!></div>'),d7={};It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-modal-contents.svelte-lwzlls {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 20px;
  overflow: auto;
  min-width: 0;
  min-height: 0;
}
.jse-modal-contents.svelte-lwzlls .jse-actions:where(.svelte-lwzlls) {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-top: var(--jse-padding, 10px);
}
.jse-modal-contents.svelte-lwzlls .jse-actions:where(.svelte-lwzlls) button.jse-primary:where(.svelte-lwzlls) {
  border: none;
  background: transparent;
  color: inherit;
  cursor: pointer;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  padding: 5px;
  margin: 0;
  background: var(--jse-button-primary-background, var(--jse-theme-color, #3883fa));
  color: var(--jse-button-primary-color, #fff);
  padding: var(--jse-padding, 10px) calc(2 * var(--jse-padding, 10px));
  border-radius: 3px;
}
.jse-modal-contents.svelte-lwzlls .jse-actions:where(.svelte-lwzlls) button.jse-primary:where(.svelte-lwzlls):hover {
  background: var(--jse-button-primary-background-highlight, var(--jse-theme-color-highlight, #5f9dff));
}
.jse-modal-contents.svelte-lwzlls .jse-actions:where(.svelte-lwzlls) button.jse-primary:where(.svelte-lwzlls):disabled {
  background: var(--jse-button-primary-background-disabled, #9d9d9d);
}
.jse-modal-contents.svelte-lwzlls table:where(.svelte-lwzlls) {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
}
.jse-modal-contents.svelte-lwzlls table:where(.svelte-lwzlls) th:where(.svelte-lwzlls),
.jse-modal-contents.svelte-lwzlls table:where(.svelte-lwzlls) td:where(.svelte-lwzlls) {
  text-align: left;
  vertical-align: middle;
  font-weight: normal;
  padding-bottom: var(--jse-padding, 10px);
}
.jse-modal-contents.svelte-lwzlls input.jse-path:where(.svelte-lwzlls) {
  width: 100%;
  box-sizing: border-box;
  padding: 5px 10px;
  border: var(--jse-input-border, 1px solid #d8dbdf);
  border-radius: var(--jse-input-radius, 3px);
  font-family: inherit;
  font-size: inherit;
  background: inherit;
  background: var(--jse-input-background-readonly, transparent);
  color: inherit;
  outline: none;
}
.jse-modal-contents.svelte-lwzlls .svelte-select input {
  box-sizing: border-box;
}
.jse-modal-contents.svelte-lwzlls .jse-space:where(.svelte-lwzlls) {
  height: 200px;
}
.jse-modal-contents.svelte-lwzlls .jse-space:where(.svelte-lwzlls) .jse-error:where(.svelte-lwzlls) {
  color: var(--jse-error-color, #ee5341);
}`);var el=Yd(()=>d7),v7=re('<tr><th class="svelte-lwzlls">Property</th><td class="svelte-lwzlls"><!></td></tr>'),f7=re('<div class="jse-error svelte-lwzlls"> </div>'),p7=re('<!> <div class="jse-modal-contents svelte-lwzlls"><table class="svelte-lwzlls"><colgroup><col width="25%"/><col width="75%"/></colgroup><tbody><tr><th class="svelte-lwzlls">Path</th><td class="svelte-lwzlls"><input class="jse-path svelte-lwzlls" type="text" readonly="" title="Selected path"/></td></tr><!><tr><th class="svelte-lwzlls">Direction</th><td class="svelte-lwzlls"><!></td></tr></tbody></table> <div class="jse-space svelte-lwzlls"><!></div> <div class="jse-actions svelte-lwzlls"><button type="button" class="jse-primary svelte-lwzlls">Sort</button></div></div>',1);It(`/* over all fonts, sizes, and colors */
/* "consolas" for Windows, "menlo" for Mac with fallback to "monaco", 'Ubuntu Mono' for Ubuntu */
/* (at Mac this font looks too large at 14px, but 13px is too small for the font on Windows) */
/* main, menu, modal */
/* jsoneditor modal */
/* tooltip in text mode */
/* panels: navigation bar, gutter, search box */
/* navigation-bar */
/* context menu */
/* contents: json key and values */
/* contents: selected or hovered */
/* contents: section of collapsed items in an array */
/* contents: highlighting of search matches */
/* contents: inline tags inside the JSON document */
/* contents: table */
/* controls in modals: inputs, buttons, and \`a\` */
/* messages */
/* svelte-select */
/* color picker */
.jse-main.svelte-1l55585 {
  width: 100%;
  height: 100%;
  min-width: 0;
  min-height: 150px;
  font-family: var(--jse-font-family, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif);
  font-size: var(--jse-font-size, 16px);
  line-height: normal;
  position: relative;
  display: flex;
  flex-direction: row;
}
.jse-main.svelte-1l55585:not(.jse-focus) {
  --jse-selection-background-color: var(--jse-selection-background-inactive-color, #e8e8e8);
  --jse-context-menu-pointer-background: var(--jse-context-menu-pointer-hover-background, #b2b2b2);
}`);var h7=re('<div role="none"><!></div> <!> <!> <!>',1);function g7(e,t){yt(t,!1);var n=R(void 0,!0),o=Zr("jsoneditor:JSONEditor"),i={text:""},a=void 0,s=!1,l=Mr.tree,c=!0,u=!0,d=!0,v=!0,f=!1,h=!1,p=10485760,y=!0,j=JSON,b=void 0,k=JSON,E={parse:O5,stringify:Eo},O=[H9],w=O[0].id,_=Ko,A=void 0,q=void 0,C=C5,z=Ko,D=Ko,H=Ko,Q=Ko,fe=Se=>{console.error(Se),alert(Se.toString())},Ie=Ko,ge=Ko,qe=m(t,"content",13,i),ce=m(t,"selection",13,a),ve=m(t,"readOnly",13,s),he=m(t,"indentation",13,2),Ue=m(t,"tabSize",13,4),Re=m(t,"truncateTextSize",13,1e3),we=m(t,"mode",13,l),ue=m(t,"mainMenuBar",13,c),ie=m(t,"navigationBar",13,u),vt=m(t,"statusBar",13,d),ft=m(t,"askToFormat",13,v),kt=m(t,"escapeControlCharacters",13,f),oe=m(t,"escapeUnicodeCharacters",13,h),Ze=m(t,"maxDocumentSizeTextMode",13,p),te=m(t,"flattenColumns",13,y),X=m(t,"parser",13,j),B=m(t,"validator",13,b),Ne=m(t,"validationParser",13,k),ee=m(t,"pathParser",13,E),L=m(t,"queryLanguages",13,O),pt=m(t,"queryLanguageId",13,w),ht=m(t,"onChangeQueryLanguage",13,_),_e=m(t,"onChange",13,A),at=m(t,"onSelect",13,q),We=m(t,"onRenderValue",13,C),Ye=m(t,"onClassName",13,z),Tt=m(t,"onRenderMenu",13,D),He=m(t,"onRenderContextMenu",13,H),qt=m(t,"onChangeMode",13,Q),S=m(t,"onError",13,fe),$=m(t,"onFocus",13,Ie),N=m(t,"onBlur",13,ge),G=R(ul(),!0),W=R(!1,!0),de=R(void 0,!0),Me=R(void 0,!0),pe=R(void 0,!0),le=R(void 0,!0),St=R(X(),!0);function lt(){return qe()}function Xe(Se){o("set");var Ee=Lv(Se);if(Ee)throw new Error(Ee);g(G,ul()),qe(Se),Xn()}function Ae(Se){o("update");var Ee=Lv(Se);if(Ee)throw new Error(Ee);qe(Se),Xn()}function $t(Se){var Ee=r(de).patch(Se);return Xn(),Ee}function sn(Se){ce(Se),Xn()}function Un(Se,Ee){r(de).expand(Se,Ee),Xn()}function Yt(Se){var Ee=arguments.length>1&&arguments[1]!==void 0&&arguments[1];r(de).collapse(Se,Ee),Xn()}function Zt(){var Se=arguments.length>0&&arguments[0]!==void 0?arguments[0]:{};r(de).transform(Se),Xn()}function Dt(){return r(de).validate()}function hn(){var Se=r(de).acceptAutoRepair();return Xn(),Se}function Hn(Se){return J.apply(this,arguments)}function J(){return(J=Pt(function*(Se){yield r(de).scrollTo(Se)})).apply(this,arguments)}function V(Se){return r(de).findElement(Se)}function Ve(){r(de).focus(),Xn()}function ye(){return rt.apply(this,arguments)}function rt(){return(rt=Pt(function*(){yield r(de).refresh()})).apply(this,arguments)}function dt(Se){var Ee,tn,Ar,jr,on,dr,vr,Br,eo,zr,Pn,yn,Wt,Wn,ir,K,Ce,P,Z,xe,ot,Qe,Je,Lt,Ct,jn,vn,er,Ot,an,fr,Gn,Nn=Object.keys(Se);for(var Ke of Nn)switch(Ke){case"content":qe((Ee=Se[Ke])!==null&&Ee!==void 0?Ee:i);break;case"selection":ce((tn=Se[Ke])!==null&&tn!==void 0?tn:a);break;case"readOnly":ve((Ar=Se[Ke])!==null&&Ar!==void 0?Ar:s);break;case"indentation":he((jr=Se[Ke])!==null&&jr!==void 0?jr:2);break;case"tabSize":Ue((on=Se[Ke])!==null&&on!==void 0?on:4);break;case"truncateTextSize":Re((dr=Se[Ke])!==null&&dr!==void 0?dr:1e3);break;case"mode":we((vr=Se[Ke])!==null&&vr!==void 0?vr:l);break;case"mainMenuBar":ue((Br=Se[Ke])!==null&&Br!==void 0?Br:c);break;case"navigationBar":ie((eo=Se[Ke])!==null&&eo!==void 0?eo:u);break;case"statusBar":vt((zr=Se[Ke])!==null&&zr!==void 0?zr:d);break;case"askToFormat":ft((Pn=Se[Ke])!==null&&Pn!==void 0?Pn:v);break;case"escapeControlCharacters":kt((yn=Se[Ke])!==null&&yn!==void 0?yn:f);break;case"escapeUnicodeCharacters":oe((Wt=Se[Ke])!==null&&Wt!==void 0?Wt:h);break;case"maxDocumentSizeTextMode":Ze((Wn=Se[Ke])!==null&&Wn!==void 0?Wn:p);break;case"flattenColumns":te((ir=Se[Ke])!==null&&ir!==void 0?ir:y);break;case"parser":X((K=Se[Ke])!==null&&K!==void 0?K:j);break;case"validator":B((Ce=Se[Ke])!==null&&Ce!==void 0?Ce:b);break;case"validationParser":Ne((P=Se[Ke])!==null&&P!==void 0?P:k);break;case"pathParser":ee((Z=Se[Ke])!==null&&Z!==void 0?Z:E);break;case"queryLanguages":L((xe=Se[Ke])!==null&&xe!==void 0?xe:O);break;case"queryLanguageId":pt((ot=Se[Ke])!==null&&ot!==void 0?ot:w);break;case"onChangeQueryLanguage":ht((Qe=Se[Ke])!==null&&Qe!==void 0?Qe:_);break;case"onChange":_e((Je=Se[Ke])!==null&&Je!==void 0?Je:A);break;case"onRenderValue":We((Lt=Se[Ke])!==null&&Lt!==void 0?Lt:C);break;case"onClassName":Ye((Ct=Se[Ke])!==null&&Ct!==void 0?Ct:z);break;case"onRenderMenu":Tt((jn=Se[Ke])!==null&&jn!==void 0?jn:D);break;case"onRenderContextMenu":He((vn=Se[Ke])!==null&&vn!==void 0?vn:H);break;case"onChangeMode":qt((er=Se[Ke])!==null&&er!==void 0?er:Q);break;case"onSelect":at((Ot=Se[Ke])!==null&&Ot!==void 0?Ot:q);break;case"onError":S((an=Se[Ke])!==null&&an!==void 0?an:fe);break;case"onFocus":$((fr=Se[Ke])!==null&&fr!==void 0?fr:Ie);break;case"onBlur":N((Gn=Se[Ke])!==null&&Gn!==void 0?Gn:ge);break;default:zn(Ke)}function zn(sr){o('Unknown property "'.concat(sr,'"'))}L().some(sr=>sr.id===pt())||pt(L()[0].id),Xn()}function At(){return en.apply(this,arguments)}function en(){return(en=Pt(function*(){throw new Error("class method destroy() is deprecated. It is replaced with a method destroy() in the vanilla library.")})).apply(this,arguments)}function Vt(Se,Ee,tn){qe(Se),_e()&&_e()(Se,Ee,tn)}function Ht(Se){ce(Se),at()&&at()(yf(Se))}function On(){g(W,!0),$()&&$()()}function dn(){g(W,!1),N()&&N()()}function Qn(Se){return Kn.apply(this,arguments)}function Kn(){return(Kn=Pt(function*(Se){we()!==Se&&(we(Se),Xn(),Ve(),qt()(Se))})).apply(this,arguments)}function Bn(Se){o("handleChangeQueryLanguage",Se),pt(Se),ht()(Se)}function Zn(Se){var{id:Ee,json:tn,rootPath:Ar,onTransform:jr,onClose:on}=Se;ve()||g(le,{id:Ee,json:tn,rootPath:Ar,indentation:he(),truncateTextSize:Re(),escapeControlCharacters:kt(),escapeUnicodeCharacters:oe(),parser:X(),parseMemoizeOne:r(n),validationParser:Ne(),pathParser:ee(),queryLanguages:L(),queryLanguageId:pt(),onChangeQueryLanguage:Bn,onRenderValue:We(),onRenderMenu:dr=>Tt()(dr,{mode:we(),modal:!0,readOnly:ve()}),onRenderContextMenu:dr=>He()(dr,{mode:we(),modal:!0,readOnly:ve(),selection:ce()}),onClassName:Ye(),onTransform:jr,onClose:on})}function yr(Se){ve()||g(pe,Se)}function Fn(Se){var{content:Ee,path:tn,onPatch:Ar,onClose:jr}=Se;o("onJSONEditorModal",{content:Ee,path:tn}),g(Me,{content:Ee,path:tn,onPatch:Ar,readOnly:ve(),indentation:he(),tabSize:Ue(),truncateTextSize:Re(),mainMenuBar:ue(),navigationBar:ie(),statusBar:vt(),askToFormat:ft(),escapeControlCharacters:kt(),escapeUnicodeCharacters:oe(),maxDocumentSizeTextMode:Ze(),flattenColumns:te(),parser:X(),validator:void 0,validationParser:Ne(),pathParser:ee(),onRenderValue:We(),onClassName:Ye(),onRenderMenu:Tt(),onRenderContextMenu:He(),onSortModal:yr,onTransformModal:Zn,onClose:jr})}function $n(Se){Se.stopPropagation()}ne(()=>(x(X()),r(St),x(qe()),ul),()=>{if(!xy(X(),r(St))){if(o("parser changed, recreate editor"),$c(qe())){var Se=r(St).stringify(qe().json);qe({json:Se!==void 0?X().parse(Se):void 0})}g(St,X()),g(G,ul())}}),ne(()=>x(qe()),()=>{var Se=Lv(qe());Se&&console.error("Error: "+Se)}),ne(()=>x(ce()),()=>{ce()===null&&console.warn("selection is invalid: it is null but should be undefined")}),ne(()=>x(X()),()=>{g(n,Ec(X().parse))}),ne(()=>x(we()),()=>{o("mode changed to",we())}),Mn();var ar={get:lt,set:Xe,update:Ae,patch:$t,select:sn,expand:Un,collapse:Yt,transform:Zt,validate:Dt,acceptAutoRepair:hn,scrollTo:Hn,findElement:V,focus:Ve,refresh:ye,updateProps:dt,destroy:At};return Ft(!0),Bf(e,{children:(Se,Ee)=>{var tn,Ar=h7(),jr=Mt(Ar);cy(I(jr),()=>r(G),Pn=>{or(o0(Pn,{get externalMode(){return we()},get content(){return qe()},get selection(){return ce()},get readOnly(){return ve()},get indentation(){return he()},get tabSize(){return Ue()},get truncateTextSize(){return Re()},get statusBar(){return vt()},get askToFormat(){return ft()},get mainMenuBar(){return ue()},get navigationBar(){return ie()},get maxDocumentSizeTextMode(){return Ze()},get escapeControlCharacters(){return kt()},get escapeUnicodeCharacters(){return oe()},get flattenColumns(){return te()},get parser(){return X()},get parseMemoizeOne(){return r(n)},get validator(){return B()},get validationParser(){return Ne()},get pathParser(){return ee()},insideModal:!1,get onError(){return S()},onChange:Vt,onChangeMode:Qn,onSelect:Ht,get onRenderValue(){return We()},get onClassName(){return Ye()},onFocus:On,onBlur:dn,get onRenderMenu(){return Tt()},get onRenderContextMenu(){return He()},onSortModal:yr,onTransformModal:Zn,onJSONEditorModal:Fn,$$legacy:!0}),yn=>g(de,yn),()=>r(de))});var on=Y(jr,2),dr=Pn=>{(function(yn,Wt){var Wn,ir;yt(Wt,!1);var K=R(void 0,!0),Ce=R(void 0,!0),P=R(void 0,!0),Z=R(void 0,!0),xe=Zr("jsoneditor:SortModal"),ot=m(Wt,"id",9),Qe=m(Wt,"json",9),Je=m(Wt,"rootPath",9),Lt=m(Wt,"onSort",9),Ct=m(Wt,"onClose",9),jn={value:1,label:"ascending"},vn=[jn,{value:-1,label:"descending"}],er="".concat(ot(),":").concat(wt(Je())),Ot=R((Wn=el()[er])===null||Wn===void 0?void 0:Wn.selectedProperty,!0),an=R(((ir=el()[er])===null||ir===void 0?void 0:ir.selectedDirection)||jn,!0),fr=R(void 0,!0);function Gn(){try{var Ke,zn,sr;g(fr,void 0);var _t=((Ke=r(Ot))===null||Ke===void 0?void 0:Ke.value)||((zn=r(Z))===null||zn===void 0||(zn=zn[0])===null||zn===void 0?void 0:zn.value)||[],_n=(sr=r(an))===null||sr===void 0?void 0:sr.value,lr=dj(Qe(),Je(),_t,_n);Lt()!==void 0&&Je()!==void 0&&Lt()({operations:lr,rootPath:Je(),itemPath:_t,direction:_n}),Ct()()}catch(Nr){g(fr,String(Nr))}}function Nn(Ke){Ke.focus()}ne(()=>(x(Qe()),x(Je())),()=>{g(K,tt(Qe(),Je()))}),ne(()=>r(K),()=>{g(Ce,Array.isArray(r(K)))}),ne(()=>(r(Ce),r(K)),()=>{g(P,r(Ce)?Lf(r(K)):void 0)}),ne(()=>(r(P),Pi),()=>{g(Z,r(P)?r(P).map(Pi):void 0)}),ne(()=>(el(),r(Ot),r(an)),()=>{el(el()[er]={selectedProperty:r(Ot),selectedDirection:r(an)}),xe("store state in memory",er,el()[er])}),Mn(),Ft(!0),Dc(yn,{get onClose(){return Ct()},className:"jse-sort-modal",children:(Ke,zn)=>{var sr=p7(),_t=Mt(sr),_n=nt(()=>r(Ce)?"Sort array items":"Sort object keys");Od(_t,{get title(){return r(_n)},get onClose(){return Ct()}});var lr=I(Y(_t,2)),Nr=Y(I(lr)),to=I(Nr),bo=Y(I(to)),jo=I(bo),M=Y(to),se=it=>{var ut=v7(),ln=Y(I(ut));ys(I(ln),{showChevron:!0,get items(){return r(Z)},get value(){return r(Ot)},set value(An){g(Ot,An)},$$legacy:!0}),U(it,ut)};be(M,it=>{r(Ce),r(Z),F(()=>{var ut;return r(Ce)&&r(Z)&&((ut=r(Z))===null||ut===void 0?void 0:ut.length)>1})&&it(se)});var Te=Y(M),Be=Y(I(Te));ys(I(Be),{showChevron:!0,clearable:!1,get items(){return vn},get value(){return r(an)},set value(it){g(an,it)},$$legacy:!0});var Oe=Y(lr,2),Ge=I(Oe),Fe=it=>{var ut=f7(),ln=I(ut);Le(()=>xt(ln,r(fr))),U(it,ut)};be(Ge,it=>{r(fr)&&it(Fe)});var mt=I(Y(Oe,2));so(()=>ze("click",mt,Gn)),go(mt,it=>Nn==null?void 0:Nn(it)),Le(it=>{Ps(jo,it),mt.disabled=(r(Ce),r(Z),r(Ot),F(()=>{var ut;return!!(r(Ce)&&r(Z)&&((ut=r(Z))===null||ut===void 0?void 0:ut.length)>1)&&!r(Ot)}))},[()=>(x(Je()),x(gn),x(Eo),F(()=>Je()&&!gn(Je())?Eo(Je()):"(document root)"))]),U(Ke,sr)},$$slots:{default:!0}}),jt()})(Pn,Hi(()=>r(pe),{onClose:()=>{var yn;(yn=r(pe))===null||yn===void 0||yn.onClose(),g(pe,void 0)}}))};be(on,Pn=>{r(pe)&&Pn(dr)});var vr=Y(on,2),Br=Pn=>{yE(Pn,Hi(()=>r(le),{onClose:()=>{var yn;(yn=r(le))===null||yn===void 0||yn.onClose(),g(le,void 0)}}))};be(vr,Pn=>{r(le)&&Pn(Br)});var eo=Y(vr,2),zr=Pn=>{(function(yn,Wt){yt(Wt,!1);var Wn=R(void 0,!0),ir=R(void 0,!0),K=R(void 0,!0),Ce=R(void 0,!0),P=Zr("jsoneditor:JSONEditorModal"),Z=m(Wt,"content",9),xe=m(Wt,"path",9),ot=m(Wt,"onPatch",9),Qe=m(Wt,"readOnly",9),Je=m(Wt,"indentation",9),Lt=m(Wt,"tabSize",9),Ct=m(Wt,"truncateTextSize",9),jn=m(Wt,"mainMenuBar",9),vn=m(Wt,"navigationBar",9),er=m(Wt,"statusBar",9),Ot=m(Wt,"askToFormat",9),an=m(Wt,"escapeControlCharacters",9),fr=m(Wt,"escapeUnicodeCharacters",9),Gn=m(Wt,"maxDocumentSizeTextMode",9),Nn=m(Wt,"flattenColumns",9),Ke=m(Wt,"parser",9),zn=m(Wt,"validator",9),sr=m(Wt,"validationParser",9),_t=m(Wt,"pathParser",9),_n=m(Wt,"onRenderValue",9),lr=m(Wt,"onClassName",9),Nr=m(Wt,"onRenderMenu",9),to=m(Wt,"onRenderContextMenu",9),bo=m(Wt,"onSortModal",9),jo=m(Wt,"onTransformModal",9),M=m(Wt,"onClose",9),se=R(void 0,!0),Te=R(void 0,!0),Be={mode:Fe(Z()),content:Z(),selection:void 0,relativePath:xe()},Oe=R([Be],!0),Ge=R(void 0,!0);function Fe(ke){return $c(ke)&&Cr(ke.json)?Mr.table:Mr.tree}function mt(){var ke,Pe=(ke=Xt(r(Oe)))===null||ke===void 0?void 0:ke.selection;Nc(Pe)&&r(se).scrollTo(st(Pe))}function it(){if(P("handleApply"),!Qe())try{g(Ge,void 0);var ke=r(Wn).relativePath,Pe=r(Wn).content,bt=[{op:"replace",path:wt(ke),value:hm(Pe,Ke()).json}];if(r(Oe).length>1){var Nt=hm(r(Oe)[r(Oe).length-2].content,Ke()).json,Qt={json:ga(Nt,bt)},xn=De(De({},r(Oe)[r(Oe).length-2]||Be),{},{content:Qt});g(Oe,[...r(Oe).slice(0,r(Oe).length-2),xn]),Xn(),mt()}else ot()(bt),M()()}catch(nn){g(Ge,String(nn))}}function ut(){var ke;P("handleClose"),r(Oe).length>1?(g(Oe,cn(r(Oe))),Xn(),(ke=r(se))===null||ke===void 0||ke.focus(),mt(),g(Ge,void 0)):M()()}function ln(ke){P("handleChange",ke),T(Pe=>De(De({},Pe),{},{content:ke}))}function An(ke){P("handleChangeSelection",ke),T(Pe=>De(De({},Pe),{},{selection:ke}))}function xo(ke){P("handleChangeMode",ke),T(Pe=>De(De({},Pe),{},{mode:ke}))}function T(ke){var Pe=ke(Xt(r(Oe)));g(Oe,[...cn(r(Oe)),Pe])}function ae(ke){g(Ge,ke.toString()),console.error(ke)}function $e(ke){var Pe,{content:bt,path:Nt}=ke;P("handleJSONEditorModal",{content:bt,path:Nt});var Qt={mode:Fe(bt),content:bt,selection:void 0,relativePath:Nt};g(Oe,[...r(Oe),Qt]),Xn(),(Pe=r(se))===null||Pe===void 0||Pe.focus()}function et(ke){ke.focus()}vo(()=>{var ke;(ke=r(se))===null||ke===void 0||ke.focus()}),ne(()=>r(Oe),()=>{g(Wn,Xt(r(Oe))||Be)}),ne(()=>r(Oe),()=>{g(ir,r(Oe).flatMap(ke=>ke.relativePath))}),ne(()=>(r(ir),Eo),()=>{g(K,gn(r(ir))?"(document root)":Eo(r(ir)))}),ne(()=>x(Ke()),()=>{g(Ce,Ec(Ke().parse))}),Mn(),Ft(!0),Dc(yn,{onClose:ut,className:"jse-jsoneditor-modal",get fullscreen(){return r(Te)},children:(ke,Pe)=>{var bt=u7();Bf(I(bt),{children:(Nt,Qt)=>{var xn=c7(),nn=Mt(xn),Yn=nt(()=>(r(Oe),F(()=>r(Oe).length>1?" (".concat(r(Oe).length,")"):"")));Od(nn,{get title(){var ct;return"Edit nested content ".concat((ct=r(Yn))!==null&&ct!==void 0?ct:"")},fullScreenButton:!0,onClose:ut,get fullscreen(){return r(Te)},set fullscreen(ct){g(Te,ct)},$$legacy:!0});var Ut=Y(nn,2),cr=Y(I(Ut),2),Rn=Y(cr,4);or(o0(I(Rn),{get externalMode(){return r(Wn),F(()=>r(Wn).mode)},get content(){return r(Wn),F(()=>r(Wn).content)},get selection(){return r(Wn),F(()=>r(Wn).selection)},get readOnly(){return Qe()},get indentation(){return Je()},get tabSize(){return Lt()},get truncateTextSize(){return Ct()},get statusBar(){return er()},get askToFormat(){return Ot()},get mainMenuBar(){return jn()},get navigationBar(){return vn()},get escapeControlCharacters(){return an()},get escapeUnicodeCharacters(){return fr()},get maxDocumentSizeTextMode(){return Gn()},get flattenColumns(){return Nn()},get parser(){return Ke()},get parseMemoizeOne(){return r(Ce)},get validator(){return zn()},get validationParser(){return sr()},get pathParser(){return _t()},insideModal:!0,onError:ae,onChange:ln,onChangeMode:xo,onSelect:An,get onRenderValue(){return _n()},get onClassName(){return lr()},get onFocus(){return Ko},get onBlur(){return Ko},get onRenderMenu(){return Nr()},get onRenderContextMenu(){return to()},get onSortModal(){return bo()},get onTransformModal(){return jo()},onJSONEditorModal:$e,$$legacy:!0}),ct=>g(se,ct),()=>r(se));var tr=I(Y(Rn,2)),wn=ct=>{var Jt=a7(),ur=I(Jt);Le(()=>xt(ur,r(Ge))),U(ct,Jt)};be(tr,ct=>{r(Ge)&&ct(wn)});var Et=Y(tr,2),fn=ct=>{var Jt=i7();un(I(Jt),{get data(){return JS}}),ze("click",Jt,ut),U(ct,Jt)};be(Et,ct=>{r(Oe),F(()=>r(Oe).length>1)&&ct(fn)});var In=Y(Et,2),xr=ct=>{var Jt=s7();so(()=>ze("click",Jt,it)),go(Jt,ur=>et==null?void 0:et(ur)),U(ct,Jt)},_r=ct=>{var Jt=l7();ze("click",Jt,ut),U(ct,Jt)};be(In,ct=>{Qe()?ct(_r,-1):ct(xr)}),Le(()=>Ps(cr,r(K))),U(Nt,xn)},$$slots:{default:!0}}),U(ke,bt)},$$slots:{default:!0}}),jt()})(Pn,Hi(()=>r(Me),{onClose:()=>{var yn;(yn=r(Me))===null||yn===void 0||yn.onClose(),g(Me,void 0)}}))};be(eo,Pn=>{r(Me)&&Pn(zr)}),Le(()=>tn=Bt(jr,1,"jse-main svelte-1l55585",null,tn,{"jse-focus":r(W)})),ze("keydown",jr,$n),U(Se,Ar)},$$slots:{default:!0}}),Rt(t,"get",lt),Rt(t,"set",Xe),Rt(t,"update",Ae),Rt(t,"patch",$t),Rt(t,"select",sn),Rt(t,"expand",Un),Rt(t,"collapse",Yt),Rt(t,"transform",Zt),Rt(t,"validate",Dt),Rt(t,"acceptAutoRepair",hn),Rt(t,"scrollTo",Hn),Rt(t,"findElement",V),Rt(t,"focus",Ve),Rt(t,"refresh",ye),Rt(t,"updateProps",dt),Rt(t,"destroy",At),jt(ar)}function m7(e){var{target:t,props:n}=e,o=s9(g7,{target:t,props:n});return o.destroy=Pt(function*(){return function(i,a){var s=If.get(i);return s?(If.delete(i),s(a)):Promise.resolve()}(o)}),Xn(),o}const b7=/"(?:_|\\u0{2}5[Ff]){2}(?:p|\\u0{2}70)(?:r|\\u0{2}72)(?:o|\\u0{2}6[Ff])(?:t|\\u0{2}74)(?:o|\\u0{2}6[Ff])(?:_|\\u0{2}5[Ff]){2}"\s*:/,y7=/"(?:c|\\u0063)(?:o|\\u006[Ff])(?:n|\\u006[Ee])(?:s|\\u0073)(?:t|\\u0074)(?:r|\\u0072)(?:u|\\u0075)(?:c|\\u0063)(?:t|\\u0074)(?:o|\\u006[Ff])(?:r|\\u0072)"\s*:/,j7=/^\s*["[{]|^\s*-?\d{1,16}(\.\d{1,17})?([Ee][+-]?\d+)?\s*$/;function x7(e,t){if(e==="__proto__"||e==="constructor"&&t&&typeof t=="object"&&"prototype"in t){w7(e);return}return t}function w7(e){console.warn(`[destr] Dropping "${e}" key to prevent prototype pollution.`)}function Gu(e,t={}){if(typeof e!="string")return e;const n=e.trim();if(e[0]==='"'&&e.endsWith('"')&&!e.includes("\\"))return n.slice(1,-1);if(n.length<=9){const o=n.toLowerCase();if(o==="true")return!0;if(o==="false")return!1;if(o==="undefined")return;if(o==="null")return null;if(o==="nan")return Number.NaN;if(o==="infinity")return Number.POSITIVE_INFINITY;if(o==="-infinity")return Number.NEGATIVE_INFINITY}if(!j7.test(e)){if(t.strict)throw new SyntaxError("[destr] Invalid JSON");return e}try{if(b7.test(e)||y7.test(e)){if(t.strict)throw new Error("[destr] Possible prototype pollution");return JSON.parse(e,x7)}return JSON.parse(e)}catch(o){if(t.strict)throw o;return e}}function k7(e,t={}){return Gu(e,{...t,strict:!0})}var S7=typeof global=="object"&&global&&global.Object===Object&&global,C7=typeof self=="object"&&self&&self.Object===Object&&self,Sj=S7||C7||Function("return this")(),Td=Sj.Symbol,Cj=Object.prototype,O7=Cj.hasOwnProperty,_7=Cj.toString,lc=Td?Td.toStringTag:void 0;function E7(e){var t=O7.call(e,lc),n=e[lc];try{e[lc]=void 0;var o=!0}catch{}var i=_7.call(e);return o&&(t?e[lc]=n:delete e[lc]),i}var T7=Object.prototype,M7=T7.toString;function $7(e){return M7.call(e)}var A7="[object Null]",z7="[object Undefined]",a0=Td?Td.toStringTag:void 0;function P7(e){return e==null?e===void 0?z7:A7:a0&&a0 in Object(e)?E7(e):$7(e)}function N7(e){return e!=null&&typeof e=="object"}var R7="[object Symbol]";function I7(e){return typeof e=="symbol"||N7(e)&&P7(e)==R7}var q7=/\s/;function D7(e){for(var t=e.length;t--&&q7.test(e.charAt(t)););return t}var L7=/^\s+/;function U7(e){return e&&e.slice(0,D7(e)+1).replace(L7,"")}function lp(e){var t=typeof e;return e!=null&&(t=="object"||t=="function")}var i0=NaN,B7=/^[-+]0x[0-9a-f]+$/i,F7=/^0b[01]+$/i,W7=/^0o[0-7]+$/i,V7=parseInt;function s0(e){if(typeof e=="number")return e;if(I7(e))return i0;if(lp(e)){var t=typeof e.valueOf=="function"?e.valueOf():e;e=lp(t)?t+"":t}if(typeof e!="string")return e===0?e:+e;e=U7(e);var n=F7.test(e);return n||W7.test(e)?V7(e.slice(2),n?2:8):B7.test(e)?i0:+e}var rf=function(){return Sj.Date.now()},J7="Expected a function",H7=Math.max,Q7=Math.min;function K7(e,t,n){var o,i,a,s,l,c,u=0,d=!1,v=!1,f=!0;if(typeof e!="function")throw new TypeError(J7);t=s0(t)||0,lp(n)&&(d=!!n.leading,v="maxWait"in n,a=v?H7(s0(n.maxWait)||0,t):a,f="trailing"in n?!!n.trailing:f);function h(_){var A=o,q=i;return o=i=void 0,u=_,s=e.apply(q,A),s}function p(_){return u=_,l=setTimeout(b,t),d?h(_):s}function y(_){var A=_-c,q=_-u,C=t-A;return v?Q7(C,a-q):C}function j(_){var A=_-c,q=_-u;return c===void 0||A>=t||A<0||v&&q>=a}function b(){var _=rf();if(j(_))return k(_);l=setTimeout(b,y(_))}function k(_){return l=void 0,f&&o?h(_):(o=i=void 0,s)}function E(){l!==void 0&&clearTimeout(l),u=0,o=c=i=l=void 0}function O(){return l===void 0?s:k(rf())}function w(){var _=rf(),A=j(_);if(o=arguments,i=this,c=_,A){if(l===void 0)return p(c);if(v)return clearTimeout(l),l=setTimeout(b,t),h(c)}return l===void 0&&(l=setTimeout(b,t)),s}return w.cancel=E,w.flush=O,w}var Oj=typeof global=="object"&&global&&global.Object===Object&&global,G7=typeof self=="object"&&self&&self.Object===Object&&self,Fa=Oj||G7||Function("return this")(),La=Fa.Symbol,_j=Object.prototype,Y7=_j.hasOwnProperty,X7=_j.toString,cc=La?La.toStringTag:void 0;function Z7(e){var t=Y7.call(e,cc),n=e[cc];try{e[cc]=void 0;var o=!0}catch{}var i=X7.call(e);return o&&(t?e[cc]=n:delete e[cc]),i}var eT=Object.prototype,tT=eT.toString;function nT(e){return tT.call(e)}var rT="[object Null]",oT="[object Undefined]",l0=La?La.toStringTag:void 0;function Fs(e){return e==null?e===void 0?oT:rT:l0&&l0 in Object(e)?Z7(e):nT(e)}function Ua(e){return e!=null&&typeof e=="object"}var aT="[object Symbol]";function hh(e){return typeof e=="symbol"||Ua(e)&&Fs(e)==aT}function iT(e,t){for(var n=-1,o=e==null?0:e.length,i=Array(o);++n<o;)i[n]=t(e[n],n,e);return i}var oa=Array.isArray,c0=La?La.prototype:void 0,u0=c0?c0.toString:void 0;function Ej(e){if(typeof e=="string")return e;if(oa(e))return iT(e,Ej)+"";if(hh(e))return u0?u0.call(e):"";var t=e+"";return t=="0"&&1/e==-1/0?"-0":t}function Wa(e){var t=typeof e;return e!=null&&(t=="object"||t=="function")}function gh(e){return e}var sT="[object AsyncFunction]",lT="[object Function]",cT="[object GeneratorFunction]",uT="[object Proxy]";function mh(e){if(!Wa(e))return!1;var t=Fs(e);return t==lT||t==cT||t==sT||t==uT}var of=Fa["__core-js_shared__"],d0=function(){var e=/[^.]+$/.exec(of&&of.keys&&of.keys.IE_PROTO||"");return e?"Symbol(src)_1."+e:""}();function dT(e){return!!d0&&d0 in e}var vT=Function.prototype,fT=vT.toString;function Ws(e){if(e!=null){try{return fT.call(e)}catch{}try{return e+""}catch{}}return""}var pT=/[\\^$.*+?()[\]{}|]/g,hT=/^\[object .+?Constructor\]$/,gT=Function.prototype,mT=Object.prototype,bT=gT.toString,yT=mT.hasOwnProperty,jT=RegExp("^"+bT.call(yT).replace(pT,"\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g,"$1.*?")+"$");function xT(e){if(!Wa(e)||dT(e))return!1;var t=mh(e)?jT:hT;return t.test(Ws(e))}function wT(e,t){return e==null?void 0:e[t]}function Vs(e,t){var n=wT(e,t);return xT(n)?n:void 0}var cp=Vs(Fa,"WeakMap"),v0=Object.create,kT=function(){function e(){}return function(t){if(!Wa(t))return{};if(v0)return v0(t);e.prototype=t;var n=new e;return e.prototype=void 0,n}}();function ST(e,t,n){switch(n.length){case 0:return e.call(t);case 1:return e.call(t,n[0]);case 2:return e.call(t,n[0],n[1]);case 3:return e.call(t,n[0],n[1],n[2])}return e.apply(t,n)}function CT(e,t){var n=-1,o=e.length;for(t||(t=Array(o));++n<o;)t[n]=e[n];return t}var OT=800,_T=16,ET=Date.now;function TT(e){var t=0,n=0;return function(){var o=ET(),i=_T-(o-n);if(n=o,i>0){if(++t>=OT)return arguments[0]}else t=0;return e.apply(void 0,arguments)}}function MT(e){return function(){return e}}var Md=function(){try{var e=Vs(Object,"defineProperty");return e({},"",{}),e}catch{}}(),$T=Md?function(e,t){return Md(e,"toString",{configurable:!0,enumerable:!1,value:MT(t),writable:!0})}:gh,AT=TT($T);function zT(e,t){for(var n=-1,o=e==null?0:e.length;++n<o&&t(e[n],n,e)!==!1;);return e}var PT=9007199254740991,NT=/^(?:0|[1-9]\d*)$/;function bh(e,t){var n=typeof e;return t=t??PT,!!t&&(n=="number"||n!="symbol"&&NT.test(e))&&e>-1&&e%1==0&&e<t}function iv(e,t,n){t=="__proto__"&&Md?Md(e,t,{configurable:!0,enumerable:!0,value:n,writable:!0}):e[t]=n}function iu(e,t){return e===t||e!==e&&t!==t}var RT=Object.prototype,IT=RT.hasOwnProperty;function Tj(e,t,n){var o=e[t];(!(IT.call(e,t)&&iu(o,n))||n===void 0&&!(t in e))&&iv(e,t,n)}function Mj(e,t,n,o){var i=!n;n||(n={});for(var a=-1,s=t.length;++a<s;){var l=t[a],c=o?o(n[l],e[l],l,n,e):void 0;c===void 0&&(c=e[l]),i?iv(n,l,c):Tj(n,l,c)}return n}var f0=Math.max;function qT(e,t,n){return t=f0(t===void 0?e.length-1:t,0),function(){for(var o=arguments,i=-1,a=f0(o.length-t,0),s=Array(a);++i<a;)s[i]=o[t+i];i=-1;for(var l=Array(t+1);++i<t;)l[i]=o[i];return l[t]=n(s),ST(e,this,l)}}function DT(e,t){return AT(qT(e,t,gh),e+"")}var LT=9007199254740991;function yh(e){return typeof e=="number"&&e>-1&&e%1==0&&e<=LT}function sv(e){return e!=null&&yh(e.length)&&!mh(e)}function UT(e,t,n){if(!Wa(n))return!1;var o=typeof t;return(o=="number"?sv(n)&&bh(t,n.length):o=="string"&&t in n)?iu(n[t],e):!1}function $j(e){return DT(function(t,n){var o=-1,i=n.length,a=i>1?n[i-1]:void 0,s=i>2?n[2]:void 0;for(a=e.length>3&&typeof a=="function"?(i--,a):void 0,s&&UT(n[0],n[1],s)&&(a=i<3?void 0:a,i=1),t=Object(t);++o<i;){var l=n[o];l&&e(t,l,o,a)}return t})}var BT=Object.prototype;function jh(e){var t=e&&e.constructor,n=typeof t=="function"&&t.prototype||BT;return e===n}function FT(e,t){for(var n=-1,o=Array(e);++n<e;)o[n]=t(n);return o}var WT="[object Arguments]";function p0(e){return Ua(e)&&Fs(e)==WT}var Aj=Object.prototype,VT=Aj.hasOwnProperty,JT=Aj.propertyIsEnumerable,$d=p0(function(){return arguments}())?p0:function(e){return Ua(e)&&VT.call(e,"callee")&&!JT.call(e,"callee")};function HT(){return!1}var zj=typeof exports=="object"&&exports&&!exports.nodeType&&exports,h0=zj&&typeof module=="object"&&module&&!module.nodeType&&module,QT=h0&&h0.exports===zj,g0=QT?Fa.Buffer:void 0,KT=g0?g0.isBuffer:void 0,Bc=KT||HT,GT="[object Arguments]",YT="[object Array]",XT="[object Boolean]",ZT="[object Date]",eM="[object Error]",tM="[object Function]",nM="[object Map]",rM="[object Number]",oM="[object Object]",aM="[object RegExp]",iM="[object Set]",sM="[object String]",lM="[object WeakMap]",cM="[object ArrayBuffer]",uM="[object DataView]",dM="[object Float32Array]",vM="[object Float64Array]",fM="[object Int8Array]",pM="[object Int16Array]",hM="[object Int32Array]",gM="[object Uint8Array]",mM="[object Uint8ClampedArray]",bM="[object Uint16Array]",yM="[object Uint32Array]",kr={};kr[dM]=kr[vM]=kr[fM]=kr[pM]=kr[hM]=kr[gM]=kr[mM]=kr[bM]=kr[yM]=!0;kr[GT]=kr[YT]=kr[cM]=kr[XT]=kr[uM]=kr[ZT]=kr[eM]=kr[tM]=kr[nM]=kr[rM]=kr[oM]=kr[aM]=kr[iM]=kr[sM]=kr[lM]=!1;function jM(e){return Ua(e)&&yh(e.length)&&!!kr[Fs(e)]}function xh(e){return function(t){return e(t)}}var Pj=typeof exports=="object"&&exports&&!exports.nodeType&&exports,wc=Pj&&typeof module=="object"&&module&&!module.nodeType&&module,xM=wc&&wc.exports===Pj,af=xM&&Oj.process,Il=function(){try{var e=wc&&wc.require&&wc.require("util").types;return e||af&&af.binding&&af.binding("util")}catch{}}(),m0=Il&&Il.isTypedArray,wh=m0?xh(m0):jM,wM=Object.prototype,kM=wM.hasOwnProperty;function Nj(e,t){var n=oa(e),o=!n&&$d(e),i=!n&&!o&&Bc(e),a=!n&&!o&&!i&&wh(e),s=n||o||i||a,l=s?FT(e.length,String):[],c=l.length;for(var u in e)(t||kM.call(e,u))&&!(s&&(u=="length"||i&&(u=="offset"||u=="parent")||a&&(u=="buffer"||u=="byteLength"||u=="byteOffset")||bh(u,c)))&&l.push(u);return l}function Rj(e,t){return function(n){return e(t(n))}}var SM=Rj(Object.keys,Object),CM=Object.prototype,OM=CM.hasOwnProperty;function _M(e){if(!jh(e))return SM(e);var t=[];for(var n in Object(e))OM.call(e,n)&&n!="constructor"&&t.push(n);return t}function kh(e){return sv(e)?Nj(e):_M(e)}function EM(e){var t=[];if(e!=null)for(var n in Object(e))t.push(n);return t}var TM=Object.prototype,MM=TM.hasOwnProperty;function $M(e){if(!Wa(e))return EM(e);var t=jh(e),n=[];for(var o in e)o=="constructor"&&(t||!MM.call(e,o))||n.push(o);return n}function Sh(e){return sv(e)?Nj(e,!0):$M(e)}var AM=$j(function(e,t,n,o){Mj(t,Sh(t),e,o)}),zM=/\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/,PM=/^\w*$/;function Ch(e,t){if(oa(e))return!1;var n=typeof e;return n=="number"||n=="symbol"||n=="boolean"||e==null||hh(e)?!0:PM.test(e)||!zM.test(e)||t!=null&&e in Object(t)}var Fc=Vs(Object,"create");function NM(){this.__data__=Fc?Fc(null):{},this.size=0}function RM(e){var t=this.has(e)&&delete this.__data__[e];return this.size-=t?1:0,t}var IM="__lodash_hash_undefined__",qM=Object.prototype,DM=qM.hasOwnProperty;function LM(e){var t=this.__data__;if(Fc){var n=t[e];return n===IM?void 0:n}return DM.call(t,e)?t[e]:void 0}var UM=Object.prototype,BM=UM.hasOwnProperty;function FM(e){var t=this.__data__;return Fc?t[e]!==void 0:BM.call(t,e)}var WM="__lodash_hash_undefined__";function VM(e,t){var n=this.__data__;return this.size+=this.has(e)?0:1,n[e]=Fc&&t===void 0?WM:t,this}function Ds(e){var t=-1,n=e==null?0:e.length;for(this.clear();++t<n;){var o=e[t];this.set(o[0],o[1])}}Ds.prototype.clear=NM;Ds.prototype.delete=RM;Ds.prototype.get=LM;Ds.prototype.has=FM;Ds.prototype.set=VM;function JM(){this.__data__=[],this.size=0}function lv(e,t){for(var n=e.length;n--;)if(iu(e[n][0],t))return n;return-1}var HM=Array.prototype,QM=HM.splice;function KM(e){var t=this.__data__,n=lv(t,e);if(n<0)return!1;var o=t.length-1;return n==o?t.pop():QM.call(t,n,1),--this.size,!0}function GM(e){var t=this.__data__,n=lv(t,e);return n<0?void 0:t[n][1]}function YM(e){return lv(this.__data__,e)>-1}function XM(e,t){var n=this.__data__,o=lv(n,e);return o<0?(++this.size,n.push([e,t])):n[o][1]=t,this}function xi(e){var t=-1,n=e==null?0:e.length;for(this.clear();++t<n;){var o=e[t];this.set(o[0],o[1])}}xi.prototype.clear=JM;xi.prototype.delete=KM;xi.prototype.get=GM;xi.prototype.has=YM;xi.prototype.set=XM;var Wc=Vs(Fa,"Map");function ZM(){this.size=0,this.__data__={hash:new Ds,map:new(Wc||xi),string:new Ds}}function e$(e){var t=typeof e;return t=="string"||t=="number"||t=="symbol"||t=="boolean"?e!=="__proto__":e===null}function cv(e,t){var n=e.__data__;return e$(t)?n[typeof t=="string"?"string":"hash"]:n.map}function t$(e){var t=cv(this,e).delete(e);return this.size-=t?1:0,t}function n$(e){return cv(this,e).get(e)}function r$(e){return cv(this,e).has(e)}function o$(e,t){var n=cv(this,e),o=n.size;return n.set(e,t),this.size+=n.size==o?0:1,this}function wi(e){var t=-1,n=e==null?0:e.length;for(this.clear();++t<n;){var o=e[t];this.set(o[0],o[1])}}wi.prototype.clear=ZM;wi.prototype.delete=t$;wi.prototype.get=n$;wi.prototype.has=r$;wi.prototype.set=o$;var a$="Expected a function";function Oh(e,t){if(typeof e!="function"||t!=null&&typeof t!="function")throw new TypeError(a$);var n=function(){var o=arguments,i=t?t.apply(this,o):o[0],a=n.cache;if(a.has(i))return a.get(i);var s=e.apply(this,o);return n.cache=a.set(i,s)||a,s};return n.cache=new(Oh.Cache||wi),n}Oh.Cache=wi;var i$=500;function s$(e){var t=Oh(e,function(o){return n.size===i$&&n.clear(),o}),n=t.cache;return t}var l$=/[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|$))/g,c$=/\\(\\)?/g,u$=s$(function(e){var t=[];return e.charCodeAt(0)===46&&t.push(""),e.replace(l$,function(n,o,i,a){t.push(i?a.replace(c$,"$1"):o||n)}),t});function d$(e){return e==null?"":Ej(e)}function Ij(e,t){return oa(e)?e:Ch(e,t)?[e]:u$(d$(e))}function uv(e){if(typeof e=="string"||hh(e))return e;var t=e+"";return t=="0"&&1/e==-1/0?"-0":t}function qj(e,t){t=Ij(t,e);for(var n=0,o=t.length;e!=null&&n<o;)e=e[uv(t[n++])];return n&&n==o?e:void 0}function v$(e,t,n){var o=e==null?void 0:qj(e,t);return o===void 0?n:o}function f$(e,t){for(var n=-1,o=t.length,i=e.length;++n<o;)e[i+n]=t[n];return e}var Dj=Rj(Object.getPrototypeOf,Object),p$="[object Object]",h$=Function.prototype,g$=Object.prototype,Lj=h$.toString,m$=g$.hasOwnProperty,b$=Lj.call(Object);function y$(e){if(!Ua(e)||Fs(e)!=p$)return!1;var t=Dj(e);if(t===null)return!0;var n=m$.call(t,"constructor")&&t.constructor;return typeof n=="function"&&n instanceof n&&Lj.call(n)==b$}function j$(){this.__data__=new xi,this.size=0}function x$(e){var t=this.__data__,n=t.delete(e);return this.size=t.size,n}function w$(e){return this.__data__.get(e)}function k$(e){return this.__data__.has(e)}var S$=200;function C$(e,t){var n=this.__data__;if(n instanceof xi){var o=n.__data__;if(!Wc||o.length<S$-1)return o.push([e,t]),this.size=++n.size,this;n=this.__data__=new wi(o)}return n.set(e,t),this.size=n.size,this}function wa(e){var t=this.__data__=new xi(e);this.size=t.size}wa.prototype.clear=j$;wa.prototype.delete=x$;wa.prototype.get=w$;wa.prototype.has=k$;wa.prototype.set=C$;var Uj=typeof exports=="object"&&exports&&!exports.nodeType&&exports,b0=Uj&&typeof module=="object"&&module&&!module.nodeType&&module,O$=b0&&b0.exports===Uj,y0=O$?Fa.Buffer:void 0,j0=y0?y0.allocUnsafe:void 0;function Bj(e,t){if(t)return e.slice();var n=e.length,o=j0?j0(n):new e.constructor(n);return e.copy(o),o}function _$(e,t){for(var n=-1,o=e==null?0:e.length,i=0,a=[];++n<o;){var s=e[n];t(s,n,e)&&(a[i++]=s)}return a}function E$(){return[]}var T$=Object.prototype,M$=T$.propertyIsEnumerable,x0=Object.getOwnPropertySymbols,$$=x0?function(e){return e==null?[]:(e=Object(e),_$(x0(e),function(t){return M$.call(e,t)}))}:E$;function A$(e,t,n){var o=t(e);return oa(e)?o:f$(o,n(e))}function up(e){return A$(e,kh,$$)}var dp=Vs(Fa,"DataView"),vp=Vs(Fa,"Promise"),fp=Vs(Fa,"Set"),w0="[object Map]",z$="[object Object]",k0="[object Promise]",S0="[object Set]",C0="[object WeakMap]",O0="[object DataView]",P$=Ws(dp),N$=Ws(Wc),R$=Ws(vp),I$=Ws(fp),q$=Ws(cp),ua=Fs;(dp&&ua(new dp(new ArrayBuffer(1)))!=O0||Wc&&ua(new Wc)!=w0||vp&&ua(vp.resolve())!=k0||fp&&ua(new fp)!=S0||cp&&ua(new cp)!=C0)&&(ua=function(e){var t=Fs(e),n=t==z$?e.constructor:void 0,o=n?Ws(n):"";if(o)switch(o){case P$:return O0;case N$:return w0;case R$:return k0;case I$:return S0;case q$:return C0}return t});var D$=Object.prototype,L$=D$.hasOwnProperty;function U$(e){var t=e.length,n=new e.constructor(t);return t&&typeof e[0]=="string"&&L$.call(e,"index")&&(n.index=e.index,n.input=e.input),n}var Ad=Fa.Uint8Array;function _h(e){var t=new e.constructor(e.byteLength);return new Ad(t).set(new Ad(e)),t}function B$(e,t){var n=_h(e.buffer);return new e.constructor(n,e.byteOffset,e.byteLength)}var F$=/\w*$/;function W$(e){var t=new e.constructor(e.source,F$.exec(e));return t.lastIndex=e.lastIndex,t}var _0=La?La.prototype:void 0,E0=_0?_0.valueOf:void 0;function V$(e){return E0?Object(E0.call(e)):{}}function Fj(e,t){var n=t?_h(e.buffer):e.buffer;return new e.constructor(n,e.byteOffset,e.length)}var J$="[object Boolean]",H$="[object Date]",Q$="[object Map]",K$="[object Number]",G$="[object RegExp]",Y$="[object Set]",X$="[object String]",Z$="[object Symbol]",eA="[object ArrayBuffer]",tA="[object DataView]",nA="[object Float32Array]",rA="[object Float64Array]",oA="[object Int8Array]",aA="[object Int16Array]",iA="[object Int32Array]",sA="[object Uint8Array]",lA="[object Uint8ClampedArray]",cA="[object Uint16Array]",uA="[object Uint32Array]";function dA(e,t,n){var o=e.constructor;switch(t){case eA:return _h(e);case J$:case H$:return new o(+e);case tA:return B$(e);case nA:case rA:case oA:case aA:case iA:case sA:case lA:case cA:case uA:return Fj(e,n);case Q$:return new o;case K$:case X$:return new o(e);case G$:return W$(e);case Y$:return new o;case Z$:return V$(e)}}function Wj(e){return typeof e.constructor=="function"&&!jh(e)?kT(Dj(e)):{}}var vA="[object Map]";function fA(e){return Ua(e)&&ua(e)==vA}var T0=Il&&Il.isMap,pA=T0?xh(T0):fA,hA="[object Set]";function gA(e){return Ua(e)&&ua(e)==hA}var M0=Il&&Il.isSet,mA=M0?xh(M0):gA,bA=1,Vj="[object Arguments]",yA="[object Array]",jA="[object Boolean]",xA="[object Date]",wA="[object Error]",Jj="[object Function]",kA="[object GeneratorFunction]",SA="[object Map]",CA="[object Number]",Hj="[object Object]",OA="[object RegExp]",_A="[object Set]",EA="[object String]",TA="[object Symbol]",MA="[object WeakMap]",$A="[object ArrayBuffer]",AA="[object DataView]",zA="[object Float32Array]",PA="[object Float64Array]",NA="[object Int8Array]",RA="[object Int16Array]",IA="[object Int32Array]",qA="[object Uint8Array]",DA="[object Uint8ClampedArray]",LA="[object Uint16Array]",UA="[object Uint32Array]",gr={};gr[Vj]=gr[yA]=gr[$A]=gr[AA]=gr[jA]=gr[xA]=gr[zA]=gr[PA]=gr[NA]=gr[RA]=gr[IA]=gr[SA]=gr[CA]=gr[Hj]=gr[OA]=gr[_A]=gr[EA]=gr[TA]=gr[qA]=gr[DA]=gr[LA]=gr[UA]=!0;gr[wA]=gr[Jj]=gr[MA]=!1;function Yu(e,t,n,o,i,a){var s,l=t&bA;if(s!==void 0)return s;if(!Wa(e))return e;var c=oa(e);if(c)s=U$(e);else{var u=ua(e),d=u==Jj||u==kA;if(Bc(e))return Bj(e,l);if(u==Hj||u==Vj||d&&!i)s=d?{}:Wj(e);else{if(!gr[u])return i?e:{};s=dA(e,u,l)}}a||(a=new wa);var v=a.get(e);if(v)return v;a.set(e,s),mA(e)?e.forEach(function(p){s.add(Yu(p,t,n,p,e,a))}):pA(e)&&e.forEach(function(p,y){s.set(y,Yu(p,t,n,y,e,a))});var f=up,h=c?void 0:f(e);return zT(h||e,function(p,y){h&&(y=p,p=e[y]),Tj(s,y,Yu(p,t,n,y,e,a))}),s}var BA=1,FA=4;function WA(e){return Yu(e,BA|FA)}var VA="__lodash_hash_undefined__";function JA(e){return this.__data__.set(e,VA),this}function HA(e){return this.__data__.has(e)}function zd(e){var t=-1,n=e==null?0:e.length;for(this.__data__=new wi;++t<n;)this.add(e[t])}zd.prototype.add=zd.prototype.push=JA;zd.prototype.has=HA;function QA(e,t){for(var n=-1,o=e==null?0:e.length;++n<o;)if(t(e[n],n,e))return!0;return!1}function KA(e,t){return e.has(t)}var GA=1,YA=2;function Qj(e,t,n,o,i,a){var s=n&GA,l=e.length,c=t.length;if(l!=c&&!(s&&c>l))return!1;var u=a.get(e),d=a.get(t);if(u&&d)return u==t&&d==e;var v=-1,f=!0,h=n&YA?new zd:void 0;for(a.set(e,t),a.set(t,e);++v<l;){var p=e[v],y=t[v];if(o)var j=s?o(y,p,v,t,e,a):o(p,y,v,e,t,a);if(j!==void 0){if(j)continue;f=!1;break}if(h){if(!QA(t,function(b,k){if(!KA(h,k)&&(p===b||i(p,b,n,o,a)))return h.push(k)})){f=!1;break}}else if(!(p===y||i(p,y,n,o,a))){f=!1;break}}return a.delete(e),a.delete(t),f}function XA(e){var t=-1,n=Array(e.size);return e.forEach(function(o,i){n[++t]=[i,o]}),n}function ZA(e){var t=-1,n=Array(e.size);return e.forEach(function(o){n[++t]=o}),n}var ez=1,tz=2,nz="[object Boolean]",rz="[object Date]",oz="[object Error]",az="[object Map]",iz="[object Number]",sz="[object RegExp]",lz="[object Set]",cz="[object String]",uz="[object Symbol]",dz="[object ArrayBuffer]",vz="[object DataView]",$0=La?La.prototype:void 0,sf=$0?$0.valueOf:void 0;function fz(e,t,n,o,i,a,s){switch(n){case vz:if(e.byteLength!=t.byteLength||e.byteOffset!=t.byteOffset)return!1;e=e.buffer,t=t.buffer;case dz:return!(e.byteLength!=t.byteLength||!a(new Ad(e),new Ad(t)));case nz:case rz:case iz:return iu(+e,+t);case oz:return e.name==t.name&&e.message==t.message;case sz:case cz:return e==t+"";case az:var l=XA;case lz:var c=o&ez;if(l||(l=ZA),e.size!=t.size&&!c)return!1;var u=s.get(e);if(u)return u==t;o|=tz,s.set(e,t);var d=Qj(l(e),l(t),o,i,a,s);return s.delete(e),d;case uz:if(sf)return sf.call(e)==sf.call(t)}return!1}var pz=1,hz=Object.prototype,gz=hz.hasOwnProperty;function mz(e,t,n,o,i,a){var s=n&pz,l=up(e),c=l.length,u=up(t),d=u.length;if(c!=d&&!s)return!1;for(var v=c;v--;){var f=l[v];if(!(s?f in t:gz.call(t,f)))return!1}var h=a.get(e),p=a.get(t);if(h&&p)return h==t&&p==e;var y=!0;a.set(e,t),a.set(t,e);for(var j=s;++v<c;){f=l[v];var b=e[f],k=t[f];if(o)var E=s?o(k,b,f,t,e,a):o(b,k,f,e,t,a);if(!(E===void 0?b===k||i(b,k,n,o,a):E)){y=!1;break}j||(j=f=="constructor")}if(y&&!j){var O=e.constructor,w=t.constructor;O!=w&&"constructor"in e&&"constructor"in t&&!(typeof O=="function"&&O instanceof O&&typeof w=="function"&&w instanceof w)&&(y=!1)}return a.delete(e),a.delete(t),y}var bz=1,A0="[object Arguments]",z0="[object Array]",Du="[object Object]",yz=Object.prototype,P0=yz.hasOwnProperty;function jz(e,t,n,o,i,a){var s=oa(e),l=oa(t),c=s?z0:ua(e),u=l?z0:ua(t);c=c==A0?Du:c,u=u==A0?Du:u;var d=c==Du,v=u==Du,f=c==u;if(f&&Bc(e)){if(!Bc(t))return!1;s=!0,d=!1}if(f&&!d)return a||(a=new wa),s||wh(e)?Qj(e,t,n,o,i,a):fz(e,t,c,n,o,i,a);if(!(n&bz)){var h=d&&P0.call(e,"__wrapped__"),p=v&&P0.call(t,"__wrapped__");if(h||p){var y=h?e.value():e,j=p?t.value():t;return a||(a=new wa),i(y,j,n,o,a)}}return f?(a||(a=new wa),mz(e,t,n,o,i,a)):!1}function Eh(e,t,n,o,i){return e===t?!0:e==null||t==null||!Ua(e)&&!Ua(t)?e!==e&&t!==t:jz(e,t,n,o,Eh,i)}var xz=1,wz=2;function kz(e,t,n,o){var i=n.length,a=i;if(e==null)return!a;for(e=Object(e);i--;){var s=n[i];if(s[2]?s[1]!==e[s[0]]:!(s[0]in e))return!1}for(;++i<a;){s=n[i];var l=s[0],c=e[l],u=s[1];if(s[2]){if(c===void 0&&!(l in e))return!1}else{var d=new wa,v;if(!(v===void 0?Eh(u,c,xz|wz,o,d):v))return!1}}return!0}function Kj(e){return e===e&&!Wa(e)}function Sz(e){for(var t=kh(e),n=t.length;n--;){var o=t[n],i=e[o];t[n]=[o,i,Kj(i)]}return t}function Gj(e,t){return function(n){return n==null?!1:n[e]===t&&(t!==void 0||e in Object(n))}}function Cz(e){var t=Sz(e);return t.length==1&&t[0][2]?Gj(t[0][0],t[0][1]):function(n){return n===e||kz(n,e,t)}}function Oz(e,t){return e!=null&&t in Object(e)}function _z(e,t,n){t=Ij(t,e);for(var o=-1,i=t.length,a=!1;++o<i;){var s=uv(t[o]);if(!(a=e!=null&&n(e,s)))break;e=e[s]}return a||++o!=i?a:(i=e==null?0:e.length,!!i&&yh(i)&&bh(s,i)&&(oa(e)||$d(e)))}function Ez(e,t){return e!=null&&_z(e,t,Oz)}var Tz=1,Mz=2;function $z(e,t){return Ch(e)&&Kj(t)?Gj(uv(e),t):function(n){var o=v$(n,e);return o===void 0&&o===t?Ez(n,e):Eh(t,o,Tz|Mz)}}function Az(e){return function(t){return t==null?void 0:t[e]}}function zz(e){return function(t){return qj(t,e)}}function Pz(e){return Ch(e)?Az(uv(e)):zz(e)}function Nz(e){return typeof e=="function"?e:e==null?gh:typeof e=="object"?oa(e)?$z(e[0],e[1]):Cz(e):Pz(e)}function Rz(e){return function(t,n,o){for(var i=-1,a=Object(t),s=o(t),l=s.length;l--;){var c=s[++i];if(n(a[c],c,a)===!1)break}return t}}var Yj=Rz();function Iz(e,t){return e&&Yj(e,t,kh)}function pp(e,t,n){(n!==void 0&&!iu(e[t],n)||n===void 0&&!(t in e))&&iv(e,t,n)}function qz(e){return Ua(e)&&sv(e)}function hp(e,t){if(!(t==="constructor"&&typeof e[t]=="function")&&t!="__proto__")return e[t]}function Dz(e){return Mj(e,Sh(e))}function Lz(e,t,n,o,i,a,s){var l=hp(e,n),c=hp(t,n),u=s.get(c);if(u){pp(e,n,u);return}var d=a?a(l,c,n+"",e,t,s):void 0,v=d===void 0;if(v){var f=oa(c),h=!f&&Bc(c),p=!f&&!h&&wh(c);d=c,f||h||p?oa(l)?d=l:qz(l)?d=CT(l):h?(v=!1,d=Bj(c,!0)):p?(v=!1,d=Fj(c,!0)):d=[]:y$(c)||$d(c)?(d=l,$d(l)?d=Dz(l):(!Wa(l)||mh(l))&&(d=Wj(c))):v=!1}v&&(s.set(c,d),i(d,c,o,a,s),s.delete(c)),pp(e,n,d)}function Xj(e,t,n,o,i){e!==t&&Yj(t,function(a,s){if(i||(i=new wa),Wa(a))Lz(e,t,s,n,Xj,o,i);else{var l=o?o(hp(e,s),a,s+"",e,t,i):void 0;l===void 0&&(l=a),pp(e,s,l)}},Sh)}var Uz=$j(function(e,t,n,o){Xj(e,t,n,o)});function Bz(e,t){var n={};return t=Nz(t),Iz(e,function(o,i,a){iv(n,t(o,i,a),o)}),n}const Fz=new RegExp("([\\p{Ll}\\d])(\\p{Lu})","gu"),Wz=new RegExp("(\\p{Lu})([\\p{Lu}][\\p{Ll}])","gu"),Vz=new RegExp("(\\d)\\p{Ll}|(\\p{L})\\d","u"),Jz=/[^\p{L}\d]+/giu,N0="$1\0$2",R0="";function Zj(e){let t=e.trim();t=t.replace(Fz,N0).replace(Wz,N0),t=t.replace(Jz,"\0");let n=0,o=t.length;for(;t.charAt(n)==="\0";)n++;if(n===o)return[];for(;t.charAt(o-1)==="\0";)o--;return t.slice(n,o).split(/\0/g)}function Hz(e){const t=Zj(e);for(let n=0;n<t.length;n++){const o=t[n],i=Vz.exec(o);if(i){const a=i.index+(i[1]??i[2]).length;t.splice(n,1,o.slice(0,a),o.slice(a))}}return t}function Qz(e,t){const[n,o,i]=Xz(e,t),a=Kz(void 0),s=Gz(void 0),l=Yz(a,s);return n+o.map((c,u)=>u===0?a(c):l(c,u)).join("")+i}function Kz(e){return t=>t.toLocaleLowerCase(e)}function Gz(e){return t=>t.toLocaleUpperCase(e)}function Yz(e,t){return(n,o)=>{const i=n[0];return(o>0&&i>="0"&&i<="9"?"_"+i:t(i))+e(n.slice(1))}}function Xz(e,t={}){const n=t.split??(t.separateNumbers?Hz:Zj),o=t.prefixCharacters??R0,i=t.suffixCharacters??R0;let a=0,s=e.length;for(;a<e.length;){const l=e.charAt(a);if(!o.includes(l))break;a++}for(;s>a;){const l=s-1,c=e.charAt(l);if(!i.includes(c))break;s=l}return[e.slice(0,a),n(e.slice(a,s)),e.slice(s)]}const kc=e=>/.+-.+/.test(e)?Qz(e):e,Zz=e=>Object.prototype.toString.call(e).slice(8,-1)==="Object";function eP(e,t){const n=Object.create(null),o=e.split(",");for(let i=0;i<o.length;i++)n[o[i]]=!0;return i=>!!n[i]}const tP=eP("String,Number,Boolean,Function,Symbol,BigInt");function nP(e){const t=e==null?void 0:e.toString().match(/^\s*function (\w+)/);return t?t[1]:e===null?"null":""}function rP(e,t){let n;const o=nP(t);if(tP(o)){const i=typeof e;n=i===o.toLowerCase(),!n&&i==="object"&&(n=e instanceof t)}else o==="Object"?n=Wa(e):o==="Array"?n=Array.isArray(e):o==="null"?n=e===null:n=e instanceof t;return{valid:n,expectedType:o}}function oP({prop:e,type:t,validator:n}){if(![void 0,null].includes(e)&&t){let o=!1;const i=Array.isArray(t)?t:[t],a=[];for(let s=0;s<i.length&&!o;s++){const{valid:l,expectedType:c}=rP(e,i[s]);a.push(c||""),o=l}if(!o)throw new TypeError(`Invalid prop: type check failed, expecting [${a.join(", ")}], receiving: ${e}`)}if(n&&!n(e))throw new Error(`Invalid prop: validator check failed, receiving: ${e}`)}function aP(e,{mergeObject:t,mergeObjectCustomizer:n,mergeFunction:o}){const i=[];for(let s=e.length-1;s>=0;s--)i.push(e[s]);const a=n||(o?(s,l)=>typeof s=="function"&&typeof l=="function"?o==null?void 0:o(l,s):void 0:void 0);return t==="deep"?Uz(...i,a):AM(...i,a)}function iP(e,{mergeFunction:t}){return e.reduce(t,()=>{})}function $i(e,t={}){const{type:n,default:o,defaultIsDynamic:i=!1,required:a=!1,validator:s,camelizeObjectKeys:l=!1,mergeObjectApplyOnlyToDefault:c=!1,mergeFunctionApplyOnlyToDefault:u=!0}=t;let{mergeObject:d="deep",mergeObjectCustomizer:v,mergeFunction:f=!1}=t;const h=[];let p,y=!1,j=!1;const b=k=>{if(k!==void 0){oP({type:n,prop:k,validator:s});const E=Zz(k),O=typeof k=="function";return y=E,j=O,E?(k=WA(k),l?Bz(k,(w,_)=>kc(_)):k):k}};for(const k of e)h.push(b(k));if(!i)h.push(b(o));else if(typeof o!="function")throw new TypeError(`Invalid option: options.default should be Function when options.defaultIsDynamic enabled, receiving: ${o}`);y||(d=!1,j||(f=!1));for(let k=0;k<h.length;k++){const E=h[k];if(E!==void 0){k===h.length-1?p=E:d?p=aP(c?[E,o]:h,{mergeObject:d,mergeObjectCustomizer:v,mergeFunction:f}):f?p=iP(u?[E,o]:h,{mergeFunction:f}):p=E;break}}if(a&&[void 0,null].includes(p))throw new Error("Missing required prop");return i?$i(e,{...t,default:o(p),defaultIsDynamic:!1}):p}function I0(e){const t=Array.from(kc(e));return t[0]=t[0].toUpperCase(),t.unshift("o","n"),t.join("")}function sP(e,{props:t=[],camelizePropNames:n=!1}={}){const o={props:{},attrs:{},listeners:{},hooks:{},slots:{}};let i;if(Array.isArray(t))i=n?t.map(a=>kc(a)):t;else if(n){i=[];for(const a in t)i.push(kc(a))}else i=Object.keys(t);for(const a in e)if(a.startsWith("@")){const s=a.substring(1);if(s.startsWith("vue:"))o.hooks[I0(s.replace("vue:","vnode-"))]=e[a];else{if(s.startsWith("vnode"))throw new Error("@vnode-* hooks are no longer supported. Use the vue: prefix instead. For example, @vnode-mounted should be changed to @vue:mounted. @vnode-* hooks support has been removed in Vue 3.4.");o.listeners[I0(s)]=e[a]}}else if(a.startsWith("#")){const s=a.substring(1);s&&(o.slots[s]=e[a])}else{const s=n?kc(a):a;i.includes(s)?o.props[s]=e[a]:o.attrs[a]=e[a]}return o}const q0="JsonEditorVue",Xu=["mainMenuBar","navigationBar","statusBar","askToFormat","readOnly","escapeControlCharacters","escapeUnicodeCharacters","flattenColumns"],Ei={},D0={},Zu="modelValue",L0="update:modelValue",U0={[Zu]:{},mode:{type:String},debounce:{type:Number},stringified:{type:Boolean,default:void 0},...Object.fromEntries(Xu.map(e=>[e,{type:Boolean,default:void 0}]))},lP=F0({name:q0,install(e,t){const n=sP(t||{},{props:U0});Object.assign(Ei,n.props),Object.assign(D0,n.attrs),e.component(q0,this)},props:U0,emits:{[L0](e){return!0},"update:mode":function(e){return!0}},setup(e,{attrs:t,emit:n,expose:o}){var i;const a=(i=vx())==null?void 0:i.proxy,s=pr(),l=pr(!1),c=pr();fx(()=>{var b;c.value=$i([e.mode,Ei.mode],{type:String}),(b=s.value)==null||b.updateProps({mode:c.value||Mr.tree})});const u=b=>{n("update:mode",b)};Ei.mode!==void 0&&e.mode===void 0&&u(Ei.mode);const d=Go(()=>$i([e.debounce,Ei.debounce,300],{type:Number})),v=Go(()=>$i([e.stringified,Ei.stringified,!0],{type:Boolean}));let f=Gu;const h=b=>{l.value=!0,!v.value&&b.text&&(s.value&&!s.value.validate()&&(b.json=f(b.text)),b.text=void 0),n(L0,b.text===void 0?b.json:b.text)},p=K7(h,d.value),y=b=>{c.value==="text"?p(b):h(b)},j=(b,k)=>(...E)=>{b(...E),k(...E)};return o==null||o({jsonEditor:s}),V0(()=>{var b;(b=s.value)==null||b.destroy()}),J0(()=>{const b=$i([e[Zu],Ei[Zu]]),k=Object.fromEntries(Array.from(Xu,O=>[O,$i([e[O],Ei[O]])]).filter(([,O])=>O!==void 0)),E=$i([k,t,D0],{camelizeObjectKeys:!0,defaultIsDynamic:!0,default:O=>{var w;return f=((w=O.parser)==null?void 0:w.parse)||Gu,{onChange:y,onChangeMode:u,mode:c.value,parser:{parse:k7,stringify:JSON.stringify},...b!==void 0&&{content:{[typeof b=="string"&&c.value==="text"&&v.value?"text":"json"]:b}}}},mergeFunction:j,mergeObject:"shallow",type:Object});s.value=m7({target:a==null?void 0:a.$refs.jsonEditorRef,props:E}),bv(()=>e[Zu],O=>{if(l.value){l.value=!1;return}s.value&&s.value.set([void 0,""].includes(O)?{text:""}:{[typeof O=="string"&&c.value==="text"&&v.value?"text":"json"]:O})},{deep:!0}),bv(()=>Array.from(Xu,O=>e[O]),O=>{var w;(w=s.value)==null||w.updateProps(Object.fromEntries(Array.from(O,(_,A)=>[Xu[A],_]).filter(([,_])=>_!==void 0)))}),bv(()=>t,O=>{var w,_;const A={};(O.onChange||O["on-change"])&&(A.onChange=y),(O.onChangeMode||O["on-change-mode"])&&(A.onChangeMode=u),f=((w=O.parser)==null?void 0:w.parse)||Gu,(_=s.value)==null||_.updateProps(Object.getOwnPropertyNames(A).length>0?$i([O,A],{camelizeObjectKeys:!0,mergeFunction:j,mergeObject:"shallow",type:Object}):O)},{deep:!0}),o||(o=O=>{for(const w in O)a[w]=ko(O[w])},o({jsonEditor:s}))}),()=>px("div",{ref:"jsonEditorRef"})}});const cP={class:"container"},uP={class:"toolbar"},dP={class:"tmdb-cache-mobile-list"},vP={class:"tmdb-cache-card-head"},fP={class:"tmdb-cache-card-title"},pP={class:"tmdb-cache-card-meta"},hP={class:"tmdb-id-value"},gP={class:"tmdb-cache-card-row"},mP={class:"tmdb-cache-card-actions"},bP={class:"pagination-wrapper"},yP={class:"tmdb-cache-mobile-pagination"},jP={class:"tmdb-cache-mobile-pagination-total"},xP={class:"tmdb-cache-mobile-pagination-controls"},wP={class:"tmdb-cache-mobile-page-indicator"},kP={key:0,class:"media-summary"},SP={class:"media-poster-wrap"},CP=["src","alt"],OP={key:1,class:"media-poster-placeholder"},_P={class:"media-summary-content"},EP={class:"media-title"},TP={class:"media-meta"},MP={class:"divider"},$P={class:"media-overview"},AP={class:"add-search-form"},zP={key:0,class:"add-result-list"},PP=["onClick"],NP={class:"add-result-poster-wrap"},RP=["src","alt"],IP={key:1,class:"add-result-poster-placeholder"},qP={class:"add-result-content"},DP={class:"add-result-title"},LP={class:"add-result-meta"},UP={class:"divider"},BP={class:"add-result-overview"},FP={class:"add-result-footer"},WP={key:1},B0="tmdb-cache-add-search",VP={__name:"TmdbCache",setup(e){const t=pr([]),n=pr(!1),o=pr(!1),i=pr(!1),a=pr(!1),s=pr(!1),l=pr(!1),c=pr([]),u=pr(null),d=pr(null),v=pr(!1),f=pr(!1),h=pr(!1),p=pr(!1),y=pr(1),j=pr(0),b=pr(null),k=pr(null),E=pr(""),O=pr(""),w=Ah({total:0,current:1,pageSize:10}),_=Ah({type:"checkbox",showCheckedAll:!0,onlyCurrent:!1}),A=pr({type:void 0,status:void 0,title:"",tmdb_id:""}),q=()=>{try{const J=JSON.parse(localStorage.getItem(B0)||"{}");return{type:["movie","tv"].includes(J.type)?J.type:"movie",keyword:typeof J.keyword=="string"?J.keyword:""}}catch{return{type:"movie",keyword:""}}},C=()=>{try{localStorage.setItem(B0,JSON.stringify(D.value))}catch(J){console.warn("保存TMDB搜索条件失败:",J)}},z=J=>{const V=String(J||"").trim(),Ve=V.match(/^(.+?)\s+((?:19|20)\d{2})$/);return{keyword:Ve?Ve[1].trim():V,year:Ve?Ve[2]:void 0}},D=pr(q()),H=pr([]),Q=Go(()=>Math.max(1,Math.ceil(w.total/w.pageSize))),fe=Go(()=>y.value*20<j.value),Ie=Go(()=>o.value?"calc(100vw - 32px)":920),ge=Go(()=>o.value?"calc(100vw - 32px)":520),qe=Go(()=>o.value?"calc(100vw - 32px)":520),ce=Go(()=>o.value?"calc(100vw - 32px)":760),ve=Go(()=>{const J=u.value;if(!(J!=null&&J.poster_path))return"";if(/^https?:\/\//.test(J.poster_path))return J.poster_path;const V=String(J.img_domain||E.value||"").replace(/\/$/,"");return V?`${V}/t/p/h632/${String(J.poster_path).replace(/^\//,"")}`:""}),he=Go(()=>Ae(d.value)),Ue=()=>{o.value=window.innerWidth<=768},Re=async()=>{n.value=!0;try{const J={page:w.current,page_size:w.pageSize,...A.value};Object.keys(J).forEach(ye=>{(J[ye]===""||J[ye]===void 0||J[ye]===null)&&delete J[ye]});const Ve=(await Si.getTmdbCacheList(J)).data;Ve.code===200?(E.value=Ve.img_domain||E.value,t.value=Array.isArray(Ve.data)?Ve.data:[],w.total=Ve.total||0,w.current=Ve.page||w.current,w.pageSize=Ve.page_size||w.pageSize):Tr.error(Ve.msg||"获取TMDB信息失败")}catch(J){console.error("获取TMDB信息失败:",J),Tr.error("获取TMDB信息失败")}finally{n.value=!1}},we=()=>{w.current=1,Re()},ue=()=>{A.value={type:void 0,status:void 0,title:"",tmdb_id:""},w.current=1,Re()},ie=()=>{s.value=!0},vt=()=>{s.value=!1,H.value=[],O.value="",p.value=!1,y.value=1,j.value=0},ft=async()=>{C(),H.value=[],p.value=!1,y.value=1,j.value=0,D.value.keyword.trim()&&await oe()},kt=async(J,V=!1)=>{var Ve,ye,rt,dt,At,en;f.value=!0;try{const Vt=z(D.value.keyword),Ht={keyword:Vt.keyword,page:J,page_size:20};Vt.year&&(Ht.primary_release_year=Vt.year);const dn=(D.value.type==="movie"?await Si.searchMovie(Ht):await Si.searchTV(Ht)).data;if(dn.code===200){const Qn=Array.isArray((Ve=dn.data)==null?void 0:Ve.results)?dn.data.results:[];H.value=V?[...H.value,...Qn]:Qn,y.value=J,j.value=Number((ye=dn.data)==null?void 0:ye.total_results)||0,O.value=((rt=dn.data)==null?void 0:rt.img_domain)||O.value,E.value=((dt=dn.data)==null?void 0:dt.img_domain)||E.value}else V||(H.value=[]),Tr.error(dn.msg||"搜索失败")}catch(Vt){console.error("搜索TMDB失败:",Vt),V||(H.value=[]),Tr.error(((en=(At=Vt.response)==null?void 0:At.data)==null?void 0:en.msg)||"搜索失败")}finally{f.value=!1}},oe=async()=>{if(!D.value.type){Tr.warning("请先选择电影或剧集");return}if(!D.value.keyword.trim()){Tr.warning("请输入搜索关键词");return}C(),p.value=!0,y.value=1,j.value=0,H.value=[],await kt(1)},Ze=async()=>{f.value||!fe.value||await kt(y.value+1,!0)},te=async J=>{var V,Ve;if(!h.value){h.value=!0;try{const ye=D.value.type,rt={type:ye,tmdb_id:String(J.id),title:Me(J),year:pe(J),season_num:null,poster_path:J.poster_path||"",backdrop_path:J.backdrop_path||"",query_url:`/3/search/${ye}/${J.id}`,query_response:JSON.stringify(J),status:1},At=(await Si.addTmdbCache(rt)).data;At.code===200?(Tr.success(At.msg||"添加成功"),vt(),w.current=1,Re()):Tr.error(At.msg||"添加失败")}catch(ye){console.error("添加TMDB缓存失败:",ye),Tr.error(((Ve=(V=ye.response)==null?void 0:V.data)==null?void 0:Ve.msg)||"添加失败")}finally{h.value=!1}}},X=J=>{u.value=J,d.value=St(J.query_response),i.value=!0,qh(()=>{$t(),Yt()})},B=()=>{i.value=!1,u.value=null,d.value=null,sn()},Ne=async J=>{var Ve,ye;if(J.statusLoading)return;const V=J.status===1?0:1;J.statusLoading=!0;try{const dt=(await Si.updateTmdbCache({id:J.id,status:V})).data;dt.code===200?(J.status=V,Tr.success(V===1?"已启用":"已禁用")):Tr.error(dt.msg||"状态更新失败")}catch(rt){console.error("更新TMDB状态失败:",rt),Tr.error(((ye=(Ve=rt.response)==null?void 0:Ve.data)==null?void 0:ye.msg)||"状态更新失败")}finally{J.statusLoading=!1}},ee=()=>{if(!c.value.length){Tr.warning("请选择要删除的TMDB信息");return}l.value=!0},L=()=>{l.value=!1},pt=async J=>{var V,Ve;try{const rt=(await Si.deleteTmdbCacheRecords({ids:c.value})).data;rt.code===200?(Tr.success(rt.msg||"批量删除成功"),c.value.length>=t.value.length&&w.current>1&&(w.current-=1),c.value=[],l.value=!1,Re(),J(!0)):(Tr.error(rt.msg||"批量删除失败"),J(!1))}catch(ye){console.error("批量删除TMDB信息失败:",ye),Tr.error(((Ve=(V=ye.response)==null?void 0:V.data)==null?void 0:Ve.msg)||"批量删除失败"),J(!1)}},ht=J=>{u.value=J,a.value=!0},_e=()=>{qh(Yt)},at=()=>{a.value=!1},We=async J=>{var V,Ve,ye;if(!((V=u.value)!=null&&V.id)){J(!1);return}try{const dt=(await Si.deleteTmdbCacheRecords({ids:[u.value.id]})).data;dt.code===200?(Tr.success("删除成功"),a.value=!1,c.value=c.value.filter(At=>At!==u.value.id),u.value=null,t.value.length===1&&w.current>1&&(w.current-=1),Re(),J(!0)):(Tr.error(dt.msg||"删除失败"),J(!1))}catch(rt){console.error("删除TMDB信息失败:",rt),Tr.error(((ye=(Ve=rt.response)==null?void 0:Ve.data)==null?void 0:ye.msg)||"删除失败"),J(!1)}},Ye=async()=>{var V,Ve,ye;if(!((V=u.value)!=null&&V.id)){Tr.warning("缺少缓存记录ID");return}const J=Xe(d.value);if(!J.valid){Tr.error(J.message);return}v.value=!0;try{const rt={id:u.value.id,type:u.value.type,tmdb_id:u.value.tmdb_id,title:u.value.title,year:u.value.year,season_num:u.value.season_num,poster_path:u.value.poster_path,backdrop_path:u.value.backdrop_path,query_url:u.value.query_url,query_response:lt(d.value),status:u.value.status},At=(await Si.updateTmdbCache(rt)).data;At.code===200?(Tr.success(At.msg||"更新成功"),i.value=!1,u.value=null,d.value=null,Re()):Tr.error(At.msg||"更新失败")}catch(rt){console.error("更新TMDB缓存失败:",rt),Tr.error(((ye=(Ve=rt.response)==null?void 0:Ve.data)==null?void 0:ye.msg)||"更新失败")}finally{v.value=!1}},Tt=J=>{w.current=J,Re()},He=J=>{w.pageSize=J,w.current=1,Re()},qt=()=>{w.current<=1||Tt(w.current-1)},S=()=>{w.current>=Q.value||Tt(w.current+1)},$=J=>(J==null?void 0:J.season_num)!==null&&(J==null?void 0:J.season_num)!==void 0&&(J==null?void 0:J.season_num)!=="",N=J=>{if(!J)return"-";const V=J.title?`${J.title} (${J.year})`:"-";return $(J)?`${V} S${J.season_num}`:V},G=J=>({movie:"电影",tv:"剧集",season:"季"})[J]||J||"-",W=J=>{if(!J)return"";const V=new Date(J);return Number.isNaN(V.getTime())?J:V.toLocaleString()},de=J=>J==null||J===""?"-":J,Me=J=>D.value.type==="movie"?J.title||"":J.name||"",pe=J=>{const V=D.value.type==="movie"?J.release_date:J.first_air_date;return V?String(V).split("-")[0]:""},le=J=>{if(!(J!=null&&J.poster_path))return"";if(/^https?:\/\//.test(J.poster_path))return J.poster_path;const V=String(O.value||E.value||"").replace(/\/$/,"");return V?`${V}/t/p/h632/${String(J.poster_path).replace(/^\//,"")}`:""},St=J=>{if(J==null||J==="")return"";if(typeof J=="object")return J;try{return JSON.parse(J)}catch{return String(J)}},lt=J=>J==null||J===""?"":JSON.stringify(typeof J=="string"?JSON.parse(J):J),Xe=J=>{if(J==null)return{valid:!1,message:"TMDB信息必须是合法的 JSON"};if(typeof J!="string")return{valid:!0,message:""};if(!J.trim())return{valid:!1,message:"TMDB信息必须是合法的 JSON"};try{return JSON.parse(J),{valid:!0,message:""}}catch{return{valid:!1,message:"TMDB信息不是合法的 JSON，请修正后再更新缓存"}}},Ae=J=>{const V=St(J);return V&&typeof V=="object"&&!Array.isArray(V)&&V.overview||""},$t=()=>{sn();const J=Un();J&&(k.value=new MutationObserver(()=>{Yt()}),k.value.observe(J,{childList:!0,subtree:!0,characterData:!0}))},sn=()=>{k.value&&(k.value.disconnect(),k.value=null)},Un=()=>{const J=b.value;return(J==null?void 0:J.$el)||null},Yt=()=>{const J=Un();if(!J)return;const V=document.createTreeWalker(J,NodeFilter.SHOW_TEXT),Ve=[];for(;V.nextNode();)Hn(V.currentNode)||Ve.push(V.currentNode);Ve.forEach(ye=>{const rt=Zt(ye.nodeValue||"");rt!==ye.nodeValue&&(ye.nodeValue=rt)}),J.querySelectorAll("input").forEach(ye=>{Dt(ye,"placeholder"),Dt(ye,"aria-label"),Dt(ye,"title"),Dt(ye,"value")}),J.querySelectorAll("button, label").forEach(ye=>{Dt(ye,"aria-label"),Dt(ye,"title"),Dt(ye,"value")}),J.querySelectorAll(".cm-search button[name]").forEach(ye=>{const rt=hn(ye.getAttribute("name"));rt&&(ye.textContent=rt)})},Zt=J=>{const V=J.trim(),Ve={Find:"查找",Replace:"替换",Next:"下一个",next:"下一个",Previous:"上一个",previous:"上一个",All:"全部",all:"全部","Replace All":"全部替换","replace all":"全部替换","match case":"区分大小写",regexp:"正则","by word":"全词匹配",close:"关闭",Close:"关闭"};return Ve[V]?J.replace(V,Ve[V]):J.replaceAll("Auto repair","自动修复").replaceAll("Show me","定位").replaceAll("Expected ',' or '}' after property value in JSON","JSON 属性值后应为 “,” 或 “}”").replaceAll("Expected ',' or ']' after array element in JSON","JSON 数组元素后应为 “,” 或 “]”").replaceAll("Expected property name or","应为属性名或").replaceAll("Expected double-quoted property name in JSON","JSON 属性名应使用双引号").replaceAll("Unexpected token","意外的字符").replaceAll("Unexpected end of JSON input","JSON 内容意外结束").replace(/\bat line (\d+) column (\d+)\b/g,"在第 $1 行第 $2 列").replace(/\(line (\d+) column (\d+)\)/g,"（第 $1 行第 $2 列）")},Dt=(J,V)=>{const Ve=J.getAttribute(V);if(!Ve)return;const ye=Zt(Ve);ye!==Ve&&J.setAttribute(V,ye)},hn=J=>({next:"下一个",prev:"上一个",select:"全部",replace:"替换",replaceAll:"全部替换"})[J]||"",Hn=J=>{const V=J.parentElement;return!!(V!=null&&V.closest(".cm-content"))};return J0(()=>{Ue(),window.addEventListener("resize",Ue),Re()}),V0(()=>{sn(),window.removeEventListener("resize",Ue)}),(J,V)=>{const Ve=ro("a-option"),ye=ro("a-select"),rt=ro("a-input"),dt=ro("a-button"),At=ro("a-space"),en=ro("a-alert"),Vt=ro("a-divider"),Ht=ro("a-table-column"),On=ro("a-tag"),dn=ro("a-switch"),Qn=ro("a-table"),Kn=ro("a-empty"),Bn=ro("a-checkbox"),Zn=ro("a-checkbox-group"),yr=ro("a-pagination"),Fn=ro("a-card"),$n=ro("a-modal"),ar=ro("a-radio"),Se=ro("a-radio-group");return Vr(),No("div",cP,[gt(Fn,{class:"general-card",bordered:!1},{title:zt(()=>V[15]||(V[15]=[qn("TMDB信息缓存")])),default:zt(()=>[kn("div",uP,[gt(At,null,{default:zt(()=>[gt(ye,{modelValue:A.value.type,"onUpdate:modelValue":V[0]||(V[0]=Ee=>A.value.type=Ee),placeholder:"媒体类型","allow-clear":"",style:{width:"140px"}},{default:zt(()=>[gt(Ve,{value:"movie"},{default:zt(()=>V[16]||(V[16]=[qn("电影")])),_:1}),gt(Ve,{value:"tv"},{default:zt(()=>V[17]||(V[17]=[qn("剧集")])),_:1}),gt(Ve,{value:"season"},{default:zt(()=>V[18]||(V[18]=[qn("季")])),_:1})]),_:1},8,["modelValue"]),gt(ye,{modelValue:A.value.status,"onUpdate:modelValue":V[1]||(V[1]=Ee=>A.value.status=Ee),placeholder:"状态","allow-clear":"",style:{width:"140px"}},{default:zt(()=>[gt(Ve,{value:1},{default:zt(()=>V[19]||(V[19]=[qn("启用")])),_:1}),gt(Ve,{value:0},{default:zt(()=>V[20]||(V[20]=[qn("禁用")])),_:1})]),_:1},8,["modelValue"]),gt(rt,{modelValue:A.value.title,"onUpdate:modelValue":V[2]||(V[2]=Ee=>A.value.title=Ee),placeholder:"模糊搜索","allow-clear":"",style:{width:"180px"},onPressEnter:we},null,8,["modelValue"]),gt(rt,{modelValue:A.value.tmdb_id,"onUpdate:modelValue":V[3]||(V[3]=Ee=>A.value.tmdb_id=Ee),placeholder:"TMDB ID","allow-clear":"",style:{width:"160px"},onPressEnter:we},null,8,["modelValue"]),gt(dt,{type:"primary",onClick:we},{icon:zt(()=>[gt(ko(zh))]),default:zt(()=>[V[21]||(V[21]=qn(" 查询 "))]),_:1}),gt(dt,{onClick:ue},{icon:zt(()=>[gt(ko(gx))]),default:zt(()=>[V[22]||(V[22]=qn(" 重置 "))]),_:1}),gt(dt,{type:"primary",status:"success",onClick:ie},{icon:zt(()=>[gt(ko(mx))]),default:zt(()=>[V[23]||(V[23]=qn(" 新增 "))]),_:1}),gt(dt,{status:"danger",disabled:c.value.length===0,onClick:ee},{icon:zt(()=>[gt(ko(bx))]),default:zt(()=>[V[24]||(V[24]=qn(" 批量删除 "))]),_:1},8,["disabled"])]),_:1})]),gt(en,{type:"info","show-icon":!1,class:"description-alert"},{default:zt(()=>V[25]||(V[25]=[qn(" 用于自定义一些tmdb里的信息，比如名称、分类等 ")])),_:1}),gt(Vt,{style:{"margin-top":"0"}}),gt(Qn,{class:"tmdb-cache-table",data:t.value,loading:n.value,pagination:!1,"row-selection":_,selectedKeys:c.value,"onUpdate:selectedKeys":V[4]||(V[4]=Ee=>c.value=Ee),"row-key":"id"},{columns:zt(()=>[gt(Ht,{title:"ID","data-index":"id",width:80}),gt(Ht,{title:"类型","data-index":"type",width:100},{cell:zt(({record:Ee})=>[gt(On,{class:"media-type-tag",color:Ee.type==="movie"?"blue":"purple"},{default:zt(()=>[Ee.type==="movie"?(Vr(),Ci(ko(Ph),{key:0})):(Vr(),Ci(ko(Fh),{key:1})),kn("span",null,qr(G(Ee.type)),1)]),_:2},1032,["color"])]),_:1}),gt(Ht,{title:"TMDB ID","data-index":"tmdb_id",width:120,ellipsis:!0,tooltip:{position:"top"}}),gt(Ht,{title:"片名","data-index":"title",width:220,ellipsis:!0,tooltip:{position:"top"}},{cell:zt(({record:Ee})=>[qn(qr(N(Ee)),1)]),_:1}),gt(Ht,{title:"状态","data-index":"status",width:110},{cell:zt(({record:Ee})=>[gt(dn,{type:"round","model-value":Ee.status===1,loading:Ee.statusLoading,onChange:tn=>Ne(Ee)},{checked:zt(()=>V[26]||(V[26]=[qn("启用")])),unchecked:zt(()=>V[27]||(V[27]=[qn("禁用")])),_:2},1032,["model-value","loading","onChange"])]),_:1}),gt(Ht,{title:"更新时间","data-index":"last_update_time",width:170},{cell:zt(({record:Ee})=>[qn(qr(W(Ee.last_update_time)),1)]),_:1}),gt(Ht,{title:"操作",width:150,fixed:"right"},{cell:zt(({record:Ee})=>[gt(At,null,{default:zt(()=>[gt(dt,{type:"primary",size:"small",onClick:tn=>X(Ee)},{default:zt(()=>V[28]||(V[28]=[qn("更新")])),_:2},1032,["onClick"]),gt(dt,{type:"primary",status:"danger",size:"small",onClick:tn=>ht(Ee)},{default:zt(()=>V[29]||(V[29]=[qn("删除")])),_:2},1032,["onClick"])]),_:2},1024)]),_:1})]),_:1},8,["data","loading","row-selection","selectedKeys"]),kn("div",dP,[!n.value&&t.value.length===0?(Vr(),Ci(Kn,{key:0})):cu("",!0),gt(Zn,{modelValue:c.value,"onUpdate:modelValue":V[5]||(V[5]=Ee=>c.value=Ee),class:"tmdb-cache-mobile-checks"},{default:zt(()=>[(Vr(!0),No(Nh,null,Rh(t.value,Ee=>(Vr(),No("div",{key:Ee.id,class:"tmdb-cache-card"},[kn("div",vP,[gt(Bn,{value:Ee.id},null,8,["value"]),kn("div",fP,qr(N(Ee)),1),gt(dn,{type:"round","model-value":Ee.status===1,loading:Ee.statusLoading,onChange:tn=>Ne(Ee)},{checked:zt(()=>V[30]||(V[30]=[qn("启用")])),unchecked:zt(()=>V[31]||(V[31]=[qn("禁用")])),_:2},1032,["model-value","loading","onChange"])]),kn("div",pP,[gt(On,{class:"media-type-tag",color:Ee.type==="movie"?"blue":"purple"},{default:zt(()=>[Ee.type==="movie"?(Vr(),Ci(ko(Ph),{key:0})):(Vr(),Ci(ko(Fh),{key:1})),kn("span",null,qr(G(Ee.type)),1)]),_:2},1032,["color"]),kn("span",hP,qr(Ee.tmdb_id||"-"),1)]),kn("div",gP,[V[32]||(V[32]=kn("span",null,"更新",-1)),kn("strong",null,qr(W(Ee.last_update_time||Ee.create_time)||"-"),1)]),kn("div",mP,[gt(dt,{onClick:tn=>X(Ee)},{default:zt(()=>V[33]||(V[33]=[qn("详情")])),_:2},1032,["onClick"]),gt(dt,{status:"danger",onClick:tn=>ht(Ee)},{default:zt(()=>V[34]||(V[34]=[qn("删除")])),_:2},1032,["onClick"])])]))),128))]),_:1},8,["modelValue"])]),kn("div",bP,[gt(yr,{class:"tmdb-cache-desktop-pagination",current:w.current,"onUpdate:current":V[6]||(V[6]=Ee=>w.current=Ee),pageSize:w.pageSize,"onUpdate:pageSize":V[7]||(V[7]=Ee=>w.pageSize=Ee),total:w.total,"show-total":"","show-jumper":"","show-page-size":"",size:"medium","page-size-options":[10,50,100,500],onChange:Tt,onPageSizeChange:He},null,8,["current","pageSize","total"]),kn("div",yP,[kn("div",jP," 共 "+qr(w.total)+" 条，每页 "+qr(w.pageSize)+" 条 ",1),kn("div",xP,[gt(dt,{disabled:w.current<=1,onClick:qt},{default:zt(()=>V[35]||(V[35]=[qn("上一页")])),_:1},8,["disabled"]),kn("div",wP," 第 "+qr(w.current)+" / "+qr(Q.value)+" 页 ",1),gt(dt,{disabled:w.current>=Q.value,onClick:S},{default:zt(()=>V[36]||(V[36]=[qn("下一页")])),_:1},8,["disabled"])])])])]),_:1}),gt($n,{visible:i.value,"onUpdate:visible":V[9]||(V[9]=Ee=>i.value=Ee),title:"TMDB信息","modal-class":"tmdb-detail-modal","body-class":"tmdb-detail-modal-body",width:Ie.value,"align-center":!1,top:5,onCancel:B},{footer:zt(()=>[gt(At,null,{default:zt(()=>[gt(dt,{onClick:B},{default:zt(()=>V[38]||(V[38]=[qn("取消")])),_:1}),gt(dt,{type:"primary",loading:v.value,onClick:Ye},{default:zt(()=>V[39]||(V[39]=[qn(" 更新缓存 ")])),_:1},8,["loading"])]),_:1})]),default:zt(()=>[u.value?(Vr(),No("div",kP,[kn("div",SP,[ve.value?(Vr(),No("img",{key:0,class:"media-poster",src:ve.value,alt:N(u.value)},null,8,CP)):(Vr(),No("div",OP,"无海报"))]),kn("div",_P,[kn("h3",EP,qr(N(u.value)),1),kn("div",TP,[kn("span",null,qr(G(u.value.type)),1),kn("span",MP,[gt(ko(Ih))]),kn("span",null,qr(de(u.value.tmdb_id)),1)]),kn("p",$P,qr(he.value||"暂无简介"),1)])])):cu("",!0),gt(en,{class:"response-tip",type:"info","show-icon":!1},{default:zt(()=>V[37]||(V[37]=[qn(" 这里的字段优先于tmdb里的字段，你可以删除任何你不需要自定义的字段，但是要保证去除后是一个合法的JSON格式。 ")])),_:1}),u.value?(Vr(),Ci(ko(lP),{key:1,modelValue:d.value,"onUpdate:modelValue":V[8]||(V[8]=Ee=>d.value=Ee),ref_key:"jsonEditorRef",ref:b,class:"response-json-editor",mode:ko(Mr).text,stringified:!1,"on-change":_e,"main-menu-bar":!1,"navigation-bar":!1,"status-bar":!1},null,8,["modelValue","mode"])):cu("",!0)]),_:1},8,["visible","width"]),gt($n,{visible:s.value,"onUpdate:visible":V[12]||(V[12]=Ee=>s.value=Ee),title:"新增TMDB缓存",width:ce.value,footer:!1,onCancel:vt},{default:zt(()=>[kn("div",AP,[gt(Se,{modelValue:D.value.type,"onUpdate:modelValue":V[10]||(V[10]=Ee=>D.value.type=Ee),class:"add-search-type",type:"button",onChange:ft},{default:zt(()=>[gt(ar,{value:"movie"},{default:zt(()=>V[40]||(V[40]=[qn("电影")])),_:1}),gt(ar,{value:"tv"},{default:zt(()=>V[41]||(V[41]=[qn("剧集")])),_:1})]),_:1},8,["modelValue"]),gt(rt,{modelValue:D.value.keyword,"onUpdate:modelValue":V[11]||(V[11]=Ee=>D.value.keyword=Ee),placeholder:"请输入电影名或剧集名","allow-clear":"",onPressEnter:oe},null,8,["modelValue"]),gt(dt,{type:"primary",loading:f.value,onClick:oe},{icon:zt(()=>[gt(ko(zh))]),default:zt(()=>[V[42]||(V[42]=qn(" 搜索 "))]),_:1},8,["loading"])]),H.value.length?(Vr(),No("div",zP,[(Vr(!0),No(Nh,null,Rh(H.value,Ee=>(Vr(),No("div",{key:`${D.value.type}-${Ee.id}`,class:W0(["add-result-item",{disabled:h.value}]),onClick:tn=>te(Ee)},[kn("div",NP,[le(Ee)?(Vr(),No("img",{key:0,class:"add-result-poster",src:le(Ee),alt:Me(Ee)},null,8,RP)):(Vr(),No("div",IP,"无海报"))]),kn("div",qP,[kn("div",DP,qr(Me(Ee))+" "+qr(pe(Ee)?`(${pe(Ee)})`:""),1),kn("div",LP,[kn("span",null,qr(G(D.value.type)),1),kn("span",UP,[gt(ko(Ih))]),kn("span",null,qr(Ee.id),1)]),kn("div",BP,qr(Ee.overview||"暂无简介"),1)])],10,PP))),128)),kn("div",FP,[fe.value?(Vr(),Ci(dt,{key:0,loading:f.value,disabled:h.value,onClick:Ze},{default:zt(()=>V[43]||(V[43]=[qn(" 加载下一页 ")])),_:1},8,["loading","disabled"])):(Vr(),No("span",WP,"已加载完毕"))])])):p.value&&!f.value?(Vr(),Ci(Kn,{key:1,description:"暂无搜索结果"})):cu("",!0)]),_:1},8,["visible","width"]),gt($n,{visible:a.value,"onUpdate:visible":V[13]||(V[13]=Ee=>a.value=Ee),title:"确认删除",width:ge.value,onCancel:at,onBeforeOk:We},{default:zt(()=>[gt(en,{type:"warning","show-icon":!1},{default:zt(()=>[qn(" 确定要删除「"+qr(N(u.value))+"」这条TMDB信息吗？此操作不可恢复。 ",1)]),_:1})]),_:1},8,["visible","width"]),gt($n,{visible:l.value,"onUpdate:visible":V[14]||(V[14]=Ee=>l.value=Ee),title:"确认批量删除",width:qe.value,onCancel:L,onBeforeOk:pt},{default:zt(()=>[gt(en,{type:"warning","show-icon":!1},{default:zt(()=>[qn(" 确定要删除选中的 "+qr(c.value.length)+" 条TMDB信息吗？此操作不可恢复。 ",1)]),_:1})]),_:1},8,["visible","width"])])}}},XP=hx(VP,[["__scopeId","data-v-a5e17216"]]);export{XP as default};
