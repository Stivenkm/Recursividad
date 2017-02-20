n=int(input(""))
def binadecimal(n):
    if n<10:
        return n
    else:
        return (n%2)+binadecimal(n/10)*2
print(binadecimal(n))
