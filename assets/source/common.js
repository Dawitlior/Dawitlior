const W=800,H=300;
function rng(s){return function(){s|=0;s=s+0x6D2B79F5|0;let t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
const renderer=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});
renderer.setSize(W,H);renderer.setPixelRatio(1);renderer.setClearColor(0x070b14,1);
document.getElementById('wrap').insertBefore(renderer.domElement,document.getElementById('wrap').firstChild);
const scene=new THREE.Scene();
const cam=new THREE.PerspectiveCamera(38,W/H,0.1,100);
function mkTex(){const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d');const gr=g.createRadialGradient(32,32,0,32,32,32);gr.addColorStop(0,'rgba(255,255,255,1)');gr.addColorStop(0.25,'rgba(255,255,255,0.55)');gr.addColorStop(1,'rgba(255,255,255,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);return new THREE.CanvasTexture(c)}
const sprite=mkTex();
const ss=(a,b,x)=>{const t=Math.min(1,Math.max(0,(x-a)/(b-a)));return t*t*(3-2*t)};
const tmpV=new THREE.Vector3();
function glow(color,size){const s=new THREE.Sprite(new THREE.SpriteMaterial({map:sprite,color:new THREE.Color(color),transparent:true,blending:THREE.AdditiveBlending,depthWrite:false}));s.scale.set(size,size,1);scene.add(s);return s}
function place(el,v,dx=0,dy=0){tmpV.copy(v).project(cam);el.style.left=((tmpV.x+1)/2*W+dx)+'px';el.style.top=((1-tmpV.y)/2*H+dy)+'px'}
