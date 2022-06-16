from asyncio.windows_events import NULL
from genericpath import exists
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
# from models import Consult
from django.contrib.auth.decorators import login_required
from .forms import SkinCareForm, BackPainForm
from django.contrib import messages
# Create your views here.

def general_info(request):
    return render(request, 'consultations/general_info.html')

def exercise(request):
    return render(request, 'consultations/exercise.html')

def self_check(request):
    return render(request, 'consultations/self_check.html')

def fasting(request):
    return render(request, 'consultations/fasting.html')

def sleep(request):
    return render(request, 'consultations/sleep.html')

def food(request):
    return render(request, 'consultations/food.html')

def skin_care(request):
    if request.method == "POST":
        form = SkinCareForm(request.POST)
        name_of_consult = "Skin Care"
        prescription = request.POST['RadioGroup1']

        messages.success(request, prescription+' self-management protocol has been sent to your email.')
        return redirect('skin_care')
        

    else:
        return render(request, 'consultations/skin_care.html')

def back_pain(request):
    if request.method == "POST":
        form = BackPainForm(request.POST)
        name_of_consult = "Back & Neck Pain"
        if request.POST["radio1"] == "yes" or request.POST["radio2"] == "yes" or request.POST["radio3"] == "yes"or request.POST["radio4"] == "yes" or request.POST["radio5"] == "yes":
            prescription = "Urgently see your doctor"
            messages.warning(request, prescription)
            return redirect('back_pain')
        
        else:
            messages.success(request, "Home Lower Back Rehabilitation Programme For 6 Weeks. has been sent to your email")
            return redirect('back_pain')

    return render(request, 'consultations/back_pain.html')

def back_pain2(request):
    return render(request, 'consultations/back_pain2.html')

def female_urinary(request):
    if request.method == "POST":
        form = BackPainForm(request.POST)
        name_of_consult = "Female Urinary"
        if request.POST["radio1"] == "yes" or request.POST["radio2"] == "yes" or request.POST["radio3"] == "yes":
            prescription = "Urgently see your doctor"
            messages.warning(request, prescription)
            return redirect('female_urinary')
        
        else:
            return redirect('female_urinary2')

    return render(request, 'consultations/female_urinary.html')

def female_urinary2(request):
    if request.method == "POST":
        form = BackPainForm(request.POST)
        name_of_consult = "Female Urinary"
        if request.POST["radio3"] == "yes":
            prescription = "combine the pelvic floor muscle training program & the bladder training program for 12 weeks. If no improvement consult a urogynaecologist."
            messages.success(request, prescription)
            return redirect('female_urinary2')
        elif request.POST["radio1"] == "yes" and request.POST["radio2"] == "yes":
            prescription = "combine the pelvic floor muscle training program & the bladder training program for 12 weeks. If no improvement consult a urogynaecologist."
            messages.success(request, prescription)
            return redirect('female_urinary2')
        elif request.POST["radio1"] == "yes" and request.POST["radio2"] == "no":
            prescription = "Do the pelvic floor muscle training program for 12 weeks. If no improvement consult a urogynaecologist."
            messages.success(request, prescription)
            return redirect('female_urinary2')
        elif request.POST["radio2"] == "yes" and request.POST["radio1"] == "no":
            prescription = "Do the bladder training program for 12 weeks. If no improvement consult a urogynaecologist."
            messages.success(request, prescription)
            return redirect('female_urinary2')
        elif request.POST["radio4"] == "yes":
            prescription = "Do the pelvic floor muscle training program for 12 weeks. If no improvement consult a urogynaecologist."
            messages.success(request, prescription)
            return redirect('female_urinary2')
        else:
            return redirect('female_urinary2')

    return render(request, 'consultations/female_urinary2.html')
