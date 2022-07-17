from typing import List


class Solution:
    # Success
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for str in strs:
            totAscii = self.getKey(str)
            if totAscii in hash.keys():
                hash[totAscii].append(str)
            else:
                hash[totAscii] = [str]

        return [val for val in hash.values()]

    def getKey(self, str: str) -> int:
        return ''.join(sorted(str))
