import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    elif len(password) >= 5:
        score += 1
    else:
        feedback.append("Password is too short (minimum 5 characters recommended).")
    
    # Uppercase letters check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for better security.")
    
    # Lowercase letters check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for better security.")
    
    # Numbers check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include numbers for better security.")
    
    # Special characters check
    if re.search(r'[^A-Za-z0-9]', password):
        score += 2
    else:
        feedback.append("Consider adding special characters (!@#$%^&* etc.) for better security.")
    
    # Determine strength level
    if score >= 8:
        strength = "Very Strong"
    elif score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback
    }

def main():
    print("\nPassword Strength Checker")
    print("-------------------------")
    print("Enter a password to check its strength (or 'quit' to exit)\n")
    
    while True:
        password = input("Enter password: ").strip()
        
        if password.lower() == 'quit':
            print("\nExiting the program. Goodbye!\n")
            break
        
        if not password:
            print("Please enter a valid password.\n")
            continue
        
        result = check_password_strength(password)
        
        print("\nPassword Strength Analysis:")
        print(f"Strength: {result['strength']} ({result['score']}/8)")
        
        if result['feedback']:
            print("\nRecommendations to improve your password:")
            for item in result['feedback']:
                print(f"- {item}")
        else:
            print("\nYour password meets all recommended security criteria!")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()