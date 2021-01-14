import requests
import json

getapi_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=7a8aab66-120d-470f-ba11-d10d18ad27bc")

loadapi = json.loads(getapi_request.content)



with open('jsonfiles/data.json' , 'r') as f:
    coins = json.load(f)



def menu():
    Input_value = input("Enter S to Search & A to add cryptocurrency: ")
    Input_value = Input_value.upper()
    if Input_value == "S":
        search(coins)
    elif Input_value == "A":
        print("Add")
    else:
        print("Invalid input")


def search(coins):
    Search = input("Enter your Cryptocurrency Symbol: ")
    Search = Search.upper()
    for coin in coins:
               if coin["symbol"] == Search:
                       for i in range(5):
                            if Search == loadapi["data"][i]["symbol"]:
                               Amount_paid = coin["amount_owned"] * coin["price_per_coin"]
                               total_current_pl = coin["amount_owned"] * loadapi["data"][i]["quote"]["USD"]["price"]
                               PL =  total_current_pl - coin["price_per_coin"]
                               print(loadapi["data"][i]["name"] + " || " + loadapi["data"][i]["symbol"])
                               print("-------------------------")
                               print(  "Current Price: " +"{0:.2f}".format(loadapi["data"][i]["quote"]["USD"]["price"]))
                               print(  "Number of Coins:" , coin["amount_owned"])
                               print(  "Amount Paid:", Amount_paid)
                               print(  "Total Supply: " + "{0:.2f}".format(loadapi["data"][i]["total_supply"]))
                               print(  "Market Cap: " + "{0:.2f}".format(loadapi["data"][i]["quote"]["USD"]["market_cap"]))
                               print("-------------------------")
                               print(  "Profit/Loss: " , PL)
                               print("-------------------------")
                               print("-------------------------")
                            else:
                                Searchresult = "Cryptocurrency not find this in your portfolio"
               else:
                   Searchresult = "Cryptocurrency not be found in your Portfolio"
    menu()

def add_coin(coins):
    add_coin_symbol = input("Enter Coin Symbol: ")
    add_amount_owned = input("Enter Amount of Coin owned: ")
    add_price_per_coin =  input ("Enter Price Per Coin: ")


    insert_data = {
        "symbol": "BTC",
        "amount_owned": 12,
        "price_per_coin": 5000
    }

    a_file = open("jsonfiles/data.json", "w")
    a_file.write(insert_data)
    a_file.close()



def rearrange(coins):
    for btc in coins:
        print(btc["symbol"])

menu()
