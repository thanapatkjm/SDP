from django.urls import path
from . import views
app_name='animal'
urlpatterns = [
    # path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('index/create/', views.created, name='created'),
    path('index/creating/', views.creating, name='creating'),
    path('<int:page_number>/detail/editing', views.remov, name='remov'),
    path('<int:page_number>/detail/editing', views.editing, name='editing'),
    path('<int:page_number>/detail/edit', views.edit_descript, name='edit'),
    path('<int:page_number>/detail/',views.detail, name='detail'),
    path('<int:page_number>/page/', views.page, name='page'),
    path('test/', views.test, name='test'),
]
    # {% for name in latest_animal_name %}
    #     <li><a href="/animalSite/{{ Animal.id }}/">{{ name.animal_name }}</a></li>
    # {% endfor %}
