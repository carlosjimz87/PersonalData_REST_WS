from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'idtypes', views.IdTypeViewSet)
router.register(r'subjects', views.SubjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^subjectbyidcard/$', views.SubjectByIDCardView.as_view()),
    url(r'^subjectbyregdate/$', views.SubjectByRegistrationDateView.as_view()),
    url(r'^subjectbybirthdate/$', views.SubjectByBirthdateView.as_view()),
    url(r'^subjectbycountry/$', views.SubjectByCountryView.as_view()),
    url(r'^subjectbygender/$', views.SubjectByGenderView.as_view()),
    url(r'^subjectbyphone/$', views.SubjectByPhone.as_view()),
    url(r'^subjectbyemail/$', views.SubjectByEmail.as_view()),
    url(r'^subjectbyidcardtype/$', views.SubjectByIdCardTypeView.as_view()),
    url(r'^subjectbyfullname/$', views.SubjectByFullName.as_view()),
]
