class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        FN_0=coordinates[0][0]
        FN_1=coordinates[0][1]
        SN_0=coordinates[1][0]
        SN_1=coordinates[1][1]
        if FN_1==SN_1:
            for point in coordinates[2:]:
                if point[1]!=FN_1:
                    return False
            return True
        rate=(SN_0-FN_0)/(SN_1-FN_1)
        for point in coordinates[2:]:
            if point[1]-FN_1==0:
                return False
            cur_rate=(point[0]-FN_0)/(point[1]-FN_1)
            if cur_rate!=rate:
                return False
        return True
