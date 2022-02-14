import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import math
import smtplib

load_dotenv()

watch_url = "https://www.amazon.com/Acer-EI342CKR-Pbmiippx-1500R-Zero-Frame/dp/B096L32K6S/ref=sr_1_18?keywords=34%22+ultrawide+monitor&qid=1639585253&refinements=p_n_feature_eleven_browse-bin%3A17726575011%7C17726576011&rnid=17726572011&s=pc&sr=1-18"
email = os.getenv("email")
password = os.getenv("password")


def get_website():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Accept-Language": "en-US,en;q=0.5"
    }
    response = requests.get(url=watch_url, headers=header)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    return soup


def get_price():
    page_info = get_website()
    price = page_info.find(name="span", class_="a-price-whole").getText().strip(".")
    return math.ceil(int(price) + 1)


def send_email(price, url):

    with open(file="email_list.txt", mode="r") as email_list:
        file = email_list.read()
        to_email = file

    with smtplib.SMTP("smtp.gmail.com", 587) as new_email:
        new_email.starttls(),
        new_email.login(user=email, password=password)
        new_email.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=f"Subject: Amazon Price Alert!\n\n The price has fallen below your target price to {price}! "
                f"Click the link below to view the item: \n"
                f"{url}"
        )

