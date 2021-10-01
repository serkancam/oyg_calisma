#%% liste ile
import time
def seq(start,end):
    lst = []
    for i in range(start,end):
        lst.append(i)
    return lst

start_time = time.time()
data = seq(100,100_000_000)
print(len(data))
end_time = time.time()
print(f"execution time: {end_time - start_time}")

#%% generator ile
import time
def seq(start,end):
    lst = []
    for i in range(start,end):
        yield i

start_time = time.time()
data = seq(100,100_000_000)
print(next(data))
print(next(data))
print(next(data))
end_time = time.time()
print(f"execution time: {end_time - start_time}")
# %%
class Solution:
    def twoSum(self, nums, target) :
        i=0
        while i<len(nums):
            kalan = target-nums[i]
            try:

                j = nums.index(kalan,i+1)
               
                return [i,j]
            except:
                pass
            finally:
                i=i+1
                
                
            
            
            
nums = [3,2,4]
c = Solution()
print(c.twoSum(nums,6))


# %%
