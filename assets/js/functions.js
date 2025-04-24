// Scroll
if (document.getElementById("site-nav")) {
  window.onscroll = function () {
    scrollFunction();
  };
}

function scrollFunction() {
  if (document.body.scrollTop > 24 || document.documentElement.scrollTop > 24) {
    document.getElementById("site-nav").classList.add("bg-primary");
  } else {
    document.getElementById("site-nav").classList.remove("bg-primary");
  }
}

// Countdowns

function countdownCalc(deadline, cityName) {
  var now = new Date().getTime();
  var t = deadline - now;
  var days = Math.floor(t / (1000 * 60 * 60 * 24));
  var hours = Math.floor((t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
  document.getElementById(`${cityName}-day`).innerHTML = days;
  document.getElementById(`${cityName}-hour`).innerHTML = hours;
  document.getElementById(`${cityName}-minute`).innerHTML = minutes;

  if (t < 0) {
    clearInterval(x);
    document.getElementById(`countdown-clock-${cityName}`).innerHTML = "Ready!";
    document.getElementById(`${cityName}-day`).innerHTML = "0";
    document.getElementById(`${cityName}-hour`).innerHTML = "0";
    document.getElementById(`${cityName}-minute`).innerHTML = "0";
  }
}

var deadline2025 = new Date("Aug 19, 2025 09:00:00").getTime();

if (document.getElementById("countdown-clock-2025")) {
  countdownCalc(deadline2025, "2025");
  var x = setInterval(() => countdownCalc(deadline2025, "2025"), 60000);
}
