print('HELLO\nWELCOME TO OUR SOFTWARE')
username = (input('ENTER YOUR USERNAME:  '))
#password = int(input('ENTER YOUR PASSWORD:  '))
access='DIVINE'
try:
    if username== access :
        password = int(input('ENTER YOUR PASSWORD:  '))
        if password == 1234 :
            print('YOU ARE WELCOME', username)
    else:
        print('invalid Username')
except Exception as e:
    print(e)


