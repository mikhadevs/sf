from celery import shared_task
from .models import Category, Post
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from config.settings import DEFAULT_FROM_EMAIL
from django.utils import timezone
import datetime


@shared_task
def created_news_notify(pk):
    post = Post.objects.get(pk=pk)
    categories = post.post_category.all()
    header = post.header
    subscribers_emails = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for sub_user in subscribers_users:
            subscribers_emails.append(sub_user.email)
    html_content = render_to_string(
        'news_created_email.html',
        {
            'text': post.models.News.description,
            'link': f'{settings.SITE_URL}/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=header,
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_mailing():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_created__gte=last_week)
    categories = set(posts.values_list('post_category__category_name', flat=True))
    subscribers = set(
        Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Articles from last week',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

