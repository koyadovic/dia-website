from surveys.models import SurveyType, Survey


def create_survey_url(email, survey_type_slug):
    """
    This function is called by other apps. This generates a unique URL for a survey of type specified with the slug.

    :param email: email for the created survey. Can be used later for filter for a specific survey result.
    :param survey_type_slug: The type previously defined thought the admin interface.
    :return: a link to the survey.
    """
    survey_type = SurveyType.objects.get(slug=survey_type_slug)
    survey = Survey.objects.create(survey_type=survey_type, rcpt=email, values={})
    return survey.external_url
