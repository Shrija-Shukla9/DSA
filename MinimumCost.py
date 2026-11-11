
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        option1 = need1 * cost1 + need2 * cost2
        common = min(need1, need2)

        option2 = (common * costBoth +
                   (need1 - common) * cost1 +
                   (need2 - common) * cost2)
        option3 = max(need1, need2) * costBoth

        return min(option1, option2, option3)
