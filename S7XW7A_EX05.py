highest_number = 9
result_number = 100


def cons(head, tails):
    result = []
    if len(tails) == 0: return [head]
    for t in tails:
        result.append([head] + t)
    return result


def random_values(values):
    if len(values) == 0:
        return [[]]
    else:
        res = random_values(values[1:])
        return cons(values[0], res) + cons(-values[0], res)


def get_ones_zeros(size):
    if size == 0:
        return [[]]
    else:
        res = get_ones_zeros(size - 1)
        return cons(0, res) + cons(1, res)


def glue(values, glues):
    index_j = 0
    index_i = 0
    size = len(values)
    result = []
    value_stack = values[0]
    while index_i < size:
        if index_i + 1 >= size:
            result.append(value_stack)
            break
        new_value = values[index_i + 1]
        if glues[index_j] == 0:
            result.append(value_stack)
            value_stack = new_value
        else:
            value_stack = value_stack * 10 + new_value
        index_i += 1
        index_j += 1
    return result


def get_numbers(stop=9):
    values = range(1, stop + 1)
    one_zeros = get_ones_zeros(stop)
    result = []
    for one_zero in one_zeros:
        res = glue(values, one_zero)
        result.append(tuple(res))
    return set(result)


def convert_to_string(num_list):
    result = ""
    for v in num_list:
        if v > 0:
            result += ' + {}'.format(v)
        else:
            result += ' - {}'.format(abs(v))
    return '{} = {}'.format(result[3:len(result)], result_number)


def solution(stop, goal):
    numbers = get_numbers(stop)
    for number in numbers:
        variations = map(lambda y: [number[0]] + y, random_values(number[1:]))
        for v in variations:
            summed_value = sum(v)
            if goal == summed_value:
                print(convert_to_string(v))


solution(highest_number, result_number)
