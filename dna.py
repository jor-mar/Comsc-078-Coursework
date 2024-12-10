proteins = {
'TTT':'Phe', 'TCT':'Ser', 'TGT':'Cys', 'TAT':'Tyr',
'TTC':'Phe', 'TCC':'Ser', 'TGC':'Cys', 'TAC':'Tyr',
'TTG':'Leu', 'TCG':'Ser', 'TGG':'Trp', 'TAG':'***',
'TTA':'Leu', 'TCA':'Ser', 'TGA':'***', 'TAA':'***',

'CTT':'Leu', 'CCT':'Pro', 'CGT':'Arg', 'CAT':'His',
'CTC':'Leu', 'CCC':'Pro', 'CGC':'Arg', 'CAC':'His',
'CTG':'Leu', 'CCG':'Pro', 'CGG':'Arg', 'CAG':'Gln',
'CTA':'Leu', 'CCA':'Pro', 'CGA':'Arg', 'CAA':'Gln',

'GTT':'Val', 'GCT':'Ala', 'GGT':'Gly', 'GAT':'Asp',
'GTC':'Val', 'GCC':'Ala', 'GGC':'Gly', 'GAC':'Asp',
'GTG':'Val', 'GCG':'Ala', 'GGG':'Gly', 'GAG':'Glu',
'GTA':'Val', 'GCA':'Ala', 'GGA':'Gly', 'GAA':'Glu',

'ATT':'Ile', 'ACT':'Thr', 'AGT':'Ser', 'AAT':'Asn',
'ATC':'Ile', 'ACC':'Thr', 'AGC':'Ser', 'AAC':'Asn',
'ATG':'Met', 'ACG':'Thr', 'AGG':'Arg', 'AAG':'Lys',
'ATA':'Ile', 'ACA':'Thr', 'AGA':'Arg', 'AAA':'Lys',
}

def get_protein(aa):
    if aa in proteins:
        return proteins[aa]
    else:
        return 'invalid sequence'

def return_proteins(seq):
    worked_seq = ''
    for char in seq:
        if char.isalpha():
            worked_seq += char

    if len(worked_seq)%3 != 0:
        return 'Error: You must give complete triples.\n'

    result = ''
    while len(worked_seq) >= 3:
        result += worked_seq[:3] + ' ' + get_protein(worked_seq[:3]) + '\n'
        worked_seq = worked_seq[3:]
    return result

def translate_to_dna(txt):
    return txt.upper().replace('U', 'T')

def main():
    while True:
        text = input('Enter a nucleotide sequence to be translated to proteins, or press ENTER to quit: ')
        if not text:
            break
        print(return_proteins(translate_to_dna(text)))

if __name__ == '__main__':
    main()