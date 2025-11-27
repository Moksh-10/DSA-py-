def get_estimated_spread(audiences_followers):
    num_fol = len(audiences_followers)
    if num_fol == 0:
        return 0
    sum = 0
    for n in audiences_followers:
        sum += n
    avg = sum / num_fol
    return avg * (num_fol ** 1.2)


def decayed_followers(intl_followers, fraction_lost_daily, days):
    # for i in days:
    return intl_followers * ((1 - fraction_lost_daily) ** days)


def num_possible_orders(num_posts):
    p = 1
    for i in range(1, num_posts + 1):
        p *= i
    return p


def get_follower_prediction(follower_count, influencer_type, num_months):
    factor = 2
    match influencer_type:
        case "fitness":
            factor = 4
        case "cosmetic":
            factor = 3
    return follower_count * (factor ** num_months)


import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)


def find_minimum(nums):
    if len(nums) == 0:
        return None
    min = float("inf")
    for i in nums:
        if i < min:
            min = i
    return min


def summed(nums):
    s = 0
    for n in nums:
        s += n
    return s


import math
def log_scale(data, base):
    a = []
    for i in data:
        a.append(math.log(i, base))
    return a


def average_followers(nums):
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)


def find_max(nums):
    max = float("-inf")
    for i in nums:
        if i > max:
            max = i
    return max


def does_name_exist(first_names, last_names, full_name):
    for i in first_names:
        for j in last_names:
            if f'{i} {j}' == full_name:
                return True
    return False


def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    avg = count / len(all_handles)
    return avg


def find_last_name(names_dict, first_name):
    # for current_first_name, last_name in names_dict.items():
    #     if current_first_name == first_name:
    #         return last_name
    return names_dict.get(first_name)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # return fib(n-1) + fib(n-2)
    current = 0
    parent = 1
    grandparent = 0
    for i in range(0, n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current

# print(fib(30))


def power_set(inp_set):
    if len(inp_set) == 0:
        return [[]]

    subsets = []
    first = inp_set[0]
    rem = inp_set[1:]
    rem_subs = power_set(rem)
    for subset in rem_subs:
        subsets.append([first] + subset)
        subsets.append(subset)
    return subsets


def cm(job_titles):
    count = 0
    for jb in job_titles:
        if jb.lower() == "something":
            count += 1
    return count


