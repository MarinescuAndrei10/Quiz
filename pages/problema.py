
def find_duplicates_with_loop(nums):
    seen=set()
    duplicates=[]
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

def find_duplicates_with_comprehensions(nums):
    seen=set()
    return [num for num in nums if num in seen or seen.add(num) is not None]

def find_duplicates_no_aux(nums):
    duplicates = []
    for i in range(len(nums)):
        idx=abs(nums[i]) -1 
        if nums[idx] < 0 :
            duplicates.append(abs(nums[i]))
        else:
            nums[idx]=-nums[idx]
    for i in range(len(nums)):
        nums[i]=abs(nums[i])
    return duplicates 




nums =[4,3,2,7,8,2,3,1]
print("Am gasit:",find_duplicates_with_loop(nums))
print("Am gasit:",find_duplicates_with_comprehensions(nums))
print("Am gasit:",find_duplicates_no_aux(nums))