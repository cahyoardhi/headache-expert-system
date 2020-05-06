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
    # global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
    # with open(os.path.join(path['path'],'diseases.txt'),'r') as diseases:
    #     temp = diseases.read()
    #     diseases_list = temp.split('\n')

    for i in os.listdir(path['path']):
        print(i)

    print('\n\n')
    for j in os.listdir(path['symptoms']):
        print(j)

    print('\n\n')
    for k in os.listdir(path['descriptions']):
        print(k)
        
    print('\n\n')
    for l in os.listdir(path['treatments']):
        print(l)

preprocess()