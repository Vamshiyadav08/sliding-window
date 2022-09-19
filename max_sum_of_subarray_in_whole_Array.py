#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,Arr,n):
        # code here 
        
        sm = 0
        mx = 0
        i = j = 0 
        while(j<n):
            sm = sm + Arr[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                mx = max(mx,sm)
                sm = sm - Arr[i]
                j=j+1
                i = i+1
        return mx
                
                
