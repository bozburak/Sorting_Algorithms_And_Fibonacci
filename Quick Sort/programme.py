#!/usr/bin/env python
# -*- coding: UTF-8 -*-

author = "Burak BOZ"
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) / 2]
    small_numbers = [x for x in arr if x < pivot]
    numbers = [x for x in arr if x == pivot]
    big_numbers = [x for x in arr if x > pivot]

    return quick_sort(small_numbers) + numbers + quick_sort(big_numbers)


print quick_sort([32,1,67,2,87,89])
