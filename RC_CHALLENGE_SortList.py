#CHALLENGE #2 - SORT A LIST

def sort_list(list, sort):
    if sort == "none":
        print(list)
    elif sort == "asc":
        list.sort()
        print(list)
    else:
        list.sort(reverse = True)
        print(list)

numList = [10, 8, 6, 5, 7, 9]
sort_list(numList,"none")
sort_list(numList,"asc")
sort_list(numList,"desc")

