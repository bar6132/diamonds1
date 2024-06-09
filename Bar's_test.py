import time

path = 'diamonds1.csv'
with open(path, 'r') as fh:
    lines = fh.readlines()


def most_expensive():
    """adding price number to list and print reverse the list form high to low
     and print the first price == most expensive price"""
    cost = []
    for line in lines:
        if 'carat,cut,color,clarity,depth,table,price,x,y,z' in line:
            continue
        columns = line.split(',')
        cost.append(int(columns[6]))
        cost.sort(reverse=True)
    print('The most expensive diamond price is:', cost[0], '$')


def avg_cost():
    """adding price number to list sum the list and divide by the len of the list
    average_price = (sum(cost) / len(cost))"""
    cost = []
    for line in lines:
        if 'carat,cut,color,clarity,depth,table,price,x,y,z' in line:
            continue
        columns = line.split(',')
        cost.append(int(columns[6]))
    average_price = (sum(cost) / len(cost))
    return print('The average price of diamond is :', average_price, '$')


def ideal_count():
    """find all ideal cut , add all to list
    and print the len of the list == count of ideal"""
    ideal_list = []
    for line in lines:
        if 'carat,cut,color,clarity,depth,table,price,x,y,z' in line:
            continue
        columns = line.split(',')
        if 'Ideal' in line:
            ideal_list.append('Ideal')
    return print('The number the ideal diamonds is :', (len(ideal_list)))


def color():
    """create color list , make the set so only one color is showed
     the print the len of the set to see the number of colors and the set itself
     to see the names"""
    color_list = []
    for line in lines:
        if 'carat,cut,color,clarity,depth,table,price,x,y,z' in line:
            continue
        columns = line.split(',')
        color_list.append(columns[2])
    print('The number of colors is:', len(set(color_list)))
    return print('The names of colors are:', set(color_list))


def half():
    """put all premium diamonds is list sort them
     cut the list in half and pick the number
     from the list in the place we cut """
    carat = []
    for line in lines:
        if 'carat,cut,color,clarity,depth,table,price,x,y,z' in line:
            continue
        columns = line.split(',')
        if 'Premium' in line:
            carat.append(columns[0])
        carat.sort()
        mid = len(carat) // 2
    print('The median of Premium diamonds cartis:', carat[mid], 'cart')


def cut_avg():
    """ create list of every type carat and the cart itself
    then create average by sum of carat in list divided by len
    of list"""
    fair_list = []
    ideal_list = []
    premium_list = []
    good_list = []
    very_good_list = []

    for line in lines:
        if 'carat,cut,color,clarity,depth,table,price,x,y,z' in line:
            continue
        columns = line.split(',')
        if 'Ideal' in line:
            ideal_list.append(float(columns[0]))
        elif 'Fair' in line:
            fair_list.append(float(columns[0]))
        elif 'Premium' in line:
            premium_list.append(float(columns[0]))
        elif 'Good' in line:
            good_list.append(float(columns[0]))
        if 'Very Good' in line:
            very_good_list.append(float(columns[0]))
    avg_carat_ideal = sum(ideal_list) / len(ideal_list)
    print('The avg carat of ideal diamonds is:', {avg_carat_ideal})
    avg_carat_fair = sum(fair_list) / len(fair_list)
    print('The avg carat of fair diamonds is:', {avg_carat_fair})
    avg_carat_premium = sum(premium_list) / len(premium_list)
    print('The avg carat of premium diamonds is:', {avg_carat_premium})
    avg_carat_good = sum(good_list) / len(good_list)
    print('The avg carat of good diamonds is:', {avg_carat_good})
    avg_carat_very_good = sum(very_good_list) / len(very_good_list)
    print('The avg carta of very good diamonds is:', {avg_carat_very_good})


def color_avg():
    """sorting colors prices to list ,
    sum and divide by the len of the list to get avg prive"""
    e_list = []
    g_list = []
    j_list = []
    d_list = []
    i_list = []
    f_list = []
    h_list = []
    for line in lines:
        if 'carat,cut,color,clarity,depth,table,price,x,y,z' in line:
            continue
        columns = line.split(',')
        if 'E' in line:
            e_list.append(int(columns[6]))
        if 'G' in line:
            g_list.append(int(columns[6]))
        if 'J' in line:
            j_list.append(int(columns[6]))
        if 'D' in line:
            d_list.append(int(columns[6]))
        if 'I' in line:
            i_list.append(int(columns[6]))
        if 'F' in line:
            f_list.append(int(columns[6]))
        if 'H' in line:
            h_list.append(int(columns[6]))

    e_avg = sum(e_list) / len(e_list)
    print('The avg price for E is:', {e_avg})
    g_avg = sum(g_list) / len(g_list)
    print('The avg price for G is:', {g_avg})
    j_avg = sum(j_list) / len(j_list)
    print('The avg price for J is:', {j_avg})
    d_avg = sum(d_list) / len(d_list)
    print('The avg price for D is:', {d_avg})
    i_avg = sum(i_list) / len(i_list)
    print('The avg price for I is:', {i_avg})
    f_avg = sum(f_list) / len(f_list)
    print('The avg price for F is:', {f_avg})
    h_avg = sum(h_list) / len(h_list)
    print('The avg price for H is:', {h_avg})


start_time = time.time()
most_expensive()
color_avg()
avg_cost()
ideal_count()
color()
half()
cut_avg()
end_time = time.time()
total_time = end_time - start_time

print("Total time to run all functions: %s seconds" % total_time)
