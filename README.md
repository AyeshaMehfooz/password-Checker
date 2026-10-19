# password-Checker
# Password Strength Checker

A simple Python utility function designed to validate the strength of a password against standard industry complexity rules. It provides descriptive feedback explaining exactly why a password fails validation, helping users create more secure credentials.

## Features

The function tests input strings against five individual complexity requirements:
*   **Minimum Length:** Verifies the password is at least 8 characters long.
*   **Uppercase Letters:** Ensures at least one uppercase letter (`A-Z`) is included.
*   **Lowercase Letters:** Ensures at least one lowercase letter (`a-z`) is included.
*   **Numeric Digits:** Requires at least one numeric digit (`0-9`).
*   **Special Characters:** Checks for at least one special symbol from the following supported set:
    `!@#$%^&*()-_=+[]{}|;:\,.<>?/~`

## Code snippet

```python
def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    
    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    
    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    
    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:\,.<>?/~"
    if not any(char in special_characters for char in password):
        return "Weak: Password must contain at least one special character."
    
    return "Strong: Your password is strong."
```

## How It Works

The function executes top-to-bottom and uses **early exit returns**. It stops checking at the very first rule violation it encounters. If the password satisfies all five criteria, the function concludes by returning a validation success message.

## Quick Start & Usage

Copy the function into your Python script and pass a string to it. Below is an example of how to implement it interactively:

```python
# Save the function into a file named password_utils.py

# Example execution:
test_passwords = [
    "short",          # Fails length
    "nouppercase1!",  # Fails uppercase
    "NOLOWERCASE1!",  # Fails lowercase
    "NoDigits!",      # Fails digits
    "NoSpecial123",   # Fails special character
    "SecUr1ty!2026"   # Passes all criteria
]

for pwd in test_passwords:
    result = check_password_strength(pwd)
    print(f"Password: {pwd:<15} -> Result: {result}")
```
