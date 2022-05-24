import binascii
#-------------バイナリ法:入力(冪乗する数，冪乗の数,modの数),出力(結果)--------------------------
def bainary(g,k,mod):
    y=1
    k=bin(k)
    k=list(k)
    k[0]=9
    k[1]=9
    for i in k:
        if int(i)==1:
            y=y*y*g
        if int(i)==0:
            y=y*y
        y=y%mod
    return(y)
#--------エルガマル暗号Enc入力(mod,g,pk,m,r),出力(pk,u,c)-------------------------
def El_Enc(mod,g,pk,m,r):
    u=bainary(g,r,mod)%mod
    #m=int(binascii.b2a_hex(u'らーめん'.encode('utf-8')),base=16)  # => b'e38193e38293e381abe381a1e381af'
    print("mは",m)
    c=bainary(y,r,mod)*m%mod
    return(u,c)
#-------エルガ丸復号，入力（暗号文,sk,mod）---------------
def El_dec(u,c,sk,mod):
    m=c/(u)**sk%mod
    return(m)
#-----gcd--------------------
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
#拡張ユークリッド入力(a,b),出力（x,y）
def ex_euclid(a,b):
    x,y,s,t=1,0,0,1
    while b!=0:
        u=a//b
        x-=u*s
        y-=u*t
        x,s=s,x
        y,t=t,y
        a, b = b, a%b
    res=[x,y]
    return res

#-------逆元計算---------
def mod_inv(a,b):
    x=ex_euclid(a,b)[0]
    if x<0:
        x=x+b
    return x
#------mod加算公式---------
def mod_kasan(P,Q,p):
    lam=(Q[1]-P[1])*mod_inv(Q[0]-P[0],p)%p
    x=(pow(lam,2)-P[0]-Q[0])%p
    y=(lam*(P[0]-x)-P[1])%p
    return [x,y]
#-------mod２倍算公式------------
def mod_nibai(P,a,p):
    lam=(3*pow(P[0],2)+a)*mod_inv(2*P[1],p)%p
    x2=(pow(lam,2)-2*P[0])%p
    y2=(lam*(P[0]-x2)-P[1])%p
    return [x2,y2]
#-----スカラ倍算-----------------
def kP(P,a,p,k): #kP
    y=P
    i=0
    l=[]
    while pow(2,i)<=k:#ビット列に
        if k%pow(2,i+1):
            l.append(1)
            k=k-pow(2,i)
        else:
            l.append(0)
        i+=1
    print(l)
    for i in range(len(l)-1):
        if l[len(l)-i-2]==1:#1が立ってた場合
            y=mod_nibai(y,a,p)
            y=mod_kasan(P,y,p)
        else:#0が立ってた場合
            y=mod_nibai(y,a,p)
    return y

p=5
g=
y=4
r=
m=
u,c=El_Enc(p,g,y,m,r)
print(u,c)

for i in range(11):
    if 2*i%11==3%11:
        print(i)