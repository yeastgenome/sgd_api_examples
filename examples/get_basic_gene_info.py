import requests

SGD_BASE_URL = 'https://www.yeastgenome.org/webservice'

def print_act1_info():
    url = SGD_BASE_URL + '/locus/act1'
    response = requests.get(url=url).json()
    # print references
    print('ACT1 REFERENCES')
    for ref in response['references']:
        name = ref['display_name']
        pmid = str(ref['pubmed_id'])
        print(pmid + ': ' + name)
     # print large scale phenotypes
    print('ACT1 OVEREXPRESSION LARGE SCALE PHENOTYPES')
    for pheno in response['phenotype_overview']['large_scale_phenotypes']['overexpression']:
        name = pheno['display_name']
        print(name)

if __name__ == '__main__':    
    print_act1_info()
