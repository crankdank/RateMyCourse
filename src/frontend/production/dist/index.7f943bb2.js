function getValueOrPlaceholderSelector(selector) {
    let el = document.querySelector(selector);
    return el.value === "" ? el.placeholder : el.value;
}
document.querySelector("p.search").addEventListener("click", async (e)=>{
    let subject = getValueOrPlaceholderSelector("#csub").toUpperCase();
    let number = getValueOrPlaceholderSelector("#cnum").toUpperCase(); // CHECK THAT COURSE EXISTS AND THAT BOTH BOXES HAVE A VALUE
    try {
        let ret = await (await fetch(`http://localhost:8000/subject/${subject}/number/${number}`)).json();
        if (ret.length !== 1) {
            swal({
                title: "Error!",
                text: "We couldn't find that course! Make sure you filled in both fields correctly.",
                icon: "error"
            });
            return;
        }
        let para = new URLSearchParams();
        para.append("subj", subject);
        para.append("num", number);
        window.open("/details.html?" + para.toString(), "_self");
    } catch (e1) {
        swal({
            title: "Error!",
            text: "Couldn't communicate with the server.",
            icon: "error"
        });
    }
});

//# sourceMappingURL=index.7f943bb2.js.map
