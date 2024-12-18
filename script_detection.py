import ollama
import pandas as pd
import time

reports_path=""

file = open(reports_path)
separator=""
reports = file.read()
reports=reports.split(sep=separator)

responses=[]

task1= "Your task is to analyze a medical report to detect if an allergic drug event that has explicitely ocurred during the hospital stay, or just before. Symptoms of allergic drug events may include drug rush (or toxidermie) or anaphylaxia in reaction to a drug, including iodine contrast agents, or medical procedures. I am not interested in the past medical history of the patient (allergies known before the hospital stay). If you detect an allergic drug event in the report, answer YES, otherwise answer NO"
task2= "Your task is to analyze a medical report to analyze an allergic drug reaction that occured during the hospital stay. Here is the report:"+data+"\n\nWhat drug(s) caused the allergic drug reaction mentioned in the report? There may be multiple candidates, include them all.-Is it an immediate (less than 48h between taking the drug and the onset of the symptoms) or a delayed (more than 48h) rectaion?\n-Was the event explicitely notified to the Pharmacovigilance team?\n Your answer must follow this template: Drug: ... \n Immediate or Delayed: ...\n Notified: ..."

tic=time.perf_counter()
for data in reports:

    print(data)
    response = ollama.chat(model='llama3.1:70b', messages=[
    {'role': 'system',
        'content': "You are an assistant answering questions about medical texts."},
    {   
        'role': 'user',
        'content': task1
    },

    ],stream=False, options={"temperature":0, "raw":0, "num_predict":1000})
    print(response)
    print(response['message']['content'])
    responses.append(response['message']['content'])

    dict={"responses":responses}
    df_final=pd.DataFrame(dict)
    df_final.to_csv("", index=False)







