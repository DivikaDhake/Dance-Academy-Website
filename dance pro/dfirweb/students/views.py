# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Student
from .forms import StudentRegistrationForm

def home(request):
    return render(request, 'students/home.html')

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form': form})

def thank_you(request):
    return render(request, 'students/thank_you.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def manage_students(request):
    students = Student.objects.all()
    return render(request, 'students/manage_students.html', {'students': students})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('manage_students')
    return render(request, 'students/delete_student.html', {'student': student})

def about(request):
    return render(request, 'students/about.html')

# Define a hard-coded password for the admin
ADMIN_PASSWORD = 'divika@143d'

def admin_login(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('manage_students')
        else:
            return render(request, 'students/admin_login.html', {'error': 'Invalid password'})
    return render(request, 'students/admin_login.html')

@login_required
def manage_students(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    students = Student.objects.all()
    return render(request, 'students/manage_students.html', {'students': students})

@login_required
def delete_student(request, pk):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('manage_students')

def contact(request):
    return render(request, 'students/contact.html')