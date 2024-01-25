from django.urls import path
from blog import views
from blog.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by('-log_date')[:5],
    context_object_name='message_list',
    template_name='blog/home.html',
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("software/", views.software, name="software"),
    path("cloud/", views.cloud, name="cloud"),
    path("data/", views.data, name="data"),
    path("it_ops/", views.it_ops, name="it_ops"),
    path("leadership/", views.leadership, name="leadership"),
    path("security/", views.security, name="security"),
    path("log/", views.log_message, name="log"),
   
]