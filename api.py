import requests
import base64

def encoder():
    sample_string = "amoghkashyap:2b11c702-4168-4a41-83c0-a1f2c597e912"
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return(base64_string)

header= {"Authorization" : encoder(), "If-Modified-Since":"2021"}

r = requests.get("https://frc-api.firstinspires.org/v3.0/:2022", headers=header)
print(r.content)