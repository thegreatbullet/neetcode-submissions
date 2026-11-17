class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        return Counter(s) == Counter(t)
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[T[i]] = 1 + countT.get(T[i], 0)
        for j in countS:
            if countS[j] != countT.get(j,0):
                return True
            return False
