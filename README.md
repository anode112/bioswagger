BBBBB  IIIIII  OOOOO  SSSSS  W   W   AAAAA  GGGGG  GGGGG  EEEEE  RRRRR  
B   B    II   O     O S      W   W  A     A G      G      E      R   R 
BBBBB     II   O     O  SSSS  W W W  AAAAAAA G  GGG G  GGG EEEE   RRRRR  
B   B    II   O     O      S  W W W  A     A G    G G    G E      R  R  
BBBBB  IIIIII  OOOOO  SSSSS   W   W  A     A  GGGGG  GGGGG  EEEEE  R   R 

# bioswagger
Classic bioinformatician toolkit for basic transformations with DNA and RNA sequences and perform FASTQ quality filtration.


![swag.png](content%2Fswag.png)


## DNA & RNA tools
Takes a list of sequences with method as last element.
### Methods
- `complement` - makes complement sequence
- `reverse complement` - makes reverse complement sequence
- `transcribe` - makes an RNA from DNA sequence
- `reverse` writes the sequence backwards

## FASTQ filtration
Perform sequence length, GC-content and phred33-score based filtrations.
Takes as input dict `{name:(sequence, quality)}`. You can pass a tuple interval or a maximum number in GC and length params.
