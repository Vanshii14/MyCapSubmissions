n=int(input("Enter the no. of terms ofthe Fibonacci series to be printed : "))
n1=0
n2=1
count=0
if n < 1:
    print("Please enter a valid no.")
elif n==1:
    print("1 term of Fibonacci series is :",n1)
else:
    print(n,"terms of the Fibonacci series are:")
    while count < n:
        print(n1)
        sum=n1+n2
        n1=n2
        n2=sum
        count=count+1
      
      
