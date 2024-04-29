from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from app.models import *

def insert_topic(request):
    tn=input('enter topic_name : ')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    TO.save()
    return HttpResponse('Topic is created successfully')





# We have got parant table Object by using get_or_create
'''
def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()

    return HttpResponse('Webpage is Created')


'''
def insert_webpage(request):
    tn=input('enter topic_name : ')
    

    #TO=Topic.objects.get(topic_name=tn)
    '''We can use get method to get the Parent Table Object but if parent table object is 
    not available it throws an error'''
    TO=Topic.objects.filter(topic_name=tn)
    if TO:
        n=input('enter name :')
        u=input('enter url :')
        e=input('enter email :')
      
        WO=Webpage.objects.get_or_create(topic_name=TO[0],name=n,url=u,email=e)[0]
        WO.save()
        return HttpResponse('Webpage is Created')
    else:
        return HttpResponse('Given Topic is Not present in My Parent Table')



def insert_access(request):
    name = input('Enter webpage name: ')
    
    # Check if the Webpage exists
    WO = Webpage.objects.filter(name=name)
    
    if WO:
        # If Webpage exists, use the first one found
        wp = WO[0]
        
        date = input('Enter date: ')
        author = input('Enter  author: ')
        
        # Create AccessRecord using get_or_create
        ARO = AccessRecord.objects.get_or_create(name = wp, date=date, author=author)[0]
        ARO.save()
        
        
        return HttpResponse('Access Record is Created')
    
        
    else:
        return HttpResponse('Given webpage is not present in the database')

