import json

import requests
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.context_processors import request
from requests.auth import HTTPBasicAuth

from myapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from myapp.models import Bookings, Contact, Register, Orders, Manager


# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def specials(request):
    return render(request, 'specials.html')

def events(request):
    return render(request, 'events.html')

def chefs(request):
    return render(request, 'chefs.html')

def gallery(request):
    return render(request, 'gallery.html')

def order(request):
    if request.method == 'POST':
        myorders = Orders(
            name = request.POST['name'],
            email = request.POST['email'],
            order_name = request.POST['order_name'],
            date = request.POST['date'],
            address = request.POST['address'],
            town = request.POST['town'],
            postal_code = request.POST['postal_code']
        )
        myorders.save()
        return redirect('/order')
    else:
        return render(request,'order.html')

def Admin(request):
    newapplicants=Register.objects.all()
    tablebookings = Bookings.objects.all()
    mycontacts = Contact.objects.all()
    theorders = Orders.objects.all()

    return render(request,'Admin.html',context={
        'newapplications':newapplicants,
        'tablesbooked':tablebookings,
        'mycontact':mycontacts,
        'customerorders':theorders
    })
def contact(request):
    if request.method == 'POST':
        ourcontacts=Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        ourcontacts.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')
def booking(request):
    if request.method == 'POST':
        ourbookings=Bookings(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            time = request.POST['time'],
            number = request.POST['number'],
            message = request.POST['message']
        )
        ourbookings.save()
        return redirect('/booking')
    else:
        return render(request,'booking.html')

def register(request):
    if request.method == 'POST':
        chefs = Register(
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            file_upload = request.POST['file_upload']
        )
        chefs.save()
        return redirect('/chefs')
    else:
        return render(request,'register.html')
def login(request):
    return render(request, 'login.html')

def delete(request, id):
    oderz = Orders.objects.get(id = id)
    oderz.delete()
    return redirect('/Admin')

def deletebooking(request, id):
    bookingz = Bookings.objects.get(id = id)
    bookingz.delete()
    return redirect('/Admin')

def deletecontact(request, id):
    contactz = Contact.objects.get(id = id)
    contactz.delete()
    return redirect('/Admin')

def deleteregister(request, id):
    registerz = Register.objects.get(id = id)
    registerz.delete()
    return redirect('/Admin')




def token(request):
    consumer_key = 'uBWUC3QGPz3f9AQI638lcScam9cft9BqwaX7SafErAYQjqtR'
    consumer_secret = 'hnmA9OMreI4YwCe48UmnvA8p6xHcjTlXoELyPGrAZ47AAJGgKWyNPjG0DzDMNDYw'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')


#Mpesa API views
def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "NostalgiaEats",
            "TransactionDesc": "Food Payment"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")


def edit(request, id):
    eddittables = Bookings.objects.get(id = id)
    return render(request,'edittable.html',{'edittabled':eddittables})

def admindashboard(request):
    if request.method == 'POST':
        if Manager.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            manager = Manager.objects.get()
            return render(request, 'admindashboard.html',{'manager':manager})
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


