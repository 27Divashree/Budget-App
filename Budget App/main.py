from matplotlib.collections import _CollectionWithSizes
import budget
from budget import create_spend_chart
from unittest import main


print("Enter initial deposit amount ")
deposit = int(input())
print("Enter amount spent on groceries ")
groceries = int(input())
print("Enter money spent on restaurant and more food ")
dessert = int(input())
print("Enter money to transfer to clothing ")
clothesTransfer = int(input())
print("Enter money spent on clothing ")
clothes = int(input())
food = budget.Category("Food")
food.deposit(deposit, "initial deposit")
food.withdraw(groceries, "groceries")
food.withdraw(dessert, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(clothesTransfer, clothing)
clothing.withdraw(clothes)
clothing.withdraw(2*clothesTransfer)
auto = budget.Category("Auto")
auto.deposit(deposit, "initial deposit")
auto.withdraw(dessert)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)

