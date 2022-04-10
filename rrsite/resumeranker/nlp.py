import spacy
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_ROOT = BASE_DIR / "resumeranker/model"

def ner(document):
    nlp = spacy.load(MODEL_ROOT)
    doc = nlp(document)
    d = {
        "Name": [],
        "College Name": [],
        "Degree": [],
        "Graduation Year": [],
        "Years of Experience": [],
        "Companies worked at": [],
        "Designation": [],
        "Skills": [],
        "Location": [],
        "Email Address": []
    }
    for ent in doc.ents:
        d[ent.label_]=[]

    for ent in doc.ents:
        d[ent.label_].append(ent.text)
    # for d in d.items():
    #     if d is None:
    #         d.append([" "])

    # print("\n********************************************")
    # print(d)
    # print("********************************************\n")
    return d
        


