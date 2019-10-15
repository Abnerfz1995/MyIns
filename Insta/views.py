from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

#HelloWorld is-a TemplateView

class HelloWorld(TemplateView):
    template_name = "test.html"

'''child class is-a parent class

class animal 

makesound()
    print "making sounds"

class dog : animal 

makesound() ##overwrite
    print "woof woof"

dog.makesound()'''