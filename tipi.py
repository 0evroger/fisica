print("""bienvenido a la presentacion de trabajo por parejas: 
para poder visualizar las preguntas tenga en cuenta esto 
preguntas tenga el pdf suministrado para poder reconocer las preguntas:
preguntas:
1.pregunta 1.1
2.pregunta 1.2
3.pregunta 1.3
4.pregunta 1.4
5.pregunta 1.5
6.pregunta 2.1
7.pregunta 2.2
8.pregunta 3.1
9.pregunta 3.2
10.pregunta 3.3
11.pregunta 3.4
12.pregunta 3.5
13.pregunta 4.1
14.pregunta 4.2
15.pregunta 4.3""")
ele=int(input("que ejercicio quiere ver:"))
if ele==1:
    X=0
    A=set()
    while (X**2)!=1:
        X=X+1
    else:
        A.add(X)
    print("el conjunto es",A)
#[1,2]
if ele==2:
    X=0
    B=set()
    for i in range (12):
        B.add(i)
    print(B)
#[1.3]
if ele==3:
    C=set()
    for i in range(100):
        if (i**2)<100:
            C.add(i)
    print(C)
#[1.4]
if ele==4:
    from math import sqrt
    D=set()
    X=0
    while sqrt(sqrt(X**2))!=sqrt(2):
        X=X+1
    if sqrt(X) is int:
        D. add(sqrt(X))
        D. add(-sqrt(X))
    print(D)
#[1.5]
if ele==5:
    E=set()
    for i in range(1,101):
        E.add(i)
    print(E)
#[2.1]
if ele==6:
    F=set()
    for i in range (1,101):
        F.add(i)
    pf=int(input("que valor desea saber si existe el conjunto"))
    if pf in F:
        print(pf,"es un elemento del conjunto")
    else:
        print(pf,"no es un elemento del conjunto")
#[2.2]
if ele==7:
    G=set()
    for i in range (1,201):
        G.add(i)
    pg=int(input("que valor desea saber si existe:"))
    if pg in G:
        print(pg,"es un elemento del conjunto")
    else:
        print(pg,"no es un elemento del conjunto")
#[3,1]
if ele==8:
    H={1}
    print(H)
    print("la cardinalidad del conjunto es",len(H))
#[3,2]
if ele==9:
    I={1,(4)}
    print(I)
    print("la cardinalidad del conjunto es",len(I))
#[3.3]
if ele==10:
    J={(4)}
    print(J)
    print("la cardinalidad del conjunto es",len(J))
#[3.4]
if ele==11:
    K={()}
    print(K)
    print("la cardinalidad del conjunto es",len(K))
#[3.5]
if 12==ele:
    L={1,(4),(5,(7,8))}
    print(L)
    print("la cardinalidad del conjunto",len(L))
#[4.1]
if 13==ele:
    a={1,2,3,4,5}
    b={0,3,6}
    print(a|b)
    print(a&b)
    print(a-b)
    print(b-a)
    print(a^b)
#[4.2]
if 14==ele:
    a={"a","b","c","d","e"}
    b={"a","b","c","d","e","f","g","h"}
    print(a|b)
    print(a&b)
    print(a-b)
    print(b-a)
    print(a^b)
#[4.3]
if 15==ele:
    a={0,2,4,6,8,10}
    b={0,1,2,3,4,5,6,}
    c={4,5,6,7,8,9,10}
    print(a&b&c)
    print(a|b|c)
    print((a|b)&c)
    print((a&b)|c)