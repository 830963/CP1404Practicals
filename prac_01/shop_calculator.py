while True:
    item_count = int(input("Number of items: "))
    if item_count < 0:
        print("number of items should be a positive integer")
    else:
        break
total_amt = 0

for i in range(item_count):
    while True:
        item_value = float(input("Price of item: "))
        if item_value < 0:
            print("price can not be negative, re-enter the value")
        else:
            total_amt += item_value
            break

if total_amt > 100:
    total_amt = 0.9*total_amt

print("Total price for %d items is $%.2f"%(item_count , total_amt))


