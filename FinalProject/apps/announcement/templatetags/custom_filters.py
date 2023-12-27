from django import template


register = template.Library()

cens = ['Какашка', 'Редиска', 'Апож']


@register.filter()

def censor(word):
   if isinstance(word, str):
      for i in word.split():
         if i.capitalize() in cens:
               word = word.replace(i, i[0] + '*' * len(i))
   else:
      raise ValueError(
         'custom_filters -> censor -> Ожидался ввод строкового значения')
   return word