const plus_spans = document.querySelectorAll('.plus-span')
plus_spans.forEach(plus_span => plus_span.addEventListener('click',()=>{
    const book_id = plus_span.getAttribute("data-id");
    fetch(`add_to_frl/?q=${parseInt(book_id)-1}`)
    .then(response => {
        if(!response.ok){
            throw new Error("Book was not added!"); 
        }
        console.log("added");
    })
    .catch(Error => console.log("Error : ",Error));
}))

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