import string
import secrets

def generate_password(length=8):
    # Allowed character set: A-Z, a-z, 0-9, symbols
    charset = string.ascii_letters + string.digits
    
    # Generate secure random password
    password = ''.join(secrets.choice(charset) for _ in range(length))
    return password

# Example usage
print("Generated Password:", generate_password(8))
