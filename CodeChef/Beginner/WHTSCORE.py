for a in range(int(input())):
    n = int(input())
    Score = {}
    for i in range(n):
        p,s = map(int,input().split())
        if  p > 8 :  continue
        
        if  p in  Score.keys():
            if s > Score[p]:
                Score[p] = s 
        else:
            Score[p] = s 
    ans  = 0 
    for  k,v in  Score.items():
        ans  +=  v  
    print(ans)