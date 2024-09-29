from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PatientForm


def home(request):
    return render(request, 'home.html')


def doctor_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Login successful! Welcome back Doctor, {user.username}.")
            return redirect('doctor_reset_password')  # Redirect to dashboard after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('doctor_login')

    return render(request, 'login.html', {
        'Page_Layout': 'Doctor Login'
    })

# Doctor logout
def doctor_logout(request):
    logout(request)
    return redirect('doctor_login')

#@login_required(login_url=reverse_lazy('doctor_login'))
def doctor_reset_password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        if password:
            # Ensure that the user is authenticated before setting the password
            if request.user.is_authenticated:
                request.user.set_password(password)
                request.user.save()  # Save the new password to the database
                messages.success(request, "Password changed successfully. Please log in again.")
                return redirect('doctor_login')
            else:
                messages.error(request, "You must be logged in to change your password.")
        else:
            messages.error(request, "Password cannot be empty.")   
    return render(request, 'reset-password.html')


def doctor_registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Create the user
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('doctor_login')
        else:
            messages.error(request, "Username already exists")
            return redirect('doctor_registration')

    return render(request, 'registration.html', {
        'Page_Layout': 'Doctor Registration'
    })


@login_required(login_url=reverse_lazy('doctor_login'))
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient added successfully.")
            return redirect('add_patient')  # Redirect after a successful save
        else:
            messages.error(request, "Something went wrong. Please check the form.")
    else:
        form = PatientForm()  # Show an empty form for GET request

    return render(request, 'add-patient.html', {
        'form': form
    })


@login_required(login_url=reverse_lazy('doctor_login'))
def dashboard(request):
    return render(request, 'dashboard.html')
