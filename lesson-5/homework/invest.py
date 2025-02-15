amount = int(input("Enter the initial amount: "))
rate = float(input("Enter the rate: "))
years = int(input("Enter the amount years: "))
def invest(amount, rate, years):
    for year in range(0,years):
        amount = round(amount+amount*(rate/100),2)
        print(f"year {year+1}: {amount}")
invest(amount,rate,years)
        