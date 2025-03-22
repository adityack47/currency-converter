import numpy as np
import requests  # To fetch live exchange rates

# 📌 API to fetch exchange rates
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # Base currency: USD

# 📌 Function to get live exchange rates
def get_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data["rates"]

# 📌 Function to convert currency
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return "Invalid currency!"
    
    # Using NumPy for currency conversion calculation
    conversion_rate = np.round(rates[to_currency] / rates[from_currency], 4)
    converted_amount = np.round(amount * conversion_rate, 2)
    
    return f"{amount} {from_currency} = {converted_amount} {to_currency}"

# 📌 Main Execution
rates = get_exchange_rates()  # Get live exchange rates
print("Available Currencies:", list(rates.keys()))

# 📌 Taking user input
amount = float(input("Enter amount: "))
from_currency = input("Enter the currency you have (e.g., USD, EUR, INR): ").upper()
to_currency = input("Enter the currency you want (e.g., USD, EUR, INR): ").upper()

# 📌 Convert and display result
result = convert_currency(amount, from_currency, to_currency, rates)
print(result)