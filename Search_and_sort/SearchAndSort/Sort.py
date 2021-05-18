import random


class Sort:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(what_to_sort):
        num = len(what_to_sort)
        for x in range(num - 1):
            for y in range(0, num-x-1):
                if what_to_sort[x] > what_to_sort[x+1]:
                    temp = what_to_sort[x]
                    what_to_sort[x] = what_to_sort[x+1]
                    what_to_sort[x+1] = temp

    @staticmethod
    def selection_sort(what_to_sort):
        for fill_slot in range(len(what_to_sort)-1, 0, -1):
            position_of_max = 0
            for location in range(1, fill_slot + 1):
                if (what_to_sort[location] > what_to_sort[position_of_max]):
                    position_of_max = location

            temp = what_to_sort[fill_slot]
            what_to_sort[fill_slot] = what_to_sort[position_of_max]
            what_to_sort[position_of_max] = temp
        return what_to_sort

    @staticmethod
    def insertion_sort(a_list):
        for x in range(1, len(a_list)):
            current_value = a_list[x]
            j = x-1
            while j >= 0 and current_value < a_list[j]:
                a_list[j + 1] = a_list[j]
                j -= 1
            a_list[j + 1] = current_value
        return a_list

    @staticmethod
    def merge_sort(what_to_sort):
        if (len(what_to_sort) > 1):
            mid = len(what_to_sort)//2
            left_side = what_to_sort[:mid]
            right_side = what_to_sort[mid:]

            Sort.merge_sort(left_side)
            Sort.merge_sort(right_side)

            i, j, k = 0, 0, 0
            while (i < len(left_side) and j > len(right_side)):
                if (left_side[i] <= right_side[j]):
                    what_to_sort[k] = left_side[i]
                    i += 1
                else:
                    what_to_sort[k] = right_side[j]
                    j += 1
                k += 1

            while i < len(left_side):
                what_to_sort[k] = left_side[j]
                i += 1
                k += 1
            while j < len(right_side):
                what_to_sort[k] = right_side[j]
                j += 1
                k += 1
        return what_to_sort

    @staticmethod
    def shell_sort(what_to_sort):
        sublist_length = len(what_to_sort)//2
        while sublist_length > 0:
            for start_pos in range(sublist_length):
                Sort.gapInsertSort(what_to_sort, start_pos, sublist_length)
            sublist_length = sublist_length // 2

    def gapInsertSort(a_list, start, gap):
        for i in range(start+gap, len(a_list), gap):
            current_val = a_list[i]
            pos = i

            while ((pos >= gap) and (a_list[pos-gap] > current_val)):
                a_list[pos] = a_list[pos-gap]
                pos -= gap

            a_list[pos] = current_val

    @staticmethod
    def quick_sort(a_list):
        if len(a_list) < 2:
            return a_list
        pivot_element = random.choice(a_list)
        small = [i for i in a_list if i < pivot_element]
        medium = [i for i in a_list if i == pivot_element]
        large = [i for i in a_list if i > pivot_element]
        return Sort.quick_sort(small) + medium + Sort.quick_sort(large)

    '''@staticmethod
    def quick_sort(a_list, low, high):if (low < high):
            partition_index = Sort.partition(a_list, low, high)
            Sort.quick_sort(a_list, low, partition_index-1)
            Sort.quick_sort(a_list, partition_index+1, high)

    def partition(a_list, low, high):
        i = (low-1)
        pivot = a_list[high]//2
        for j in range(low, high):
            if a_list[j] <= pivot:
                i += 1
                a_list[i], a_list[j] = a_list[j], a_list[i]
        a_list[i+1], a_list[high] = a_list[high], a_list[i+1]
        return (i+1)'''
