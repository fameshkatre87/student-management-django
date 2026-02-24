from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student

@login_required
def student_list(request):
    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(
            name__icontains=query
        ) | Student.objects.filter(
            roll_number__icontains=query
        )
    else:
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})


@login_required
def add_student(request):
    if request.method == 'POST':
        roll = request.POST['roll']
        email = request.POST['email']

        #  Roll number validation
        if Student.objects.filter(roll_number=roll).exists():
            messages.error(request, "Roll number already exists!")
            return redirect('add_student')

        #  Email validation
        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('add_student')

        Student.objects.create(
            name=request.POST['name'],
            roll_number=roll,
            department=request.POST['Course'],
            email=email
        )

        messages.success(request, "Student added successfully!")
        return redirect('student_list')

    return render(request, 'students/add_student.html')

@login_required
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        email = request.POST['email']
        dept = request.POST['Course']

        #  Roll number validation (exclude current student)
        if Student.objects.filter(roll_number=roll).exclude(id=student.id).exists():
            messages.error(request, "Roll number already exists!")
            return redirect('edit_student', id=student.id)

        #  Email validation (exclude current student)
        if Student.objects.filter(email=email).exclude(id=student.id).exists():
            messages.error(request, "Email already exists!")
            return redirect('edit_student', id=student.id)

        # Update allowed
        student.name = name
        student.roll_number = roll
        student.department = dept
        student.email = email
        student.save()

        messages.success(request, "Student updated successfully!")
        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


def login_view(request):
    error = None
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('student_list')
        else:
            error = "Invalid username or password"

    return render(request, 'students/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_list_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_api(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(
            {'error': 'Student not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student.delete()
        return Response(
            {'message': 'Student deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
