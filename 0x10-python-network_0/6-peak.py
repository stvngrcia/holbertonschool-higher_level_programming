#!/usr/bin/python3


def find_peak(nums):
    '''
        Finds the pick in a list of numbers
    '''
    length = len(nums) - 1

    for idx, value in enumerate(nums):
        if idx > 0 and idx < length:
            if nums[idx + 1] < value and nums[idx - 1] < value:
                pick = value
        else:
            if idx == 0 and nums[idx + 1] < value:
                pick = value
            elif idx == length and nums[idx - 1] < value:
                pick = value
    return pick
