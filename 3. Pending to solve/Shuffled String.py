class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        k = []
        for i in range(len(s)):
            k.append(s[indices.index(i)])
        return ''.join(k)
