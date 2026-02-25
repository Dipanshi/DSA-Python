#Merge all overlapping intervals and return a list of non-overlapping intervals that cover the same ranges.
# Intervals = [[1,3], [2,6], [8,10], [15,18]]
# Step 1: Understand overlaps
# [1,3] and [2,6] overlap
# [8,10] does not overlap with [1,6]
# [15,18] does not overlap with others
# Step 2: Merge overlapping intervals
# [1,3] and [2,6] → merge into [1,6]
# So final result: [[1,6], [8,10], [15,18]]

def MergeInterval(intervals):
    intervals.sort(key=lambda x :x[0])
    merge=[intervals[0]]
    for current in intervals[1:]:
        last=merge[-1]
        if current[0]<=last[1]:
            merge[-1]=[last[0],max(last[1],current[1])]
        else:
            merge.append(current)

    return merge

Intervals = [[1,3], [2,6], [8,10], [15,18]]
print(MergeInterval(Intervals))