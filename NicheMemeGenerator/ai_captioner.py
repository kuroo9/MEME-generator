# ai_captioner.py
import random
import os

class AICaptioner:
    def __init__(self, niche_phrases_file="niche_phrases.txt"):
        self.phrases = []
        if os.path.exists(niche_phrases_file):
            with open(niche_phrases_file, 'r', encoding='utf-8') as f:
                self.phrases = [line.strip() for line in f if line.strip()]
            print(f"Loaded {len(self.phrases)} niche phrases.")
        else:
            print(f"Warning: Niche phrases file '{niche_phrases_file}' not found. Caption suggestions will be generic.")
            # Fallback generic phrases
            self.phrases = [
                "Such a great day", "Is this real life?", "When you realize...",
                "Just another Tuesday", "This is fine.", "What a twist!",
                "Wait, what?", "It really do be like that sometimes."
            ]

    def suggest_caption(self, part="any"): # part can be "top", "bottom", "any"
        if not self.phrases:
            return "No phrases loaded."
        return random.choice(self.phrases)

    # Placeholder for more advanced AI in the future
    def generate_caption_with_ai(self, image_context=""):
        # This would involve a pre-trained or fine-tuned text generation model
        # For demonstration, we'll just suggest a random one.
        print("Using advanced AI (placeholder for now)...")
        return self.suggest_caption()

# If you want to test it
if __name__ == "__main__":
    # Create a dummy niche_phrases.txt for testing
    with open("niche_phrases.txt", "w", encoding="utf-8") as f:
        f.write("Rock and Stone!\n")
        f.write("Did I hear a Rock and Stone?\n")
        f.write("For Karl!\n")
        f.write("We're rich!\n")
        f.write("Mushroom!\n")

    captioner = AICaptioner()
    print(f"Suggested top caption: {captioner.suggest_caption('top')}")
    print(f"Suggested bottom caption: {captioner.suggest_caption('bottom')}")
    print(f"AI Generated caption: {captioner.generate_caption_with_ai('drg_mission_fail.jpg')}")