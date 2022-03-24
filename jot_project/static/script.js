document.querySelectorAll(".accordion-button").forEach((button) => {
  button.addEventListener("click", () => {
    const accordionContent = button.nextElementSibling;

    button.classList.toggle("accordion-button-active");

    if (button.classList.contains("accordion-button-active")) {
      accordionContent.style.maxHeight = "81%";
      accordionContent.style.padding = "2%";
      accordionContent.style.fontSize = "2vw";
    } else {
      accordionContent.style.maxHeight = 0;
      accordionContent.style.padding = "0";
      accordionContent.style.fontSize = "0px";
    }
  });
});
