from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from .models import Genre, Track

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='genre_list'
    def get_queryset(self):
        return Genre.objects.all()

class GenreDetail(SingleObjectMixin, generic.ListView):
    paginate_by = 10
    template_name = "music/genre_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Genre.objects.all())
        return super(GenreDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GenreDetail, self).get_context_data(**kwargs)
        context['genre']=self.object
        return context

    def get_queryset(self):
        return self.object.track_set.all()
