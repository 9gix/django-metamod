from django.views.generic import ListView
from django.shortcuts import render
from boutique.models import Cloth

class ApprovedClothesView(ListView):
    def get_queryset(self):
        return Cloth.objects.approved()

class AllClothesView(ListView):
    def get_queryset(self):
        return Cloth.objects.all()

class RejectedClothesView(ListView):
    def get_queryset(self):
        return Cloth.objects.rejected()

class ProcessedClothesView(ListView):
    def get_queryset(self):
        return Cloth.objects.pending()

# All clothes
all_clothes = AllClothesView.as_view()

# Approved Clothes
approved_clothes = ApprovedClothesView.as_view()

# Rejected Clothes
rejected_clothes = RejectedClothesView.as_view()

# Waiting for Moderation
pending_clothes = PendingClothesView.as_view()

