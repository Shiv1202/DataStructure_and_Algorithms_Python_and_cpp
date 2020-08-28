# def countSquares(X,  Y, N) : 
#     count = 0;   
#     points = [];    
#     vertical = dict.fromkeys(X, None);  
#     print(vertical)
#     for i in range(N) : 
#         points.append((X[i], Y[i])); 
#     for i in range(N) : 
#         if vertical[X[i]] is None : 
#             vertical[X[i]] = [Y[i]]; 
#         else : 
#             vertical[X[i]].append(Y[i]);  
#     for line in vertical : 
#         X1 = line;  
#         yList = vertical[line];  
  
#         for i in range(len(yList)) : 
#             Y1 = yList[i];  
#             for j in range(i + 1, len(yList)) : 
#                 Y2 = yList[j];  
#                 side = abs(Y1 - Y2);  
#                 X2 = X1 + side; 
#                 if ( X2, Y1 ) in points and ( X2, Y2 ) in points :  
#                     count += 1; 
  
#     return count;  
  
# # Driver Code  
# if __name__ == "__main__" :  
#     n = int(input())
#     X, Y = [], []
#     for i in range(n):
#         x, y = map(int, input().split())
#         X.append(x)
#         Y.append(y)
  
#     print(countSquares(X, Y, n)); 



def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in range(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B

A = list(map(int, input().split()))
B = performOps(A)
for i in range(len(B)):
    print(B[i])