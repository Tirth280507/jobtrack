const stages=["Saved","Applied","Screening","Interview","Offer","Rejected"];
const seed=[
{id:1,company:"Siemens",role:"Product Analyst",location:"Berlin · Hybrid",salary:"€55k–€70k",status:"Interview",date:"2026-09-29",url:"https://www.siemens.com",nextAction:"Prepare interview questions"},
{id:2,company:"Zalando",role:"Data Analyst",location:"Berlin",salary:"€50k–€65k",status:"Screening",date:"2026-10-01",url:"https://jobs.zalando.com",nextAction:"Reply to recruiter"},
{id:3,company:"Celonis",role:"Business Analyst",location:"Munich",salary:"€55k–€72k",status:"Applied",date:"2026-10-02",url:"https://www.celonis.com",nextAction:"Follow up Friday"},
{id:4,company:"SAP",role:"Junior Product Manager",location:"Walldorf · Hybrid",salary:"€52k–€68k",status:"Applied",date:"2026-09-27",url:"https://www.sap.com",nextAction:"Check application status"},
{id:5,company:"Delivery Hero",role:"Strategy Intern",location:"Berlin",salary:"€18–€22/hr",status:"Saved",date:"2026-10-03",url:"https://www.deliveryhero.com",nextAction:"Tailor CV"}];
let apps=JSON.parse(localStorage.getItem("jobtrack-apps")||"null")||seed;
const $=s=>document.querySelector(s); const esc=s=>String(s||"").replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function save(){localStorage.setItem("jobtrack-apps",JSON.stringify(apps));render()}
function show(view){document.querySelectorAll(".view").forEach(x=>x.classList.add("hidden"));$("#"+view+"View").classList.remove("hidden");document.querySelectorAll(".nav-item").forEach(x=>x.classList.toggle("active",x.dataset.view===view));$("#pageTitle").textContent=view[0].toUpperCase()+view.slice(1);render()}
function counts(){return Object.fromEntries(stages.map(s=>[s,apps.filter(a=>a.status===s).length]))}
function render(){
 const c=counts(), active=apps.filter(a=>a.status!=="Rejected").length, responses=apps.filter(a=>["Screening","Interview","Offer","Rejected"].includes(a.status)).length;
 $("#activeStat").textContent=active;$("#interviewStat").textContent=c.Screening+c.Interview;$("#offerStat").textContent=c.Offer;$("#responseStat").textContent=apps.length?Math.round(responses/apps.length*100)+"%":"0%";$("#weeklyCount").textContent=apps.filter(a=>a.date>="2026-10-01").length;
 $("#pipeline").innerHTML=stages.map(s=>'<div class="stage"><b>'+c[s]+'</b><span>'+s+"</span></div>").join("");
 $("#nextActions").innerHTML=apps.slice().sort((a,b)=>a.date.localeCompare(b.date)).slice(0,4).map(a=>'<div class="action"><b>'+esc(a.company)+" · "+esc(a.role)+'</b><small>'+esc(a.nextAction||"No next action")+"</small></div>").join("")||"<p>No actions yet.</p>";
 $("#recentList").innerHTML=apps.slice().reverse().slice(0,5).map(a=>'<div class="app-row"><div><b>'+esc(a.company)+" · "+esc(a.role)+'</b><small>'+esc(a.location)+'</small></div><span class="badge">'+esc(a.status)+"</span></div>").join("");
 const q=($("#searchInput")?.value||"").toLowerCase(), f=$("#statusFilter")?.value||"all", filtered=apps.filter(a=>(f==="all"||a.status===f)&&((a.company+" "+a.role).toLowerCase().includes(q)));
 $("#resultCount").textContent=filtered.length+" applications";
 $("#kanban").innerHTML=stages.map(s=>'<div class="column"><h4>'+s+" · "+filtered.filter(a=>a.status===s).length+"</h4>"+filtered.filter(a=>a.status===s).map(a=>'<div class="card"><b>'+esc(a.company)+'</b><p>'+esc(a.role)+'</p><p>'+esc(a.location)+'</p><select data-id="'+a.id+'">'+stages.map(x=>'<option '+(x===a.status?"selected":"")+">"+x+"</option>").join("")+"</select></div>").join("")+"</div>").join("");
 $("#insightApps").textContent=apps.length; const top=stages.slice().sort((a,b)=>c[b]-c[a])[0]; $("#insightStage").textContent=c[top]?top:"—"; $("#insightFollow").textContent=apps.filter(a=>a.nextAction).length; $("#insightHealth").textContent=apps.length>=5?"Active":"Building";
 $("#insightHeadline").textContent=apps.length>=5?"Your pipeline has enough signal to prioritize follow-ups.":"Start by adding a few applications."; $("#insightCopy").textContent=apps.length>=5?"Focus on the stages with the most momentum, and keep a concrete next action on every active application.":"Once you have activity in the pipeline, JobTrack will surface simple patterns to help you decide where to focus next.";
 $("#insightActions").innerHTML=apps.filter(a=>a.nextAction).map(a=>'<div class="action"><b>'+esc(a.company)+" · "+esc(a.role)+'</b><small>'+esc(a.nextAction)+"</small></div>").join("");
}
document.addEventListener("click",e=>{const v=e.target.dataset.view||e.target.dataset.viewLink;if(v)show(v);if(e.target.id==="addTop")$("#modal").showModal();if(e.target.id==="cancelModal")$("#modal").close();if(e.target.id==="resetDemo"){apps=seed;save()}});
document.addEventListener("change",e=>{if(e.target.matches(".card select")){const a=apps.find(x=>x.id==e.target.dataset.id);if(a){a.status=e.target.value;save()}}});
$("#searchInput")?.addEventListener("input",render);$("#statusFilter")?.addEventListener("change",render);
$("#applicationForm").addEventListener("submit",e=>{e.preventDefault();const f=new FormData(e.target);apps.push({id:Date.now(),company:f.get("company"),role:f.get("role"),location:f.get("location"),salary:f.get("salary"),status:f.get("status"),date:f.get("date")||new Date().toISOString().slice(0,10),url:f.get("url"),nextAction:f.get("nextAction")});e.target.reset();$("#modal").close();save()});
render();