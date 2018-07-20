import bcrypt

password = 'baker'
password2 = 'baker'

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

print('hashed pw',hashed)

if bcrypt.checkpw(password2.encode(), hashed):
    print('yes it worked')
else:
    print('no it didnt')
