""" django views file for the datafiles app """
from django.shortcuts import render
from datasets.serializer import *
from .forms import UploadFileForm
from workflow.wf_functions import ingest


def ingestion(request):
    """ ingestion SciData JSON-LD file """
    user = request.user
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file')
            for file in files:
                ingest(file, user)
    else:
        form = UploadFileForm()
    context = {'form': form}
    return render(request, 'datafiles/ingestion.html', context)


def viewfile(request, fileid):
    """view to generate list of substances on homepage"""
    file = JsonLookupSerializer(JsonLookup.objects.get(id=fileid))
    return render(request, "datafiles/viewfile.html", {'file': file.data})




# ###
# def upload_pdf(request):
#     if request.method == “POST”:
#          form = ResumeUpload(request.POST, request.FILES)
#          files = request.FILES.getlist(‘resumes’)
#          if form.is_valid():
#              for f in files:
#                  file_instance = UploadPdf(resumes=f)
#                  file_instance.save()
#      else:
#          form = ResumeUpload()
#  return render(request, ‘web_app/upload_pdf.html’, {‘form’: form})