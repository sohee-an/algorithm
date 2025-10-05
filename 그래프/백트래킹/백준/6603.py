while True:
    nums = list(map(int, input().split()))
  
    if nums[0] == 0:  # 종료 조건
        break
    k = nums[0]
    arr = nums[1:]
    path=[]
   
   
    def dfs(start,depth):
        if depth==6:
            print(*path)
            return
        for i in range(start,k):            
            path.append(arr[i])          
            dfs(i+1,depth+1)            
            path.pop()
        
      

    dfs(0,0)
    print()


