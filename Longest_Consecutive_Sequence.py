'''Problem : Longest Consecutive Sequence '''

#CODE :

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        segments = {}
        reversedSegments = {}
        for item in set(num):
            if item in segments and item in reversedSegments:
                newEnd = segments[item]
                del segments[item]
                newBegin = reversedSegments[item]
                del reversedSegments[item]
                segments[newBegin-1] = newEnd
                reversedSegments[newEnd+1] = newBegin
            elif item in segments:
                oldEnd = segments[item]
                del segments[item]
                segments[item-1] = oldEnd
                reversedSegments[oldEnd+1] = item
            elif item in reversedSegments:
                oldBegin = reversedSegments[item]
                del reversedSegments[item]
                segments[oldBegin-1] = item
                reversedSegments[item+1] = oldBegin
            else:
                
                segments[item-1] = item
                reversedSegments[item+1] = item
        
        maxLen = 0
        for segmentBegin in segments:
            segmentEnd = segments[segmentBegin]
            maxLen = max(maxLen, segmentEnd- segmentBegin)
        return maxLen
