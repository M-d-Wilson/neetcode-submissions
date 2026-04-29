class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for w in strs:
            mykey = [0] * 26
            for c in w:
                mykey[ord(c) - ord('a')] += 1
            groups.setdefault(tuple(mykey), []).append(w)
        print(groups.values())
        return list(groups.values())