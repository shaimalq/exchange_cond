A= int(input("enter the value A :"))
B= int(input("enter the value  B :"))
if A*B > 0 :
    C=A
    A=B
    B=A
else:
    C=A+B 
    D=A*B
    A=C
    B=D
    print("new value the A is" ,A)
    print("new value the B is" ,B)
