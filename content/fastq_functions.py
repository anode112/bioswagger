def count_gc(sequence) -> int:
    """
    Count G and C in sequence
    :param sequence: str
    :return: int
    """
    return (sequence.count("G") + sequence.count("C")) / len(sequence) * 100


def get_seq_quality(quality) -> float:
    """
    Counts quality in phred33 score
    :param quality: str
    :return: int
    """
    q_score = [ord(letter) - 33 for letter in quality]
    return sum(q_score) / len(quality)
