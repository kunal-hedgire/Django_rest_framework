from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
import requests
import json
from .forms import StudentForm

# Create your views here.

def Links(request):
    return render(request,'FirstPage.html')


def Login_Page(request):
    if request.method == 'POST':
        student = StudentForm(request.POST)
        print("hello")
    else:
        student = StudentForm()
        return render(request, "Home.html", {'form': student})



def savestudinfo(request):
    if request.method == 'POST':
        student=StudentForm(request.POST)
        if student.is_valid():
            print(request.POST)
           
 resposne = requests.post("http://localhost:9000/stud/create/",data=request.POST)
            #print(resposne.status_code)
            return render(request, 'FirstPage.html')
        else:
            student=StudentForm()
            return render(request,"Home.html",{'form' : student})

def GetData(request):
        response = requests.get('http://127.0.0.1:9000/stud/')
        all_topics_json = response.json()
        #listOfTopics = []
        '''
        for item in all_topics_json:
            tp = Topics(item['id'], item['First_Name'], item['Last_Name'],item['Email'],item['Age'],item['Mobile'],item['Gender'],item['Remarks'],item['created_at'],item['updated_at'] )
            listOfTopics.append(tp)
        '''
        return render(request, 'show.html', {"mylist": all_topics_json})
'''
class Topics:

    def __init__(self,id,fn,ln,em,ag,mo,Ge,re,crt,updt):
        self.id = id
        self.First_Name = fn
        self.Last_Name = ln
        self.Email = em
        self.Age = ag
        self.Mobile=mo
        self.Gender=Ge
        self.Remarks=re
        self.created_at = crt
        self.updated_at = updt

    def __str__(self):
        return " ID : {} \n First Name : {} \n  Last Name : {} \n Email : {} \n Age :{} \n  Mobile :{} \n  Gender: {} \n Reamrk:{}"\
            .format(self.id,self.First_Name,self.Last_Name,self.Email,self.Age,self.Mobile,self.Gender,self.Remarks,self.created_at,self.updated_at)
'''
def SingleData(request):
    ide=request.GET['id']
    print(ide)
    #uriget=
    response = requests.get("http://localhost:9000/stud/{}".format(ide))
    getid=response.json()
    print(getid)
    return render(request,'Single.html',{'mylist':getid})

def GetId(request):
        return render(request,'id.html')




def Delete(request):
    #print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    ide = request.GET['id']
    #print(ide)
    # uriget=
    response = requests.delete("http://localhost:9000/stud/delete/{}".format(ide))
    #getid = response.json()
    return render(request,'Delete.html')



ide1 = 0
def Update(request):
   #ide = request.GET['id']

   if request.method=='GET':
         ide = request.GET['id']
         global ide1
         ide1 = ide
         response = requests.get("http://localhost:9000/stud/{}".format(ide))
         getid = response.json()

         #print("single Data--------------------",getid)
         #student = StudentForm()
         form = StudentForm(getid)

         return render(request,'UpdateSubmit.html',{'form':form,'userid':getid})
   else:
       #ide1 = request.POST['id']

       student = StudentForm(request.POST)
       print(request.POST)
       #putid= "http://localhost:9000/stud/update/{}/".format(ide1)
       #print("==========URL=======",putid)
       #resposne = requests.put("http://localhost:9000/stud/update/",data=request.POST)
       response=requests.put("http://localhost:9000/stud/update/{}/".format(ide1),data=request.POST)
       print(response.status_code)
       return render(request, 'FirstPage.html')
