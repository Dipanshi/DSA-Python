import random

class RandomPickBlacklist:
    """
    Pick random number from [0, n) excluding blacklist
    O(B) preprocessing, O(1) pick where B = blacklist size
    """
    def __init__(self, n, blacklist):
        self.n = n - len(blacklist)
        self.remap = {}
        
        # Create mapping for blacklisted numbers in [0, n)
        blacklist_set = set(blacklist)
        
        # Find valid numbers at the end
        last = n - 1
        for b in blacklist:
            if b < self.n:  # Only remap blacklisted in range
                # Find next valid number from end
                while last in blacklist_set:
                    last -= 1
                self.remap[b] = last
                last -= 1
    
    def pick(self):
        """Pick random number"""
        num = random.randint(0, self.n - 1)
        return self.remap.get(num, num)

# Usage:
rp = RandomPickBlacklist(7, [2, 3, 5])
# Can return: 0, 1, 4, 6 with equal probability
print(rp.pick())