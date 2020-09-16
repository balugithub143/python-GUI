
x=int(input())
j=1

k=2*x-3

for i in range(1,x*2):
    
    if(i<=4):
        print("  "*(x-i) + " *"*j)
        j=j+2
    else:
        print("  "*(i-x) + " *"*k)
        k=k-2
 