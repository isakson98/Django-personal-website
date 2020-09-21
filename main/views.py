from django.shortcuts import render, redirect
from .models import Project, Introduction, Education, Skill, Language, Tools, Connect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


# Create your views here.
# function called homepage because that how we called the path in urls.py
def homepage(request):

    # ordering abilities from greatest to least
    skill_ordered = Skill.objects.order_by("-skill_rating")
    language_ordered = Language.objects.order_by("-language_rating")
    tool_ordered = Tools.objects.order_by("-tool_rating")

    form = ContactForm()
    # contact me form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                messages.info(request, message="Message sent!")
                send_mail(subject, message, from_email, ['isakson98@gmail.com'],  fail_silently=False)
                print("Great success")
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # need to include the name of the app + colon before the name of the view 
            return redirect("main:homepage")


    return render(request = request,
                  template_name = "main/home.html",
                  context = {"intro" : Introduction.objects.all,
                             "projects" : Project.objects.all,
                             "education" : Education.objects.all,
                             "skill" : skill_ordered,
                             "language" : language_ordered,
                             "tool" : tool_ordered,
                             "form" : form,
                             "connect" : Connect.objects.all})
    