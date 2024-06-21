class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result =[]


        def backtrack(start, total_val, path):
            if total_val == target:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if total_val + candidates[i] > target:
                    return
                elif i> start and candidates[i] == candidates[i-1]:
                    continue
                else:
                    backtrack(i+1, total_val+candidates[i], path +[candidates[i]])
        backtrack(0,0,[])
        return result