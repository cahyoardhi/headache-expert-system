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
        print('\n\nHalo namaku iBot, expert system yang akan mendiagnosis pasien!')
        print('tolong jawab beberapa pertanyaan berikut dengan jujur ya!\n\n')
        print('Inputan y = ya\tn = tidak')
        yield Fact(action='find_disease')
        
    @Rule(Fact(action='find_disease'), NOT(Fact(g1=W())), salience = 1)        
    def symptom1(self):
        self.declare(Fact(g1=input('Lelah\t\t\t\t\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g2=W())), salience = 1)        
    def symptom2(self):
        self.declare(Fact(g2=input('Nyeri Otot Leher\t\t\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g3=W())), salience = 1)        
    def symptom3(self):
        self.declare(Fact(g3=input('Pusing Berputar\t\t\t\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g4=W())), salience = 1)        
    def symptom4(self):
        self.declare(Fact(g4=input('Nyeri Kepala Terpusat  Pada Satu Mata\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g5=W())), salience = 1)        
    def symptom5(self):
        self.declare(Fact(g5=input('Kemerahan Pada Sisi Mata Yang Terkena\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g6=W())), salience = 1)        
    def symptom6(self):
        self.declare(Fact(g6=input('Keluarnya Air Mata\t\t\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g7=W())), salience = 1)        
    def symptom7(self):
        self.declare(Fact(g7=input('Nyeri Seperti Tertekan\t\t\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g8=W())), salience = 1)        
    def symptom8(self):
        self.declare(Fact(g8=input('Gelisah\t\t\t\t\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g9=W())), salience = 1)        
    def symptom9(self):
        self.declare(Fact(g9=input('Konsentrasi Tertanggu\t\t\t: ')))
    @Rule(Fact(action='find_disease'), NOT(Fact(g10=W())), salience = 1)        
    def symptom10(self):
        self.declare(Fact(g10=input('Sulit Tidur / Mudah Bangun\t\t: ')))


    @Rule(Fact(action='find_disease'), Fact(g1=0), Fact(g2=1), Fact(g3=0), Fact(g4=1), Fact(g5=1), Fact(g6=1), Fact(g7=0), Fact(g8=0), Fact(g9=1), Fact(g10=0))
    def disease1(self):
        self.declare(Fact(disease='Sakit Kepala Cluster'))        
    
    @Rule(Fact(action='find_disease'), Fact(g1='y'), Fact(g2='y'), Fact(g3='y'), Fact(g4='n'), Fact(g5='n'), Fact(g6='n'), Fact(g7='n'), Fact(g8='n'), Fact(g9='y'), Fact(g10='n'))
    def disease2(self):
        self.declare(Fact(disease='Sakit Kepala Migrain'))        
    
    @Rule(Fact(action='find_disease'), Fact(g1='n'), Fact(g2='y'), Fact(g3='n'), Fact(g4='n'), Fact(g5='n'), Fact(g6='n'), Fact(g7='y'), Fact(g8='y'), Fact(g9='y'), Fact(g10='y'))
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
        Fact(g6 = MATCH.g6),
        Fact(g7 = MATCH.g7),
        Fact(g8 = MATCH.g8),
        Fact(g9 = MATCH.g9),
        Fact(g10 = MATCH.g10),
        NOT(Fact(disease=MATCH.disease)), salience = -999)

    def notmatch(self, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10):
        print('\nMaaf expert system tidak menemukan jenis sakit kepala yang cocok untuk gejala anda')
        glist = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
        max_count   = 0
        max_disease = ''
        try:
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
            
        except:
            pass
            





if __name__ == "__main__":    
    fpreprocess()
    engine  = ExpertSystem()
    while(1):
        engine.reset()
        engine.run()
        print('Apakah anda ingin di diagnosa lagi? (y/n)')
        if input() == 'n':
            exit()            

