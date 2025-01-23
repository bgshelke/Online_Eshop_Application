from django.shortcuts import render, redirect
from .models.product import Product
from .models.catagory import Catagory
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
# Create your views here.


# def index_view(request):
#     template_name = 'stores/index.html'
#     product_data =None
#     catagories = Catagory.objects.all()
#     catagoryID = request.GET.get('catagory')
#     if catagoryID:
#         product_data=Product.objects.filter(catagory=catagoryID
#
#     else:
#         product_data = Product.objects.all()
#     data={}
#     data['products']=product_data
#     data['catagories']=catagories
#     context={'product_data':product_data,'catagories':catagories,'data':data}
#     return render(request,template_name,context)


# this method is used only for validation purpose for customers which registered using sign-up form
# def validate_customer(obj):
#     error_msg = None
#     if (not obj.fname):
#         error_msg = 'Fname is required to create an account'
#     if (not obj.lname):
#         error_msg = 'lname is required to create an account'
#
#     if (not obj.email):
#         error_msg = 'Email is required to create an account'
#     if (not obj.phone):
#         error_msg = 'Phone number is required to create an account'
#     if (not obj.password):
#         error_msg = 'Password is required to create an account'
#     if len(obj.fname) < 4 or len(obj.lname) < 4:
#         error_msg = 'Fname/Lname length should be grater than 4'
#     if not obj.email.endswith('@gmail.com'):
#         error_msg = 'Please provide valid email address'
#
#     isExist = obj.ifExist()
#
#     if isExist:
#         error_msg = 'This Email Id is Already registered!!!'
#
#     return error_msg


# class SignupView(View):
#     def get(self,request):
#         template_name = 'signup.html'
#         context = {}
#         return render(request, template_name, context)
#
#     def post(self,request):
#         if request.method == 'POST':
#             print('signup caalled')
#             fn = request.POST['fname']
#             ln = request.POST['lname']
#             email = request.POST['email']
#             phn = request.POST['phone']
#             pw = request.POST['password']
#
#             password = make_password(pw)
#
#             # filled data is taking for resubmission purpose
#
#             filled_data = {
#                 'fname': fn,
#                 'lname': ln,
#                 'email': email,
#                 'phone': phn,
#                 'password': pw
#             }
#
#             obj = Customer(fname=fn, lname=ln, email=email, phone=phn, password=password)
#             error_msg = validate_customer(obj)
#             # data saving
#             if not error_msg:
#                 obj.save()
#                 print('After Error Handling')
#                 return redirect('home_url')
#             data = {
#                 'error_msg': error_msg,
#                 'filled_data': filled_data
#             }
#             return render(request, 'signup.html', {'data': data})

# def signup_view(request):
#     template_name = 'signup.html'
#     print('method----->',request.method)
#     if request.method == 'POST' :
#         print('signup caalled')
#         fn = request.POST['fname']
#         ln = request.POST['lname']
#         email = request.POST['email']
#         phn = request.POST['phone']
#         pw = request.POST['password']
#
#         password=make_password(pw)
#
#         # filled data is taking for resubmission purpose
#
#         filled_data = {
#             'fname':fn,
#             'lname':ln,
#             'email':email,
#             'phone':phn,
#             'password':pw
#         }
#
#         obj = Customer(fname=fn, lname=ln, email=email, phone=phn, password=password)
#
#         error_msg = validate_customer(obj)
#
#
#         # data saving
#         if not error_msg:
#             obj.save()
#             print('After Error Handling')
#             return redirect('home_url')
#
#         data={
#             'error_msg': error_msg,
#             'filled_data':filled_data
#         }
#         return render(request,'signup.html',{'data':data})
#     context={}
#     return render(request,template_name,context)



# class LoginView(View):
#     def get(self,request):
#         template_name = 'login.html'
#         context = {}
#         return render(request, template_name, context)
#
#     def post(self,request):
#         email = request.POST['email']
#         pw = request.POST['password']
#         customer = Customer.objects.get(email=email)
#         password = check_password(pw, customer.password)
#         error_msg = None
#         print('password-->', password)
#         if customer.email == email and password == True:
#             return redirect('home_url')
#         else:
#             error_msg = 'Password or EmailId is Incorrect'
#             context = {'error_msg': error_msg}
#             return render(request, 'login.html', context)


# def login_view(request):
#     if request.method == 'GET':
#         template_name = 'login.html'
#         context={}
#         return render(request, template_name, context)
#     else:
#
#         email = request.POST['email']
#         pw=request.POST['password']
#         customer = Customer.objects.get(email=email)
#         password = check_password(pw,customer.password)
#         error_msg = None
#         print('password-->',password)
#         if customer.email == email and password==True:
#             return redirect('home_url')
#         else:
#             error_msg = 'Password or EmailId is Incorrect'
#             context = {'error_msg':error_msg}
#             return render(request, 'login.html', context)