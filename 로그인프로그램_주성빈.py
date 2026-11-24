user = input('아이디를 입력해주세요 : ')
password = input('패스워드를 입력해주세요 : ')

if user == "admin" and password == "1234":
    print('로그인 성공')
elif user == "admin" and password != "1234":
    print('패스워드가 틀렸습니다. 다시 입력하세요.')
elif user != "admin" and password == "1234":
    print('없는 아이디입니다. 다시 확인하고 입력하세요')
else:
    print('로그인 실패')