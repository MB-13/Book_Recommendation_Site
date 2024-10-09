function leftscroll1() {
  const container = document.querySelector('.container-body-1');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: -scrollAmount, // Scroll to the left by 5 cards
      behavior: 'smooth'
  });
  console.log("hello");
}

function rightscroll1() {
  const container = document.querySelector('.container-body-1');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: scrollAmount, // Scroll to the right by 5 cards
      behavior: 'smooth'
  });
  console.log("hello");
}

function leftscroll2() {
  const container = document.querySelector('.container-body-2');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: -scrollAmount, // Scroll to the left by 5 cards
      behavior: 'smooth'
  });
  console.log("hello");
}

function rightscroll2() {
  const container = document.querySelector('.container-body-2');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: scrollAmount, // Scroll to the right by 5 cards
      behavior: 'smooth'
  });
  console.log("hello");
}