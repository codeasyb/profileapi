from rest_framework import generics, viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from userapi.models import Profile, ProfileStatus
from userapi.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly
from userapi.api.serializers import ProfileAvatarSerializer, ProfileSerializer, ProfileStatusSerializer

class AvatarUpdateView(generics.UpdateAPIView):
    
    serializer_class = ProfileAvatarSerializer
    permissions_class = [IsAuthenticated]
    
    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object
    

class ProfileViewSet(mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly ] 
    filter_backends = [SearchFilter]
    search_fields = ["city"]

class ProfileStatusViewSet(ModelViewSet):
    """
        Model viewset
        This will read, update, and delete single profile status instances
        Search context - [?search=value]
    """
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    """
        Filtering system, Getting pacific status instances 
        Get the pacific query from the database else get the whole queryset instance
        by using paramters [?username=username]
    """
    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(user_profile_user_username=username)
        return queryset
    
    """
        Overwriting create method for: 
        considering we want to automatically connect new profile statuses isntances to the 
        profile of the user that us making the request we are overriding the perform create method 
        below
    """
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)