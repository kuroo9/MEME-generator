# main.py
import os
import random
from scraper import scrape_images
from meme_generator import create_meme
from ai_captioner import AICaptioner

def main():
    print("Welcome to the Niche Meme Generator!")
    print("-" * 30)

    # Ensure directories exist
    os.makedirs("templates", exist_ok=True)
    os.makedirs("generated_memes", exist_ok=True)

    # --- Step 1: Ensure templates are available ---
    template_files = [f for f in os.listdir("templates") if f.endswith(('.jpg', '.png'))]
    if not template_files:
        print("No image templates found. Let's try to scrape some!")
        target_url = input("Enter the URL of your niche image gallery to scrape (e.g., https://example.com/gallery): ")
        if target_url:
            scrape_images(target_url)
            template_files = [f for f in os.listdir("templates") if f.endswith(('.jpg', '.png'))]
            if not template_files:
                print("Scraping failed or no images found. Please check URL and scraper settings.")
                return
        else:
            print("No URL provided. Cannot proceed without templates.")
            return

    # Initialize AI Captioner
    captioner = AICaptioner()
    font_path = "impact.ttf" # Or your downloaded font

    while True:
        print("\n--- Meme Generation Menu ---")
        print("1. Generate a random meme with AI captions")
        print("2. Generate a meme with custom captions")
        print("3. Scrape more templates (if needed)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            selected_template_name = random.choice(template_files)
            selected_template_path = os.path.join("templates", selected_template_name)

            suggested_top = captioner.suggest_caption("top")
            suggested_bottom = captioner.suggest_caption("bottom")

            print(f"Using template: {selected_template_name}")
            print(f"AI Suggested Top: '{suggested_top}'")
            print(f"AI Suggested Bottom: '{suggested_bottom}'")

            create_meme(selected_template_path, suggested_top, suggested_bottom, font_path)
            # 
        elif choice == '2':
            print("Available templates:")
            for i, template in enumerate(template_files):
                print(f"{i+1}. {template}")
            try:
                template_idx = int(input("Enter the number of the template to use: ")) - 1
                if 0 <= template_idx < len(template_files):
                    selected_template_name = template_files[template_idx]
                    selected_template_path = os.path.join("templates", selected_template_name)

                    top_text = input("Enter top text: ")
                    bottom_text = input("Enter bottom text: ")

                    create_meme(selected_template_path, top_text, bottom_text, font_path)
                    # 
                else:
                    print("Invalid template number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            target_url = input("Enter the URL of your niche image gallery to scrape: ")
            if target_url:
                scrape_images(target_url)
                template_files = [f for f in os.listdir("templates") if f.endswith(('.jpg', '.png'))]
                print("Templates updated.")
            else:
                print("No URL provided.")
        elif choice == '4':
            print("Exiting. Rock and Stone!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()