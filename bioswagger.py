from content.dna_rna_tools import reverse, reverse_complement, transcribe, complement, is_valid_seq
from content.fastq_functions import count_gc, get_seq_quality
import os

def read_fastq(fastq_file) -> dict:
    """
    read file and transforms it into dict
    :return:
    """
    # no fastq file check
    with open(fastq_file) as fastq:
        parsed_fq = {}
        # deleting exceed symbols
        seqs = [line.strip() for line in fastq.readlines()]
        if seqs % 4 != 0:
            raise ValueError("Broken FASTQ! Lines dont divided by 4!")
        # lets divide by 4 our lines via zip
        # make iterator based on our list
        it = iter(seqs)

        for name, sequence, info, quality in zip(it, it, it, it):
            # write to dict
            parsed_fq[name] = (sequence, quality)
        # в блоке или нет?
        return parsed_fq



def write_fastq(seqs: dict, output_suffix: str):
    """
    Write file into a folder 'filtered' with prename suffix 'output_fastq' given

    """
    # checking folder
    if not os.path.isdir('filtered'):
        os.mkdir('filtered')
    #to fitered folder
    
    pass


def run_dna_rna_tools(*input_list) -> list:
    """
    Takes list of seqs with method as last argument
    :param input_list: list
    :return: list
    """
    # переписать тут, чтобы было как на консе у антона
    *input_list, method = input_list
    # method = input_list.pop()  # выбираем функцию
    if not is_valid_seq(input_list):
        print("Wrong sequence!")
        return None

    if method == "reverse":
        res = list(map(reverse, input_list))
        return res[0] if len(res) == 1 else res
    if method == "transcribe":
        res = list(map(transcribe, input_list))
        return res[0] if len(res) == 1 else res
    if method == "reverse_complement":
        res = list(map(reverse_complement, input_list))
        return res[0] if len(res) == 1 else res
    if method == "complement":
        res = list(map(complement, input_list))
        return res[0] if len(res) == 1 else res


def filter_fastq(input_fastq, output_fastq, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0) -> dict:
    """
    Perform FASTQ filtering, based on GC-content, length and quality.
    :param seqs: dict
    :param gc_bounds: tuple | int
    :param length_bounds: tuple | int
    :param quality_threshold: int
    :return: dict | None
    """

    # open path, make list of files
    for file in os.listdir(input_fastq):
        # make dict
        read_fastq(file)
        # do smth
        write_fastq()
        pass


    # проверяем тип аргумента в gc_bounds
    # если это не кортеж -- подставляем число в верхнюю границу
    if isinstance(gc_bounds, (int, float)):
        gc_bounds = (0, gc_bounds)

    if isinstance(length_bounds, (int, float)):
        length_bounds = (0, length_bounds)

    # итерируемся по словарю с сиквенсами
    filtered_seqs = {}
    for name, sequence, quality) in seqs.items():
        if (gc_bounds[0] <= count_gc(sequence) <= gc_bounds[1] and
                length_bounds[0] <= len(sequence) <= length_bounds[1] and
                get_seq_quality(quality) >= quality_threshold):
            filtered_seqs[name] = (sequence, quality)

    return filtered_seqs
