from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact_us(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=request.POST.get('subject')
        msz=request.POST.get('message')

        print(name)

        obj=contact()
        obj.name=name
        obj.email=email
        obj.subject=sub
        obj.message=msz
        
        obj.save()
        return HttpResponse(f"Thanks {name} for the input!")

    return render(request,'contact.html')

def about(request):
    
    return render(request,'about.html')
@login_required   
def Order(request):
   
    appetizers=MenuItem.objects.filter(category__name__contains='Appetizer')
    entres=MenuItem.objects.filter(category__name__contains='Entre')
    desserts=MenuItem.objects.filter(category__name__contains='Dessert')
    drinks=MenuItem.objects.filter(category__name__contains='Drink')

    context={
    'appetizers':appetizers,
    'entres':entres,
    'desserts':desserts,
    'drinks':drinks,
    }

    

    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip')
        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        test= request.POST.getlist('sel[]')
        test1=[]
        print(test)
        for i in test:
            if i !='':
                test1.append(int(i))
        
        print(test1)
        print(items)
        c=0
        if(len(items)==len(test1)):
            for item in items:
                menu_item = MenuItem.objects.get(pk=int(item))
                print('menu item',float(menu_item.price))
                print(c,'at beg')
                print( 'number of item', float(test1[c]))
                f_p=((float(menu_item.price))*(float(test1[c])))
                print('total',f_p)
                item_data = {
                    'id': menu_item.pk,
                    'name': menu_item.name,
                    'e_p': menu_item.price,
                    'price': f_p,
                    'num':test1[c],
                }
                order_items['items'].append(item_data)
                c=c+1

                print(c,'at end')

                price = 0.0
                item_ids = []
                item_num=[]

            for item in order_items['items']:
                price += item['price']
                item_ids.append(item['id'])
                item_num.append(item['num'])
            
            print(item_num, 'final items')

            order = ordermodel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                state=state,
                city=city,
                zip_code=zip_code
                )
            order.set_num(item_num)
            order.items.add(*item_ids)
            order.save()

            
            

            context = {
                'items': order_items['items'],
                'price': price,
                'obj':order.num,
                
                
                
            }

            return render(request, 'order_confirmation.html', context)
        else:
            messages.error(request,"Please select the checkbox and also mention the quantity !")
            return redirect('order')

    return render(request,'order.html',context)  

def conf(request):
    obj=ordermodel.objects.order_by('id').last()
    return render(request,'pay.html',{'o':obj})
    


# Create your views here.
def home(request):
    return render(request,"restora/register.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        name=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already registred!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request,"Passwords did not match")
        
        myuser=User.objects.create_user(username,email,pass1)
        
        myuser.first_name=name
        myuser.save()

        messages.success(request,"Your account has been succesfully created.")
        
        return redirect('signin')

    return render(request,"restora/register.html")
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
           
            login(request,user)
            name=user.first_name
            return render(request,"index.html",{'name':name})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')
    return render(request,"restora/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')

def reg(request):
    return render(request,"restora/register.html")


def dash(request):
    return render(request,'choice/dashboard.html')

def menu_list(request):
    context={'menu_list':MenuItem.objects.all()}
    return render(request,'menu_reg/menu_list.html',context)

def menu_form(request,id=0):

    if request.method=='GET':
        if id==0:
            form= Menuform()
        else:
            menu=MenuItem.objects.get(id=id)
            form=Menuform(instance=menu)
        return render(request,'menu_reg/menu_form.html',{'form':form})
    else:
        if id==0:
            form= Menuform(request.POST,request.FILES)
        else:
            menu= MenuItem.objects.get(pk=id)
            form=Menuform(request.POST,request.FILES,instance=menu)
        if form.is_valid():
            form.save()
        return redirect('menu_list')
def menu_delete(request,id):
    menu= MenuItem.objects.get(pk=id)
    menu.delete()
    return redirect('menu_list')


def order_list(request):
    context={'order_list':ordermodel.objects.all()}
    return render(request,'order_reg/order_list.html',context)

def order_form(request,id=0):
    if request.method=='GET':
        
        order=ordermodel.objects.get(id=id)
        form=orderform(instance=order)
        return render(request,'order_reg/order_form.html',{'form':form})
    else:
        
        order= ordermodel.objects.get(pk=id)
        form=orderform(request.POST,instance=order)
        if form.is_valid():
            form.save()
        return redirect('order_list')

def order_delete(request,id):
    order= ordermodel.objects.get(pk=id)
    order.delete()
    return redirect('order_list')


def con_list(request):
    context={'con_list':contact.objects.all()}
    return render(request,'contact_reg/con_list.html',context)


    
def con_delete(request,id):
    con= contact.objects.get(pk=id)
    con.delete()
    return redirect('con_list')


def adm_list(request):
    context={'adm_list':adminuser.objects.all()}
    return render(request,'admin_reg/adm_list.html',context)


def user_list(request):
    context={'user_list':User.objects.filter(is_staff=False)}
    return render(request,'user_reg/user_list.html',context)


    
def user_delete(request,id):
    user= User.objects.get(pk=id)
    user.delete()
    return redirect('user_list')

def adm_form(request,id=0):

    if request.method=='GET':
        if id==0:
            form= admform()
        else:
            adm=adminuser.objects.get(id=id)
            form=admform(instance=adm)
        return render(request,'admin_reg/adm_form.html',{'form':form})
    else:
        if id==0:
            form= admform(request.POST)
        else:
            adm= adminuser.objects.get(pk=id)
            form=admform(request.POST,instance=adm)
        if form.is_valid():
            form.save()
        return redirect('adm_list')
    
def adm_delete(request,id):
    adm= adminuser.objects.get(pk=id)
    adm.delete()
    return redirect('adm_list')


def adm_log(request):
    return render(request,'adm/signin.html')
def ad(request):
    
    a=request.POST.get('username')
    b=request.POST.get('pass1')
    if adminuser.objects.filter(username=a,pwd=b,is_admin=True):
        
        return render(request,'choice/dashboard.html')
    else:
        messages.error(request,"Bad Credentials!")
        return redirect('adm_log')





