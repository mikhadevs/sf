
from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):

    help = 'Deletes news in the selectred category'

    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории '
                       f'{options["category"]}? y/n ')
        if answer != 'y':
            self.stdout.write(self.style.ERROR('Cancelled'))
            return
        try:
            category = Category.objects.get(category_name=options['category'])
            Post.objects.filter(post_category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Удалено {category.category_name}'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Категория не найдена {category}'))
