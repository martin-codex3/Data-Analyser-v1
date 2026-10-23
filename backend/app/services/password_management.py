from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def hash_tenant_password(password: str) -> str:
    """This will hash the password
    using the argon algorithm"""
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """This will get tenant password and verify if it is valid"""
    return password_hash.verify(plain_password, hashed_password)
