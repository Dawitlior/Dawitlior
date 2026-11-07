import math, random
def V(x,y): return (x,y)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def mul(a,k): return (a[0]*k,a[1]*k)
def norm(a):
    l=math.hypot(*a) or 1;return (a[0]/l,a[1]/l)
def dirv(theta_deg):
    t=math.radians(theta_deg);return (-math.sin(t),math.cos(t))   # 0deg = straight down (SVG y down); +deg tilts to -x
def smooth(pts,closed=True,jit=0.0,seed=1):
    rnd=random.Random(seed)
    P=[(x+rnd.uniform(-jit,jit),y+rnd.uniform(-jit,jit)) for x,y in pts]
    n=len(P)
    d=f"M{P[0][0]:.1f} {P[0][1]:.1f} "
    rng=range(n) if closed else range(n-1)
    for i in rng:
        p0=P[(i-1)%n] if (closed or i>0) else P[i]
        p1=P[i];p2=P[(i+1)%n]
        p3=P[(i+2)%n] if (closed or i+2<n) else P[(i+1)%n]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6)
        c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f"C {c1[0]:.1f} {c1[1]:.1f}, {c2[0]:.1f} {c2[1]:.1f}, {p2[0]:.1f} {p2[1]:.1f} "
    return d+("Z" if closed else "")
INK="var(--txt)";PAPER="var(--node)";PAPER2="var(--node2)"
def ink(d,w=1.5,fill=None,op=1,extra=""):
    f=fill if fill else "none"
    return f'<path d="{d}" fill="{f}" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}" {extra}/>'
def hatch_lines(segs,w=0.9,op=0.65):
    d="".join(f"M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f} " for a,b in segs)
    return f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/>'
FING=[  # name, base, a0, deltas, lens, widths, seed
 ("pinky",(-40,102),22,[12,18],[30,22,18],[16,14,12],11),
 ("ring",(-15,115),10,[10,18],[40,30,23],[19,17,14],12),
 ("middle",(14,120),0,[-8,16],[46,34,25],[20,18,15],13),
 ("index",(42,112),-14,[-12,14],[40,30,23],[19,17,14],14),
 ("thumb",(52,70),-62,[-4,-14],[34,32,26],[24,20,16],15)]
def finger(f):
    name,base,a0,dl,lens,wd,seed=f
    th=[a0,a0+dl[0],a0+dl[0]+dl[1]]
    P=[base]
    for i in range(3): P.append(add(P[-1],mul(dirv(th[i]),lens[i])))
    dirs=[dirv(t) for t in th]
    nodedir=[dirs[0],norm(add(dirs[0],dirs[1])),norm(add(dirs[1],dirs[2])),dirs[2]]
    widths=[wd[0],(wd[0]+wd[1])/2,(wd[1]+wd[2])/2,wd[2]*0.8]
    nrm=lambda d:(d[1],-d[0])   # right-hand normal
    left=[];right=[]
    for p,d,w in zip(P,nodedir,widths):
        n=nrm(d);left.append(add(p,mul(n,-w/2)));right.append(add(p,mul(n,w/2)))
    tip=P[3];d3=dirs[2];n3=nrm(d3);w3=widths[3]
    cap=[add(add(tip,mul(n3,-w3/2*math.cos(a))),mul(d3,w3/2*math.sin(a)+2)) for a in (math.pi*0.3,math.pi*0.5,math.pi*0.7)]
    poly=left+[cap[0],cap[1],cap[2]][::-1]+right[::-1]
    # arrange: left side (base->tip), cap (left->right), right side (tip->base)
    capL=[add(add(tip,mul(n3,-w3/2*math.cos(a))),mul(d3,w3/2*math.sin(a)+2)) for a in (0.25*math.pi,0.5*math.pi,0.75*math.pi)]
    poly=left+capL+right[::-1]
    out=[]
    d=smooth(poly,True,0.5,seed)
    out.append(ink(d,1.7,PAPER))
    out.append(ink(smooth(poly,True,0.7,seed+50),0.8,None,0.35))
    segs=[]
    for i in range(3):
        a=P[i];b=P[i+1];L=lens[i];n=nrm(dirs[i]);w=(widths[i]+widths[i+1])/2
        steps=max(3,int(L/2.9))
        for s in range(steps):
            t=(s+0.5)/steps;c=add(a,mul(sub(b,a),t))
            e1=add(c,mul(n,w/2-0.6));e2=add(add(c,mul(n,-w*0.12)),mul(dirs[i],3))
            segs.append((e1,e2))
    out.append(hatch_lines(segs,1.0,0.75))
    for i in (1,2):
        p=P[i];n=nrm(nodedir[i]);w=widths[i]
        a=add(p,mul(n,-w*0.36));b=add(p,mul(n,w*0.36));c=add(p,mul(nodedir[i],2))
        out.append(f'<path d="M{a[0]:.1f} {a[1]:.1f} Q{c[0]:.1f} {c[1]:.1f} {b[0]:.1f} {b[1]:.1f}" fill="none" stroke="{INK}" stroke-width="1.1" opacity="0.8"/>')
    # nail
    c=add(P[2],mul(dirs[2],lens[2]*0.52));rx=wd[2]*0.3;ry=lens[2]*0.3
    ang=th[2]
    pts=[]
    for k in range(10):
        a=2*math.pi*k/10;x=rx*math.cos(a);y=ry*math.sin(a)
        rx2=x*math.cos(math.radians(-ang))-y*math.sin(math.radians(-ang));ry2=x*math.sin(math.radians(-ang))+y*math.cos(math.radians(-ang))
        pts.append((c[0]+rx2,c[1]+ry2))
    out.append(ink(smooth(pts,True,0.25,seed+7),1.1,PAPER2))
    # knot at tip
    kt=add(tip,mul(d3,2))
    out.append(f'<circle cx="{kt[0]:.1f}" cy="{kt[1]:.1f}" r="2.6" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>')
    out.append(f'<path d="M{kt[0]:.1f} {kt[1]:.1f} l-3 5 M{kt[0]:.1f} {kt[1]:.1f} l3.5 4.5" stroke="{INK}" stroke-width="1" fill="none" stroke-linecap="round"/>')
    return "".join(out),kt,(P,lens)
