exchange_rates = {
    "EUR": 0.92,  # 1 USD = 0.92 EUR
    "GBP": 0.79,  # 1 USD = 0.79 GBP
    "JPY": 148.67, # 1 USD = 148.67 JPY
    "TRY" : 35.62 # 1 USD = 35.62 TRY
}

amount = float(input("Enter amount in USD: "))
currency = input("Enter target currency (EUR, GBP, JPY,TRY): ").upper()

if currency in exchange_rates:
    converted_amount = amount * exchange_rates[currency]
    print(f"{amount} USD is equal to {converted_amount:.2f} {currency}")
else:
    print("Invalid currency!")
