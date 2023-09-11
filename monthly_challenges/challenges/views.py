from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenge_dict = {
    'january': 'do some january shit',
    'february': 'eat some candy',
    'march': 'come in like a lion',
    'april': 'be a flower',
    'may': 'be in love',
    'june': 'wish for summer',
    'july': 'go outside',
    'august': None
}


def index(request):
    month_dicts = {}
    month_names = list(challenge_dict.keys())
    for month in month_names:
        month_path = reverse("month-challenge", args=[month])
        month_dicts[month] = month_path
    print(month_dicts)
    return render(request, 'challenges/index.html', {
        "months": month_names
    })


def monthly_challenge_by_int(request, month):
    months = list(challenge_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = challenge_dict[month]
        return render(request, 'challenges/challenge.html', {
            "month": month,
            "goal": challenge_text
        })
    except:
        raise Http404()
