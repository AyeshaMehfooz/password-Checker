#function to check password strength
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
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if not any(char in special_characters for char in password):
        return "Weak: Password must contain at least one special character."
    
    return "Strong: Your password is strong."
