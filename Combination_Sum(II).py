'''Problem : COMBINATION  SUM II '''


# CODE :

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        dp = [set() for _ in range(target + 1)]
        dp[0].add(())
        for c in candidates:
            for subtarget in reversed(range(len(dp))):
                if dp[subtarget]:
                    new_combo = set([combo + (c, ) for combo in dp[subtarget]])
                    if subtarget + c <= target:
                        dp[subtarget + c] = dp[subtarget + c].union(new_combo)
        return list(map(list, dp[target]))
