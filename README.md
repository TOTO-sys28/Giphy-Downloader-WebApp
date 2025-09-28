# Giphy-Downloader-WebApp
A simple and beautifully designed web application that allows you to search for and download GIFs from Giphy.com without needing an API key. Built with Python, Flask, and vanilla JavaScript.

- **API-Free**: Scrapes Giphy.com directly, so no API key is needed.
- **Search or URL**: Find GIFs by entering a search term or pasting a Giphy URL.
- **Modern UI**: A clean, responsive, dark-mode interface.
- **Direct Download**: Download GIFs to your computer with a single click.
- **Loading Indicators**: A smooth loading spinner provides feedback while fetching GIFs.

## Technologies Used

- **Frontend**:
  - HTML5
  - CSS3 (with Google Fonts)
  - Vanilla JavaScript
- **Backend**:
  - Python
  - Flask (for the web server)
  - Requests (for making HTTP requests)
  - BeautifulSoup4 (for web scraping)

## Setup and Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.x installed on your system.
- `pip` for installing Python packages.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/TOTO-sys28/Giphy-Downloader-WebApp.git
    cd Giphy-Downloader-WebApp
    ```

2.  **Install the required Python packages:**
    ```sh
    pip install Flask requests beautifulsoup4
    ```

## How to Run

1.  **Run the Flask server:**
    ```sh
    python main.py
    ```

2.  **Open the application in your browser:**
    Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```
. GiphyDownloader/
├── main.py             # Flask backend server
├── index.html          # Main HTML file
├── style.css           # CSS for styling
├── script.js           # JavaScript for application logic
├── task.txt            # User-provided tasks
├── project_plan.txt    # Development progress tracker
└── github_setup.txt    # This file
```

## How It Works

The application uses a Python Flask backend to serve a simple HTML, CSS, and JavaScript frontend. When a user enters a search query, the frontend sends a request to the backend. The backend then scrapes the Giphy website for the relevant GIF, extracts the image URL, and sends it back to the frontend to be displayed.
```
