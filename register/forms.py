from django import forms

class ScanForm(forms.Form):
    upc = forms.CharField(max_length=14, label="Scan/Enter UPC")
