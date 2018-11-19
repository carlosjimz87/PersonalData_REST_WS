from rest_framework import generics
from .serializers import *
from rest_framework import viewsets


class SubjectByGenderView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        gender = self.request.query_params.get('gender', None)
        if gender is not None:
            return queryset.filter(Gender=gender).distinct()
        return Subject.objects.none()


class SubjectByPhone(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        phone = self.request.query_params.get('phone', None)
        if phone is not None:
            return queryset.filter(Phone__istartswith=phone).distinct()
        return Subject.objects.none()


class SubjectByEmail(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            return queryset.filter(Email__contains=email).distinct()
        return Subject.objects.none()


class SubjectByIdCardTypeView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        idcardtype = self.request.query_params.get('idcardtype', None)
        if idcardtype is not None:
            return queryset.filter(IdCardType=idcardtype).distinct()
        return Subject.objects.none()


class SubjectByCountryView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        country = self.request.query_params.get('country', None)
        if country is not None:
            return queryset.filter(Country=country).distinct()
        return Subject.objects.none()


class SubjectByFullName(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        name = self.request.query_params.get('name', None)
        surname = self.request.query_params.get('surname', None)
        secondsurname = self.request.query_params.get('secondsurname', None)

        if name is not None:
            return queryset.filter(Name__contains=name)
        if surname is not None:
            return queryset.filter(Surname__contains=surname)
        if name is not None and surname is not None:
            return queryset.filter(Surname__contains=surname).filter(Name__contains=name)
        if secondsurname is not None and name is not None and surname is not None:
            return queryset.filter(Name__contains=name).filter(Surname__contains=surname).filter(SecondSurname__contains=secondsurname)
        return Subject.objects.none()


class SubjectByBirthdateView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if end_date is None:
            end_date = datetime.date.today()
        if start_date is not None:
            return queryset.filter(BirthDate__range=(start_date, end_date)).distinct()
        return Subject.objects.none()


class SubjectByRegistrationDateView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if end_date is None:
            end_date = datetime.date.today()
        if start_date is not None:
            return queryset.filter(RegistrationDate__range=(start_date, end_date)).distinct()
        return Subject.objects.none()


class SubjectByIDCardView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        idcard = self.request.query_params.get('idcard', None)
        if idcard is not None:
            return queryset.filter(IdCard=idcard).distinct()
        return Subject.objects.none()


class SubjectViewSet(viewsets.ModelViewSet):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class IdTypeViewSet(viewsets.ModelViewSet):

    queryset = IdType.objects.all()
    serializer_class = IdTypeSerializer
