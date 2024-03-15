import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email)

def filter_valid_emails(emails):
    valid_emails = filter(lambda x: is_valid_email(x), emails)
    return sorted(valid_emails)
