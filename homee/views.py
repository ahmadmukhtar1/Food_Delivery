from django.shortcuts import render, redirect
from .models import detail
from .forms import createform
# Create your views here.
def Home(request):
	return render(request, 'home.html')

def create(request):
	forms = createform()
	if request.method == 'POST':
		#print('printing POST:', request.POST)
		forms = createform(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('home')

	context = {'forms':forms}
	return render(request, 'form.html', context)

def List(request):
	details = detail.objects.all()
	context = {'details':details}

	return render(request, 'list.html', context)

def Menu(request):
	return render(request, 'menu.html')

def Faq(request):
	return render(request, 'faq.html')

def Contact(request):
	return render(request, 'contact.html')

def Update(request, id):
	order = detail.objects.get(id=id)
	forms = createform(instance=order)

	if request.method == 'POST':
		forms = createform(request.POST, instance=order)
		if forms.is_valid():
			forms.save()
			return redirect('list')

	context = {'forms':forms}
	return render(request, 'form.html', context)