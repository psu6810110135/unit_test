def alternate(s): # main function
    max_length = 0
    unique = list(set(s))
    pairs = create_pair(unique)
    # print(*pairs)
    for pair in pairs:
        text = [sch for sch in s if sch in pair]
        if is_alternating(text) and len(text) > max_length:
            max_length = len(text)
    return max_length

def is_alternating(text): # check is alternating ? 
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            return False
    return True


def create_pair(unique): # create pair 
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            yield (unique[i], unique[j])
            
            
# if __name__ == '__main__':
#     s = input()
#     result = alternate(s)
#     print(result)
