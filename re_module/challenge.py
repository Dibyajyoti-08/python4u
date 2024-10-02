'''
Write a Python function that checks if a string is a 
valid email address using regular expressions.
'''

from re import match

def email_verify(mail_id):
    pattern = r'^[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$'
    match_value = match(pattern, mail_id)
    if match_value:
        print(f"The email - {mail_id} is valid")
    else:
        print(f"The email - {mail_id} is not valid ")
    
if __name__ == '__main__':
    email_verify("test@gmail.com")