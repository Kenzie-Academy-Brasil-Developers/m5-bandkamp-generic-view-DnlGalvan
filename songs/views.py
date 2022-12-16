from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from albums.models import Album
from django.shortcuts import get_object_or_404
from .serializers import SongSerializer


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        album_id = self.kwargs["pk"]
        album_obj = get_object_or_404(Album, pk=album_id)
        return serializer.save(album=album_obj)
