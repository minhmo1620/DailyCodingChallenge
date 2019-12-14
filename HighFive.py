#link: https://leetcode.com/problems/high-five/submissions/
#result: 72ms, beat 93% time, 100% space
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key = lambda tup : tup[0])
        res = []
        d = dict()
        for i in items:
            if i[0] not in d:
                d[i[0]] = len(res)
                res.append([i[0], [i[1]]])
            else:
                res[d[i[0]]][1].append(i[1])
 
        new = []
        for i in res:
            if len(i[1]) >= 5:
                x = sorted(i[1], reverse = True)
                new.append([i[0], sum(x[:5])//5])
            else:
                new.append([i[0], sum(i[1])//len(i[1])])
        return new
