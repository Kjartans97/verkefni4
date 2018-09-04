n = int(input("Enter the length of the sequence: ")) # Do not change this line
if n==1:
    print("1")
elif n==2:
        print("1\n2")
elif n==3:
        print("1\n2\n3")
elif n>3:
    a=1
    b=2
    c=3
    print("1\n2\n3")
    for i in range(3,n):
          d= a+b+c
          a=b
          b=c
          c=d
          print(d)