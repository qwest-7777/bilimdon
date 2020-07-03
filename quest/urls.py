from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns 

urlpatterns = [ 
    path('i18n/', include('django.conf.urls.i18n')),
] 

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('question.urls')),
    path('referrals/', include('pinax.referrals.urls', namespace='pinax_referrals')),
    path('payments/', include('payments.urls')),
    path('payments/', include('click.urls')),
)
