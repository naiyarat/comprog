import statistics
def main():
    arr = []
    while True:
        try: 
            arr.append(float(input()))
        except:
            if len(arr) == 0:
                print("No Data")
                return
            break
        
    print('\n',round(statistics.mean(arr), 2), sep='')
    return

main()