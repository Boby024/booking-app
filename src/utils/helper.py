from datetime import datetime, timezone
import random
import string


def get_dt_utcnow():
    return datetime.now(timezone.utc) # datetime.now(datetime.timezone.utc)


def generate_verification_code(length=10):
    """
    Generates a random alphanumeric verification code.

    Args:
        length (int): The length of the verification code. Default is 6.

    Returns:
        str: The generated verification code.
    """
    # Choose from uppercase letters and digits
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(characters, k=length))
    return code

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
