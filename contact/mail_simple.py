from django.shortcuts import redirect
from django.views.genric import FormView
from demos.forms import FormEmailSend
from django.core.mail import send_mail, EmailMessage

class ViewSendEmail(FormView):
    form_class = FormEmailSend
    template_name = 'email_send.html'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        form_email = form.cleaned_data['from_email']
        to_email = form.cleaned_data['to_email']
        emails = []
        if ',' in to_email:
            for email in to_email.split(','):
                emails.append(email)
        else:
            send_email_message(subject, message, from_email, emails)
        return redirect("demos-email-simple")

def send_email_message(subject, message, from_email, emails):
    email = EmailMessage(subject, message, from_email, to=emails)
    email.send()

def send_mail_example(subject, message, from_email, emails):
    send_mail(subject, message, from_email, emails)
