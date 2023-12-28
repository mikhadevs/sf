from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import PostCategory
from django.contrib.auth.models import User
from config.settings import DEFAULT_FROM_EMAIL
from allauth.account.signals import user_signed_up


def send_notification(preview, pk, header, subscribers):
    html_content = render_to_string(
        'news_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=header,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(m2m_changed, sender=PostCategory)
def new_post_notifier(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.post_category.all()
        subscribers = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]
        send_notification(instance.preview(), instance.pk, instance.header, subscribers)



@receiver(post_save, sender=User)
def welcome_email(created, **kwargs):
    instance = kwargs['instance']
    if created:
        html_content = render_to_string(
            'account/email/email_confirmation_signup.html',
            {
                'text': f'{instance.username}, Регистрация выполнена!',
            }
        )
        msg = EmailMultiAlternatives(
            subject='Добро пожаловать!',
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=[instance.email]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
