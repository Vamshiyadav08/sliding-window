
class Solution:
    def maxSlidingWindow(self, Arr: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        que = []
        quepop = []
        for i in range(len(Arr)):
            while q and Arr[q[-1]]<=Arr[i]:
                q.pop() 
                
            q.append(i)#we are appending index values
            if q[0]<=i-k:
                q.popleft()#sliding window is out of
            if i>=k-1:
                res.append(Arr[q[0]])
        return res
            
        #first we append elements
        #Then we check whether the elements list [1,1,1,4] 0,1,2,3
        #when i is incresed to 3 we check whether previos elements are lesser or no if less we pop it out
        #when we increse the i value we check with quees last element is lesser with iincremented value or not if yes we pop out the ele 
        
        
        
                
            
            
                
                
                
            
                

        
        
                
        
      
            
            
                
                
        
