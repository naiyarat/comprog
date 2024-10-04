import datetime
def main():
    date = str(input())
    print(datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%B %-d, %Y"))
    
if __name__ == '__main__': 
    main()