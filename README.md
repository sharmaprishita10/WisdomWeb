# WisdomWeb

WisdomWeb is a web-based project designed to create a Wikipedia-like online encyclopedia that allows users to view, search, create, and edit encyclopedia entries.

### Description

This project is an online encyclopedia where each entry is stored as a Markdown file. Users can navigate between entry pages, create new entries, edit existing ones, search for entries, and access a random entry. The content written in Markdown is converted to HTML for display, making it easier to write and manage entries.

### Getting Started

1. Run python manage.py runserver to start the Django development server.
2. Visit http://127.0.0.1:8000/ in your web browser to use the encyclopedia.

### Specification

#### Index Page

- The index page lists all encyclopedia entries.
- Each entry name links to its respective entry page.

#### Entry Page

- A page displaying the entry's content.
- If the entry does not exist, an error page is shown.

#### Search

- Users can search for entries using a query.
- If the query matches an entry title, users are redirected to that entry page.
- If the query is a substring of any entry titles, a list of matching entries is displayed.

#### New Page

- Users can create new entries by entering a title and Markdown content.

#### Edit Page

- Users can edit existing entries.

#### Additional Feature

- **Random Page**: Users can access a random encyclopedia entry by clicking the "Random Page" link.

### CSS and Design

The design is minimalistic and user-friendly, ensuring a clean and intuitive user interface.

### About

This project was developed to demonstrate proficiency in web development using Django and Markdown to create a functional and user-friendly online encyclopedia.

### Video Demo

You can view a video showcasing the project on [YouTube](https://www.youtube.com/watch?v=1-uYDiCR_tw).
