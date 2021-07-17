from django.shortcuts import render, redirect
from .forms import CmdForm
from .models import Commande, Products
import sys
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
 
@login_required(login_url='login')
def easyCmd(request):
	user_name = request.user
	products = Products.objects.all()
	get_mdc = Commande.objects.filter(productype='Médicament').filter(username=user_name).order_by('creation_date')
	get_mdc_count =Commande.objects.filter(productype='Médicament').filter(username=user_name).count()
	get_art = Commande.objects.filter(productype='Article').filter(username=user_name).order_by('creation_date')
	get_art_count = Commande.objects.filter(productype='Article').filter(username=user_name).count()
	get_other = Commande.objects.filter(productype='Autres').filter(username=user_name).order_by('creation_date')
	get_other_count = Commande.objects.filter(productype='Autres').filter(username=user_name).count()
	form = CmdForm(request.POST or None)
	get_all = Commande.objects.values_list('product', flat=True)
	get_allc = Commande.objects.all().count()

	if request.method == 'POST':
		if form.is_valid():
			get_prod_name = Commande.objects.filter(username=user_name).values_list('product', flat=True)
			current_product = request.POST['product']
			producs = []
			for prod in get_prod_name:
				producs.append(prod.replace(" ",""))

			cu_prods = current_product.replace(" ","")
			print(current_product,list(get_prod_name), products, cu_prods)
			sys.stdout.flush()
			if cu_prods in producs:
				messages.error(request, current_product.upper() + ' exist deja ')
				form = CmdForm()
			if cu_prods not in producs:
				instance = form.save(commit=False)
				instance.username=user_name
				instance.save()
				get_mdc_count =Commande.objects.filter(productype='Médicament').filter(username=user_name).count()
				get_art_count = Commande.objects.filter(productype='Article').filter(username=user_name).count()
				get_other_count = Commande.objects.filter(productype='Autres').filter(username=user_name).count()
				form = CmdForm()
					
				

	context = {
	'mdcs' : get_mdc,'form' : form, 'arts': get_art,'autres' : get_other, 'countmdc': get_mdc_count,
	'countart' : get_art_count, 'countother' : get_other_count, 'prods': products
	}
	return render(request,'index.html',context)

@login_required(login_url='login')
def manageItems(request):
	user_name = request.user
	if 'cmd' in request.POST:
		checked_items = request.POST.getlist('checks')
		for item in checked_items:
			get_seleted_db = Commande.objects.filter(username=user_name).get(product=item)
			get_seleted_db.completed = True
			get_seleted_db.save()
	if 'arr' in request.POST:
		checked_items = request.POST.getlist('checks')
		for item in checked_items:
			get_seleted_db = Commande.objects.filter(username=user_name).get(product=item)
			get_seleted_db.delete()
	return HttpResponseRedirect('/')




def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else : 
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else : 
				messages.info(request, "Nom d'utilisateur ou Mot de passe est incorrect")


		return render(request,'login.html', {})

def logoutUser(request):
	logout(request)
	return redirect('login')


def addProducts(request):
# 	form = addForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = addForm()

	return render(request, 'add.html', {'form' : form})