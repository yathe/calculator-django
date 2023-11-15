# # calculator/views.py
# from django.shortcuts import render
# from django.http import HttpResponse

# def calculator(request):
#     return render(request, 'calculator.html')

# def calculate(request):
#     if request.method == 'POST':
#         num1 = float(request.POST['num1'])
#         num2 = float(request.POST['num2'])
#         opr = request.POST['opr']

#         if opr == 'add':
#             result = num1 + num2
#         elif opr == 'subtract':
#             result = num1 - num2
#         elif opr == 'multiply':
#             result = num1 * num2
#         elif opr == 'divide':
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 result = 'Division by zero is not allowed'
#         else:
#             result = 'Invalid operation'

#         return render(request, 'calculator.html', {'result': result})
# calculator/views.py
from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    return render(request, 'calculator.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Division by zero is not allowed'
        else:
            result = 'Invalid operation'

        return render(request, 'calculator.html', {'result': result})



