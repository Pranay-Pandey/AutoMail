from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .send_auto_mail import send_email
import csv
import io
# Create your views here.
# Views scripts takes in request and produces response

def home(request):
    return render(request, "landing_page.html" , {"name":"Pranay"})

def say_hello(request):


    if request.method=="POST":
        i = 0
        success_list = []
        failure_list = []
        sender_email = request.POST['sender_email']
        sender_password = request.POST['sender_password']
        sender_name = request.POST['sender_name']
        receiver_email = request.POST['receiver_email']
        subject = request.POST['subject']
        message = request.POST['message']
        fil=None
        try:
            fil = request.FILES['fil']
        except:
            pass
        receiver_list = None
        try:
            
            receiver_list_csv = request.FILES['receiver_csv']
            # receiver_list = csv.reader(receiver_list_csv)
            # print(type(receiver_list_csv))
            file = receiver_list_csv.read().decode('utf-8')
            reader = io.StringIO(file)

            # Generate a list comprehension
            receiver_list = [line for line in reader]
        except:
            receiver_list = [receiver_email]
        for receiver_item in receiver_list:
            print(receiver_item)
            try:
                send_email(sender_email, sender_name, sender_password, receiver_item, subject,
                message, fil)
                i = i+1
                success_list.append(receiver_item)
            except Exception as e:
                print("exception = ",e)
                failure_list.append(receiver_item)


        messages.success(request, "Success")

        response = HttpResponse(content_type="text/plain")
        response["Content-Disposition"] = 'attachment; filename=successreport.txt'

        lines = [f"Succeeded in sending emails to {i} contacts\n"]
        for user in success_list:
            lines.append(user+'\n')
        lines.append("\n\n Failed to send to these contacts\n")
        for user in failure_list:
            lines.append(user+'\n')


        response.writelines(lines)
        return response

        return render(request, "hello_world.html", {"success": i, "sender_email":sender_email, 
        "sender_password":sender_password})

    return render(request, "hello_world.html", {"name":"Pranay"})