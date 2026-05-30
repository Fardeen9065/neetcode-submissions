class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strr = ""
        for i in s:
            if (i >= "a" and i <= "z") or (i >= "0" and i <= "9"):
                strr += i
        i = 0
        j = len(strr)-1
        while i < j:
            if strr[i] != strr[j]:
                return False
            i += 1
            j -= 1
        return True
        