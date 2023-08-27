def solution(info, edges):
    
    visited = [0] * len(info)
    result = []
    def dfs(wolf, sheep) :
        
        if wolf < sheep :
            result.append(sheep)
        else :
            return
        
        for i, j in edges : #i는 부모노드, j는 자식노드
            #부모노드는 방문했지만 자식노드는 아직 방문안했을경우
            if visited[i] and not visited[j] : 
                visited[j] = 1
                if info[j] == 0 :
                    dfs(wolf, sheep + 1)
                else :
                    dfs(wolf+1, sheep)
                
                visited[j] = 0
                
    visited[0] = 1
    dfs(0,1)
    answer = max(result)

    return answer