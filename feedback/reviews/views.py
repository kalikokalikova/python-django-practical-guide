from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from reviews.models import Review
from .forms import ReviewForm

# Create your views here.

def review(request):
  if request.method == "POST":
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/thank-you")
  else: # GET request
    form = ReviewForm()

  return render(request, "reviews/review.html", {
    "form": form
  })


class ThankYouView(TemplateView): # special django template just for rendering simple views. Does not need a get or render. Just serves the template.
  template_name = "reviews/thank_you.html"

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['message'] ="This works!"
      return context

class ReviewsListView(TemplateView):
  template_name = "reviews/review_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    reviews = Review.objects.all()
    context["reviews"] = reviews
    return context

class ReviewDetail(TemplateView):
  template_name = "reviews/review_detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    review = Review.objects.get(id=kwargs['id'])
    context["review"] = review
    return context


