class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}
        h_map = {}

        for i in range (len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1 

            if t[i] in h_map:
                h_map[t[i]] += 1
            else:
                h_map[t[i]] = 1 
        
        return hash_map == h_map




        