class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp_list=[]
        res=[]
        def solution(start,sum):
            if sum(temp_list) > target:
                return
            if sum(temp_list)==target:
                res.append(temp_list[:])
                
                return
            

            
            for i in range(start,len(candidates)):
               
                temp_list.append(candidates[i])
                solution(i)
                temp_list.pop()


        solution(0)
        return res
        