class Solution:
    # Success
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash = {}
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hash.keys() and words[i] not in hash.values():
                hash[pattern[i]] = words[i]
            elif words[i] in hash.values() and pattern[i] not in hash.keys():
                return False
            elif words[i] != hash[pattern[i]]:
                return False
        return True
