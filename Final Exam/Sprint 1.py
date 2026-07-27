# Sprint 1
# Coin Converter
# Converts pseudo-English coin descriptions into dollars.

coin_values = {
    "penny": 1,
    "pennies": 1,
    "nickel": 5,
    "nickels": 5,
    "dime": 10,
    "dimes": 10,
    "quarter": 25,
    "quarters": 25
}

sentence = input("Enter coin description: ")

words = sentence.lower().split()

total_cents = 0

for i in range(len(words)):
    if words[i].isdigit():

        quantity = int(words[i])

        if i + 1 < len(words):

            coin = words[i + 1].replace(",", "")

            if coin in coin_values:

                total_cents += quantity * coin_values[coin]

total_dollars = total_cents / 100

print(f"Total: ${total_dollars:.2f}")