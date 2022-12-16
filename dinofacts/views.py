from datetime import datetime
from django.shortcuts import render

def show_dino(request, name):
    data = {
        "dinosaurs": [
            "Tyrannosaurus",
            "Stegosaurus",
            "Raptor",
            "Triceratops",
        ],
        "now": datetime.now(),
    }

    return render(request, name + ".html", data)
