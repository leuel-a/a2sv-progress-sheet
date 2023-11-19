class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)

        dict_s = set()
        for val in count.values():
            if val in dict_s:
                return False
            dict_s.add(val)
        return True