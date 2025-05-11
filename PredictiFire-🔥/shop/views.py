from .models import ContactUs
from django.shortcuts import render
from django.contrib import messages
import numpy as np
import joblib
import pandas as pd

def index(request):
    if request.method == "POST":
        area = request.POST['area']
        bhk = request.POST['bhk']
        bath = request.POST['bath']
        location = request.POST['location']
        if int(area)<10 or int(area)>10000000 or int(bhk)<1 or int(bhk)>100 or int(bath)<1 or int(bath)>100 or len(location)<2 or len(location)>50:
            messages.error(request, "Please fill the form correctly")
        else:
            predict=[area,bhk,bath,location]
            print(predict_price(predict[3],predict[0],predict[2],predict[1]))

    return render(request, 'shop/index.html')


def tool(request):
    if request.method == "POST":
        area = request.POST['area']
        bhk = request.POST['bhk']
        bath = request.POST['bath']
        location = request.POST['location']
        if int(area)<10 or int(area)>10000000 or int(bhk)<1 or int(bhk)>100 or int(bath)<1 or int(bath)>100 or len(location)<2 or len(location)>50:
            messages.error(request, "Please fill the form correctly")
        else:
            predict=[area,bhk,bath,location]
            print(predict_price(predict[3],predict[0],predict[2],predict[1]))
            results=predict_price(predict[3],predict[0],predict[2],predict[1])
            return render(request,'shop/result.html',{'res':results})

    return render(request, 'shop/tool.html')

#-------------------------------------- ACTUAL-MODEL---------------------------
# Converting CSV File to DataFrame
data=pd.read_csv('Prediction_Model/predictifire.csv')

# Differntaiting InDependent(X) variables & Dependent (Y) variable
X=data.drop('price',axis=1)
Y=data.price

res=joblib.load('Prediction_Model/predictifire.joblib')

# Making Function to Predict Price
def predict_price(location,sqft,bath,bhk):
    loc_index = np.where(X.columns==location)[0][0]
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return "%.2f" % res.predict([x])[0]

#----------------------------------------------------------------------------------------------------------------------

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact1 = ContactUs(name=name, email=email, phone=phone, content=content)
            contact1.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "shop/contact.html")

