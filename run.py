import random
from user import User, Credential
# from user import User

def create_user(user_name, password):
    new_user = User(user_name, password)
    return new_user

def save_user(user):
    User.save_user(user)

def verify_user(user_name, password):
    check_user = Credential.check_user(user_name, password)
    return check_user

def generate_password():
    new_password = Credential.generate_password()
    return new_password

def new_credential(user_name, site_name, account_name, password):
    my_credential = Credential(user_name, site_name, account_name, password)
    return my_credential


def save_credential(credential):
    Credential.save_credentials(credential)

def display_credentials(user_name):
    return Credential.display_credentials(user_name)




# def main():

#     while True:
#         user_list = []

     

#         print("Welcome to password locker!!!")
#         print('\n')
#         print("Select a short code to navigate through:to create new user use 'nu':To login to your account 'lg' or 'ex' to exit ")
#         short_code = input().lower()
#         print('\n')


#         if short_code == 'nu':
#             print("create username")
#             created_user_name = input()

#             print('create password')
#             created_user_password = input()

#             print('confirm password')
#             confirm_password = input()



#             while confirm_password != created_user_password:
#                 print('invalid password did not match')
#                 print('Enter your password')
#                 created_user_password =input()
#                 print('confirm your password')
#                 confirm_user_password = input()

#             else:
#                 print(f"Congratulation {created_user_name}! account creation successful")
#                 print('\n')
#                 print('Proceed to login')
#                 print('username')
#                 entered_user_name = input()
#                 print('Your password')
#                 entered_password = input()
#                 user_list.append(created_user_name)
#                 user_list.append(created_user_password)
#                 user_name = created_user_name
#                 password = created_user_password
#                 save_user(create_user(user_name, password))
#                 print(user_list)

#             while entered_user_name != created_user_name or entered_password != created_user_password:
#                 print('Invalid username or password')
#                 print("username")
#                 entered_user_name =input()
#                 print('Your password')
#                 entered_password = input()

#             else:
#                 print(f"welcome: {entered_user_name} to your account")
#                 print('\n')

#         elif short_code == 'lg':
#             print("~" * 120)
#             # print(' ')
#             print('To login, enter your account details:')
#             user_name = input('Enter your first name - ').strip()
#             password = str(input('Enter your password - '))
#             user_exists = verify_user(user_name, password)
#             if user_exists == user_name:
#                 print(" ")
#                 print(f'Welcome {user_name}. Please choose an action to continue.')
#                 print(' ')
#                 while True:
#                     print("-" * 60)
#                     print(
#                         'Input the following keywords to navigate: \n create-Create a Credential \n display-Display Credentials \n copy-Copy Password \n exit-Exit')
#                     short_code = input('Enter a choice: ').lower().strip()
#                     print("-" * 60)
#                     if short_code == 'exit':
#                         print(" ")
#                         print(f'Goodbye {user_name}')
#                         break
#                     elif short_code == 'create':
#                         print(' ')
#                         print('Enter your credential details:')
#                         site_name = input('Enter the site\'s name- ').strip()
#                         account_name = input('Enter your account\'s name - ').strip()
#                         while True:
#                             print(' ')
#                             print("-" * 60)
#                             print(
#                                 'Please choose an option for entering a password: \n existing-enter existing password \n generate-generate a password \n exit-exit')
#                             psw_choice = input('Enter an option: ').lower().strip()
#                             print("-" * 60)
#                             if psw_choice == 'existing':
#                                 print(" ")
#                                 password = input('Enter your password: ').strip()
#                                 break
#                             elif psw_choice == 'generate':
#                                 password = generate_password()
#                                 break
#                             elif psw_choice == 'exit':
#                                 break
#                             else:
#                                 print('Invalid option, Try again.')
#                         save_credential(new_credential(user_name, site_name, account_name, password))
#                         print(' ')
#                         print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')                           
#                         print(' ')
#                     elif short_code == 'display':
#                         print(' ')
#                         if display_credentials(user_name):
#                             print('My saved credentials')
#                             # print(' ')
#                             for credential in display_credentials(user_name):
#                                 print(
#                                     f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
#                             print(' ')
#                         else:
#                             # print(' ')
#                             print("No saved credentials found")
#                             print(' ')
#                     elif short_code == 'copy':
#                         print(' ')
#                         chosen_site = input('Enter the site name for the credential password to copy: ')
#                         copy_credential(chosen_site)
#                         print('')
#                     else:
#                         print('Invalid option, Try again.')

#             else:
#                 print(' ')
#                 print('Wrong details entered, try again with correct details or Create an Account.')

#         else:
#             print("-" * 60)
#             print(' ')
#             print('Incorrect password entered, Retry with correct password.')


# if __name__ == '__main__':
#     main() 







