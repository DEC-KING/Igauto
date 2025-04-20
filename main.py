
import requests

def create_instagram_account(email, password):
    # Simulated placeholder for account creation logic
    print(f"Creating account with {email}:{password}")
    return {"status": "success", "username": email.split("@")[0]}

if __name__ == "__main__":
    email = input("Enter temp mail: ")
    password = input("Enter password: ")
    result = create_instagram_account(email, password)
    print("Result:", result)
