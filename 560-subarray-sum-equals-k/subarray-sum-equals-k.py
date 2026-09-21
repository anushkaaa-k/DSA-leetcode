class Solution(object):
    def subarraySum(self, nums, k):
        mpp = {0:1}
        presum = 0
        cnt = 0
        for num in nums:
            presum +=num
            remove = presum -k
            if remove in mpp:
                cnt += mpp[remove]
            mpp[presum]= mpp.get(presum,0) + 1
        return cnt
        