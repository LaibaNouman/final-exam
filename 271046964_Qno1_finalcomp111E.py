
#QUESTION NO.1:

def decimal_to_binary(n):

    if n==0:
        return 0
    return decimal_to_binary_helper(n)

def decimal_to_binary_helper(n):
    if n==0:
        return 0
    else:
        return (decimal_to_binary_helper(n//2)*10)+(n%2)


if __name__=="__main__":
    
    n1=7
    n2=10

binary_n1=decimal_to_binary(n1)
binary_n2=decimal_to_binary(n2)

print(f"The binary representation pf (n1) is :{decimal_to_binary(n1)}")
print(f"The binary representation pf (n2) is :{decimal_to_binary(n2)}")