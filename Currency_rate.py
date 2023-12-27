from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = float(input("Enter amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

conversion_rate = c.get_rate(from_currency, to_currency)
converted_amount = amount * conversion_rate

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
