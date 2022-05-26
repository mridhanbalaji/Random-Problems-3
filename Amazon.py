class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # arr.sort()
        newarr = []
        final = []
        # lowdifference = arr[1] - arr[0]
        # for i in arr:
        #     for j in arr:
        #         if i - j == lowdifference:
        #             newarr.append([j,i]) 
        # return newarr
        
        for i in arr:
            for j in arr:
                a = abs(i - j)
                newarr.append(a)
        newarr.sort()
        newarr = [i for i in newarr if i != 0]
        
        for i in arr:
            for j in arr:
                if i - j == newarr[0]:
                    final.append([j,i])
        
        final.sort()
        return final
                    
                    