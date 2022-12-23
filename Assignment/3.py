# Input series length (min. 100) from user and print fibonacci sequence
chk = 0
while chk<1:
    nterms = int(input('\nHow many terms? (min. 100)\n'))
    if(nterms>=100):
        chk = 1
    else:
        print('\nEnter valid series length')

n1, n2 = 0, 1
count = 0
print("\nFibonacci Sequence - First",nterms,"terms\n")

while count < nterms-1:
       print(n1, end = " , ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print(n1)