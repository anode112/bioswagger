def count_gc(sequence) -> int:
    """
    Count G and C in sequence
    :param sequence: str
    :return: int
    """
    return (sequence.count('G') + sequence.count('C')) / len(sequence)

def get_seq_quality(quality) -> float:
    """
    Counts quality in phred33 score
    :param quality: str
    :return: int
    """
    quality = quality.split()
    q_score = [ord(quality) - 33 for letter in quality]
    return sum(q_score)/len(quality)

# rкак обыграли с 1 верхним порогом?
# смотреть комменты по коду в гх

