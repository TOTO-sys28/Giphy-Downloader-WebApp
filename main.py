import os
from flask import Flask, request, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup

# Create a Flask web server
app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    """Serve the index.html file."""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    """Serve static files (css, js)."""
    return send_from_directory('.', path)

@app.route('/api/get-gif')
def get_gif():
    """
    API endpoint to get a GIF from Giphy by scraping.
    Takes a 'query' parameter which can be a search term or a Giphy URL.
    """
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # If the query is already a direct GIF link, just return it
    if query.endswith('.gif'):
        return jsonify({'gif_url': query})

    try:
        if 'giphy.com/gifs/' in query:
            # If the query is a Giphy page URL, we fetch that page
            url = query
        else:
            # Otherwise, we perform a search
            url = f'https://giphy.com/search/{query.replace(" ", "-")}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://giphy.com/'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the GIF URL from the page's meta tags, which is more reliable
        gif_meta = soup.find('meta', property='og:image')
        
        if gif_meta and gif_meta.get('content'):
            gif_url = gif_meta['content']
            # some urls are for mp4, we need to convert them to gif
            if gif_url.endswith('.mp4'):
                gif_url = gif_url.replace('.mp4', '.gif')
            return jsonify({'gif_url': gif_url})
        else:
            # Fallback to searching for image tags if meta tag not found
            gif_img = soup.find('img', src=lambda s: s and 'giphy.com/media/' in s and s.endswith('.gif'))
            if gif_img and gif_img.get('src'):
                return jsonify({'gif_url': gif_img['src']})
            else:
                return jsonify({'error': 'Could not find a GIF for your query.'}), 404

    except requests.exceptions.RequestException as e:
        print(f"Error scraping Giphy: {e}")
        return jsonify({'error': 'Failed to scrape Giphy.'}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    # To run this application:
    # 1. Install the required libraries: pip install Flask requests beautifulsoup4
    # 2. Run this script: python main.py
    # 3. Open your web browser and go to http://127.0.0.1:5000
    app.run(debug=True)