from django.urls import path
from . import views

urlpatterns = [
  path("", views.review),
  path("thank-you", views.ThankYouView.as_view()),
  path("reviews", views.ReviewsListView.as_view()),
  path("reviews/<int:id>", views.ReviewDetail.as_view())
]
