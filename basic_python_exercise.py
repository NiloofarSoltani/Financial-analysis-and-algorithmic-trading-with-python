import math

# EXERCISE 1
# Given price = 144 , use python to figure out the square root of the price.
ch = 144
print(math.sqrt(ch))

# EXERCISE 2
# Given the string: stock_index = "SP500"
# Grab '500' from the string using indexing.
stock_index = "SP500"
print(stock_index[:2])
print(stock_index[2:])

# EXERCISE 3
# Given the variable of a nested dictionary with nested lists:Use indexing and key calls to grab the following items:
# Yesterday's SP500 price (250)
stock_info = {'sp500': {'today': 300, 'yesterday': 250}, 'info': ['Time', [24, 7, 365]]}
print(stock_info['sp500']['yesterday'])
print('day', stock_info['info'][1][1])
print('year', stock_info['info'][1][2])


# EXERCISE 4
# Given strings with this form where the last source value is always separated by two dashes -- "PRICE:345.324:SOURCE--QUANDL"
# Create a function called source_finder() that returns the source. For example, the above string passed into the function would return "QUANDL"
def source_finder(s):
    return s.split('--')[-1]


print(source_finder("PRICE:345.324:SOURCE--QUANDL"))


# EXERCISE 5
# Create a function called price_finder that returns True if the word 'price' is in a string. Your function should work even if 'Price' is capitalized or next to punctuation ('price!')  **
def price_finder(s):
    return 'price' in s.lower()


print(price_finder("What is the price?"))
print(price_finder("DUDE, WHAT IS PRICE!!!"))
print(price_finder("The price is 300"))


# EXERCISE 6
# Create a function called count_price() that counts the number of times the word "price" occurs in a string. Account for capitalization and if the word price is next to punctuation. **
def count_price(s):
    return s.lower().count('price')


def count_price_2(s):
    count = 0
    for word in s.lower().split():
        if 'price' in word:
            count += 1
    return count


s = 'Wow that is a nice price, very nice Price! I said price 3 times.'
print('count price is :', count_price(s))
print('count price is :', count_price_2(s))