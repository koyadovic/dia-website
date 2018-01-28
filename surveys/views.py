from django.shortcuts import render
from django.conf import settings

from surveys.models import Survey
from surveys.utils.crypto import percent_decoding, hmac_sha1_base64


def survey_view(request):
    survey_id = request.GET.get('id', '')
    signature = request.GET.get('s', '')

    signature = percent_decoding(signature)
    calculated_signature = hmac_sha1_base64('{}'.format(survey_id), key=settings.SECRET_KEY)

    if signature != calculated_signature:
        return render(request, 'surveys/error.html')

    survey = Survey.objects.get(id=int(survey_id))

    if survey.completed:
        return render(request, 'surveys/survey_completed.html')

    if request.method.lower() == 'get':
        context = {
            "title": survey.survey_type.title,
            "fields": survey.survey_type.fields
        }
        return render(request, 'surveys/survey.html', context)
    else: # post
        survey.values = {}
        dict_data = dict(request.POST)
        for k, v in dict_data.items():
            if k not in ['submit', 'csrfmiddlewaretoken'] and v[0] != '':
                if len(v) == 1:
                    survey.values.update({k: v[0]})
                else:
                    survey.values.update({k: v})
        survey.completed = True
        survey.save()
        return render(request, 'surveys/survey_completed.html')
