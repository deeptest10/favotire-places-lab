from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import Http404
from .forms import PlaceForm
from datetime import date
import random


def home(request):
    places = request.session.get("places", [])

    selected_place = None
    selection_requested = request.GET.get("pick") == "1"

    if selection_requested and places:
        weights = []

        for place in places:
            weights.append(place["rating"])

        selected_place = random.choices(places, weights=weights, k=1)[0]

    context = {
        "site_name": "Куди піти?",
        "description": "Мій список улюблених місць.",
        "selected_place": selected_place,
        "selection_requested": selection_requested,
    }

    return render(request, "places/home.html", context)


def place_list(request):
    places = request.session.get("places", [])

    context = {
        "places": places,
    }

    return render(request, "places/place_list.html", context)


def place_detail(request, place_id):
    places = request.session.get("places", [])

    for place in places:
        if place["id"] == place_id:
            context = {
                "place": place,
            }

            return render(
                request,
                "places/place_detail.html",
                context,
            )

    raise Http404("Місце не знайдено")


def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)

        if form.is_valid():
            places = request.session.get("places", [])

            next_id = request.session.get("next_place_id", 1)

            new_place = form.cleaned_data.copy()
            new_place["id"] = next_id
            new_place["created_at"] = date.today().isoformat()

            places.append(new_place)

            request.session["places"] = places
            request.session["next_place_id"] = next_id + 1

            return redirect("places:list")
    else:
        form = PlaceForm()

    context = {
        "form": form,
    }

    return render(request, "places/place_form.html", context)