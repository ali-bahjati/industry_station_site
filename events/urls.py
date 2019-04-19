from django.conf.urls import url

from events.views import SeminarView, WorkshopView, SpeakerView

urlpatterns = [
    url(r'seminar/(?P<pk>\d+)/$', SeminarView.as_view(), name='seminar'),
    url(r'company/(?P<pk>\d+)/$', SpeakerView.as_view(), name='speaker'),
    url(r'workshop/(?P<pk>\d+)/$', WorkshopView.as_view(), name='workshop'),
]
