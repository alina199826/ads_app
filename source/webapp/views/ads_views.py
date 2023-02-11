from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from webapp.models import Ads, Comment
from webapp.forms import AdForm, SimpleSearchForm


class IndexViews(ListView):
    template_name = 'ads/index.html'
    context_object_name = 'ads'
    model = Ads
    ordering = ('-created_at')
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = Ads.objects.filter(status='published')
        if self.search_value:
            queryset = queryset.filter(Q(text__icontains=self.search_value) | Q(description__icontains=self.search_value)).filter(status='published')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class AdView(DetailView):
    template_name = 'ads/ad_detail.html'
    model = Ads

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        comments = article.comments.order_by('-created_at')
        context['comments'] = comments
        return context




class AdCreateView(LoginRequiredMixin, CreateView):
    template_name = 'ads/ad_create.html'
    model = Ads
    form_class = AdForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "ads/ad_update.html"
    form_class = AdForm
    model = Ads
    context_object_name = 'ad'
    permission_required = 'webapp.change_ad'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user



class AdDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'ads/ad_confirm_delete.html'
    model = Ads
    success_url = reverse_lazy('webapp:index')

    def has_permission(self):
        return self.get_object().user == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = 'to_delete'
        self.object.save()
        return redirect('webapp:index')

# class LikeView(PermissionRequiredMixin View):
#     def post(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         if request.user in article.likes.all():
#             response = JsonResponse({'error': 'Лайк уже поставлен'})
#             response.status_code = 403
#         else:
#             article.likes.add(request.user)
#             response = JsonResponse({"count": article.get_likes_count()})
#
#         return response
#
# class AnLikeView(LoginRequiredMixin, View):
#     def delete(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         if request.user in article.likes.all():
#             article.likes.remove(request.user)
#             response = JsonResponse({"count": article.get_likes_count()})
#         else:
#             response = JsonResponse({'error': 'Лайк не был поставлен'})
#             response.status_code = 403
#
#         return