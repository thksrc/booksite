from werkzeug.security import generate_password_hash, check_password_hash

def set_password(password):
    password = generate_password_hash(password)
    return password

def check_password(hsh, password):
    return check_password_hash(hsh, password)