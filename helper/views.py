from django.shortcuts import render
from helper.util import borangRenderer, StreamingConvertedPdf
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json, base64

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from helper.models import Borang


@csrf_exempt
def cetak_borang(request, jenis):

    borang_directory =f"/Users/pipeline-dev/Documents/aset_borang_docx/{jenis}.docx"
    content_borang = json.loads(request.body)[0]
    print(content_borang)

    inst = borangRenderer(borang_directory, content_borang)
    res = inst.cetak()

    new_borang = Borang.objects.create()
    new_borang.signature.save('pdf', res) 

    pdf_path = new_borang.signature.name
    pdf_file = open(pdf_path, 'rb')
    pdf_file_64 = base64.encodebytes(pdf_file.read())

    return HttpResponse(pdf_file_64)


