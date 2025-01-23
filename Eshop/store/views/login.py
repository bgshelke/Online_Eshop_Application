from django.views import View
from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.catagory import Catagory
from ..models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password



class LoginView(View):
    def get(self,request):
        template_name = 'login.html'
        context = {}
        return render(request, template_name, context)

    def post(self,request):
        email = request.POST['email']
        pw = request.POST['password']
        customer = Customer.objects.get(email=email)
        # password = check_password(pw, customer.password)
        error_msg = None
        # print('password-->', password)
        if customer:
            flag=check_password(pw,customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['email'] = customer.email
                return redirect('home_url')
            else:
                error_msg = 'Password or EmailId is Incorrect'
                context = {'error_msg': error_msg}
                return render(request, 'login.html', context)
        # if customer.email == email and password == True:
        #     return redirect('home_url')
        # else:
        #     error_msg = 'Password or EmailId is Incorrect'
        #     context = {'error_msg': error_msg}
        #     return render(request, 'login.html', context)

