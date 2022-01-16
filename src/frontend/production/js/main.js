document.querySelector("p.search").addEventListener("click", (e) => {
  let para = new URLSearchParams();
  para.append("courseID", "VALUE");
  window.open("/details.html?" + para.toString(), "_self");
});
