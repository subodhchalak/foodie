from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import (
    FormView
)


from accounts_app.forms import (
    UserForm
)


# Create your views here.


class RegisterUserFV(FormView):
    form_class = UserForm
    template_name = 'accounts_app/register_user.html'
    http_method_names  = ['post', 'get']
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = UserForm(data=data)
        context = {
            'form': form
        }
 
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'customer'
            user.save()
            messages.success(request, "User registered successfuly!")
            return redirect('home')
        else:
            message = \
                "Something went wrong! Please enter the correct information."
            messages.error(request, message)
            return render(request, self.template_name, context)