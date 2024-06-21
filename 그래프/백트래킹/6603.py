from itertools import combinations

while True:
    # 한 줄의 입력을 받음
    line = input().split()
    
    # 첫 번째 숫자를 k로 설정
    k = int(line[0])
    
    # k가 0이면 종료
    if k == 0:
        break
    
    # 나머지 숫자 리스트
    s = list(map(int, line[1:]))
    
    
    temp_list=[]
    def solution(start,s):
        if len(temp_list)==6:
            print(' '.join(map(str,temp_list)))
            return 
        
        for i in range(start,k):
            temp_list.append(s[i])
            solution(i+1,s)
            temp_list.pop()
        
    solution(0,s)
    
  
    print()
