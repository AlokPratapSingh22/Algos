
def get_per_2(nums, x):

    for i in range(x, len(nums)):
        nums[x], nums[i] = nums[i], nums[x]
        get_per_2(nums, x+1)
        nums[x], nums[i] = nums[i], nums[x]

    if x == len(nums)-1:
        print(nums)
        return


def get_per_1(nums, ds, visited):
    if len(ds) == len(nums):
        print(ds)
        return

    for i in range(len(nums)):
        if not visited[i]:
            ds.append(nums[i])
            visited[i] = True
            get_per_1(nums, ds, visited)
            ds.pop()
            visited[i] = False


def all_permutations(arr: list):
    ds = []
    visit = [False]*len(arr)
    get_per_1(arr, ds, visit)
    get_per_2(arr, 0)


all_permutations([1, 2, 3])
