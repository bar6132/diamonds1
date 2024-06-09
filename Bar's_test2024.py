import time


path = 'diamonds1.csv'
with open(path, 'r') as fh:
    lines = fh.readlines()

header = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]
"""carat,cut,color,clarity,depth,table,price,x,y,z"""


def most_expensive(data):
    """adding price number to list and print reverse the list form high to low
     and print the first price == most expensive price"""
    cost = 0
    for row in data:
        price = float(row[6])
        if price > cost:
            cost = price
    print('The most expensive diamond price is:', cost, '$')


def avg_cost(data):
    """adding price number to list sum the list and divide by the len of the list
    average_price = (sum(cost) / len(cost))"""
    cost = []
    for row in data:
        cost.append(int(row[6]))
    average_price = (sum(cost) / len(cost))
    return print('The average price of diamond is :', average_price, '$')


def ideal_count(data):
    """find all ideal cut , add all to list
    and print the len of the list == count of ideal"""
    ideal_list = []
    for row in data:
        if 'Ideal' in row:
            ideal_list.append('Ideal')
    return print('The number the ideal diamonds is :', (len(ideal_list)))


def color(data):
    """create color list , make the set so only one color is showed
     the print the len of the set to see the number of colors and the set itself
     to see the names"""
    color_set = set()
    for row in data:
        color_set.add(row[2])  # Assuming the color is in the 3rd column

    print('The number of colors is:', len(color_set))
    print('The names of colors are:', color_set)


def half(data):
    """put all premium diamonds is list sort them
     cut the list in half and pick the number
     from the list in the place we cut """
    carat = [float(row[0]) for row in data if 'Premium' in row]

    carat.sort()
    mid = len(carat) // 2

    if len(carat) % 2 == 0:
        median = (carat[mid - 1] + carat[mid]) / 2
    else:
        median = carat[mid]

    print('The median of Premium diamonds carats:', median, 'carats')


def color_avg(data):
    """Calculate the average price per color using dictionaries for efficiency."""
    color_prices = {}
    color_counts = {}

    for columns in data:
        color = columns[2]
        price = int(columns[6])

        if color in color_prices:
            color_prices[color] += price
            color_counts[color] += 1
        else:
            color_prices[color] = price
            color_counts[color] = 1

    for color in color_prices:
        avg_price = color_prices[color] / color_counts[color]
        print(f'The avg price for {color} is: {avg_price}')


def cut_avg(data):
    """Calculate the average carat weight per cut using dictionaries for efficiency."""
    cut_weights = {}
    cut_counts = {}

    for columns in data:
        cut = columns[1]
        carat = float(columns[0])

        if cut in cut_weights:
            cut_weights[cut] += carat
            cut_counts[cut] += 1
        else:
            cut_weights[cut] = carat
            cut_counts[cut] = 1

    for cut in cut_weights:
        avg_carat = cut_weights[cut] / cut_counts[cut]
        print(f'The avg carat of {cut} diamonds is: {avg_carat}')


start_time = time.time()
most_expensive(data)
avg_cost(data)
ideal_count(data)
color(data)
half(data)
color_avg(data)
cut_avg(data)
end_time = time.time()
total_time = end_time - start_time

print("Total time to run all functions: %s seconds" % total_time)
