from currency_converter import CurrencyConverter

c = CurrencyConverter()
amount = int(input("Enter The Amount :"))
given = input("Enter The currency You Have (INR) : ")
to = input("Enter The Currency You Want to convert (USD): ")
temp = c.convert(amount, given, to)

print(f"Converted From {given} to {to} : {temp}")