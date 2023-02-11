# from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from webapp.models import Ads, Comment
from webapp.forms import AdForm






class IndexViews( ListView):
    template_name = 'ads/index.html'
    context_object_name = 'ads'
    model = Ads
    ordering = ('-created_at')


class AdView(DetailView):
    template_name = 'ads/ad_detail.html'
    model = Ads



class AdCreateView( CreateView):
    template_name = 'ads/ad_create.html'
    model = Ads
    form_class = AdForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class AdUpdateView(UpdateView):
    template_name = "ads/ad_update.html"
    form_class = AdForm
    model = Ads
    context_object_name = 'ad'
    permission_required = 'webapp.change_ad'

    # def has_permission(self):
    #     return super().has_permission() or self.get_object().author == self.request.user


class AdDeleteView(DeleteView):
    model = Ads
    template_name = "ads/ad_confirm_delete.html"
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_ad'

    # def has_permission(self):
    #     return super().has_permission() or self.get_object().author == self.request.user