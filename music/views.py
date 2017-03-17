from django.views import generic
from .models import Genre

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='genre_list'
    def get_queryset(self):
        return Genre.objects.all()

class GenreDetail(generic.DetailView):
    model = Genre
    def get_context_data(self, **kwargs):
        context = super(GenreDetail, self).get_context_data(**kwargs)
        return context
