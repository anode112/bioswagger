import pytest
import os
from bioswagger import read_fastq, count_gc, filter_fastq

# 1
def test_read_fastq_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_fastq("non_existent_file.fastq")

# 2
def test_count_gc():
    seq = "AGAGAGACACAC"
    assert count_gc(seq) == 50.0

# 3
# basic test
def test_filter_fastq():
    seqs = {
        "seq1": ("AGCTAGCTAG", "IIIIIIIIII"),
        "seq2": ("ATGCATGC", "IIIIIIII"),
    }
    result = filter_fastq(seqs, gc_bounds=(30, 60), quality_threshold=30)
    assert len(result) == 2
    assert "seq1" in result
    assert "seq2" in result

# 4
def test_filter_fastq_low_q():
    seqs = {
        "seq1": ("AGCTAGCTAG", "!!!!!!!!!!")}
    result = filter_fastq(seqs, quality_threshold=30)
    assert len(result) == 0

# 5
def test_filter_fastq_length():
    seqs = {
        "seq1": ("AGC", "III"),
        "seq2": ("ATGCATGCATGCATGC", "IIIIIIIIIIIIIIII"),
    }
    result = filter_fastq(seqs, length_bounds=(5, 20))
    assert len(result) == 1
    assert 'seq1' not in result

# 6
def test_filter_fastq_length_onegc():
    seqs = {"seq1": ("AGCTAGCTAG", "IIIIIIIIII")}
    result = filter_fastq(seqs, gc_bounds=100)
    assert 'seq1' in result

# 7
def test_filter_fastq_gc_bounds_str():
    seqs = {
        'seq1': ('AGCTAGCTAG', 'IIIIIIIIII'),
    }
    with pytest.raises(TypeError):
        filter_fastq(seqs, gc_bounds="str input", quality_threshold=30)
# 8
def test_read_fastq_lines_divisible_by_four():
    valid_fastq_content = """@SEQ1
ACTG
+
IIII
@SEQ2
CGTA
+
JJJJ
"""
    with open('test_valid.fastq', 'w') as f:
            f.write(valid_fastq_content)

    result = read_fastq('test_valid.fastq')

    with open('test_valid.fastq') as f:
        lines = f.readlines()
        
    os.remove('test_valid.fastq')
    assert len(lines) % 4 == 0, "Количество строк в файле должно делиться на 4"

# босс я устал придумывать тесты