def login(username, password):
    
    if username == 'JuneBai0000' and password == '0000':
        return True
    else:
        return False
    
if __name__ == '__main__' :
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python login_script.py <username> <password> check ID&PW")
        sys.exit(1)
        
    username = sys.argv[1]
    password = sys.argv[2]
    
    if login(username, password):
        print("로그인 성공")
    else:
        print("ID와 PW를 다시 확인해주세요.")
        
    