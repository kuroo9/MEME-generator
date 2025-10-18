⛏️ AI-Powered Niche Meme Generator (The Deep Dive)

🌟 Project Overview

This project is a Python-based utility that automates the entire lifecycle of niche visual content creation: from scraping image templates from specialized community sites to generating meme captions using AI/NLP and overlaying them onto the images.

The goal is to rapidly create topical, community-specific memes that require minimal manual input, perfectly tailored for platforms like niche subreddits or Discord channels.

Key Features

Niche Template Scraper (scraper.py): Downloads image templates from specified community websites (e.g., fan wikis, image galleries).

Intelligent Caption Suggestions (ai_captioner.py): Uses a dictionary of niche phrases and NLP techniques to suggest relevant, context-aware captions.

Image Overlayer (meme_generator.py): Uses the Pillow library to expertly draw white text with black outlines (classic meme style) onto the image templates.

Simple Command Line Interface: Easy workflow for scraping, suggesting, and generating memes.

🖼️ Visual Demo

This section showcases the process and the final output.

Step 1: Template Scraping

Step 2: AI Captioning

Step 3: Final Output

<img src="./assets/screenshot_1_scraper_output.png" alt="Screenshot showing the console output of images being downloaded into the templates folder." width="300" />

<img src="./assets/screenshot_2_ai_suggestion.png" alt="Screenshot of the command line interface showing the AI suggesting 'Rock and Stone!' and 'Mushroom!'" width="300" />

<img src="./assets/screenshot_3_final_meme.png" alt="A final generated meme image with impact font text overlaid on a niche image template." width="300" />

🛠️ Getting Started

Follow these steps to get the project running on your local machine.

Prerequisites

You need Python 3.8+ installed. All dependencies are managed via pip.

Installation

Clone the Repository

git clone [https://github.com/your-username/NicheMemeGenerator.git](https://github.com/your-username/NicheMemeGenerator.git)
cd NicheMemeGenerator


Create and Activate Virtual Environment

# Create the environment
python -m venv venv 

# Activate (Windows)
.\venv\Scripts\activate
# Activate (macOS/Linux)
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


Install Meme Font (Recommended)
For optimal meme aesthetics, download a TTF font like Impact and save it in your project root as impact.ttf. If you skip this, the script will use a system default font.

🚀 Usage

The project is driven by the main.py script.

Step 1: Collect Niche Phrases (AI Data)

Edit the niche_phrases.txt file in the project root. Populate it with 50-100 phrases, dialogue snippets, or common jokes from your niche community. These phrases fuel the AI's caption suggestions.

Step 2: Scrape Templates

Run main.py and choose Option 3 to scrape:

python main.py
# Choose 3. Scrape more templates (if needed)
# Enter the URL of your niche image gallery to scrape (e.g., [https://example.com/gallery](https://example.com/gallery)):


The images will be saved to the ./templates directory.

Step 3: Generate Memes

Run main.py and choose Option 1 or 2:

Option 1 (AI Guided): Automatically selects a random template and uses phrases from niche_phrases.txt for the top and bottom captions, saving the image to ./generated_memes.

Option 2 (Custom): Allows you to select a specific template and type in your own custom captions before generating the image.

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

🗺️ Roadmap

[ ] Implement Topic Modeling (LDA/NLTK) to cluster scraped templates by visual theme.

[ ] Integrate a basic Flask web frontend for browser-based usage.

[ ] Add the ability to automatically adjust font size based on the length of the text to prevent overflow.
