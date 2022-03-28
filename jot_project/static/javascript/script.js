//JavaScript
document.querySelectorAll(".accordion-button").forEach((button) => {
  button.addEventListener("click", () => {
    const accordionContent = button.nextElementSibling;

    button.classList.toggle("accordion-button-active");

    if (button.classList.contains("accordion-button-active")) {
      accordionContent.style.maxHeight = "81%";
      accordionContent.style.padding = "2%";
      accordionContent.style.fontSize = "1vw";
    } else {
      accordionContent.style.maxHeight = 0;
      accordionContent.style.padding = "0";
      accordionContent.style.fontSize = "0px";
    }
  });
});

//JQuery
$(document).ready(function () {
  var eT=0;
  $('.books-list li').hide().each(function (i) {
  $(this).delay(eT).fadeIn(1000);
  eT += 400; // Fade in speed
  });
  
  $('.logo').hide().each(function () {
    $(this).fadeIn(2500);
  });

  $('.h3-subtitle-block').hide().each(function (i) {
    $(this).delay(eT).fadeIn(2500);
  });

  $('.main-paragraph').hide().each(function (i) {
    $(this).delay(eT).fadeIn(2500);
  });

  $('.svg-inline--fa').hide().each(function (i) {
    $(this).delay(eT).fadeIn(2500);
  })

});

//AJAX