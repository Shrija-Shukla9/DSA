class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            nxt[i] = stack[-1] if stack else n
            stack.append(i)

        LOG = n.bit_length()
        jump = [nxt]
        cost = [[
            nums[i] * (nxt[i] - i)
            - (pref[nxt[i]] - pref[i])
            for i in range(n)
        ]]
        for b in range(1, LOG):
            prev_jump = jump[-1]
            prev_cost = cost[-1]

            nj = [n] * n
            nc = [0] * n

            for i in range(n):
                mid = prev_jump[i]

                if mid < n:
                    nj[i] = prev_jump[mid]
                    nc[i] = prev_cost[i] + prev_cost[mid]
                else:
                    nc[i] = prev_cost[i]

            jump.append(nj)
            cost.append(nc)
        def getCost(l, r):
            cur = l
            total = 0

            for b in range(LOG - 1, -1, -1):
                dest = jump[b][cur]

                if dest <= r + 1:
                    total += cost[b][cur]
                    cur = dest

                    if cur == n:
                        break
            if cur <= r:
                total += (
                    nums[cur] * (r - cur + 1)
                    - (pref[r + 1] - pref[cur])
                )

            return total

        ans = 0
        for l in range(n):
            low, high = l, n - 1
            best = l - 1

            while low <= high:
                mid = (low + high) // 2

                if getCost(l, mid) <= k:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1

            ans += best - l + 1

        return ans
