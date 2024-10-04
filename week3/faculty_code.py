def main(code):
    try: 
        if (code in ['01', '02'] or int(code) in range(20,41) or int(code) in [51,53,55,58]):
            print('OK')
            return
        else:
            raise Exception
    except:
        print('Error')
        return
if __name__ == '__main__': 
    code = str(input())
    main(code)