from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from .models import Genre, Track
from graphos.sources.model import ModelDataSource
from graphos.renderers.gchart import BarChart

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name='genre_list'
    def get_queryset(self):
        return Genre.objects.all()

class GenreDetail(SingleObjectMixin, generic.ListView):
    #paginate_by = 10
    template_name = "music/genre_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Genre.objects.all())
        return super(GenreDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GenreDetail, self).get_context_data(**kwargs)
        context['genre']=self.object

        #data = Track.objects.filter(genreid=self.object.genreid)

        data = Track.objects.raw("select Track.TrackId, Artist.Name as Artist, round(avg(Track.Milliseconds)/60000,2) as Avg_Miliseconds from Track, Album, Artist where Track.AlbumId = Album.AlbumId and Artist.ArtistId = Album.ArtistId and Track.GenreId = "+str(self.object.genreid)+" group by Artist.ArtistId;")

        options = {
            'animation':{
                'duration': 1500,
                'startup': 'true'
            },
            'legend':{
                'position':'none'
            },
            'title':"Average Duration by Artist"
        }

        data_source = ModelDataSource(data, fields=['Artist', 'Avg_Miliseconds'])
        chart = BarChart(data_source, options=options, height=500, width="100%")
        context['chart'] = chart

        return context

    def get_queryset(self):
        return self.object.track_set.all().order_by()
