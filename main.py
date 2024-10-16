def power(n):
    if n<=0:
        return False
    return(n&(n-1))==0
n=int(input("taking number from the user") )
if power(n):
    print("number is power") 
else:
    print("number is not power")  