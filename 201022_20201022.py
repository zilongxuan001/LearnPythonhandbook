user = input()
long= len(user)
code= ""
for i in range(long):
    if user[i] in ["X","Y","Z","x","y","z"]:
        code +=chr(ord(user[i])-23)
    elif 65 <= ord(user[i]) <=88 or 97 <=  ord(user[i]) <= 119:
        code +=chr(ord(user[i])+3)
    else:
        code +=user[i] 
    
print(code)

