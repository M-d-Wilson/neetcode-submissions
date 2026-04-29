class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        for x in nums: # Adds how many of each number are in the array
            if x in myDict:
                myDict[x] = myDict[x] + 1
            else:
                myDict[x] = 1
                
        returnArr = []

        for z in range(k): # Gets the biggest numbers and adds them to the return array
            max_key = max(myDict, key = myDict.get)
            myDict.pop(max_key)
            returnArr.append(max_key)

        print(myDict)
        return returnArr
        