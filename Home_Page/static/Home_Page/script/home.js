function leftscroll1() {
  const container = document.querySelector('#container-body-1');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: -scrollAmount, // Scroll to the left by 5 cards
      behavior: 'smooth'
  });

}

function rightscroll1() {
  const container = document.querySelector('#container-body-1');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: scrollAmount, // Scroll to the right by 5 cards
      behavior: 'smooth'
  });
}

function leftscroll2() {
  const container = document.querySelector('#container-body-2');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: -scrollAmount, // Scroll to the left by 5 cards
      behavior: 'smooth'
  });
}

function rightscroll2() {
  const container = document.querySelector('#container-body-2');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: scrollAmount, // Scroll to the right by 5 cards
      behavior: 'smooth'
  });
}

function leftscroll3() {
  const container = document.querySelector('#container-body-3');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: -scrollAmount, // Scroll to the left by 5 cards
      behavior: 'smooth'
  });
}

function rightscroll3() {
  const container = document.querySelector('#container-body-3');
  const cardWidth = document.querySelector('.card-box').offsetWidth; // Get width of one card
  const scrollAmount = window.innerWidth < 800 ? cardWidth * 1 : cardWidth * 5;
  container.scrollBy({
      left: scrollAmount, // Scroll to the right by 5 cards
      behavior: 'smooth'
  });
}


// to clear session when clicked log out
document.querySelector(".logout").addEventListener('click',()=>{
  fetch('logout/')
  .then(response => {
    if(!response.ok){
      throw new Error("Some error occured while logging out!");
    }
    console.log(response.json())
  })
  .catch(Error =>{
    console.log("Error : ",Error)
  });
})



// To add book in future reads list
const plus_spans = document.querySelectorAll(".plus-span");
plus_spans.forEach(plus_span => plusSpanFun(plus_span));

// To remove book from future reads list
document.querySelectorAll('.cross-span').forEach(cross_span => cross_span_fun(cross_span))


function plusSpanFun(plus_span){
  plus_span.addEventListener('click',()=>{
    const book_id = plus_span.getAttribute("data-id") - 1;
    fetch(`add_to_frl/?q=${book_id}`)
    .then(response => {
      if (!response.ok){
        throw new Error('failed to add book');
      }
      return response.json();
    })
    .then(data => {
      const outercontainer = document.getElementById('container-body-3');
      const pmdiv = document.createElement('div')
      pmdiv.className = "pm-div";
      pmdiv.setAttribute("data-id-div",`${parseInt(data.book_detail.book_id) + 1}`)

      const pmdivspan = document.createElement('span');
      const pmdivspan_classlist = pmdivspan.classList;
      pmdivspan_classlist.add("linear_span")
      pmdivspan_classlist.add("cross-span")
      pmdivspan.setAttribute("data-id",`${parseInt(data.book_detail.book_id) + 1}`)
      // console.log(pmdivspan);
      cross_span_fun(pmdivspan);
  
      pmdivspan.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 32 32" viewBox="0 0 32 32" id="cross"><path d="M31.5,2.42828c0-0.51752-0.20148-1.00427-0.56763-1.36987c-0.73224-0.73224-2.00751-0.73224-2.73975,0L16,13.25104L3.80737,1.05841c-0.73224-0.73224-2.00751-0.73224-2.73975,0C0.70154,1.42401,0.5,1.91077,0.5,2.42828c0,0.51746,0.20154,1.00421,0.56763,1.36987l12.19263,12.19263L1.06763,28.18341C0.70154,28.54901,0.5,29.03577,0.5,29.55328c0,0.51746,0.20154,1.00421,0.56763,1.36987c0.73224,0.73224,2.00751,0.73224,2.73975,0L16,18.73053l12.19263,12.19263c0.36615,0.36609,0.85242,0.56763,1.36987,0.56763c0.51752,0,1.00378-0.20154,1.36987-0.56763C31.29852,30.5575,31.5,30.07074,31.5,29.55328c0-0.51752-0.20148-1.00427-0.56763-1.36987L18.73975,15.99078L30.93237,3.79816C31.29852,3.4325,31.5,2.94574,31.5,2.42828z" fill="#595bd4" class="color000000 svgShape"></path></svg>'

      const bookancor = document.createElement('a');
      const bookElement = document.createElement('div');
      bookElement.className = 'card-box';
      bookElement.innerHTML = `
          <img src="${data.book_detail.book_coverurl}" alt="${data.book_detail.book_title}" loading="lazy">
      `;
      bookancor.appendChild(bookElement)
      bookancor.setAttribute('href',`/book/${parseInt(data.book_detail.book_id) + 1}`)
      pmdiv.appendChild(bookancor)
      pmdiv.appendChild(pmdivspan)
      outercontainer.appendChild(pmdiv);
    })
    .catch(error => {
      console.log("Error : ",error)
    });

    // console.log("added")
  })
}


function cross_span_fun(cross_span){
  cross_span.addEventListener('click',()=>{
    const book_id = cross_span.getAttribute("data-id") - 1;
    fetch(`remove_from_frl/?q=${book_id}`)
    .then(response => {
      if (!response.ok){
        throw new Error("Book was unable to be removed");
      }
      return response.json()
    })
    .then(data => {
      const bid = parseInt(data.book_detail.book_id) + 1
      // console.log(bid);
      const to_rmv_book = document.querySelector(`[data-id-div = "${bid}"]`)
      console.log(to_rmv_book)
      to_rmv_book.remove()
    })
    .catch(error =>{
      console.log("Error : ",error)
    });
  })
}