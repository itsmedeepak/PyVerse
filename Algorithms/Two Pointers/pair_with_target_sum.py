class TwoPointer:
    def pairWithTargetSum(self, arr, target):
        startIdx = 0
        endIdx = len(arr)-1
        
        while startIdx < endIdx:
            potentialSum = arr[startIdx] + arr[endIdx]
            if potentialSum == target:
                return [arr[startIdx], arr[endIdx]]
            elif potentialSum > target:
                endIdx -= 1
            else:
                startIdx += 1
    
    def pairWithTargetSumHash(self, arr, target):
        map_ = {}
        for i in range(len(arr)):
            y = target - arr[i]  # 9
            if y in map_:
                return [arr[i], y]
            else:
                map_[arr[i]] = True
        return [-1,-1]
        


arr = [2, 2, 5, 9, 11]
target=4
obj = TwoPointer()
print(obj.pairWithTargetSumHash(arr, target))

# target sum problem
