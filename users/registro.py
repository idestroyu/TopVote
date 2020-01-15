from passlib.hash import pbkdf2_sha256

def hash_password(password):
    salt = os.urandom(16)

    m = hashlib.md5()
    m.update(salt + password)
    return m.hexdigest(), salt

def verify_password(password, salt):
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),  # Convert the password to bytes
        salt,
        10000
    )

    return str(key)