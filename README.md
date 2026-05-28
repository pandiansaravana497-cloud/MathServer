# Ex.04 Design a Website for Server Side Processing
## Date:

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
~~~
## views.py
from django.shortcuts import render

def bill(request):
    total = None

    if request.method == "POST":
        price = float(request.POST.get("price"))
        gst = float(request.POST.get("gst"))

        total = price + (price * gst / 100)

    return render(request, "bill.html", {"total": total})
```

---

## urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill, name='bill'),
]
```

---

## bill.html
<!DOCTYPE html>
<html>
<head>
    <title>GST Bill Calculator</title>

    <style>
        body{
            font-family: Arial;
            margin: 50px;
        }

        .box{
            width: 350px;
            padding: 20px;
            border: 1px solid gray;
            border-radius: 10px;
        }

        input{
            width: 100%;
            padding: 10px;
            margin-top: 10px;
        }

        button{
            margin-top: 15px;
            padding: 10px 20px;
        }
    </style>
</head>

<body>

<div class="box">
    <h2>GST Bill Calculator</h2>

    <form method="POST">
        {% csrf_token %}

        <label>Price</label>
        <input type="number" name="price" required>

        <label>GST Percentage</label>
        <input type="number" name="gst" required>

        <button type="submit">Calculate</button>
    </form>

    {% if total %}
        <h3>Total Bill Amount: ₹ {{ total }}</h3>
    {% endif %}

</div>

</body>
</html>
```
~~~


## OUTPUT - SERVER SIDE:
<img width="944" height="328" alt="Screenshot 2026-05-28 092816" src="https://github.com/user-attachments/assets/d201b26c-592d-4e3d-95e0-d291351380ff" />


## OUTPUT - WEBPAGE:
<img width="1675" height="941" alt="Screenshot 2026-05-28 093043" src="https://github.com/user-attachments/assets/bca2064e-e70d-4a3e-9fc8-02d40e2fd2b2" />


## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
