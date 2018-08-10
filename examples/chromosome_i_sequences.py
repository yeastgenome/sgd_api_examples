import requests

SGD_BASE_URL = 'https://www.yeastgenome.org/webservice'

def print_chromosome_i_sequences():
    url = SGD_BASE_URL + '/contig/chromosome_i/sequence_details'
    response = requests.get(url=url).json()
    for locus in response['genomic_dna']:
        name = locus['locus']['display_name']
        sequence = locus['residues']
        print(name + ': ' + sequence)

if __name__ == '__main__':    
    print_chromosome_i_sequences()
