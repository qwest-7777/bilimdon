from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('question.urls')),
    path('referrals/', include('pinax.referrals.urls', namespace='pinax_referrals')),
    path('payments/', include('payments.urls')),
    path('payments/', include('click.urls')),
]
