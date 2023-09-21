from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="Your Name", max_length=100, error_messages={"required": "NO EMPTIES!", "max_length": "TOO LONG"})
#   review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#   rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    # fields = '__all__' => render all fields
    # exclude = ['owner_comment'] => don't render this field
    fields = ['user_name', 'review_text', 'rating'] # or just list the fields you want
    labels = {
      "user_name": "Your Name",
      "review_text": "Your Feedback",
      "rating": "Your Rating"
    }
    error_messages = {
      "user_name": {
        "required": "NO EMPTIES!@!",
        "max_length": "TOO LONG!!!"
      }
    }
