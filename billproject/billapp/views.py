from django.shortcuts import render

def home(request):

    total = None

    if request.method == "POST":

        price = float(request.POST.get('price'))
        gst = float(request.POST.get('gst'))

        total = price + (price * gst / 100)

        print("Total Bill Amount =", total)

    return render(request, 'index.html', {'total': total})