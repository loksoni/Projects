series =[]
def fibonacci(n):
    if n<=1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n=int(input("Enter length of fibonacci series:"))
for i in range(0,n):
    series.append(fibonacci(i))
print(series)