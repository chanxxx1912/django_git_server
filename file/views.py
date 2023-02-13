from django.shortcuts import render



from django.core.files.storage import FileSystemStorage



from .models import File



import os, datetime



import json



from rest_framework import generics







from .serializers import FileSerializer











# Create your views here.



class FileListCreate(generics.ListCreateAPIView):



    queryset = File.objects.all()



    serializer_class = FileSerializer



# Create your views here.

from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

import json



def index(request):
    if request.method == 'POST' and request.FILES['file']:
        upload_file = request.FILES['file']
        data = json.load(upload_file)

        result = []
        traverse(data, result)

        output = "\n".join(result)

        path = "output.txt"
        with open(path, "w") as file:
            file.write(output)

        # Do something with the output file
        ...

        return render(request, 'file/index.html', {
            'upload_file_path': output,
            'path': path,
        })
    else:
        return render(request, 'file/index.html')

def traverse(item, result, path=""):
    if isinstance(item, dict):
        for key, value in item.items():
            traverse(value, result, f'{path}."{key}"')
    elif isinstance(item, list):
        for value in item:
            traverse(value, result, path)
    else:
        result.append(f'{path[1:]}."{item}",')
