import experta

diseases_list       = []
diseases_symptoms   = []
symptom_map         = {}
d_desc_map          = {}
d_treatment_map     = {}

def preprocess():
    global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
    with open(r'knowledgebase\diseases.txt','r') as diseases:
        temp = diseases.read()
        diseases_list = temp.split('\n')
    
    for disease in diseases_list:
        print(disease)

preprocess()