# Login accounts
user_login_accounts = {
1: {"first name": "Jughead", "last name": "Jones", "email address": "jughead@riverdale.com", "password": "jughead_riverdale1"},
2: {"first name": "Archie", "last name": "Andrews", "email address": "archie@riverdale.com", "password": "archie_riverdale2"},
3: {"first name": "Veronica", "last name": "Lodge", "email address": "veronica@riverdale.com", "password": "veronica_riverdale3"},
4: {"first name": "Betty", "last name": "Cooper", "email address": "betty@riverdale.com", "password": "betty_riverdale4"},
5: {"first name": "Cheryl", "last name": "Blossom", "email address": "cheryl@riverdale.com", "password": "cheryl_riverdale5"},
}


# User login: ask for email address
user_email = input("Enter your email address: ")

# User login: ask for password
user_password = input("Enter your password: ")

# Identify first id_val
id_val = 1

# id_val has to be less than max length of dict. id's in order to go through the user_login_accounts
while int(id_val) < len(user_login_accounts):
  
# If so, look for id_val and account_info in user_login_account
    for id_val, account_info in user_login_accounts.items():

   
        # Check for valid email address and password
        if user_email == account_info["email address"] and user_password == account_info["password"]:
            print(user_email, "and", user_password, "are correct")
            print("Hello,", account_info["first name"], account_info["last name"], ". You have successfully logged in")
            break

    # Give an error if email or password is not correct
    else:
        print("Failed to login. Password", user_password, "or email address", user_email," is not correct. Try again.")
        break
    
         
    # Make sure to stop this loop after running one time
    break


        
