def solution(numbers, target):
    answer = 0
    
    def dfs(index, result):
        
        if index == len(numbers) and result == target:
            nonlocal answer
            answer += 1
            return
        
            
        if index < len(numbers):
            dfs(index+1, result + numbers[index])
            dfs(index+1, result - numbers[index])
            
            
    dfs(0,0)
    
    return answer