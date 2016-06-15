def bubble(bad_list):
    length = len(bad_list) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i + 1]:
                is_sorted = False
                bad_list[i], bad_list[i + 1] = bad_list[i + 1], bad_list[i]
                print(bad_list)
    return bad_list
