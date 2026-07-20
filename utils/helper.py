import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)

def print_menu(title, options):
    print_header(title)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print("-" * 60)

def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if not value and required:
            print("Input cannot be empty. Please try again.")

def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt, min_value=0, max_value=100):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value < min_value or value > max_value:
                print(f"Value must be between {min_value} and {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_menu_choice(num_options):
    return get_int_input("Enter your choice: ", min_value=1, max_value=num_options)

def parse_score(score_str):
    scores = {}
    if not scores_str:
        return scores
    for pair in scores_str.split(","):
        if ":" in pair:
            subject, value = pair.split(":", 1)
            try:
                scores[subject.strip()] = float(value.strip())
            except ValueError:
                continue  # Skip invalid score values
    return scores