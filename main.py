import json
import os
from datetime import datetime

# Load tips and quotes from JSON file
def load_data():
    with open("tips.json", "r") as f:
        return json.load(f)

def save_output(content):
    with open("output.txt", "a") as f:
        f.write(content + "\n")

def generate_study_tips(data):
    print("\n📚 Here are your Study Tips:")
    tips = data["study_tips"]
    output = "--- Study Tips ---\n"
    for i, tip in enumerate(tips, 1):
        line = f"  {i}. {tip}"
        print(line)
        output += line + "\n"
    save_output(output)

def generate_motivation_quote(data):
    import random
    print("\n💡 Motivation Quote for You:")
    quote = random.choice(data["motivation_quotes"])
    output = f"--- Motivation Quote ---\n  \"{quote}\"\n"
    print(f'  "{quote}"')
    save_output(output)

def display_datetime():
    now = datetime.now()
    formatted = now.strftime("%A, %d %B %Y — %I:%M:%S %p")
    print(f"\n🕐 Current Date & Time:\n  {formatted}")
    save_output(f"--- Date & Time ---\n  {formatted}\n")

def main():
    print("=" * 45)
    print("   🎓 Smart Student Assistant 🎓")
    print("=" * 45)

    name = input("\nHello! What's your name? ").strip()
    print(f"\nWelcome, {name}! Let's get you sorted. 🚀")
    save_output(f"Session started by: {name} on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")

    data = load_data()

    while True:
        print("\n--- Main Menu ---")
        print("  1. Generate Study Tips")
        print("  2. Get a Motivation Quote")
        print("  3. Display Current Date & Time")
        print("  4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            generate_study_tips(data)
        elif choice == "2":
            generate_motivation_quote(data)
        elif choice == "3":
            display_datetime()
        elif choice == "4":
            print(f"\nGoodbye, {name}! Keep grinding! 💪\n")
            save_output("Session ended.\n" + "="*40 + "\n")
            break
        else:
            print("  ❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
