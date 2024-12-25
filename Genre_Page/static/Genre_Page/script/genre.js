// Correctly extract the genre from the current URL path.
const pathArray = window.location.pathname.split('/').filter(Boolean);
// console.log(pathArray);
const genreIndex = pathArray.indexOf("Genre") + 1; // Find the index after "Genre"
const genre = pathArray[genreIndex];

if (!genre) {
    console.error("Genre is not defined. Please check the URL structure.");
} else {
    let currentPage = 1;
    const booksContainer = document.getElementById('gmrc');
    const loadingIndicator = document.getElementById('loading');
    // const bookurlspan = document.getElementById('spanforbookurl');
    // book_detail_url = bookurlspan.getAttribute('data-url');
    // console.log(book_detail_url);
    let loading = false;

    function fetchBooks(page) {
        if (loading) return;
        loading = true;
        loadingIndicator.style.display = 'block';

        const url = `/Genre/${genre}?page=${page}`;

        fetch(url, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            loadingIndicator.style.display = 'none';
            if (data.books.length === 0) {
                window.removeEventListener('scroll', handleScroll);
                return;
            }
            data.books.forEach(book => {

                const pmdiv = document.createElement('div');
                const pmdivspan = document.createElement('span');
                pmdivspan.className = 'plus-span';
                pmdivspan.setAttribute("data-id",`${book.id}`);
                pmdivspan.addEventListener('click',()=>{
                    fetch(`add-to-frl/?q=${parseInt(book.id)-1}`)
                    .then(response => {
                        if(!response.ok){
                            throw new Error("Book Not Added");
                        }
                        console.log("addedq");
                    })
                    .catch(Error => console.log("Error : ",Error));
                })
            
                pmdiv.className = 'pm-div';
                pmdivspan.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8" id="Plus"><path d="M3 0v3H0v2h3v3h2V5h3V3H5V0H3z" fill="#595bd4" class="color000000 svgShape"></path></svg>'

                const bookancor = document.createElement('a');
                const bookElement = document.createElement('div');
                bookElement.className = 'card-box';
                bookElement.innerHTML = `
                    <img src="${book.Cover_url}" alt="${book.title}" loading="lazy">
                `;
                bookancor.appendChild(bookElement)
                bookancor.setAttribute('href',`/book/${book.id}`)
                pmdiv.appendChild(bookancor)
                pmdiv.appendChild(pmdivspan)
                booksContainer.appendChild(pmdiv);
                
            });
            currentPage++;
        })
        .catch(error => {
            console.error('Error fetching books:', error);
            loadingIndicator.innerHTML = 'Failed to load books. Please try again later.';
        })
        .finally(() => {
            loading = false;
        });
    }

    function handleScroll() {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200 && !loading) {
            fetchBooks(currentPage);
        }
    }

    window.onload = () => {
        fetchBooks(currentPage);
        window.addEventListener('scroll', handleScroll);
    };
}

function adjustScrollPosition() {
    const booksContainer = document.getElementById('gmrc');
    const lastBook = booksContainer.lastElementChild; // Get the last book element

    if (lastBook) {
        const lastBookRect = lastBook.getBoundingClientRect(); // Get position of the last book
        const windowHeight = window.innerHeight; // Get the window height

        // Check if the last book is above the bottom of the viewport
        if (lastBookRect.bottom < windowHeight) {
            // Scroll to the bottom of the books container
            booksContainer.scrollIntoView({ behavior: 'smooth', block: 'end' });
        }
    }
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
