#link:https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        d = dict()
        res = []
        for i in folder:
            check = "/"
            flag = True
            if len(i) == 2:
                res.append(i)
                d[i] = 1
                continue
            for j in range (1,len(i)):
                if i[j] != "/":
                    check += i[j]
                else:
                    if check in d:
                        flag = False
                        break
                    else:
                        check += i[j]
            if flag:
                print(check)
                d[check] = 1
                res.append(check)
        return res
                
                
