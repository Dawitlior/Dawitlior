import {spawn} from 'node:child_process';
import fs from 'node:fs';
const dir=process.argv[2], frames=+process.argv[3], T=+process.argv[4], scene=process.argv[5]||'scene.html', out=process.argv[6]||'frames';
fs.mkdirSync(dir+'/'+out,{recursive:true});
const br=spawn('/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',['--headless=new','--remote-debugging-port=9333','--user-data-dir='+dir+'/prof_'+out,'--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--disable-gpu-sandbox','--hide-scrollbars','--window-size=800,300','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let ver; for(let i=0;i<60;i++){try{ver=await (await fetch('http://127.0.0.1:9333/json/version')).json();break}catch{await sleep(300)}}
const tabs=await (await fetch('http://127.0.0.1:9333/json')).json();
const page=tabs.find(t=>t.type==='page');
const ws=new WebSocket(page.webSocketDebuggerUrl);
await new Promise(r=>ws.onopen=r);
let id=0;const pend=new Map();
ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pend.has(m.id)){pend.get(m.id)(m);pend.delete(m.id)}};
const send=(method,params={})=>new Promise(r=>{const i=++id;pend.set(i,r);ws.send(JSON.stringify({id:i,method,params}))});
await send('Page.enable');await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride',{width:800,height:300,deviceScaleFactor:1,mobile:false});
await send('Page.navigate',{url:'file://'+dir+'/'+scene});
for(let i=0;i<80;i++){const r=await send('Runtime.evaluate',{expression:'window.ready===true',returnByValue:true});if(r.result?.result?.value)break;await sleep(250)}
const err=await send('Runtime.evaluate',{expression:'document.querySelector("canvas")?1:0',returnByValue:true});
console.log('canvas',err.result.result.value);
for(let f=0;f<frames;f++){
  const t=f/frames*T;
  await send('Runtime.evaluate',{expression:`renderAt(${t})`});
  const s=await send('Page.captureScreenshot',{format:'png'});
  fs.writeFileSync(`${dir}/${out}/f${String(f).padStart(3,'0')}.png`,Buffer.from(s.result.data,'base64'));
}
ws.close();br.kill();console.log('done',frames);
process.exit(0);
