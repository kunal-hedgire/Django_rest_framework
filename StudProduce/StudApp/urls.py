from django.contrib import admin
from django.urls import path
#from . import views
from django.conf.urls import url
from . import views
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='API name')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create/',views.PostCreate.as_view()),
    path('delete/<int:pk>/', views.PostDelete.as_view()),
    path('update/<int:pk>/',views.PostUpdate.as_view()),
    # url(r'^docs/$', schema_view, name="schema_view")  # swagger -- rest api
]
