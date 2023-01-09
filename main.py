import httpx

base_currency = input("Digite a sigla da moeda que deseja converter (ex: BRL, USD, EUR): ").upper()
currency = input("Insira a moeda que deseja a conversão (símbolo): ").upper()

#Buscar valores da moedas em API publica

response = httpx.get(
    url=f'https://api.exchangerate.host/latest?base={base_currency}'
).json()
currency_data = response['rates']

print(f'1 {base_currency} vale {currency_data.get(currency)} {currency}')