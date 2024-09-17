def main(sales):
    total = 0
    for sale in sales.split():
        total += int(sale)
    print(total)
    return
if __name__ == '__main__': 
    sales = str(input())
    main(sales)