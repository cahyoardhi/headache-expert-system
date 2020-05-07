import os
from experta import *

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

def fpreprocess():
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
        




def fidentify(*args):
    symptom_list = []
    for symptom in args:
        symptom_list.append(symptom)
    
    return symptom_map[str(symptom_list)]





def fdetail(disease):
    return d_desc_map[disease]





def ftreatments(disease):
    return d_treatment_map[disease]        





def ifnotmatch(disease):
    id          = disease
    detail      = fdetail(id)
    treatment   = ftreatments(id)

    print(f'\n\nKemungkinan sakit kepala yang diterita adalah\t: {id}\n\n{detail}\n\n')
    print(f'penangan yang tepat untuk penyakit ini adalah:\n\n{treatment}')





class ExpertSystem(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print('Halo namaku iBot, expert system yang akan mendiagnosis pasien!')
        print('tolong jawab beberapa pertanyaan berikut dengan jujur ya!\n\n')

        yield Fact(action='find_disease')
        
    @Rule(Fact(action='find_disease'), NOT(Fact(g1=W())), salience = 1)        
    def symptom1(self):
        self.declare(Fact(g1=input('Gejala 1\t: ')))

    @Rule(Fact(action='find_disease'), NOT(Fact(g2=W())), salience = 1)        
    def symptom2(self):
        self.declare(Fact(g2=input('Gejala 2\t: ')))

    @Rule(Fact(action='find_disease'), NOT(Fact(g3=W())), salience = 1)        
    def symptom3(self):
        self.declare(Fact(g3=input('Gejala 3\t: ')))

    @Rule(Fact(action='find_disease'), NOT(Fact(g4=W())), salience = 1)        
    def symptom4(self):
        self.declare(Fact(g4=input('Gejala 4\t: ')))

    @Rule(Fact(action='find_disease'), NOT(Fact(g5=W())), salience = 1)        
    def symptom5(self):
        self.declare(Fact(g5=input('Gejala 5\t: ')))





    @Rule(Fact(action='find_disease'), Fact(g1='y'), Fact(g2='n'), Fact(g3='y'), Fact(g4='n'), Fact(g5='y'))
    def disease1(self):
        self.declare(Fact(disease='Migrain'))        

    @Rule(Fact(action='find_disease'), Fact(g1='n'), Fact(g2='y'), Fact(g3='n'), Fact(g4='y'), Fact(g5='n'))
    def disease2(self):
        self.declare(Fact(disease='Sakit Kepala Cluster'))        

    @Rule(Fact(action='find_disease'), Fact(g1='y'), Fact(g2='y'), Fact(g3='n'), Fact(g4='y'), Fact(g5='y'))
    def disease3(self):
        self.declare(Fact(disease='Sakit Kepala Tegang'))        





    @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease), salience= -998)
    def disease(self, disease):
        id          = disease
        detail      = fdetail(id)
        treatment   = ftreatments(id)

        print(f'\n\nKemungkinan sakit kepala yang diterita adalah\t: {id}\n\n{detail}\n\n')
        print(f'penangan yang tepat untuk penyakit ini adalah:\n\n{treatment}') 






    @Rule(Fact(action='find_disease'),
        Fact(g1 = MATCH.g1),
        Fact(g2 = MATCH.g2),
        Fact(g3 = MATCH.g3),
        Fact(g4 = MATCH.g4),
        Fact(g5 = MATCH.g5),
        NOT(Fact(disease=MATCH.disease)), salience = -999)





    def notmatch(self, g1, g2, g3, g4, g5):
        print('\nMaaf expert system tidak menemukan jenis sakit kepala yang cocok untuk gejala anda')
        glist = [g1,g2,g3,g4,g5]
        max_count   = 0
        max_disease = ''

        for k, v in symptom_map.items():
            count = 0
            temp  = eval(k)
            for j, in range(len(glist)):
                if temp[j] == glist[j] and temp[j] == 'y':
                    count += 1
            
            if count > max_count:
                max_count = count
                max_disease = v
        
        ifnotmatch(max_disease)





fpreprocess()
engine  = ExpertSystem()
while(1):
    engine.reset()
    engine.run()
    print(engine.facts)
    print('apakah anda ingin melakukan diagnosa lagi?')
    if input() == 'n':
        exit()


