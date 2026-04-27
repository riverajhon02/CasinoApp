import random
from app.core.redis_client import redis_client

OTP_EXPIRATION = 300  # 5 minutos

def generate_otp():
    return str(random.randint(100000, 999999))


def save_otp(email: str, otp: str):
    redis_client.setex(f"otp:{email}", OTP_EXPIRATION, otp)


def verify_otp(email: str, otp: str):
    stored_otp = redis_client.get(f"otp:{email}")

    if stored_otp and stored_otp == otp:
        redis_client.delete(f"otp:{email}")
        return True

    return False