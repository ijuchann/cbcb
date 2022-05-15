import random


def check() :
    for i in range(0,3)  : 
        
        dapji=[1,2,3,4,1,2,3,4,1,2]

        print("과목%d:"% (k+1), end="")

        for i in range(0,10) :
            print("%d" % dapji[i], end="")

        
        print("\n ", end=" ")




        
    print("\n------------------------------------------")




    for i in range(0,3) : 

        
        stu_ans = [] 

        for i in range(0,10) :
            ans = random.randrange(1,5)
            stu_ans.append(ans) 
           


        print("\n학생%d"% (j+1), end=" ")
     

        o = 0
        
        
        print("\n", end=" ")
        for i in range(0,3)  :
            print("과목%d:"% (k+1), end=" ")
            for i in range(0,10) :
                
                if dapji[i] == stu_ans[i] :
                    print(" O", end= " ")
                    o = o + 1
                else :
                    print( " X", end=" ")
        
            print("%3d점" % (o * 10))
        

    print("\n------------------------------------------")

    

def ten() :
    
     
    x = []
    for i in range(0,10) :
        x.append(random.randrange(0,100))
        print(" %d" % x[q], end="")
    print("")

    result1 = max(x)
    print(result1)
    
    result2 = min(x)
    print(result2)
    
    result3 = sum(x)
    print(f"ave : {result3 / len(x)}")
    
    
    
    


def num_hap() :


    even_hap = 0

    for i in range(0,10) :
        if (i % 2) == 0 : 
            even_hap = even_hap + i
            print("%d even number sum = %d"% (i, even_hap))

    print("even number sum = %d"% even_hap)


    odd_hap = 0

    for i in range(0,10) :
        if (i % 2) == 1 : 
            odd_hap = odd_hap + i
            print("%d odd number sum = %d"% (i, odd_hap))
            
    print("even number sum = %d"% odd_hap)



while True :
    print("-------------------")
    print(" 1 : 채점          ")
    print(" 2 : 10개의 변수   ")
    print(" 3 : 구간 합 구하기")
    print(" 4 : 소감          ")
    print(" 5 : 종료          ")
    print("-------------------")
    
    n = input(" n: ")
    n = int(n)
    
    if n == 1 :
        print("채점")
        check()
        
    elif n == 2 :
        print("10개의 변수")
        ten()
    elif n == 3 :
        print("구간 합 구하기")
        num_hap()
        
    elif n == 4 :
        print("없어요")
        
    elif n == 5 :
        print("종료")
        exit(1)
        
    else :
        continue
