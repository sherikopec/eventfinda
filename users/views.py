from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

class UserView(generic.DetailView):
    model = User
    template_name = 'users/login.html'



# user view
# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'password')

# def Users(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         return HttpResponseRedirect(reverse('eventFinderApp:index'))
#     else:
#         # Return an 'invalid login' error message.
#         return HttpResponseRedirect(reverse('eventFinderApp: addevent'))