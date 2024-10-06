# проверка правильности сиквенса
def is_valid_seq(seq):
    """
    Checking both T and U abundance in sequence.
    """
    for i in seq:
        if ("t" in i or "T" in i) and ("u" in i or "U" in i):
            return False
    return True


def transcribe(seq):
    """
    Make RNA from DNA
    """
    return complement(seq).replace("t", "u", -1).replace("T", "U", -1)
    # seq.replace('a', 'u').replace('A', 'U').replace('t', 'a').replace('T', 'A').replace('g', 'c').replace('G', 'C').replace('c', 'g').replace('C', 'G')
    # for seq in input_list:
    # result = []
    # result.append(seq.('T', 'U').replace('t', 'u').('T', 'U').replace('t', 'u'))


def reverse(seq: str) -> str:
    """
    Return reverse sequence
    """
    # old version
    # result = []
    # for i in seq:
    #     result.append(i[::-1])
    # return result
    return seq[::-1]


def complement(seq):
    result = []
    for nucl in seq:
        if nucl == "t":
            result.append("a")
            continue
        if nucl == "T":
            result.append("A")
            continue
        if nucl == "c":
            result.append("g")
            continue
        if nucl == "C":
            result.append("G")
            continue
        if nucl == "g":
            result.append("c")
            continue
        if nucl == "G":
            result.append("C")
            continue
        if nucl == "a":
            result.append("t")
            continue
        if nucl == "A":
            result.append("T")
            continue
    return "".join(result)

    # return seq.replace('t', 'a').replace('T', 'A').replace('g', 'c').replace('G', 'C').replace('c', 'g').replace('C', 'G')


def reverse_complement(seq):
    """
    Return reverse complement DNA sequence
    """
    return complement(reverse(seq))


# moved to main script
# def run_dna_rna_tools(input_list):
#     method = input_list.pop()  # выбираем функцию
#     if not is_seq(input_list):
#         print("Wrong sequence!")
#         return None

#     if method == "reverse":
#         return list(map(reverse, input_list))
#     if method == "transcribe":
#         return list(map(transcribe, input_list))
#     if method == "reverse_complement":
#         return list(map(reverse_complement, input_list))
#     if method == "complement":
#         return list(map(complement, input_list))
