
// var inputField = document.querySelector('.search-bar input');
// var searchBar = document.querySelector('.search-bar');

// // Listen for input events on the search field
// inputField.addEventListener('input', function() {
//     if (inputField.value.trim() !== "") {
//         searchBar.classList.add('typing-active');
//     } else {
//         searchBar.classList.remove('typing-active');
//     }
// });

function getSuggestions(query) {
    const dropdown = document.getElementById('suggestions');
    const dropdownUL = document.getElementById('suggestions-ul');
    dropdownUL.innerHTML = '';

    if(query === ""){
        dropdown.style.display = 'none';
        return;
    }

    dropdownUL.innerHTML = '<li class="loading">Loading...</li>';
    dropdown.style.display = 'flex';

    fetch(`/search/search-suggestions/?q=${query}`)
        .then(response => (response.json()))
        .then(data=>{
            dropdownUL.innerHTML = '';
            // console.log(`data is ${data}`);
            if (data.length === 0){
                dropdown.style.display = 'none';
                return;
            }

            data.forEach(suggestion => {
                // console.log(suggestion)
                const li = document.createElement('li');
                li.innerHTML = suggestion;
                li.onclick = () => selectSuggestion(suggestion);
                dropdownUL.appendChild(li);
            });

            dropdown.style.display = 'flex';
        })
        .catch(error => {
            console.error("Error : ",error);
            dropdown.style.display = 'none';
        });
}

function selectSuggestion(suggestion){
    document.getElementById('search-input-field').value = suggestion;
    document.getElementById("suggestions").style.display = 'none';
    document.querySelector(".result-div").style.display = 'flex';
    document.querySelector(".search-query").innerHTML = suggestion;
    getResult(suggestion);
}

document.addEventListener('click',function(event){
    const dropdown = document.getElementById("suggestions");
    const searchcontainer = document.querySelector('.search-bar');
    if(!searchcontainer.contains(event.target)){
        dropdown.style.display = 'none';
    }
})


// Code for getting the results when clicked search button

document.getElementById("search-btn").addEventListener('click',() => {
    const search_value = document.getElementById('search-input-field').value
    document.querySelector(".result-div").style.display = 'flex';
    document.querySelector(".search-query").innerHTML = search_value;
    getResult(search_value);
});

document.querySelector(".search-bar").addEventListener("keypress",(event) => {
    if (event.key === 'Enter'){
        const search_value_ = document.getElementById('search-input-field').value
        // console.log(event);
        document.querySelector(".result-div").style.display = 'flex';
        document.querySelector(".search-query").innerHTML = search_value_;
        getResult(search_value_);
    }
})

function getResult(search_var){
    // document.querySelector(".result-div").style.display = 'flex';
    document.getElementById("suggestions").style.display = 'none';
    if(search_var === ""){
        return;
    }
    const resultContainer = document.querySelector(".result-cont");
    // console.log(search_var);
    
    fetch(`/search/search-result/?q=${search_var}`)
        .then(response => response.json())
        .then(data => {
            resultContainer.innerHTML = "";
            data.forEach(book => {
                // console.log(book)


                const pmdiv = document.createElement('div')
                pmdiv.className = "pm-div";

                const pmdivspan = document.createElement('span');
                pmdivspan.className = "plus-span";
                pmdivspan.setAttribute("data-id",`${parseInt(book[0]+1)}`);
                pmdivspan.addEventListener('click',() => {
                    fetch(`add_to_frl/?q=${book[0]}`)
                    .then(response => {
                        if (!response.ok){
                            throw new Error('failed to add book');
                        }
                        console.log("added")
                    })
                    .catch(error => console.log(error));
                })
            
                pmdivspan.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8" id="Plus"><path d="M3 0v3H0v2h3v3h2V5h3V3H5V0H3z" fill="#595bd4" class="color000000 svgShape"></path></svg>'
                
                const bookancor = document.createElement('a');
                const bookElement = document.createElement('div');
                bookElement.className = 'card-box';
                bookElement.innerHTML = `
                    <img src="${book[1]}" alt="${book[2]}" loading="lazy">
                `;
                bookancor.appendChild(bookElement)
                bookancor.setAttribute('href',`/book/${book[0]+1}`)
                pmdiv.appendChild(bookancor)
                pmdiv.appendChild(pmdivspan)
                resultContainer.appendChild(pmdiv);
                
            });
        })
        .catch(error => {
            console.error("Error : ",error);
        })
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