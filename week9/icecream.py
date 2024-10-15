from functools import reduce
menu, sales, menu_sales = {}, {}, {}
for i in range(int(input())):
    name, price = input().split()
    menu[name] = float(price)
for i in range(int(input())):
    name, amount = input().split()
    if name in sales.keys():
        sales[name] = sales[name] + float(amount)
    else:
        sales[name] = float(amount)
    
    
for name, amount in sales.items():
    try:
        price = menu[name]
        total_price = price * amount
        menu_sales[name] = total_price
    except:
        continue
    
if len(menu_sales) == 0:
    print("No ice cream sales")
    exit()
    
top_sale = max(menu_sales.values())
top_menu_sales = sorted(list(filter(lambda k: k[1] == top_sale, menu_sales.items())))
print(f'Total ice cream sales: {reduce(lambda a, b: a + b, menu_sales.values()):.1f}')
print(f'Top sales: {", ".join(i[0] for i in top_menu_sales)}')