def palm():
    pts=[(-30,-4),(-44,36),(-52,76),(-48,104),(-22,120),(14,125),(46,116),(58,92),(54,56),(38,22),(30,-4)]
    d=smooth(pts,True,0.6,3)
    out=[ink(d,1.9,PAPER),ink(smooth(pts,True,0.8,33),0.8,None,0.35)]
    segs=[]
    for y in range(6,112,3):
        xl=-30-(14*min(1,y/40))-(8*min(1,max(0,(y-40)/36)))
        segs.append(((xl+0.5,y),(xl+14,y+7)))
    for x in range(-30,54,3):
        yb=104+ (math.sin((x+30)/84*math.pi))*16
        segs.append(((x,yb-0.5),(x+6,yb-9)))
    out.append(hatch_lines(segs,1.0,0.7))
    out.append(ink('M40 40 C 52 52, 58 70, 54 88 C 46 80, 40 66, 40 40 Z',1.2,None,0.7))
    out.append(hatch_lines([((44+i*1.2,48+i*3.2),(50+i*1.2,52+i*3.2)) for i in range(10)],0.9,0.6))
    for kx,ky,dx in [(-12,112,-8),(14,118,-2),(38,110,6)]:
        out.append(f'<path d="M{kx} {ky} C {kx+dx} {ky-34}, {kx+dx*1.5} {ky-62}, {kx+dx*2} {ky-92}" fill="none" stroke="{INK}" stroke-width="1" opacity="0.7"/>')
    return "".join(out)
def hand(rot_deg=0):
    parts=[];tips=[]
    for f in FING:
        s,kt,_=finger(f);parts.append((f[0],s));tips.append((f[0],kt))
    order={"pinky":0,"ring":1,"middle":2,"index":3,"thumb":4}
    # draw thumb first (behind palm), then palm, then other fingers? fingers emerge from under palm bottom edge -> draw fingers, then palm
    body="".join(s for n,s in parts if n=="thumb")+"".join(s for n,s in parts if n!="thumb")+palm()
    return body,tips
def rotp(p,deg,origin=(0,0)):
    a=math.radians(deg);x,y=p[0]-origin[0],p[1]-origin[1]
    return (origin[0]+x*math.cos(a)-y*math.sin(a),origin[1]+x*math.sin(a)+y*math.cos(a))
def arm():
    # forearm from the slit (top, y=-70) to wrist (0,0); local frame with wrist at origin, pointing down
    L=[(-40,-72),(-38,-36),(-33,-6)];R=[(40,-72),(38,-36),(33,-6)]
    pts=[L[0],L[1],L[2],(-30,10),(0,14),(30,10),R[2],R[1],R[0]]
    d=smooth(pts,False,0.5,9)+" "
    outline=f"M{L[0][0]} {L[0][1]} C {L[1][0]-3} {L[1][1]}, {L[2][0]-1} {L[2][1]-14}, {L[2][0]} {L[2][1]+6} L {R[2][0]} {R[2][1]+6} C {R[2][0]+1} {R[2][1]-14}, {R[1][0]+3} {R[1][1]}, {R[0][0]} {R[0][1]} Z"
    out=[ink(outline,1.9,PAPER)]
    segs=[((-40+i*0.5,y),(-40+10+i*0.5,y+6)) for i,y in enumerate(range(-70,-6,4))]
    out.append(hatch_lines(segs,0.9,0.55))
    # cuff band
    out.append(f'<path d="M-35 -22 C -12 -17, 12 -17, 35 -22 M-34 -12 C -12 -7, 12 -7, 34 -12" fill="none" stroke="{INK}" stroke-width="1.4"/>')
    out.append(hatch_lines([((-35+i*3.5,-20+ (i%2)),(-35+i*3.5+4,-13)) for i in range(0,17)],0.8,0.5))
    return "".join(out)
