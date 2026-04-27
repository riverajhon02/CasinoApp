import os
import sib_api_v3_sdk

def send_otp_email(to_email: str, otp: str):
    config = sib_api_v3_sdk.Configuration()
    config.api_key['api-key'] = os.getenv("BREVO_API_KEY")

    api = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(config)
    )

    email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": to_email}],
        subject="Código OTP",
        html_content=f"<h2>Tu código es: {otp}</h2>",
        sender={"email": os.getenv("BREVO_SENDER")}
    )

    api.send_transac_email(email)