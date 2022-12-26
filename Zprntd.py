def func():
    print('********')
    i=6 
    for i in range (7,1,-1):
        print('*'.rjust(len('*')+i-1))
        i-1
    print('********')
    print('25/12/22')