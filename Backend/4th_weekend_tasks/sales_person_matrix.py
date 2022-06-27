def sales_per_salesperson_total(sales_list):
    total = 0
    for item in range(0, len(sales_list)):
        for row in sales_list:
            total += row[item]
            print(total)
            return total


def total_sales_for_each_product(sales_list):
    total = 0
    for row in sales_list:
        for i in row:
            total += sales_list[row][i]
            print(total)
            return total


# persons = len(sales_list[0])
# products = len(sales_list)

def company_sales_header(*sales_list):
    print(f"Sales Persons Column")
    for item in range(len(sales_list[0])):
        # if item < len(sales_list[0]):
        print([item], end=" ")
        print("")
    return sales_table(sales_list)


def sales_table(sales_list):
    for item in range(len(sales_list)):
        print("Products [%d]" % item, )
        for row in range(len(sales_list[0])):
            print('  '.join(map(str, sales_list[item][row])))
            # print(sales_list[item][row], " ")


test_list = [
    [21, 34, 54, 19],
    [24, 19, 53, 13],
    [21, 34, 12, 90],
    [23, 15, 18, 11],
    [20, 10, 17, 21]
]

print(company_sales_header(test_list))
