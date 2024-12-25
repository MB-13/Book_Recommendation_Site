# 📚 Book Recommendation Site

Welcome to the **Book Recommendation Site** repository! This project is a full-stack web-based application developed using **Django**. It is designed to provide users with personalized book recommendations, embedding-based search capabilities, real-time search suggestions, and dynamic content loading. The application utilizes **SBERT** (Sentence-BERT) and the **SentenceTransformer** library for advanced natural language processing.

<p> <img src="demo/Screenshot (7).png" alt="Screenshot 1" style="width:50%; max-width:600px;"/> <img src="demo/Screenshot (8).png" alt="Screenshot 1" style="width:50%; max-width:600px;"/></p>

<p> <img src="demo/Screenshot (9).png" alt="Screenshot 1" style="width:50%; max-width:600px;"/> <img src="demo/Screenshot (10).png" alt="Screenshot 1" style="width:50%; max-width:600px;"/></p>


---

## ✨ Features

### 1. **Personalized Book Recommendations**
   - Recommends books based on the user's future reading list.
   - Dynamically adapts to user preferences to provide tailored suggestions.

### 2. **Embedding-Based Search**
   - Allows users to search for books using semantic similarity.
   - The search function retrieves books that are contextually similar to the query.

### 3. **Search Suggestions**
   - Provides real-time suggestions for queries based on user input.
   - Uses embeddings to suggest relevant and meaningful terms or titles.

### 4. **MyFutureRead**
   - Enables users to create and manage their future reading list for personalized recommendations.

### 5. **Bestseller and Most Reads**
   - Displays a curated list of bestselling books and the most-read books to help users discover popular titles.

### 6. **User Session Management**
   - Supports user authentication for saving preferences and managing sessions securely.

### 7. **Infinite Scroll**
   - Implements infinite scrolling for seamless browsing of book lists without page reloads.

### 8. **Database Creation through Web Scraping**
   - Data for books, authors, and reviews is scraped from Goodreads using **Beautiful Soup**.

### 9. **Developed with Django**
   - The website backend is powered by Django, ensuring scalability and maintainability.

---

## 🛠 Technologies Used

### Backend:
- **Python**
- **Django**
- **SBERT (Sentence-BERT)**
- **SentenceTransformer Library**

### Frontend:
- **HTML/CSS/JavaScript**

### Others:
- **Beautiful Soup** (for web scraping)
- **Embedding Models** (e.g., pre-trained BERT models)

---

## 🚀 Installation and Setup

### Prerequisites:
- Python 3.7+
- Pip (Python package manager)

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/MB-13/Book_Site.git
   cd Book_Site
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python manage.py runserver
   ```
   (Replace `manage.py` with the Django project management script.)

4. Access the site at:
   ```
   http://127.0.0.1:8000
   ```

---

## 💻 Usage

1. **Search for Books**: Use the search bar to find books by entering keywords or phrases. The system will return semantically similar results.
2. **Get Recommendations**: Add books to your future reading list to receive personalized recommendations.
3. **Explore Suggestions**: While typing in the search bar, view dynamic suggestions to refine your query.
4. **Discover Bestsellers and Most Reads**: Explore popular titles based on curated lists.
5. **Infinite Scroll**: Browse large lists of books without interruptions.
6. **User Management**: Log in to save preferences and manage your session effectively.

---

## 📁 Folder Structure

```
Book_Site/
|├── manage.py             # Django project management file
|├── templates/          # HTML templates for the frontend
|├── static/             # Static files (CSS, JS, images)
|├── books/              # Django app for managing book-related logic
|├── data/               # Book datasets and scraped data
|├── models/             # Pre-trained models and embeddings
|├── scraping/           # Scripts for web scraping Goodreads
|└── requirements.txt    # Python dependencies
```

---

## 🎥 Demo


<video controls style="width:100%; max-width:600px;">
  <source src="demo/Demo-video.mp4" type="video/mp4">
</video>

---

## 🔮 Future Enhancements

1. **Advanced Filtering**:
   - Enable filtering recommendations by genre, author, or publication year.
2. **Collaborative Recommendations**:
   - Incorporate collaborative filtering to enhance personalization.
3. **Improved UI/UX**:
   - Optimize the frontend for better user experience.
4. **Mobile Optimization**:
   - Ensure a seamless experience on mobile devices.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for improvements and new features.

### Steps to Contribute:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your branch.
4. Open a pull request.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments
- **SBERT (Sentence-BERT)** for powering the semantic search and recommendation engine.
- **SentenceTransformer Library** for its ease of integration and high-quality embeddings.
- **Beautiful Soup** for facilitating efficient web scraping of Goodreads data.

---

Happy Reading! :books:

