class Solution:

		"""
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

		def topKFrequent(self, nums, k):
				# Decalare the out lis and data dictionary
		        data, res = {}, []
		        # Loop input list Polulate the data dictionary
		        for i in nums:
		            data[i] = data[i] + 1 if i in data else 1
		        # Sort the data dictionary
		        sorted_data = sorted(data.iteritems(), key=operator.itemgetter(1), reverse=True)
		        # Fetch the Top K
		        for i in xrange(k):
		            res.append(sorted_data[i][0])
		        return res
