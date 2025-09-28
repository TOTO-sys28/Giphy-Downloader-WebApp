const getGifBtn = document.getElementById('get-gif-btn');
const giphyUrlInput = document.getElementById('giphy-url');
const gifContainer = document.getElementById('gif-container');
const downloadBtn = document.getElementById('download-btn');
const loader = document.querySelector('.loader');

getGifBtn.addEventListener('click', async () => {
    const query = giphyUrlInput.value.trim();
    if (!query) {
        alert('Please enter a search term.');
        return;
    }

    // Reset UI
    gifContainer.innerHTML = ''; // Clear previous GIF or message
    loader.style.display = 'block';
    downloadBtn.style.display = 'none';
    gifContainer.appendChild(loader);

    try {
        const response = await fetch(`/api/get-gif?query=${encodeURIComponent(query)}`);
        const data = await response.json();

        loader.style.display = 'none'; // Hide loader

        if (data.error) {
            gifContainer.innerHTML = `<p style="color: var(--accent-color);">${data.error}</p>`;
            return;
        }

        const gifUrl = data.gif_url;
        const img = document.createElement('img');
        img.src = gifUrl;
        img.alt = "Giphy GIF";
        gifContainer.appendChild(img);

        downloadBtn.setAttribute('data-url', gifUrl);
        downloadBtn.style.display = 'inline-block'; // Show download button

    } catch (error) {
        console.error('Error fetching GIF:', error);
        loader.style.display = 'none'; // Hide loader
        gifContainer.innerHTML = '<p style="color: var(--accent-color);">Failed to fetch GIF. Please try again.</p>';
    }
});

downloadBtn.addEventListener('click', async (event) => {
    event.preventDefault();
    const url = event.target.getAttribute('data-url');
    if (!url) return;

    // Show loading state on button
    const originalText = event.target.textContent;
    event.target.textContent = 'Downloading...';

    try {
        const response = await fetch(url);
        const blob = await response.blob();
        const objectUrl = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = objectUrl;
        a.download = 'giphy.gif';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        URL.revokeObjectURL(objectUrl);
    } catch (error) {
        console.error('Download failed:', error);
        alert('Failed to download GIF.');
    } finally {
        // Restore button text
        event.target.textContent = originalText;
    }
});