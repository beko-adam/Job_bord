
from django.forms import ModelForm
from .models import Apply, Job


class Apply_form(ModelForm):

    class Meta:

        model = Apply
        fields = '__all__'
        exclude = ('job_link',)


class jobsss(ModelForm):

    class Meta:

        model = Job
        fields = '__all__'
        exclude = ('slug',)
        