from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View

from .models import Thread

#class ForumView(TemplateView):

#    template_name = 'index.html'

#index = ForumView.as_view()

class ForumView(ListView):

    model = Thread
    paginate_by = 10
    template_name = 'forumIndex.html'

    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context


index = ForumView.as_view()