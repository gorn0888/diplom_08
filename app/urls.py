from django.urls import path
from app.views import person_list, person_detail, category_list, division_list,\
     create_person, PersonDeleteView, PersonUpdateView, report, dismissed_person

urlpatterns = [
    path("", person_list, name='person_list_url'),
    path("person/<int:pk>/", person_detail, name='person_detail_url'),
    path("category/<int:pk>/", category_list, name='category_list_url'),
    path("division/<int:pk>/", division_list, name='division_list_url'),
    path("create_person/", create_person, name='create_person_url'),
    path("dismissed_person/", dismissed_person, name='dismissed_person_url'),
    path("person/<int:pk>/edit", PersonUpdateView.as_view(), name='edit_person_url'),
    path("person/<int:pk>/delete", PersonDeleteView.as_view(), name='delete_person_url'),
    path("report/", report, name='report_url'),
]