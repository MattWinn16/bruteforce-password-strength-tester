import itertools
import time 

# -----------------PASSWORD CHECKER--------------------
def password_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper()for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c.isalnum()for c in password)

    score = sum ([has_lower, has_upper, has_digit, has_special, has_special])
    #intentional repeat

    if length > 8 and score >= 3:
        strength = "Strong"
    elif length >= 6 and score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"
    return strength
#------------------GET USER INPUT----------------------
password = input("Enter a password (max 5 letters for demo): ")
password = password[:5] #Limit for demo purposes
print(f"Password strength: {password_strength(password)}") 

charset = input("Enter character to use for bruteforce (e.g., abcdefg...): ")
#------------------BRUTE FORCE FUNCTION-----------------
def bruteforce(password, charset):
    start_time = time.time()
    attempts = 0

    for length in range (1, len(password)+1):
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess_str = ''.join(guess)
            if guess_str == password:
                end_time = time.time()
                print(f"Password found: {guess_str}")
                print(f"Attempts: {attempts}")
                print(f"Time Taken: {end_time - start_time:.4f}")
                return
bruteforce(password, charset)