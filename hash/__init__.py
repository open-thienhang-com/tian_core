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
from .jwt import encode, decode, decode_no_verify

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


def create_token(identify, payload, secret):
        """
        Creates an authentication token for a user.

        Args:
            username (str): The username for which to create the token.

        Returns:
            str: The generated authentication token.
        """
        headers = {
            'identity': identify,
        }
        return encode(headers=headers, payload=payload, secret=secret)


def decode_token(token, secret):
    """
    Decodes an authentication token to retrieve the user identity.

    Args:
        token (str): The authentication token to decode.

    Returns:
        str: The user identity extracted from the token.
    """
    try:
        decoded = decode(token, secret)
        return decoded.get('identity')
    except Exception as e:
        return None
    
def decode_token_no_verify(token):
    """
    Decodes an authentication token without verifying the signature.

    Args:
        token (str): The authentication token to decode.

    Returns:
        str: The user identity extracted from the token.
    """
    try:
        decoded = decode_no_verify(token)  # No secret for verification
        return decoded.get('identity')
    except Exception as e:
        return None
def create_refresh_token(identify, secret):
    """
    Creates a refresh token for a user.

    Args:
        username (str): The username for which to create the refresh token.

    Returns:
        str: The generated refresh token.
    """
    headers = {
        'identity': identify,
    }
    payload = {'exp': time.time() + 3600*24}
    return encode(headers=headers, payload=payload, secret=secret) #TODO: Need to check


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

def create_session(device_id:str, username:str):
    """
    Creates a session for a user.

    Args:
        username (str): The username for which to create the session.

    Returns:
        str: The generated session ID.
    """
    # session_id = base64.b64encode(secrets.token_bytes(32)).decode()
    # session = {
    #     'device_id': device_id,
    #     'username': username,
    #     'expiry': time.time() + 3600
    # }
    session = f"{device_id}:{username}:{int(time.time() + 3600)}"
    
    return hashlib.sha256(session.encode()).hexdigest()
