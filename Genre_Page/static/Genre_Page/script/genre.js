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
                const bookancor = document.createElement('a');
                const bookElement = document.createElement('div');
                bookElement.className = 'card-box';
                bookElement.innerHTML = `
                    <img src="${book.Cover_url}" alt="${book.title}" loading="lazy">
                `;
                bookancor.appendChild(bookElement)
                bookancor.setAttribute('href',`/book/${book.id}`)
                booksContainer.appendChild(bookancor);
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




// const params = new URLSearchParams(window.location.search);
// // const genre = params.get('genre'); // e.g., ?genre=fiction

// let currentPage = 1; 
// const booksContainer = document.getElementById('gmrc');
// let loading = false; 

// function fetchBooks(page) {
//     if (loading) return; // Prevent duplicate fetch calls
//     loading = true;

//     const url = `/Genre/${genre}?page=${page}`;

//     console.log(`Fetching books from: ${url}`); // Debugging log

//     fetch(url, {
//         headers: {
//             'X-Requested-With': 'XMLHttpRequest' // Specify this as an AJAX request
//         }
//     })
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log(`Received ${data.books.length} books`); // Debugging log
//             if (data.books.length === 0) {
//                 window.removeEventListener('scroll', handleScroll);
//                 return;
//             }
//             data.books.forEach(book => {
//                 const bookElement = document.createElement('div');
//                 bookElement.className = 'card-box';
//                 bookElement.innerHTML = `
//                     <img src="${book.Cover_url}" alt="${book.title}" loading="lazy">
//                 `;
//                 booksContainer.appendChild(bookElement);
//             });
//             adjustScrollPosition(); // Adjust scroll after loading new books
//             currentPage++; 
//         })
//         .catch(error => {
//             console.error('Error fetching books:', error);
//             booksContainer.innerHTML = '<p>Failed to load books. Please try again later.</p>';
//         })
//         .finally(() => {
//             loading = false; 
//         });
// }

// function adjustScrollPosition() {
//     const lastBook = booksContainer.lastElementChild; // Get the last book element

//     if (lastBook) {
//         const lastBookRect = lastBook.getBoundingClientRect(); // Get position of the last book
//         const windowHeight = window.innerHeight; // Get the window height

//         // Check if the last book is above the bottom of the viewport
//         if (lastBookRect.bottom < windowHeight) {
//             // Scroll to the bottom of the books container
//             lastBook.scrollIntoView({ behavior: 'smooth', block: 'end' });
//         }
//     }
// }

// function handleScroll() {
//     if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200 && !loading) {
//         console.log('Near bottom, loading more books...'); // Debugging log
//         fetchBooks(currentPage);
//     }
// }

// window.onload = () => {
//     fetchBooks(currentPage); 
//     window.addEventListener('scroll', handleScroll); 
// };

