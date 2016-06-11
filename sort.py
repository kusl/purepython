def bubble(bad_list):
    length = len(bad_list) - 1
    unsorted = True
    while unsorted:
        for element in range(0, length):
            unsorted = False
            if bad_list[element] > bad_list[element + 1]:
                hold = bad_list[element + 1]
                bad_list[element + 1] = bad_list[element]
                bad_list[element] = hold
                print(bad_list)
            else:
                unsorted = True
