class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for word in strs:
            subAnagram = []
            print(strs)
            for gram in strs:
                if sorted(word) == sorted(gram):
                    subAnagram.append(gram)
            anagrams.append(subAnagram)
            for x in subAnagram:
                strs.remove(x)

            strs.insert(0, "|")
        return anagrams
                    