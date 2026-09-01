"""
MEDAI - Medical Assistance Program
Educational CLI application for basic health information.

This project is for learning/demo purposes only. It does not diagnose
conditions, prescribe medicines, or replace professional medical advice.
"""


def get_int(prompt, minimum=None, maximum=None):
    """Read a validated integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a value >= {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Please enter a value <= {maximum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def show_symptom_guidance():
    """Provide general educational guidance without diagnosing or prescribing."""
    symptoms = {
        1: (
            "Headache",
            "Rest, drink water and reduce screen strain. Seek medical help for a "
            "sudden severe headache, confusion, weakness, fainting or vision loss."
        ),
        2: (
            "Stomach ache",
            "Rest and stay hydrated. Persistent, severe or worsening abdominal pain, "
            "repeated vomiting, blood in stool/vomit or fainting needs medical attention."
        ),
        3: (
            "Cold and cough",
            "Rest, fluids and monitoring may help with mild symptoms. Seek care for "
            "breathing difficulty, chest pain, dehydration or symptoms that worsen."
        ),
        4: (
            "Ear problem",
            "Avoid putting objects or drops into the ear unless advised by a clinician. "
            "Severe pain, discharge, injury or hearing loss should be assessed."
        ),
        5: (
            "Eye irritation/infection",
            "Avoid rubbing the eye and wash hands regularly. Eye pain, injury, light "
            "sensitivity or vision changes require prompt professional assessment."
        ),
        6: (
            "Pain",
            "Identify the cause rather than relying on self-medication. Severe, unexplained "
            "or persistent pain should be evaluated by a healthcare professional."
        ),
        7: (
            "Vomiting",
            "Take small sips of fluids if tolerated and monitor for dehydration. Repeated "
            "vomiting, blood, severe pain or inability to keep fluids down needs care."
        ),
        8: (
            "Chest pain",
            "Chest pain can be serious. If it is severe, new, persistent, or associated "
            "with breathing difficulty, sweating, fainting or pain spreading to the arm/jaw, "
            "seek emergency medical help immediately."
        ),
        9: (
            "Breathing problem",
            "Breathing difficulty can be an emergency. Severe or rapidly worsening breathing "
            "difficulty, blue lips, confusion or fainting requires emergency medical help."
        ),
        10: (
            "Fever",
            "Rest and maintain fluids while monitoring symptoms. Seek medical advice for "
            "very high or persistent fever, severe weakness, confusion, breathing difficulty "
            "or other concerning symptoms."
        ),
        11: (
            "Seasonal allergies",
            "Reduce exposure to known triggers and keep the environment clean. Swelling of "
            "the face/throat or difficulty breathing requires emergency medical help."
        ),
        12: (
            "Throat infection",
            "Warm fluids and rest may provide comfort. Severe swallowing difficulty, breathing "
            "problems, dehydration or worsening symptoms should be professionally assessed."
        ),
        13: (
            "Joint/body pain",
            "Rest the affected area and monitor the symptoms. Significant injury, swelling, "
            "weakness, numbness or persistent severe pain should be assessed by a clinician."
        ),
    }

    while True:
        print("\n--- Symptom Guidance ---")
        for key, (name, _) in symptoms.items():
            print(f"{key}. {name}")
        print("14. Back")

        choice = get_int("Choose a symptom: ", 1, 14)
        if choice == 14:
            return

        name, guidance = symptoms[choice]
        print(f"\n{name}")
        print("-" * len(name))
        print(guidance)
        print("\nNote: MEDAI provides general information only; it does not diagnose conditions.")


def show_first_aid():
    """Show concise first-aid education and emergency guidance."""
    first_aid = {
        1: ("Unresponsive person", "Call emergency services and follow dispatcher instructions. Begin CPR if trained and it is appropriate."),
        2: ("Bleeding", "Apply firm direct pressure with clean material. For severe bleeding, seek emergency medical help."),
        3: ("Choking", "If the person cannot cough, speak or breathe normally, use appropriate first-aid choking procedures and seek emergency help."),
        4: ("Burns", "Cool a minor burn with cool running water. Do not apply ice or break blisters. Seek care for serious burns."),
        5: ("Blisters", "Keep the area clean and protected. Avoid intentionally breaking a blister unless advised by a professional."),
        6: ("Sprains", "Rest and protect the injured area, and consider cold therapy for short periods. Seek care for severe pain or inability to use the limb."),
        7: ("Nosebleed", "Sit upright, lean slightly forward and pinch the soft part of the nose continuously. Seek care if bleeding is heavy or does not stop."),
        8: ("Bee/insect sting", "Move away from the source and monitor symptoms. Difficulty breathing or swelling of the face/throat is an emergency."),
        9: ("First-aid kit", "Useful basics include sterile gauze, adhesive bandages, antiseptic supplies, gloves, scissors and emergency contact information."),
    }

    while True:
        print("\n--- First Aid ---")
        for key, (name, _) in first_aid.items():
            print(f"{key}. {name}")
        print("10. Back")

        choice = get_int("Choose an option: ", 1, 10)
        if choice == 10:
            return

        name, guidance = first_aid[choice]
        print(f"\n{name}\n{'-' * len(name)}\n{guidance}")
        print("\nFor emergencies, contact local emergency medical services immediately.")


def bmi_calculator():
    """Calculate BMI as an educational health metric."""
    print("\n--- BMI Calculator ---")
    weight = get_int("Weight (kg): ", 1, 500)
    height_cm = get_int("Height (cm): ", 50, 250)
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight range"
    elif bmi < 25:
        category = "Healthy weight range"
    elif bmi < 30:
        category = "Overweight range"
    else:
        category = "Obesity range"

    print(f"\nBMI: {bmi:.1f}")
    print(f"Category: {category}")
    print("BMI is a general screening measure and should not be treated as a diagnosis.")


def medical_bot():
    """Collect basic user information and provide symptom guidance."""
    print("\n--- MEDAI Medical Assistance ---")
    name = input("Enter your name: ").strip() or "User"
    age = get_int("Enter your age: ", 0, 120)
    print(f"\nHello, {name}! (Age: {age})")
    print("Choose a topic to receive general educational information.")
    show_symptom_guidance()


def main():
    print("=" * 48)
    print("        MEDAI - MEDICAL ASSISTANCE")
    print("=" * 48)
    print("Educational/demo application - not medical advice.\n")

    while True:
        print("\n1. Medical symptom guidance")
        print("2. First aid information")
        print("3. BMI calculator")
        print("4. Exit")

        choice = get_int("Enter your choice: ", 1, 4)
        if choice == 1:
            medical_bot()
        elif choice == 2:
            show_first_aid()
        elif choice == 3:
            bmi_calculator()
        else:
            print("\nThank you for using MEDAI. Stay safe!")
            break


if __name__ == "__main__":
    main()
