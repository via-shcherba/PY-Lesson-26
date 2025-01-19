from rest_framework import viewsets
from .models import Tag, Profession
from .serializers import TagSerializer, ProfessionSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .permissions import ReadOnly

class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer