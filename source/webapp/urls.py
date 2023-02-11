from django.urls import path
from webapp.views.ads_views import IndexViews, AdDeleteView, AdUpdateView, AdView, AdCreateView, AdList, AdYes, Adn
from webapp.views.coments_views import AdCommentCreateView, CommentDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('ad/<int:pk>/', AdView.as_view(), name='ad_view'),
    path('ad/add/', AdCreateView.as_view(), name='ad_add'),
    path('ad/<int:pk>/update', AdUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete', AdDeleteView.as_view(), name='ad_delete'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),
    path('ad/<int:pk>/comment/add/', AdCommentCreateView.as_view(), name='ad_comment_add'),
    path('no_moderated/', AdList.as_view(), name="no_moderated"),
    path('no_moderated/', AdYes.as_view(), name="yes"),
    path('no_moderated/', Adn.as_view(), name="no")


]