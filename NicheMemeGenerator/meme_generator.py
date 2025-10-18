# meme_generator.py
from PIL import Image, ImageDraw, ImageFont
import os

def create_meme(template_path, top_text="", bottom_text="", font_path="arial.ttf", output_dir="generated_memes"):
    try:
        img = Image.open(template_path).convert("RGB") # Ensure RGB for consistent saving
    except FileNotFoundError:
        print(f"Error: Template not found at {template_path}")
        return None
    except Exception as e:
        print(f"Error opening image {template_path}: {e}")
        return None

    draw = ImageDraw.Draw(img)
    img_width, img_height = img.size

    # --- FONT & TEXT SETTINGS ---
    # You might need to adjust font_path for your OS or download one.
    # Example for macOS: "arial.ttf" might be available, or download a TTF font.
    # For a more robust solution, bundle a font with your project.
    try:
        font = ImageFont.truetype(font_path, int(img_height * 0.08)) # Adjust font size dynamically
    except IOError:
        print(f"Warning: Font '{font_path}' not found. Using default Pillow font.")
        font = ImageFont.load_default()
        # If default font is too small, you can manually set a smaller point size
        # font = ImageFont.truetype("arial.ttf", 20) # Fallback to a fixed size if possible

    # Helper function to draw text with outline
    def draw_text_with_outline(draw_obj, text, position, font, fill_color, outline_color=(0,0,0)):
        x, y = position
        # Draw outline (adjust offset for thickness)
        for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
             draw_obj.text((x+dx, y+dy), text, font=font, fill=outline_color)
        draw_obj.text(position, text, font=font, fill=fill_color)

    # Calculate text position (centered)
    def get_text_position(text, font, img_dim, offset_factor, is_top=True):
        text_width, text_height = draw.textbbox((0,0), text, font=font)[2:] # get width/height from bounding box
        x = (img_dim[0] - text_width) / 2
        y = img_dim[1] * offset_factor if is_top else img_dim[1] * (1 - offset_factor) - text_height
        return (x, y)

    if top_text:
        top_text_pos = get_text_position(top_text, font, img.size, 0.05, is_top=True)
        draw_text_with_outline(draw, top_text, top_text_pos, font, fill_color=(255,255,255)) # White text

    if bottom_text:
        bottom_text_pos = get_text_position(bottom_text, font, img.size, 0.05, is_top=False)
        draw_text_with_outline(draw, bottom_text, bottom_text_pos, font, fill_color=(255,255,255)) # White text

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.basename(template_path).split('.')[0] + "_meme.jpg"
    output_path = os.path.join(output_dir, output_filename)
    img.save(output_path)
    print(f"Generated meme saved to: {output_path}")
    return output_path

# ... (imports and functions remain the same) ...

if __name__ == "__main__":
    from ai_captioner import AICaptioner # Import it here

    font_path = "impact.ttf" # Or your chosen font

    captioner = AICaptioner() # Initialize the AI captioner

    template_files = [f for f in os.listdir("templates") if f.endswith(('.jpg', '.png'))]
    if template_files:
        selected_template = random.choice(template_files) # Choose a random template
        first_template = os.path.join("templates", selected_template)
        print(f"Using template: {first_template}")

        # Get AI suggestions
        suggested_top = captioner.suggest_caption("top")
        suggested_bottom = captioner.suggest_caption("bottom")

        print(f"\nAI Suggested Top Caption: \"{suggested_top}\"")
        print(f"AI Suggested Bottom Caption: \"{suggested_bottom}\"")

        # Option 1: Use AI suggestions directly
        create_meme(
            template_path=first_template,
            top_text=suggested_top,
            bottom_text=suggested_bottom
        )

        # Option 2: Prompt user for input (optional, uncomment to enable)
        # user_top_text = input(f"Enter top text (or leave blank for '{suggested_top}'): ") or suggested_top
        # user_bottom_text = input(f"Enter bottom text (or leave blank for '{suggested_bottom}'): ") or suggested_bottom
        # create_meme(
        #     template_path=first_template,
        #     top_text=user_top_text,
        #     bottom_text=user_bottom_text
        # )
        # 
    else:
        print("No templates found in 'templates' directory. Run scraper.py first!")