class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for x in nums:
            if x in myDict:
                myDict[x] = myDict[x] + 1
            else:
                myDict[x] = 1

        returnArr = []

        for z in range(k):
            max_key = max(myDict, key = myDict.get)
            myDict.pop(max_key)
            returnArr.append(max_key)

        print(myDict)
        return returnArr
        