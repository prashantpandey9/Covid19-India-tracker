from Django import forms
class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email