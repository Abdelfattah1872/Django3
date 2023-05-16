from .models import Student
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, request
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

def get_data(request):

    myData = Student.objects.all().values()
    context={'myData':myData}

    return render(request, 'showData.html', context)


def index(request):
    

    return render(request, 'show.html')



class StudentCreate(CreateView):
    model = Student
    fields = ['fName', 'lName']


class StudentList(ListView):
# specify the model for list view
    model = Student



class StudentUpdateView(UpdateView):
    # specify the model you want to use
    model = Student
    # specify the ﬁelds
    ﬁelds = [
    "fName",
    "lName"
    ]
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"


class StudentDeleteView(DeleteView):
    # specify the model you want to use
    model = Student
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"
    template_name = "students/student_conﬁrm_delete.html"