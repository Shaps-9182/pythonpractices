import list_operations as lo

# Example usage
my_list = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9, 9, 1]
print("Original list :", my_list)
print("Add element 10:", lo.add_elements(my_list, 10))
print("Remove element 4:", lo.remove_elements(my_list, 4))
print("Remove duplicates:", lo.unique_elements(my_list))
print("count occurrences of 7:", lo.count_elements(my_list, 7))
print("Reverse list:", lo.reverse_list(my_list))
print("Sort list (descending):", lo.sort_list(my_list))
print("Merge lists:", lo.merge_lists(my_list, [10, 11, 12, 15, 13, 14]))
print("Clear list:", lo.clear_list(my_list))
