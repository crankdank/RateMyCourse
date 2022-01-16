function getValueOrPlaceholderSelector(selector) {
  let el = document.querySelector(selector);

  return el.value === "" ? el.placeholder : el.value;
}

document.querySelector("p.search").addEventListener("click", (e) => {
  let subject = getValueOrPlaceholderSelector("#csub").toUpperCase();
  let number = getValueOrPlaceholderSelector("#cnum").toUpperCase();

  // CHECK THAT COURSE EXISTS AND THAT BOTH BOXES HAVE A VALUE

  let para = new URLSearchParams();
  para.append("subj", subject);
  para.append("num", number);
  window.open("/details.html?" + para.toString(), "_self");
});
