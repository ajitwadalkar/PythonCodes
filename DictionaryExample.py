prices = {'apple': 0.40, 'banana': 0.50, 'mango':0.80}
my_purchase = {
    'apple': 1,
    'banana': 6,
    'mango':3}
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)

grocery_bill2=0;
for fruit in my_purchase:
    grocery_bill2 = grocery_bill2+ (prices[fruit] * my_purchase[fruit])
print('I owe the grocer $%.2f' % grocery_bill2)
