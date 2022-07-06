import openpyxl
from django.db import IntegrityError, transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from umkd_api.forms import UploadFileForm
from umkd_api.models import Competence, Indicator
from umkd_api.serializer import DesktopCompetenceSerializer


class ListOfCompetences(APIView):
    def get(self, request):
        competences = Competence.objects.all()
        serializer = DesktopCompetenceSerializer(instance=competences, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['competences']
        wb = openpyxl.load_workbook(file)
        worksheet = wb["Sheet1"]
        for row in worksheet.iter_rows():
            this_row_competence = None
            for i in range(0, len(row), 2):
                if i == 0:
                    if row[i].value:
                        competence_code = row[i].value
                        competence_description = row[i + 1].value
                        try:
                            with transaction.atomic():
                                this_row_competence = Competence.objects.create(code=competence_code, description=competence_description)
                        except IntegrityError:
                            pass
                else:
                    if row[i].value:
                        indicator_code = row[i].value
                        indicator_description = row[i + 1].value.split(":")
                        indicator_type = indicator_description[0]+":"
                        indicator_description = indicator_description[1][1:]
                        try:
                            with transaction.atomic():
                                Indicator.objects.create(code=indicator_code,
                                                         description=indicator_description,
                                                         type=indicator_type,
                                                         competence=this_row_competence)
                        except IntegrityError:
                            pass
        if form.is_valid():
            return UploadFileForm('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
