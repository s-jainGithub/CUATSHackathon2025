class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums = sorted(nums)
        output = []
        #First sort the list in O(nlogn) time
        #Then use a two pointer approach
        i=0
        while nums[i]<=0:
            I = nums[i]
            l = i+1
            r = N-1
            while r>l:
                L = nums[l]
                R = nums[r]
                total = I+L+R
                if R<0:
                    break
                if total==0:
                    output.append([I,L,R])
                    while nums[l]==L:
                        l+=1
                        if l==N:
                            break
                    while nums[r]==R:
                        r-=1
                        if r==-1:
                            break
                elif total<0:
                    while nums[l]==L:
                        l+=1
                        if l==N:
                            break
                else:
                    while nums[r]==R:
                        r-=1
                        if r==-1:
                            break
            while nums[i]==I:
                i+=1
                if i==N:
                    return output
        return output
