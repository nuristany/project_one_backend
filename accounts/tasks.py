from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import UserAccount
@shared_task
def send_activation_email(subject, message, recipient_email, email_body):
    try:
        send_mail(
            subject,
            message,
            from_email=None,
            recipient_list=[recipient_email],
            html_message=email_body
        )

        return "Email sent successfully"
    except Exception as e:
        return f"failed to send email: {str(e)}"
