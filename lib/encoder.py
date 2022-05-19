from cryptography.fernet import Fernet


class Password:
    @staticmethod
    async def encrypt(pwd: str, key: bytes):
        return Fernet(key).encrypt(pwd.encode()).decode()
