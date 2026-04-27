from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class VerifyOTPRequest(BaseModel):
    temp_token: str
    otp: str