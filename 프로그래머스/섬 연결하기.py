def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) 
    
    link = set([costs[0][0]])


    while len(link) != n:
        
        for vertics in costs:
            if vertics[0] in link and vertics[1] in link:
                continue
                
            if vertics[0] in link or vertics[1] in link:
                link.update([vertics[0], vertics[1]])
                answer += vertics[2]
                break
                
    return answer