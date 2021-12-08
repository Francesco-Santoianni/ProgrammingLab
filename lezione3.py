values = []

my_file = open('shampoo_sales.txt', 'r')

for line in my_file:
    elements = line.split(',')
    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]

        values.append(float(value))

def sum_list(list):
    sum = 0
    for item in list:
        sum += item
    print(sum)

sum_list(values)