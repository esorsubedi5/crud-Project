from django.shortcuts import render
from django.shortcuts import redirect  
from .forms import StudentDetailForm  
from .models import StudentDetail  
from django.contrib import messages  


def addStudent(request):
    if request.method == "POST":
        sset = StudentDetailForm(request.POST)
        if sset.is_valid():
            sset.save()
            messages.success(request, 'Student Added Successfully')
    sset = StudentDetailForm()
    data = StudentDetail.objects.all()
    return render(request, 'index.html', context={'fm': sset, 'studata': data})
def deleteStudent(request, id):
    StudentDetail.objects.get(pk=id).delete()
    messages.success(request, 'Student Record Deleted')
    return redirect('/')
def edit(request, id):
    inst = StudentDetail.objects.get(pk=id)
    if request.method == "POST":
        sset = StudentDetailForm(request.POST, instance=inst)
        if sset.is_valid():
            sset.save()
            messages.success(request, 'Student Record Updated')
            return redirect('/')
    sset = StudentDetailForm(instance=inst)
    return render(request, 'basic.html', context={'fm': sset})