# scraper.py
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin # Helps handle relative image URLs

def scrape_images(base_url, output_dir="templates"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Scraping images from: {base_url}")
    try:
        response = requests.get(base_url)
        response.raise_for_status() # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # --- CUSTOMIZE THIS SECTION BASED ON YOUR TARGET WEBSITE ---
        # Example: Find all <img> tags within a specific div or with a certain class
        # This is a generic example. You'll need to adjust selectors.
        images = soup.find_all('img', {'class': 'my-image-class'}) # Or 'src' attribute, or parent div
        if not images:
            print("No images found with the specified criteria. Check your selectors!")
            # Fallback: try finding all images and filter later
            images = soup.find_all('img')
        # -----------------------------------------------------------

        for img_tag in images:
            img_url = img_tag.get('src')
            if img_url and (img_url.endswith('.jpg') or img_url.endswith('.png')):
                # Handle relative URLs
                full_img_url = urljoin(base_url, img_url)
                img_name = os.path.basename(full_img_url)
                img_path = os.path.join(output_dir, img_name)

                try:
                    img_data = requests.get(full_img_url).content
                    with open(img_path, 'wb') as handler:
                        handler.write(img_data)
                    print(f"Downloaded: {img_name}")
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading {full_img_url}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {base_url}: {e}")
    print("Scraping complete.")


if __name__ == "__main__":
    # --- REPLACE WITH YOUR NICHE WEBSITE'S URL ---
    target_url = "https://imgflip.com/"
    scrape_images(target_url)