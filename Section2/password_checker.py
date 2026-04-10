import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one number")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character")

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, suggestions


# ---- Main Program ----
password = input("Enter your password: ")

score, strength, suggestions = check_password_strength(password)

print("\nPassword Strength Report")
print("------------------------")
print(f"Score: {score}/5")
print(f"Strength: {strength}")

if suggestions:
    print("\nRecommendations:")
    for s in suggestions:
        print(f"- {s}")
else:
    print("\nExcellent! Your password is strong.")
