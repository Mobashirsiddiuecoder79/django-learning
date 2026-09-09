from django.shortcuts import render

# Create your views here.
def student_fee(request):
    return render(request,template_name= 'fee/student.html')