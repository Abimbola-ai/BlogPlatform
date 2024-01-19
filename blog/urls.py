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
    path("blog/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]