# Link: https://leetcode.com/problems/partition-labels/submissions/


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = dict()

        for i in range(len(S)):
            if S[i] not in d:
                d[S[i]] = [i, i]
            else:
                d[S[i]][1] = i

        L = 0
        R = d[S[L]][1]
        res = []
        while True:
            if L > R:
                break

            if L < R:
                i = L
                tmp = dict()
                while i < R:
                    if S[i] not in tmp:
                        tmp[S[i]] = 1
                        R = max(R, d[S[i]][1])
                    i += 1

            if R >= len(S) - 1:
                break
            else:
                res.append(R - L + 1)
            L = R + 1
            R = d[S[L]][1]

        if R == len(S) - 1:
            res.append(R - L + 1)
        return res
