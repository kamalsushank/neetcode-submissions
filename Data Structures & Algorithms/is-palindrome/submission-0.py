class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0 
        r = len(s)-1
        pat = "abcdefghijklmnopqrstuvwxyz1234567890"
        while l<=r:
            if s[l] not in pat:
                l+=1
            elif s[r] not in pat :
                r-=1
            else:
                if s[l] != s[r]:
                    return False
                else:   
                    l+=1
                    r-=1
        return True