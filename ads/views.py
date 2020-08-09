from .models import Ad
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView



class AdListView(OwnerListView):
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text']

class AdDeleteView(OwnerDeleteView):
    model = Ad