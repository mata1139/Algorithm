def solution(n, computers):
    answer =0 
    
    visited = [0 for i in range(n)]
    
    def dfs(now):
        if visited[now] == 0:
            visited[now] = 1
                
        for i in range(n):
            if computers[now][i] == 1 and visited[i] == 0:
                dfs(i)
                
                
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer+=1
                
      
    return answer