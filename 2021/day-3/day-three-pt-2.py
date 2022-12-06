
def get_oxygen_rating(binary_list, digit):
    ones = []
    zeroes = []

    if len(binary_list) == 1:
        return binary_list

    for i in range(0, len(binary_list)):
        binary_num = binary_list[i]
    
        if int(binary_num[digit]) == 1:
            ones.append(binary_num)
        else:
            zeroes.append(binary_num) 
    
    digit = digit + 1
    return get_oxygen_rating(ones if len(ones) >= len(zeroes) else zeroes, digit)


def get_co2_rating(binary_list, digit):
    ones = []
    zeroes = []

    if len(binary_list) == 1:
        return binary_list

    for i in range(0, len(binary_list)):
        binary_num = binary_list[i]
    
        if int(binary_num[digit]) == 1:
            ones.append(binary_num)
        else:
            zeroes.append(binary_num) 
    
    digit = digit + 1
    return get_co2_rating(ones if len(ones) < len(zeroes) else zeroes, digit)

with open('input.txt') as f:
    lines = f.read().splitlines() 
    oxygen_rating = int(get_oxygen_rating(lines, 0)[0], 2)
    co2_rating = int(get_co2_rating(lines, 0)[0], 2)
    result = oxygen_rating * co2_rating
    print("result: {}".format(result))
    
    
    
    