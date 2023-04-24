import random

MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
OUTPUT_FILE = "prices.txt"
MAX_DAYS = 426

price = INITIAL_PRICE
print(f"${price:,.2f}")

for day in range(1, MAX_DAYS):
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    price = max(price, MIN_PRICE)
    price = min(price, MAX_PRICE)
    print(f"On day {day} price is: ${price:,.2f}")

print(f"Final price after 425 days is: ${price:,.2f}")

out_file = open(OUTPUT_FILE, 'w')
out_file.write(f"Starting price: ${INITIAL_PRICE:,.2f}\n")
for day in range(1, 426):
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    price = max(price, MIN_PRICE)
    price = min(price, MAX_PRICE)
    out_file.write(f"On day {day} price is: ${price:,.2f}\n")
