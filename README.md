```
       (        )   (                                            (     
   (   )\ )  ( /(   )\ )  (  (       (      (       (            )\ )  
 ( )\ (()/(  )\()) (()/(  )\))(   '  )\     )\ )    )\ )    (   (()/(  
 )((_) /(_))((_)\   /(_))((_)()\ )((((_)(  (()/(   (()/(    )\   /(_)) 
((_)_ (_))    ((_) (_))  _(())\_)())\ _ )\  /(_))_  /(_))_ ((_) (_))   
 | _ )|_ _|  / _ \ / __| \ \((_)/ /(_)_\(_)(_)) __|(_)) __|| __|| _ \  
 | _ \ | |  | (_) |\__ \  \ \/\/ /  / _ \    | (_ |  | (_ || _| |   /  
 |___/|___|  \___/ |___/   \_/\_/  /_/ \_\    \___|   \___||___||_|_\  
```
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
### Arguments and default values
- `seqs` - dictionary with sequences
- `gc_bounds = (20, 80)`
- `length_bounds = (0, 2**32)`
- `quality_threshold = 0`
FASTQ input example:
```
EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079801': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCC', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGE'),
    '@SRX079803': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFB'),
```
