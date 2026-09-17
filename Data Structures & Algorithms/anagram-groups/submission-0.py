class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for n in strs:
            anagram.setdefault(''.join(sorted(n)),[]).append(n)
        anagrams = list(anagram.values())
        return anagrams

                
        