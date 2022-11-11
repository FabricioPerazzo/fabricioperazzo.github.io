const sections = document.querySelectorAll(".top-links a");

sections.forEach((section) => {
    section.addEventListener("click", (event) => {
        const href = this.getAttribute("href");
        document.querySelector(href).scrollIntoView({behavior: "smooth"});
    })
});