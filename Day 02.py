"""
🖤 Roxy V.0.1 🖤
A simple interactive Python program that checks your mood, energy, 
and available time, then gives a personalized workout suggestion.

Author: Arun Arun Roy
GitHub: https://github.com/arvinarun
"""

# Helper function for validated input
def get_choice(prompt, choices):
    choice = input(prompt).strip()
    while choice not in choices:
        print("❌ Invalid choice. Try again.")
        choice = input(prompt).strip()
    return choice

# Program starts here
print("🖤 Welcome to your Life & Mood Assistant 🖤")
name = input("What do I call you? ").strip()

running = True
while running:
    print(f"\n👋 Welcome back, {name}!")

    # Mood input
    mood = get_choice(
        "How is your mood today? (1) Happy 😊 (2) Sad 😔 (3) Excited 😆: ", 
        ["1", "2", "3"]
    )

    if mood == "1":
        mood_state = "Good"
        energy_prompt = "That's great to hear! How's your energy today? (1) High ⚡ (2) Moderate 🌤️ (3) Low 💤: "
    elif mood == "2":
        mood_state = "Bad"
        energy_prompt = "Tough days happen. But a workout can help! How's your energy? (1) High ⚡ (2) Moderate 🌤️ (3) Low 💤: "
    else:
        mood_state = "Good"
        energy_prompt = "Excitement is contagious! How's your energy today? (1) High ⚡ (2) Moderate 🌤️ (3) Low 💤: "

    energy = get_choice(energy_prompt, ["1", "2", "3"])
    energy_state = {"1": "High ⚡", "2": "Moderate 🌤️", "3": "Low 💤"}[energy]

    # Time / workout question
    time_prompt = f"You have {energy_state} energy. Do you have time for a workout today? (1) Yes 🏋️‍♂️ (2) No 🛋️: "
    time_choice = get_choice(time_prompt, ["1", "2"])
    time_state = "Yes 🏋️‍♂️" if time_choice == "1" else "No 🛋️"

    # 🏋️ Workout suggestion — now correctly inside the loop!
    if time_state.startswith("Yes"):
        if energy_state.startswith("High"):
            print(f"💪 Awesome, {name}! You have {energy_state} energy. Try a full workout today! 🏋️‍♂️")
        elif energy_state.startswith("Moderate"):
            print(f"🏃‍♂️ Nice, {name}! You have {energy_state} energy. Do a moderate workout or cardio session today.")
        else:
            print(f"🧘‍♀️ Take it easy, {name}. You have {energy_state} energy. Try stretching or yoga.")
    else:
        if energy_state.startswith("High"):
            print(f"💤 No workout today, {name}? Maybe do a short 5-min movement break to stay active.")
        elif energy_state.startswith("Moderate"):
            print(f"🛋️ It's okay, {name}. Light activity or a short walk could lift your mood.")
        else:
            print(f"🛌 Rest up, {name}. Focus on recovery and self-care today.")

    # Ask if they want to repeat
    again = get_choice("Do you want to answer again? (yes/no): ", ["yes", "no"])
    if again == "no":
        running = False

        print("🌟 Have a great day! Keep taking care of yourself!")
