from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    
    answer = 0
    
    while people :
        heavy = people.pop()
        
        if len(people) > 0 and heavy + people[0] <= limit :
             people.popleft()
            
            
        answer +=1
            
    
    
   
    return answer