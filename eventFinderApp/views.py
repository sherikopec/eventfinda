from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Event, Category
from .forms import EventForm
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class AccountView(generic.ListView):
    template_name = 'eventFinderApp/account.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.filter(host = self.request.user)

    
class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

@login_required(login_url = 'login')
def addevent(request):
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = EventForm(request.POST)
        # check whether it is valid
        if form.is_valid():
            #process the data in form.cleaned_data as required
            #get the new event from the form but don't save it yet
            new_event = form.save(commit=False)
            # add the host
            new_event.host = request.user
            form.save()
            return HttpResponseRedirect(reverse('eventFinderApp:index'))
        return render(request, 'eventFinderApp/addevent.html', {'eventform': form})
    # if it is a GET request (or any other method) we'll create a blank form
    else:
        eventform = EventForm()
        return render(request, 'eventFinderApp/addevent.html', {'eventform': eventform})

def account(request):
    return render(request, 'eventFinderApp/account.html')


class EditEventView(generic.UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('eventFinderApp:account')
    template_name = 'eventFinderApp/editevent.html'

@login_required(login_url = 'login')
def editevent(request):
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = EventForm(request.POST)
        # check whether it is valid
        if form.is_valid():
            #process the data in form.cleaned_data as required
            #get the new event from the form but don't save it yet
            edited_event = form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('eventFinderApp:account'))
        return render(request, 'eventFinderApp/addevent.html', {'eventform': form})
    # if it is a GET request (or any other method) we'll create a blank form
    else:
        eventform = EventForm()
        return render(request, 'eventFinderApp/addevent.html', {'eventform': eventform})



