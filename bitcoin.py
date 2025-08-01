import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
        
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        api_key ="04416997c0391c53fd3dcab94cc0ab3252843b34cdca3372131d99eb462d89bc"
        url = f"https://api.coincap.io/v2/assets/bitcoin"
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        price = float(data["data"]["priceUsd"])
        total_cost = bitcoins * price

        print(f"${total_cost: , .4f}")
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

if __name__ == "__main__":
    main()







             
     


