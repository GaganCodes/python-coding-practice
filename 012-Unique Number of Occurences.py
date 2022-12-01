class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Keeping a hashmap of all occurrences
        occurence = dict()

        for item in arr:
            if item in occurence:
                occurence[item] += 1
            else:
                occurence[item] = 1
        # Looping through the values of hashmaps to see if there are any duplicates
        occ_list = []
        for num_occ in occurence.values():
            if num_occ in occ_list:
                return False
            else:
                occ_list.append(num_occ)

        return True
