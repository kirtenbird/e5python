n=str(input("请输入一个数:"))
r=n 
s=[]
e=int(input("请输入你输入的是几进制:"))
m=0
if e==10:
    while True:
        n=int(n)
        r=n%2
        n=n//2
        s.append(r)
        if n==0:
            break
    s=s[::-1]
    print("十进制转二进制为",s)
elif e==2:
    for i in range(len(n)):
     #   q=int(q)
     #   s.append(q)
    #for t in range(0,len(s)):
       # m=(s[t])*(2**t)
       m=m+int(n[i])*2**(len(n)-1-i)
    print("二进制转十进制为",m)
else:
    print("请输入二进制或十进制的数其他无效")
    
