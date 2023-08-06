from typing import List


class Solution:
    def getLettersOfNumber(self, number: str) -> List[str]:
        if number == "2":
            return ["a", "b", "c"]
        elif number == "3":
            return ["d", "e", "f"]
        elif number == "4":
            return ["g", "h", "i"]
        elif number == "5":
            return ["j", "k", "l"]
        elif number == "6":
            return ["m", "n", "o"]
        elif number == "7":
            return ["p", "q", "r", "s"]
        elif number == "8":
            return ["t", "u", "v"]
        elif number == "9":
            return ["w", "x", "y", "z"]
        
    def getLetterCombinations(self, digits: str, letters: List) -> List[str]:
        if len(digits) == 0:
            return letters
                
        currDigit = digits[0]
        currLetters = self.getLettersOfNumber(currDigit)
        newLetters = []

        if len(letters) == 0:
            return self.getLetterCombinations(digits[1:], currLetters)

        for letter in letters:
            for currLetter in currLetters:
                newLetters.append(letter + currLetter)
        
        return self.getLetterCombinations(digits[1:], newLetters)
        

    def letterCombinations(self, digits: str) -> List[str]:
        # print(self.getLetterCombinations(digits, list()))
        return self.getLetterCombinations(digits, list())

        
        


sol = Solution()
sol.letterCombinations("22")