class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        like_dict = {}
        for pair in dislikes:
            if pair[0] in like_dict:
                like_dict[pair[0]].add(pair[1])
            else:
                like_dict[pair[0]] = set([pair[1]])
            if pair[1] in like_dict:
                like_dict[pair[1]].add(pair[0])
            else:
                like_dict[pair[1]] = set([pair[0]])
                
        room_wise = {}
        for i in range(1, N + 1):
            if i not in room_wise:
                room_wise[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    if a in like_dict:
                        for b in like_dict[a]:
                            if b in room_wise:
                                if room_wise[a] == room_wise[b]:
                                    return False
                            else:
                                room_wise[b] = (room_wise[a] + 1) % 2
                                stack.append(b)
        return True
