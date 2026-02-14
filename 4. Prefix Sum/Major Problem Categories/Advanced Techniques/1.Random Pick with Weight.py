# Pick index with probability proportional to weight
# Initialize - O(n),Pick random index - O(log n)

import random
import bisect

class RandomPickWeight:
    def __init__(self,weights):
        total=0
        self.prefix_sum=[]
        for i,w in enumerate(weights):
            total+=w
            self.prefix_sum.append(total)
        
    def pickindex(self):
        r_num= random.randint(1,self.prefix_sum[-1])
        print(r_num)
        ixd=bisect.bisect_left(self.prefix_sum,r_num)
        return ixd

rpw = RandomPickWeight([1, 3, 2, 4])
print(rpw.pickindex())

        