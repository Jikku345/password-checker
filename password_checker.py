import re

def check_password_strength(password):
    """Check the strength of a given password."""
    strength = 0
    remarks = ""

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Check if contains numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks += "Password should contain at least one number.\n"

    # Check if contains uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one uppercase letter.\n"

    # Check if contains lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one lowercase letter.\n"

    # Check if contains special character
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks += "Password should contain at least one special character (@, $, !, %, *, ?, &).\n"

    # Final evaluation
    if strength == 5:
        return "Strong Password ✅"
    elif strength >= 3:
        return f"Moderate Password ⚠️\n{remarks}"
    else:
        return f"Weak Password ❌\n{remarks}"

# Taking user input
password = input("Enter your password: ")
print(check_password_strength(password))
