def is_consecutive(*a_list):
    """Determine if a list is consecutive"""
    for a_list in a_list[1:-1]:
        if a_list == [a_list + 1] - 1:
            print("Consecutive")
        else:
            print("Not Consecutive")

is_consecutive(1, 2, 3, 4, 5)