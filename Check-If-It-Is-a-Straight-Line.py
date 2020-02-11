#link:https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        else:
            if (coordinates[1][0] - coordinates[0][0]) != 0:
                a = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
                b = coordinates[0][1] - a * coordinates[0][0]

                flag = True
                for i in range (len(coordinates)):
                    if (coordinates[i][0] * a + b) != float(coordinates[i][1]):
                        # print(coordinates[i][0] * a + b,float(coordinates[i][1]) )
                        return False
                return True
            else:
                for i in range (len(coordinates)):
                    if coordinates[i][0] != coordinates[0][0]:
                        return False
                return True
