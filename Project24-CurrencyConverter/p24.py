import requests
import time


def from_country(country):
    try:
        country_name = country.upper()
        responce = requests.get(
            f"https://open.er-api.com/v6/latest/{country_name}")
        ratios = responce.json()["rates"]
    except:
        print("the currency does not exist")
    return ratios


def to_country(country):
    return country.upper()


def converter():

    print("====Simple Currency Converter====")
    print("🔁 Getting exchange rates ...")
    time.sleep(1)
    print("✅ Got rates Succesfully")
    print("💼 Popular USD EUR GBP JPY CAD AUD CNY INR")

    print("Enter Details:\n")

    from_currency = input("From Currency Code (e.g USD) : ")
    to_currency = input("To Currency Code (e.g USD) : ")
    amount = int(input(f"Amount in {from_currency} : "))

    ratios = from_country(from_currency)
    to_c = to_country(to_currency)
    current_ratio = 0
    if to_c in ratios:
        current_ratio += ratios[to_c]
    print(
        f"💰 Result: {amount}{from_currency} = {current_ratio*amount}{to_currency}")


def initialize():

    while True:
        converter()
        try_again = input("🔁 Convert again (y/n) : ")
        if try_again.startswith('n'):
            print("👏 Thankkyou for using the converter")
            break


initialize()
