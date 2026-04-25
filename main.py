import time
import smtplib
import requests
from datetime import datetime

MY_LAT = 12.858097 # Your latitude
MY_LONG = 80.132315 # Your longitude

def iss_postions():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <=MY_LONG+5:
        return True


def check_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour=datetime.now().hour
    
    if current_hour > sunset or current_hour < sunrise:
        return True
    
def sent_email():
      
        email="Email"
        app_password="Your Password"
      
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=app_password)
            connection.sendmail(
                from_addr=email,
                to_addrs="Your Email",
                msg="Subject:Look Up \n\n The ISS is right above you in the sky"
            )
while True:
    time.sleep(60)    
           
    if iss_postions() and check_night():
        
        sent_email()
    

