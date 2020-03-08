""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Program for Best Fit algorithm in Memory
Management.
Implementation:
1- Input memory blocks and processes with
   sizes.
2- Initialize all memory blocks as free.
3- Start by picking each process and find the
   minimum block size that can be assigned to
   current process i.e., find min(bockSize[1], 
   blockSize[2],.....blockSize[n]) > 
   processSize[current], if found then assign 
   it to the current process.
5- If not then leave that process and keep
   checking the further processes.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""

# BestFit Function.
def bestFit(blockSize, m, processSize, n):  
    # Stores block id of the block  
    # allocated to a process  
    allocation = [-1] * n  
    # pick each process and find suitable  
    # blocks according to its size ad  
    # assign to it 
    for i in range(n):      
        # Find the best fit block for 
        # current process  
        bestIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if bestIdx == -1:  
                    bestIdx = j  
                elif blockSize[bestIdx] > blockSize[j]:  
                    bestIdx = j 
        # If we could find a block for  
        # current process  
        if bestIdx != -1:  
            # allocate block j to p[i] process  
            allocation[i] = bestIdx  
            # Reduce available memory in this block.  
            blockSize[bestIdx] -= processSize[i] 
    print("Process No.-Process Size-Block no.") 
    for i in range(n): 
        print(i + 1, "      ", processSize[i],
        end = "      ")  
        if allocation[i] != -1:  
            print(allocation[i] + 1)  
        else: 
            print("Not Allocated")

# Main Function.
def main():
    b = [100, 500, 200, 300, 600]  
    p = [212, 417, 112, 426]  
    m = len(b)  
    n = len(p)  
    bestFit(b, m, p, n)

# Driver Code.
if __name__ == "__main__":
    main()