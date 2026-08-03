import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .data import CARS, DEALERS, REVIEWS


def _dealer(dealer_id):
    return next((dealer for dealer in DEALERS if dealer["id"] == dealer_id), None)


def _sentiment(text):
    positive = {"fantastic", "great", "friendly", "helpful", "quick", "excellent", "clear"}
    negative = {"bad", "slow", "poor", "rude", "terrible"}
    words = {word.strip(".,!?").lower() for word in text.split()}
    if words & negative:
        return "negative"
    if words & positive:
        return "positive"
    return "neutral"


def home(request):
    return render(request, "home.html", {"dealers": DEALERS})


def login_page(request):
    username = request.GET.get("username", "root")
    user, _ = User.objects.get_or_create(username=username, defaults={"email": "root@example.com"})
    user.set_password("root")
    user.save()
    login(request, user)
    return redirect("home")


def logout_page(request):
    logout(request)
    return render(request, "logged_out.html")


def dealer_detail(request, dealer_id):
    dealer = _dealer(dealer_id)
    reviews = [review for review in REVIEWS if review["dealership"] == dealer_id]
    return render(request, "dealer_detail.html", {"dealer": dealer, "reviews": reviews})


def dealers_by_state_page(request, state):
    matches = [dealer for dealer in DEALERS if dealer["state"].lower() == state.lower()]
    return render(request, "home.html", {"dealers": matches, "state_filter": state})


def post_review(request, dealer_id):
    dealer = _dealer(dealer_id)
    if request.method == "POST":
        review_text = request.POST.get("review", "")
        REVIEWS.append(
            {
                "id": 1000 + len(REVIEWS),
                "dealership": dealer_id,
                "name": request.POST.get("name", request.user.username or "Guest"),
                "purchase": request.POST.get("purchase") == "on",
                "review": review_text,
                "sentiment": _sentiment(review_text),
                "car_make": request.POST.get("car_make", "Toyota"),
                "car_model": request.POST.get("car_model", "Camry"),
                "car_year": int(request.POST.get("car_year", "2024")),
            }
        )
        return redirect("dealer_detail", dealer_id=dealer_id)
    return render(request, "post_review.html", {"dealer": dealer, "cars": CARS})


@csrf_exempt
def api_login(request):
    payload = request.POST or json.loads(request.body or "{}")
    username = payload.get("userName", payload.get("username", "root"))
    password = payload.get("password", "root")
    user, _ = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.save()
    auth_user = authenticate(request, username=username, password=password)
    login(request, auth_user)
    return JsonResponse({"userName": username, "status": "Authenticated"})


def api_logout(request):
    username = request.user.username if request.user.is_authenticated else "anonymous"
    logout(request)
    return JsonResponse({"userName": username, "status": "Logged out"})


def get_dealers(request):
    return JsonResponse({"status": 200, "dealers": DEALERS})


def get_dealers_by_state(request, state):
    matches = [dealer for dealer in DEALERS if dealer["state"].lower() == state.lower()]
    return JsonResponse({"status": 200, "state": state, "dealers": matches})


def get_dealer_by_id(request, dealer_id):
    return JsonResponse({"status": 200, "dealer": _dealer(dealer_id)})


def get_dealer_reviews(request, dealer_id):
    reviews = [review for review in REVIEWS if review["dealership"] == dealer_id]
    return JsonResponse({"status": 200, "dealer_id": dealer_id, "reviews": reviews})


def get_cars(request):
    return JsonResponse({"status": 200, "cars": CARS})


@csrf_exempt
def analyze_review(request):
    payload = request.POST or json.loads(request.body or "{}")
    text = payload.get("review", payload.get("text", ""))
    return JsonResponse({"status": 200, "review": text, "sentiment": _sentiment(text)})
