# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            cnt += 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        return cnt

    def numberOfStepsBitwise(self, num: int) -> int:
        cnt = 0
        while num > 0:
            cnt += 1
            if num & 1 == 0:  # bitwise operation and with returns 1 if odd else returns 0
                num >>= 1  # shift last bit by 1 to half the value
            else:
                num -= 1  # Simply substract 1
        return cnt
