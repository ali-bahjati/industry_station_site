from django.views.generic import DetailView

from WSS.mixins import FooterMixin
from events.models import Seminar, Workshop
from people.models import Speaker
from WSS.models import WSS


class SeminarView(FooterMixin, DetailView):
    template_name = 'events/seminar.html'
    context_object_name = 'seminar'
    model = Seminar

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['wss'] = self.object.wss
        return context


class SpeakerView(FooterMixin, DetailView):
    template_name = 'events/speaker.html'
    context_object_name = 'speaker'
    model = Speaker

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        # FIXME: Doesn't work for multiple years, add wss to speaker
        context['wss'] = WSS.objects.order_by('-id').first
        return context


class WorkshopView(FooterMixin, DetailView):
    template_name = 'events/workshop.html'
    context_object_name = 'workshop'
    model = Workshop

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['wss'] = self.object.wss
        return context
