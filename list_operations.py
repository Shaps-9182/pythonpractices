def add_elements(lst, item):
    """Add an item to the end of the list."""
    lst.append(item)
    return lst


def remove_elements(lst, item):
    """Remove an item from the list if it exists."""
    if item in lst:
        lst.remove(item)
    return lst


def unique_elements(lst):
    """Remove duplicates."""
    a = []
    for i in lst:
        if i not in a:
            a.append(i)
    return a


def count_elements(lst, item):
    """Count the occurrences of an item in the list."""
    return lst.count(item)


def reverse_list(lst):
    """Reverse the list."""
    return lst[::-1]


def sort_list(lst):
    """Sort the list in descending order."""
    desc = sorted(lst, reverse=True)
    return desc


def merge_lists(lst1, lst2):
    """Merge two lists into one."""
    return lst1 + lst2


def clear_list(lst):
    """Clear all elements from the list."""
    lst.clear()
    return lst
