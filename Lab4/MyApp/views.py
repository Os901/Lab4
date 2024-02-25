from django.shortcuts import render
from django.http import HttpResponse

def defult_page(request):
    return render(request, "default_page.html")

def anyNumber(request):
    price = request.GET.get("price") or "Write any number after adding ?price=(number) to the URL"
    try:
        price = float(price)  # Convert the string to a float
        total = price * 1.15   # Calculate the total plus tax
        return HttpResponse("The total plus tax is {:.2f}".format(total))
    except ValueError:
        return HttpResponse("Invalid price format. Please enter a valid number.")

def tax_rate(request):
    tax_rate = 0.15
    context = {'tax_rate': tax_rate}
    return render(request, 'tax_rate.html', context)