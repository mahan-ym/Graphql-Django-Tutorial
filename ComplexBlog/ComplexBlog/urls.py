from django.contrib import admin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/',csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
