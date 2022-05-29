def sort_employees(employees, sort_by):
    new_list = employees[:]
    def func_sort(lst):
        if sort_by == "name":
            return lst[0]
        if sort_by == "age":
            return lst[1]
        if sort_by == "salary":
            return lst[2]
    
    #sorted(new_list, key=func_sort)
    new_list.sort(key=func_sort)
    return new_list


employees = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 10000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]

sort_by = "age"

print(sort_employees(employees, sort_by))