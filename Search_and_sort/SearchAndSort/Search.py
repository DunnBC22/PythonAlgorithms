class Search:
    def __init__(self):
        pass

    @staticmethod
    def seq_search(what_to_search, for_what):
        found = False
        pos = 0
        while ((pos < len(what_to_search)) and (found == False)):
            if (what_to_search[pos] == for_what):
                found = True
            else:
                pos += 1
        return (pos)

    @staticmethod
    def remove_all_duplicates(a_list):
        return list(set(a_list))

    @ staticmethod
    def binary_search(what_to_search, for_what):
        '''requires that the data structure is sorted'''
        first = 0
        last = len(what_to_search)-1
        found = False
        while first <= last and found == False:
            mid = (first + last)//2
            if (what_to_search[mid] == for_what):
                found = True
            else:
                if (what_to_search[mid] > for_what):
                    last = mid - 1
                elif(what_to_search[mid] < for_what):
                    first = mid + 1
        return mid


'''
alternative for the remove all duplicates (but it took longer to complete):
  output_list = []
        for x in a_list:
            if x not in output_list:
                output_list.append(x)
        return output_list
'''
