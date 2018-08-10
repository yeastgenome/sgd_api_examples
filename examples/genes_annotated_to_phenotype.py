import requests

SGD_BASE_URL = 'https://www.yeastgenome.org/webservice'

def print_phenotype_loci():
    url = SGD_BASE_URL + '/phenotype/abnormal_mating_response/locus_details'
    response = requests.get(url=url).json()
    print('LOCI ANNOTATED TO abnormal_mating_response')
    for annotation in response:
        gene_name = annotation['locus']['display_name']
        reference_citation = annotation['reference']['display_name']
        print(gene_name + ', reference citation:' + reference_citation)

if __name__ == '__main__':    
    print_phenotype_loci()
