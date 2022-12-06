

def bitListToInt(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def get_bit_length():
    with open('input.txt') as f:
        return len(f.readline())

def init_freq_array(size):
    retval = []
    for i in range(0, size):
        retval.append(0)
    return retval; 

bit_length = get_bit_length() - 1 #removes new line character
gamma_array = init_freq_array(bit_length)
epsilon_array = init_freq_array(bit_length)

num_lines = 0
with open('input.txt') as f:
    cur_line = f.readline()
    
    while cur_line:
        for i in range(0,len(gamma_array)):
            gamma_array[i] += int(cur_line[i])
        
        num_lines += 1
        cur_line = f.readline()
    
    for i in range(0, len(gamma_array)):
        frequency = gamma_array[i]
        gamma_array[i] = 1 if frequency / num_lines > 0.5 else 0
        epsilon_array[i] = 1 if frequency / num_lines < 0.5 else 0

print(gamma_array)
print(epsilon_array)

gamma = bitListToInt(gamma_array)
epsilon = bitListToInt(epsilon_array)
consumption = gamma * epsilon

print("gamma: {}".format(gamma))
print("epsilon: {}".format(epsilon))
print("consumption: {}".format(consumption))



