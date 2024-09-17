def main():
    phone = input()
    if len(phone) == 10 and phone[:2] in ['08', '06', '09']:
        print('Mobile number')
        return
    print('Not a mobile number')
    return
    
if __name__ == '__main__':
    main()