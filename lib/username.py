import secrets
import math


def generate_random_username():
    """
    Create a random username
    """
    username = secrets.token_urlsafe(math.floor(32 / 1.3))
    return username

