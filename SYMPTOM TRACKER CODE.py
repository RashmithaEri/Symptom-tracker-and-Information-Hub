import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

symptom_conditions = pd.DataFrame({
    'symptom': ['headache', 'fever', 'cough', 'fatigue', 'nausea', 'diarrhea', 'sore throat', 
                'runny nose', 'muscle aches', 'shortness of breath', 'chest pain', 'abdominal pain', 
                'vomiting', 'dizziness', 'chills', 'loss of appetite', 'weakness', 'body aches', 
                'joint pain', 'nasal congestion'],
    'conditions': [['migraine', 'tension headache', 'sinusitis'],
                   ['flu', 'common cold', 'pneumonia'],
                   ['common cold', 'bronchitis', 'pneumonia'],
                   ['anemia', 'hypothyroidism', 'fibromyalgia'],
                   ['food poisoning', 'migraine', 'pregnancy'],
                   ['food poisoning', 'gastroenteritis', 'irritable bowel syndrome'],
                   ['strep throat', 'tonsillitis', 'mononucleosis'],
                   ['common cold', 'sinusitis', 'allergic rhinitis'],
                   ['influenza', 'fibromyalgia', 'hypothyroidism'],
                   ['asthma', 'pneumonia', 'chronic obstructive pulmonary disease'],
                   ['heart attack', 'pneumonia', 'costochondritis'],
                   ['appendicitis', 'gallstones', 'irritable bowel syndrome'],
                   ['gastroenteritis', 'food poisoning', 'migraine'],
                   ['anxiety', 'hypotension', 'vertigo'],
                   ['influenza', 'malaria', 'lyme disease'],
                   ['depression', 'thyroid disorder', 'cancer'],
                   ['anemia', 'chronic fatigue syndrome', 'hypothyroidism'],
                   ['influenza', 'fibromyalgia', 'rheumatoid arthritis'],
                   ['arthritis', 'bursitis', 'lupus'],
                   ['sinusitis', 'allergic rhinitis', 'nasal polyps']]
})

def check_symptoms(user_symptoms):
    matched_conditions = set()
    for symptom in user_symptoms:
        conditions = symptom_conditions[symptom_conditions['symptom'] == symptom]['conditions'].values
        if len(conditions) > 0:
            matched_conditions.update(conditions[0])
    return list(matched_conditions)

def main():
    def on_submit():
        user_input = entry_symptoms.get()

        user_symptoms = [symptom.strip() for symptom in user_input.split(',')]

        matched_conditions = check_symptoms(user_symptoms)

        messagebox.showinfo("Matching Conditions", f"Input symptoms: {user_symptoms}\nMatching conditions: {matched_conditions}")

        plt.figure(figsize=(10, 8))
        condition_counts = {}
        for condition in matched_conditions:
            count = sum(symptom_conditions['conditions'].apply(lambda x: condition in x))
            condition_counts[condition] = count

        plt.bar(condition_counts.keys(), condition_counts.values(), color='skyblue')
        plt.xlabel('Conditions')
        plt.ylabel('Frequency')
        plt.title('Frequency of Conditions Matching Input Symptoms')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    root = tk.Tk()
    root.title("Symptom Checker")

    lbl_symptoms = tk.Label(root, text="Enter symptoms separated by comma (,):")
    lbl_symptoms.pack()
    entry_symptoms = tk.Entry(root, width=50)
    entry_symptoms.pack()

    btn_submit = tk.Button(root, text="Submit", command=on_submit)
    btn_submit.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
