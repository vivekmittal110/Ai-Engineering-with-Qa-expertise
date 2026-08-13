class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        if len(s)%2==1:
            return False
        
        for i in list(s):
            if i == "(" or i == "[" or i == "{":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                top = st.pop()

                if i == ")" and top != "(":
                    return False
                if i == "}" and top != "{":
                    return False
                if i == "]" and top != "[":
                    return False
        return len(st)==0

s = Solution()
print(s.isValid("{[]}"))