n = int(input("Enter ur value::"))


while True:
       c =input("Enter ur choice::")
       c= c.lower().strip() 
       if (c=='q'):
           break

       if (c=='1'):
            for i in range(n):
               print(("*")*(n-i))

       elif(c=='2'):
            for i in range(n):
                for j in range(n-i):
                    print(j+1,end=" ")
                print()

       elif(c=='3'):
            for i  in range(n): 
                for k in range(i):
                    print(" ", end=" ")
                for j in range(n-i):
                    print(n-j,end=" ")
                print()
    
       elif(c=='4'):
            for i in range(n):
                print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))
       elif (c=='5'):
            for i in range(n):
                print(' '*(n-i-1),end='')
                for j in range(i+1):
                    print(chr(64+n-j),end=" ")
                print()
       elif(c=='6'):
            for i in range(n):
                for j in range(i+1):
                    print(chr(65+j),end=' ')
                print()
 
            for i in range(n-1):
                for j in range(n-i-1):
                    print(chr(65+j),end=' ')
                print()

       elif(c=='7'):
           for i in range(n):
               print(" "*i,end=" ")
               for j in range(n-i):
                   print(chr(65+j),end=" ")
               print()
       elif (c=='8'):
           for i in range(n):
               print(" "*(n-i-1)+(("*"+" ")*(i+1)))
           for i in range(n-1):
               print(" "*(i+1)+"* "*(n-i-1))
       else:
            print("Another choice not this one <:)")
