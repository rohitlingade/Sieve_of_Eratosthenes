def sieve_of_eratostenes(num):
    prime=[True for i in range(num)]
    prime[0]=False
    n=2
    while n**2<num:
        for i in range(n**2,num+1,n):
            prime[i-1]=False
        n+=1
    c=0
    for p in prime:
        if p==True:
            c+=1
    print(c)
    prime_nos=[]
    for i in range(num):
        if prime[i]==True:
            prime_nos.append(i+1)
    return prime_nos

def main():
    num=int(input("Enter a number: "))
    prime_numbers=sieve_of_eratostenes(num)
    print("Prime numbers upto",num,"are",prime_numbers)

if __name__=="__main__":
    main()
