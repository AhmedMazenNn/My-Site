from django import forms
from . models import Comments


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["post"]
        labels = {
            "user_name": "Your Name: ",
            "user_email": "Your Email",
            "text": "Your Comment"
        }

        def user_name(self):
            return str(self.user_name).capitalize()
