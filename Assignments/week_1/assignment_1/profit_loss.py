# Calculate Profit or Loss
# Input cost price and selling price. Display either:
# Profit and amount, or
# Loss and amount, or
# No Profit No Loss

costPrice=int(input("please enter cost price : "))
sellingPrice=int(input("please enter selling price : "))

profit=sellingPrice-costPrice

if costPrice < sellingPrice:
    print("Profit : ",profit)
elif costPrice > sellingPrice:
    print("Loss : ",abs(profit))
else:
    print("No Profit , No loss")