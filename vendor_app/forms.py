from django import forms

from accounts_app.models import (
    User,
    Profile
)
from vendor_app.models import (
    Vendor
)


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = (
            'name',
            'license_image'
        )


