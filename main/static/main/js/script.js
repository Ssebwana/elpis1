document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");

    if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", function () {
            navMenu.classList.toggle("show");
        });
    }

   document.addEventListener("DOMContentLoaded", function () {
    const faqQuestions = document.querySelectorAll(".faq-question");

    faqQuestions.forEach(function (question) {
        question.addEventListener("click", function () {
            const faqItem = this.closest(".faq-item");
            if (faqItem) {
                faqItem.classList.toggle("active");
            }
        });
    });
});
});