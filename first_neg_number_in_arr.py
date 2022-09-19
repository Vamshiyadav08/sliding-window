from collections import deque
def printFirstNegativeInteger( A, N, k):
    # code here
    i = j =0
    res = []
    q = deque()
    while(j<N):
        if A[j]<0:
            q.append(A[j])
        
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            if len(q)==0:
                res.append(0)
            else:
                res.append(q[0])
                if A[i]==q[0]:
                    q.popleft()
            i+=1
            j+=1
   
    return res
            
