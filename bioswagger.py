def run_dna_rna_tools(input_list):
    method = input_list.pop()  # выбираем функцию
    if not is_seq(input_list):
        print("Wrong sequence!")
        return None

    if method == "reverse":
        return list(map(reverse, input_list))
    if method == "transcribe":
        return list(map(transcribe, input_list))
    if method == "reverse_complement":
        return list(map(reverse_complement, input_list))
    if method == "complement":
        return list(map(complement, input_list))
    