def parseFASTA(content):
    sequences = []
    current_string = ''
    for index,elem in enumerate(content[1:]):
        if '>Rosalind' in elem:
            sequences.append(current_string)
            current_string = ''
        else:
            current_string += elem
    sequences.append(current_string)        
    return(sequences)


def TTRatio(s1,s2):
    transition_dict = {'A':'G', 'C':'T', 'G':'A', 'T':'C'}
    transition_count = 0
    transversion_count = 0
    for index,char in enumerate(s1):
        if char == s2[index]:
            continue
        if transition_dict[char] == s2[index]:
            transition_count += 1
        elif transition_dict[char] != s2[index]:
            transversion_count += 1
    return(transition_count/transversion_count)
