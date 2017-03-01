from django.conf.urls import url

from lxd_launcher.views import ContainerView


urlpatterns = [
    url(r'^api/containers$', ContainerView.as_view()),
]
