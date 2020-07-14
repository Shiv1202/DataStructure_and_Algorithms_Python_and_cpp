class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        output_intersections = []
        ptr_1 = ptr_2 = 0
        
        while ptr_1 < len(A) and ptr_2 < len(B):
            start_interval = max(A[ptr_1][0], B[ptr_2][0])
            end_interval = min(A[ptr_1][1], B[ptr_2][1])
            
            if start_interval <= end_interval:
                output_intersections.append([start_interval, end_interval])
                
            if A[ptr_1][1] < B[ptr_2][1]:
                ptr_1 += 1
            else:
                ptr_2 += 1
        return output_intersections
