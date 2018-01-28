from django.contrib.postgres.fields import JSONField
from django.core.urlresolvers import reverse
from django.db import models
from autoslug import AutoSlugField
from django.conf import settings
from surveys.utils.crypto import percent_encoding, hmac_sha1_base64


class SurveyType(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True)
    title = models.CharField(max_length=255, default='', blank=False, null=False)
    fields = JSONField(default=[], blank=False, null=False)

    def __str__(self):
        return self.slug

    def __repr__(self):
        return self.__str__()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        for field in self.fields:
            assert 'key' in field, 'field without key, invalid data.'
            assert 'type' in field, 'field without type, invalid data.'
            assert 'display' in field, 'field without display, invalid data.'

            assert field['type'] in ['text', 'evaluation', 'select', 'multiselect'],\
                'Invalid field type, possible values are "text", "evaluation", "select" and "multiselect"'
            if field['type'] == 'text':
                assert 'options' not in field, 'options only valid for types "evaluation", "select" and "multiselect"'
            else:
                assert 'options' in field, 'options is a must for types "evaluation", "select" and "multiselect"'
                for option in field['options']:
                    assert 'display' in option, 'option without display, invalid data.'
                    assert 'value' in option, 'option without value, invalid data.'

        return super().save(force_insert=force_insert, force_update=force_update, using=using,
             update_fields=update_fields)


class Survey(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    survey_type = models.ForeignKey(SurveyType)
    rcpt = models.CharField(max_length=255, default='', blank=False, null=False)

    completed_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    values = JSONField({}, blank=True, null=False)

    def __str__(self):
        return '{} - {}'.format(self.survey_type, self.rcpt)

    def __repr__(self):
        return self.__str__()

    @property
    def external_url(self):
        if self.id is None:
            return ""
        else:
            from surveys.configuration import ROOT_SERVER_URL

            # With signature there is no chance for an user to access other surveys specifying aleatory IDs.
            signature = percent_encoding(hmac_sha1_base64('{}'.format(self.id), settings.SECRET_KEY))
            relative_url = '{}?id={}&s={}'.format(reverse('surveys:surveys'), self.id, signature)
            survey_url = ROOT_SERVER_URL + relative_url
            return survey_url
