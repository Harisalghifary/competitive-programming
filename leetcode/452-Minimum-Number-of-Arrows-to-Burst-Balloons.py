def findMinArrowShots(self, points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    count,anchor = 1, points[0][1]
    for start,end in points:
        if anchor < start:
            anchor = end
            count+=1
    return count