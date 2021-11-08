from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, Http404 

from portal.models import LetterTemplate 
 
from app.helpers.helpers import docx_to_pdf_stream 
 
def doc_test(request): 
    letter_template = LetterTemplate.objects.all()[0] 
    context = { 'company_name' : "World company" } 
    response = docx_to_pdf_stream(letter_template, context) 
    return response 
