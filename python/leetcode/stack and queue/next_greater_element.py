class Solution:
    def nextGreaterElement(self, nums1: list[int], arr: list[int]) -> list[int]:
        n = len(arr)
        ans = {}

        st = []

        for i in range(n-1,-1,-1):
            while len(st)>0 and arr[i]>st[-1]:
                st.pop()
            if len(st)==0:
                ans[arr[i]] = -1
            else:
                ans[arr[i]] = st[-1]
            st.append(arr[i])

        res = []
        for i in nums1:
            res.append(ans[i])
        
        return res