async function populate(){const e=new URLSearchParams(new URL(window.location.href).search);e.get("subj"),e.get("num");let t={faculty:"Science",subject:"CMPUT",course_num:"401",average_overall:4.5,average_workload:3.1,average_interest:4.5,average_usefulness:5,average_difficulty:2,assignedProfs:"TBA",hasLab:!1};const r={type:"doughnut",data:{datasets:[{data:[t.average_overall,5-t.average_overall],backgroundColor:["rgb(39, 93, 56)","rgba(255, 255, 255, 0)"],hoverOffset:4}]},options:{plugins:{tooltip:{enabled:!1}},events:[],cutout:"65%"}};new Chart(document.getElementById("doughnutChart"),r);document.querySelector("p.back").addEventListener("click",(e=>{window.open("/","_self")})),document.querySelector("#title").innerHTML=`${t.subject} ${t.course_num}`,document.querySelector("#fac").innerHTML=`Faculty of ${t.faculty}`,document.querySelector("#overallRating").innerHTML=`${t.average_overall.toFixed(1)}`,document.querySelector("#diff").innerHTML=`${t.average_difficulty.toFixed(1)}`,document.querySelector("#use").innerHTML=`${t.average_usefulness.toFixed(1)}`,document.querySelector("#work").innerHTML=`${t.average_workload.toFixed(1)}`,document.querySelector("#interest").innerHTML=`${t.average_interest.toFixed(1)}`}populate();
//# sourceMappingURL=details.78f21c2b.js.map
