import jwt

def encode(headers, payload, secret):
    """Encode a payload into a JWT token using the given secret."""
    return jwt.encode(payload=payload, algorithm='HS256', headers=headers, key=secret)

def decode(token, secret):
    """Decode a JWT token using the given secret."""
    return jwt.decode(token, secret, algorithms=['HS256'])

def decode_no_verify(token):
    """Decode a JWT token without verifying the signature."""
    return jwt.get_unverified_header(token)


def decode_unsafe(token, secret):
    """Decode a JWT token using the given secret without verifying the signature."""
    return jwt.decode(token, secret, algorithms=['HS256'], verify=False)

def decode_unsafe_no_verify(token):
    """Decode a JWT token without verifying the signature."""
    return jwt.decode(token, verify=False)

def decode_unsafe_no_verify_no_alg(token):
    """Decode a JWT token without verifying the signature and without specifying the algorithm."""
    return jwt.decode(token, verify=False, algorithms=['none'])