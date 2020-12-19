# I have created This file - Manik
from django.http import HttpResponse
from django.shortcuts import render
import string
def home(request):
   return render(request,"index.html")

def Analyze(request):

   # values from request
   djtext=request.GET.get('text','default')
   remove_punc = request.GET.get('remove_punc','OFF')
   sap_remov = request.GET.get('sap_remov','OFF')
   new_line = request.GET.get('new_line','OFF')
   char_cnt = request.GET.get('char_cnt','OFF')
   capital = request.GET.get('capital','OFF')

   # intializing our variable
   analysed=""


   if(remove_punc == "on"):
      punctuations='''!"#$%&'()‘*+,-./:;<=>?@[]^_`{|\\}~'''
      for char in djtext:
         if char not in punctuations:
            analysed=analysed+char
      djtext=analysed 
    
   
   if sap_remov == "on":
      analysed = ""
      for index,char in enumerate (djtext):
         if index<len(djtext)-1 and djtext[index] ==' ' and djtext[index+1] ==' ':
            continue
         else:
            analysed = analysed+char

      djtext = analysed
  
   if new_line == "on":
      analysed = ""
      for char in djtext:
         if char != '\n':
            analysed = analysed + char

      djtext = analysed


   cnt=0
   if char_cnt == "on":
      analysed = ""
      for char in djtext:
         cnt = cnt+1
      
     

   if capital == "on":
      analysed = ""

      for char in djtext:
         analysed = analysed + char.upper()
  

   param = {'count':char_cnt,'charac_cnt':cnt,'analyzed_text':analysed}
   return render(request,'punctuation.html',param)