# Sprint 2
# Improved Coin Converter

import string

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

# Remove punctuation and convert to lowercase
sentence = sentence.lower().translate(
    str.maketrans("", "", string.punctuation)
)

words = sentence.split()

total_cents = 0

for i in range(len(words)):

    if words[i].isdigit():

        quantity = int(words[i])

        if i + 1 < len(words):

            coin = words[i + 1]

            if coin in coin_values:

                total_cents += quantity * coin_values[coin]

            else:

                print(f'Unsupported coin: "{coin}"')

total_dollars = total_cents / 100

print(f"\nTotal Amount: ${total_dollars:.2f}")