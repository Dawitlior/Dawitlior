import re,sys
h=open("system-map.svg",encoding="utf-8").read()
n0=len(h)
h=re.sub(r">\s*\n\s*<","><",h)
# 1. packet fade (map packets only)
h=re.sub(r'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0\.1;0\.9;1"[^>]*/>',"",h)
# 2. marching dashes -> one CSS animation
h=h.replace('stroke-dasharray="5 7"><animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.6s" repeatCount="indefinite"/></path>','class="mc"/>')
h=re.sub(r'stroke-dasharray="4 6"><animate attributeName="stroke-dashoffset" from="20" to="0" dur="1\.6s" repeatCount="indefinite"/></path>','class="mc"/>',h)
h=h.replace("</style>",".mc{stroke-dasharray:5 7;animation:mc 1.6s linear infinite}@keyframes mc{from{stroke-dashoffset:24}to{stroke-dashoffset:0}}</style>",1)
# 3. banner node radius pulse
h=re.sub(r'<animate attributeName="r" values="1\.8;3\.8;1\.8"[^>]*/>',"",h)
open("system-map-opt.svg","w",encoding="utf-8").write(h)
print(n0,"->",len(h))
# --- extra slimming
h=open("system-map-opt.svg",encoding="utf-8").read()
ls=list(re.finditer(r"<line [^>]*>.*?</line>",h))
for k,m in reversed(list(enumerate(ls))):
    if k%2==1: h=h[:m.start()]+h[m.end():]
cnt={}
def drop(m):
    i=m.group(1);cnt[i]=cnt.get(i,0)+1
    return "" if cnt[i]>2 else m.group(0)
h=re.sub(r'<circle r="3\.8"[^>]*><animateMotion[^>]*><mpath href="#(\w+)"/></animateMotion></circle>',drop,h)
open("system-map-opt.svg","w",encoding="utf-8").write(h)
print("slim",len(h))
