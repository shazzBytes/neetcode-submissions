class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        # in the list the key is element and value is count
        freq = []
        for n, cnt in count.items():
            freq.append([cnt, n])
        freq.sort()

        # now the elements are sorted according to their 
        # frequency in the array in
        # ascending order
        tfreq = []
        while len(tfreq) < k:
            tfreq.append(freq.pop()[1])

        return tfreq