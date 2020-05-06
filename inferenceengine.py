import os
import experta

diseases_list       = []
diseases_symptoms   = []

symptom_map         = {}
d_desc_map          = {}

d_treatment_map     = {}


path                = { 'path'          : r'knowledgebase',
                        'symptoms'      : r'knowledgebase\symptoms',
                        'descriptions'  : r'knowledgebase\descriptions',                                
                        'treatments'    : r'knowledgebase\treatments',                                
                    }

def preprocess():
    global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
    with open(os.path.join(path['path'],'diseases.txt'),'r') as diseases:

        temp = diseases.read()
        diseases_list = temp.split('\n')
    
    for disease in diseases_list:
        with open(f"{path['symptoms']}\{disease}.txt",'r') as diseasef:

            temp    = diseasef.read()
            temp2   = temp.split('\n')

            diseases_symptoms.append(temp2)
            symptom_map[str(temp2)] = disease

        with open(f"{path['descriptions']}\{disease}.txt",'r') as diseasef:

            temp    = diseasef.read()
            d_desc_map[disease] = temp

        with open(f"{path['treatments']}\{disease}.txt",'r') as diseasef:

            temp    = diseasef.read()
            d_treatment_map[disease] = temp
        
    # for i , (d , s, dd, t) in enumerate(diseases_list, symptom_map.values(), d_desc_map.values(), d_treatment_map.values()):
    #     print(f'{i+1}\t{d}')
    #     print(f'{s}')
    #     print(f'{dd}')
    #     print(f'{t}')

    print('DAFTAR PENYAKIT')
    for i, d in enumerate(diseases_list):
        print(f'{i}\t{d}')

    print('\n\nDAFTAR GEJALA')
    for i, s in enumerate(symptom_map.keys()):
        print(f'{i}\t{s}')

    print('\n\nDAFTAR DESKRIPSI')
    for i, dd in enumerate(d_desc_map.values()):
        print(f'{i}\t{dd}')

    print('\n\nDAFTAR PENANGAN')
    for i, t in enumerate(d_treatment_map.values()):
        print(f'{i}\t{t}')
        
            
preprocess()