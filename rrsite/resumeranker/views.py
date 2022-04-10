from django.shortcuts import render, HttpResponse
from .models import * 
from .conversion import extract_text_from_pdf, extract_text_from_doc
from .nlp import ner
from .ranking import rank
from django.shortcuts import get_object_or_404

# Create your views here
def index(request):      
    return render(request, "resumeranker/index.html",{
        "part": "part1"
    })

def send_files(request):
    if request.method=="POST":
        myfile = request.FILES.getlist("files")
        for f in myfile:
            myUploadFile(myfiles=f).save()
            current_file=None
            current_file = myUploadFile.objects.all().order_by('-id')[0]
            txt=None
            txt = convert_file_to_txt(current_file)
            if txt is not None:
                dict=None
                dict = ner(txt)
                if dict is not None:
                    Data(text=txt, name=dict["Name"], collegeName=dict["College Name"],degree=dict["Degree"],
                        graduationYear=dict["Graduation Year"],yearsOfExperience=dict["Years of Experience"],
                        companiesWorkedAt=dict["Companies worked at"],designation=dict["Designation"],skills=dict["Skills"],
                        Location=dict["Location"],emailAddress=dict["Email Address"]
                    ).save()
        return render(request, "resumeranker/index.html",{
            "part": "part2"
        }) 

    return render(request, "resumeranker/index.html",{
            "part": "part1"
        })
    

def convert_file_to_txt(current_file):
    extractedtext=None
    current_file_extension = current_file.myfiles.path.split(".")[1].lower()
    if current_file_extension == "pdf":
        extractedtext = extract_text_from_pdf(current_file.myfiles.path)
    elif current_file_extension == ".doc" or current_file_extension == "docx":
        extractedtext = extract_text_from_doc(current_file.myfiles.path)
    return extractedtext


def send_keywords(request):
    if request.method=="POST":
        keywords = request.POST["keywords"]
        data = rank(keywords, Data.objects.all())
        rank_data=[]
        for d in data:
            rank_data.append(get_object_or_404(Data, id = d))
        return render(request, "resumeranker/index.html",{
            "data": Data.objects.all(),
            "rank": rank_data,
            "part": "part3"
        }) 

    return render(request, "resumeranker/index.html",{
            "part": "part2"
        })

def reset(request):
    ids = Data.objects.all().values_list('id', flat=True)
    for i in ids:
        file_obj = get_object_or_404(myUploadFile, id = i)
        file_obj.delete()
        data_obj = get_object_or_404(Data, id = i) 
        data_obj.delete()

    return index(request) 