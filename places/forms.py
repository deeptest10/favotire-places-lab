from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(
        label="Назва місця:",
        max_length=100,
    )

    description = forms.CharField(
        label="Опис місця:",
        widget=forms.Textarea,
    )

    place_type = forms.CharField(
        label="Тип місця:",
        max_length=50,
    )

    location = forms.CharField(
        label="Локація:",
        max_length=200,
        required=False,
    )

    rating = forms.IntegerField(
        label="Рейтинг",
        min_value=1,
        max_value=5,
    )