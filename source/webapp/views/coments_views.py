from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Comment, Ads


class AdCommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment/create.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('webapp:ad_view', kwargs={'pk': self.object.ad.pk})

    def form_valid(self, form):
        ad = get_object_or_404(Ads, pk=self.kwargs.get('pk'))
        form.instance.ad = ad
        form.instance.author = self.request.user
        return super().form_valid(form)



class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.request.user.has_perm('webapp.delete_comment') or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:ad_view', kwargs={'pk': self.object.ad.pk})