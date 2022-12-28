from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from  .models import *
from django.contrib import auth
from django.contrib.auth.models import User
import os
import random
import string
from django.conf import settings
from django.core.mail import send_mail
import hashlib
import datetime

# return to same page 
# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Create your views here.
def index(request):
	# data=productup.objects.all()
	mob=productup.objects.filter(catagory="mobiles").order_by('-id')[:3]
	tv=productup.objects.filter(catagory="tv").order_by('-id')[:3]
	appliances=productup.objects.filter(catagory="appliances").order_by('-id')[:3]
	camera=productup.objects.filter(catagory="camera").order_by('-id')[:3]
	return render(request,"index.html",{"mob":mob,"tv":tv, "appliances":appliances,"camera":camera})

def register(request):
	if request.method == "POST":
		name=request.POST['Name']
		email=request.POST['Email']
		password=request.POST['Password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		add=register_form(name=name,email=email,password=password,hashpass=hashpass)
		add.save()
		x = ''.join(random.choices(name + string.digits, k=8))
		y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
		subject = 'welcome to electrostore'
		message = f'Hi {name}, thank you for registering in electrostore . your user username: {email} and  password: {password}. '
		email_from = settings.EMAIL_HOST_USER 
		recipient_list = [email, ] 
		send_mail( subject, message, email_from, recipient_list )
		return render(request,"index.html",)
	else:
		return render(request,"index.html")

def login(request):
	if request.method == "POST":
		name=request.POST['Name']
		password=request.POST['Password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		data= register_form.objects.filter(name=name,hashpass=hashpass)
		if data:
			for x in data:
				request.session['user_id']=x.id
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def logout(request):
	if request.session.has_key('user_id'):
		del request.session['user_id']
	return HttpResponseRedirect('/')
	
def about(request):
	return render(request,"about.html")

def contact(request):
	if request.method == "POST":
		name=request.POST['name']
		email=request.POST['email']
		message=request.POST['message']
		add=contact_form(name=name,message=message,email=email)
		add.save()
		return render(request,"contact.html")
	else:
		return render(request,"contact.html")

def faqs(request):
	return render(request,"faqs.html")

def help(request):
	return render(request,"help.html")

def privacy(request):
	return render(request,"privacy.html")

def product(request):
	newmobiles=productup.objects.filter(catagory="newmobiles")
	mob=productup.objects.filter(catagory="mobiles")
	laptop=productup.objects.filter(catagory="laptop")
	accessories=productup.objects.filter(catagory="accessories")
	return render(request,"product.html",{"newmobiles":newmobiles,"mob":mob, "laptop":laptop,"accessories":accessories})

def product2(request):
	tv=productup.objects.filter(catagory="tv")
	appliances=productup.objects.filter(catagory="appliances")
	smallappliances=productup.objects.filter(catagory="smallappliances")
	camera=productup.objects.filter(catagory="camera")
	return render(request,"product2.html",{"tv":tv, "appliances":appliances,"smallappliances":smallappliances,"camera":camera})
	
def single(request):
	pid=request.GET['pid']
	products=productup.objects.filter(id=pid)
	return render(request,"single.html",{'prd':products})

def single2(request):
	return render(request,"single2.html")

def terms(request):
	return render(request,"terms.html")

                 # Admin

def adminindex(request):
	return render(request,"admin/adminindex.html")

# from reportlab.pdfgen import canvas 
# from django.views.generic import View
# from electrostore.utils import render_to_pdf
# def sample(request):
# 	uid=request.GET['uid']
# 	data=register_form.objects.filter(id=uid)

# 	pdf=render_to_pdf('admin/sample.html',{"data":data})
# 	return HttpResponse(pdf,content_type='application/pdf')

def blocks(request):
	return render(request,"admin/blocks.html")

def cards(request):
	return render(request,"admin/cards.html")

def carousels(request):
	return render(request,"admin/carousels.html")

def forms(request):
	return render(request,"admin/forms.html")

def people(request):
	return render(request,"admin/people.html")

def viewdata(request):
	user= request.session['user_id']
	data= register_form.objects.all().filter(id=user)
	return render(request,"viewdata.html",{'datakey':data})

def pricing(request):
	user= request.session['adminid']
	details= register_form.objects.all()
	prd= productup.objects.all()
	return render(request,"admin/pricing.html",{'datakey':details,"product":prd})

def adminlogin(request):
	if request.method == "POST":
		email=request.POST['email']
		password=request.POST['pswd']
		data= User.objects.filter(email=email,password=password)
		if data:
			for x in data:
				request.session['adminid']=x.id
			return render(request,"admin/adminindex.html",)
		else:
			return render(request,"admin/adminlogin.html",{'error': 'Invalid Credentionals'})
	else:
		return render(request,"admin/adminlogin.html")

def adlogout(request):
	if request.session.has_key('adminid'):
		del request.session['adminid']
	return render(request,"adminlogin.html")

def addproduct(request):
	if request.method=='POST':		
		catagory=request.POST['catagory']
		model_name=request.POST['model_name']
		price=request.POST['price']
		fake_price=request.POST['fake_price']
		specs1=request.POST['specs1']
		specs2=request.POST['specs2']
		specs3=request.POST['specs3']
		specs4=request.POST['specs4']
		specs5=request.POST['specs5']
		img=request.FILES['img']
		add=productup(catagory=catagory,model_name=model_name,price=price,fake_price=fake_price,img=img,specs1=specs1,specs2=specs2,specs3=specs3,specs4=specs4,specs5=specs5)
		add.save()
		return render(request,"admin/addproduct.html",)
	else:
		return render(request,"admin/addproduct.html")

def productupdate(request):
	if request.method=='POST':
		user=request.GET['adminid']
		catagory=request.POST['catagory']	
		model_name=request.POST['model_name']
		price=request.POST['price']
		fake_price=request.POST['fake_price']
		specs1=request.POST['specs1']
		specs2=request.POST['specs2']
		specs3=request.POST['specs3']
		specs4=request.POST['specs4']
		specs5=request.POST['specs5']
		img=request.POST['img']
		if img=='yes':
			image1=request.FILES['imgfile']
			oldrec=productup.objects.filter(id=user)
			updrec=productup.objects.get(id=user)
			for x in oldrec:
				imgurl=x.img.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.img=image1
			updrec.save()
		updatedata=productup.objects.filter(id=user).update(catagory=catagory,model_name=model_name,price=price,fake_price=fake_price,specs1=specs1,specs2=specs2,specs3=specs3,specs4=specs4,specs5=specs5)
		return HttpResponseRedirect('/pricing/')
	else:
		user=request.GET['adminid']
		data= productup.objects.filter(id=user)
		return render(request,"admin/productupdate.html",{"prd":data})

# def details(request):
# 	user=register_form.objects.all()
# 	return render(request,"admin/details.html",{"user":user})

# def view(request):
# 	print("hello")
# 	a=request.GET.get('p')
# 	b=register_form.objects.filter(id=a)
# 	for x in b:
# 		v=x.name
# 		w=x.email
		
# 	dat={"aa":v,"bb":w}
# 	print(dat)
# 	return JsonResponse(dat)	                      


	                   # cart

def addcart(request):
	if request.session.has_key('user_id'):
		if request.method=='POST':               
			prdid=request.POST['pid']
			prdpr=productup.objects.filter(id=prdid)
			for x in prdpr:
				price=x.price
			prd=productup.objects.get(id=prdid)
			uid=request.session['user_id']
			userid=register_form.objects.get(id=uid)
			data=cart_tb.objects.filter(uid=uid)
			check=cart_tb.objects.filter(pid=prd,uid=userid,status="pending")
			if check:
				return render(request,"cart.html",{"error":"already added in cart","datakey":data})
			else:
				add=cart_tb(pid=prd,uid=userid,status="pending",totalprice=price)
				add.save()
				return HttpResponseRedirect('/cart/')
		else:
			pid=request.GET['pid']
			products=productup.objects.filter(id=pid)
			return render(request,"single.html",{'prd':products})		
	else:
		return HttpResponseRedirect('/login/')

def cart(request):
	if request.session.has_key('user_id'):
		uid=request.session['user_id']
		data=cart_tb.objects.filter(uid=uid,status='pending')
		return render(request,"cart.html",{"datakey":data})
	else:
		return HttpResponseRedirect('/login/')

def deleteitem(request):
	pid=request.GET['pid']
	data= cart_tb.objects.filter(id=pid).delete()
	return HttpResponseRedirect('/cart/')

def checkout(request):
	if request.session.has_key('user_id'):			
		if request.method == "POST":
			fullname=request.POST['fullname']
			number=request.POST['number']
			landmark=request.POST['landmark']
			city=request.POST['city']
			TOTAL=request.GET['total']
			print(TOTAL,"---------------------")
			uid=request.session['user_id']
			uid=register_form.objects.get(id=uid)
			add=shipping(fullname=fullname,number=number,landmark=landmark,city=city,uid=uid)
			add.save()
			return render(request,"payment.html",{"total":TOTAL})
		else:
			uid=request.session['user_id']
			data=cart_tb.objects.filter(uid=uid,status="pending")
			total=0
			for x in data:
				totalprice=x.totalprice
				total=total+float(totalprice)
			return render(request,"checkout.html",{"datakey":data,"total":total})
	else:
		return HttpResponseRedirect('/login/')

def cartupdate(request):
	# if request.method =="POST":
	cid=request.GET['cid']
	print(cid,"*******************")
	quantity=request.POST['quantity']
	print(quantity)
	data=cart_tb.objects.filter(id=cid)
	for x in data:
		itemprice=(int(x.pid.price))
		totalprice=(int(quantity)*itemprice)
	chk=cart_tb.objects.filter(id=cid).update(quantity=quantity,totalprice=totalprice)
	return HttpResponseRedirect('/checkout/')

def payindex(request):
	if request.session.has_key('user_id'):
		if request.method=='POST':
			total=request.POST['total']
			uid=request.session['user_id']
			uidd=register_form.objects.get(id=uid)
			pdate=datetime.datetime.now()
			pay=payment_tb(totalamount=total,uid=uidd,date=pdate,status="paid")
			pay.save()
			chk=cart_tb.objects.filter(uid=uid,status="pending").update(status="paid")
			return HttpResponseRedirect("/")

		else:
			total=request.GET['total']
			return render(request,"payment/payindex.html",{"total":total})
	else:
		return HttpResponseRedirect('/login/')