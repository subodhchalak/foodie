from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView
)
from accounts_app.models import User
from vendor_app.models import (
    Vendor
)
from vendor_app.forms import (
    VendorForm
)
from accounts_app.forms import (
    UserForm
)

# Create your views here.


class RegisterVendorCV(CreateView):
    form_class = VendorForm
    queryset = Vendor.objects.all()
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('vendor_app: register_vendor')
    template_name = 'vendor_app/register_vendor.html'
    vendor_form = VendorForm()
    form = UserForm()
    extra_context = {
        'form': form,
        'vendor_form': vendor_form
    }
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES
        vendor_form = VendorForm(data=data, files=data)
        form = UserForm(data=data)

        print(f"vendor form valid: {vendor_form.is_valid()}")
        print(f"user form valid: {form.is_valid()}")

        if vendor_form.is_valid() and form.is_valid():
            user = form.save(commit=False)
            user.role = 'vendor'
            user.set_password(data['password'])
            user.save()

            # user = User(
            #     first_name = data['first_name'],
            #     last_name = data['last_name'],
            #     phone_number = data['phone_number'],
            #     email = data['email'],
            #     username = data['username'],
            #     role = 'restaurant'
            # )
            # user.set_password(data['password'])
            # user.save()

            vendor = Vendor(
                user = user,
                profile = user.profile,
                license_image = files['license_image'],
                name = data['name']
            )
            vendor.save()

            messages.success(
                request = request,
                message = "Vendor Saved Successfully"
            )

        else:
            messages.error(
                request = request,
                message = "Please enter the data correctly!"
            )

        return render(
            request = request,
            template_name = self.template_name
        )