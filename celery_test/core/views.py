from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts
from django.core.mail import send_mail
from django.shortcuts import render

from core.tasks import task_mail

class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')


def task_use_celery(request):
    task_mail.delay()
    return render(request,
                  'core/process_done.html')