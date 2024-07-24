from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#This is for Home page
def home(request):
    peoples=[
        {'name':"syeda",'age':29},
        {'name':'banu','age':15},
        {'name':'shruthi','age':26},
        {'name':'pooja','age':18},
        {'name':'heer','age':12},
        {'name':'mahi','age':26},
    ]

    
    # for people in peoples
    #     print(people)    
    # text="""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corrupti, maxime sint iste perferendis minus optio culpa, omnis necessitatibus ducimus adipisci quia! Consectetur facere odit dolor doloremque nihil, placeat deleniti iusto."""
    
    
    vegetables=['cucumber','pumpkin','tomato','potato','carrot']

    return render(request, "index.html", context = {'page':'Django Practice app', 'peoples':peoples,'vegetables':vegetables})


#this is for about page
def about(request):
    context = {'page': 'about'}   #this is to modify the page tittle name
    return  render(request, "about.html",context)


#This is for contact page
def contact(request):
    context = {'page': 'contact'}
    return  render(request, "contact.html", context)
    

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Hey!!!!!!! This is success page </h1> ")

