from dataclasses import dataclass, field
from typing import Optional, List
import os
from typing import List, Dict, Any

import time
import hashlib
import hmac
import base64
import secrets
import os
import hashlib
import binascii
from .jwt import encode, decode
from .hash import *

def generate_mfa_code(username):
    """
    Generates a Multi-Factor Authentication (MFA) code for a user.

    Args:
        username (str): The username for which to generate the MFA code.

    Returns:
        str: The generated 6-digit MFA code.
    """
    mfa_codes = {}
    code = str(secrets.randbelow(1000000)).zfill(6)  # Generate a 6-digit code
    mfa_codes[username] = {'code': code, 'expiry': time.time() + 300}  # Code expires in 5 minutes

    return code

def hash_pass(password):
    """Hash a password for storing."""

    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash)  # return bytes


def create_token(identity):
        """
        Creates an authentication token for a user.

        Args:
            username (str): The username for which to create the token.

        Returns:
            str: The generated authentication token.
        """
        token = base64.b64encode(secrets.token_bytes(32)).decode()
        return encode({'identity': identity, 'exp': time.time() + 3600}, token)

def create_refresh_token(identity):
    """
    Creates a refresh token for a user.

    Args:
        username (str): The username for which to create the refresh token.

    Returns:
        str: The generated refresh token.
    """
    refresh_token = base64.b64encode(secrets.token_bytes(32)).decode()
    return encode({'identity': identity, 'exp': time.time() + 3600}, refresh_token)


def hash_password(password):
        """
        Hashes a password using SHA-256.

        Args:
            password (str): The plain text password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain_password, hashed_password):
    """
    Verifies a plain text password against a hashed password.

    Args:
        plain_password (str): The plain text password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return hash_password(plain_password) == hashed_password

def create_session(device_id:str, username:str, secret_key:str):
    """
    Creates a session for a user.

    Args:
        username (str): The username for which to create the session.

    Returns:
        str: The generated session ID.
    """
    # session_id = base64.b64encode(secrets.token_bytes(32)).decode()
    session = {
        'device_id': device_id,
        'username': username,
        'expiry': time.time() + 3600
    }
    return hashlib.sha256(session).hexdigest()


