text = "Welcome to your CrypFolio"
print(f"{text:'^50}")

import requests
import json

#Use an API of a crypto currency tracking website that allows users to fetch cryptocurrency data such as price, volume, market cap, and exchange data etc...

api_request = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false"  #Crypto-INR pair
)
api = json.loads(api_request.content)

# currencies symbol = "btc", "xrp", "eth", "ada" etc

Portfolio_profit_loss = 0

total_portfolio_value = 0

print("-"*50)

for x in range(30000):

    coin = input(
        "enter the coin symbol ex: BTC, ETH, MATIC, DOGE or type Q to quit and view your overall portfolio value:\n ------------------------------------------\n").lower()

    print("-"*30)

    if coin == "q":
        break

    amount_owned = input("enter the total number of coins you own: ")
    cost_per_coin = input("Enter the price you bought the coin for(in INR): ")

    print("------------------------------------------")

    for data in api:

        if coin == data["symbol"]:

            #Let's do some math

            total_paid = float(amount_owned) * float(cost_per_coin)
            current_value = float(amount_owned) * float(data["current_price"])
            profit_loss = current_value - total_paid
            Portfolio_profit_loss += profit_loss
            total_portfolio_value = +current_value
            profit_loss_per_coin = float(
                data["current_price"]) - float(cost_per_coin)

            print("You are looking at {} ".format(data["name"]))
            print(data["name"], "is Ranked {}".format(data["market_cap_rank"]),
                  "Among top 100 coins in marketcap")
            print("Current Price is ₹{0:.2f}".format(
                float(data["current_price"])))
            print("24h high: ₹{0:.2f}".format(float(data["high_24h"])))
            print("24h low: ₹{0:.2f}".format(float(data["low_24h"])))
            print("24h change in percentage: {}".format(
                data["price_change_percentage_24h"]) + ("%"))
            print("All time high: ₹{}".format(data["ath"]))

            print("------------------------------------------")

            print("Total amount paid: ₹{0:2f}".format(float(total_paid)))
            print("Current value of your Portfolio: ₹{}".format(
                float(current_value)))
            print("Total profit/loss for", (data["name"]),
                  "is ₹{0:.2f}".format(profit_loss))

            print("------------------------------------------")

            break

    else:

        print("Please enter the correct symbol or type Q to exit:\n")
        print("------------------------------------------")
        print("------------------------------------------")

print("Your Overall Portfolio's Profit/Loss is: ₹{0:.2f}".format(
    float(Portfolio_profit_loss)))
print("total amount in portfolio: ₹{0:.2f}".format(total_portfolio_value))

print("------------------------------------------")
print("------------------------------------------")
