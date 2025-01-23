from django.views import View
from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.catagory import Catagory
from ..models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password

def validate_customer(obj):
    error_msg = None
    if (not obj.fname):
        error_msg = 'Fname is required to create an account'
    if (not obj.lname):
        error_msg = 'lname is required to create an account'

    if (not obj.email):
        error_msg = 'Email is required to create an account'
    if (not obj.phone):
        error_msg = 'Phone number is required to create an account'
    if (not obj.password):
        error_msg = 'Password is required to create an account'
    if len(obj.fname) < 4 or len(obj.lname) < 4:
        error_msg = 'Fname/Lname length should be grater than 4'
    if not obj.email.endswith('@gmail.com'):
        error_msg = 'Please provide valid email address'

    isExist = obj.ifExist()

    if isExist:
        error_msg = 'This Email Id is Already registered!!!'

    return error_msg


class SignupView(View):
    def get(self, request):
        template_name = 'signup.html'
        context = {}
        return render(request, template_name, context)

    def post(self, request):
        if request.method == 'POST':
            print('signup caalled')
            fn = request.POST['fname']
            ln = request.POST['lname']
            email = request.POST['email']
            phn = request.POST['phone']
            pw = request.POST['password']

            password = make_password(pw)

            # filled data is taking for resubmission purpose

            filled_data = {
                'fname': fn,
                'lname': ln,
                'email': email,
                'phone': phn,
                'password': pw
            }

            obj = Customer(fname=fn, lname=ln, email=email, phone=phn, password=password)
            error_msg = validate_customer(obj)
            # data saving
            if not error_msg:
                obj.save()
                print('After Error Handling')
                return redirect('home_url')
            data = {
                'error_msg': error_msg,
                'filled_data': filled_data
            }
            return render(request, 'signup.html', {'data': data})
