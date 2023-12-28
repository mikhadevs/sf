from django import template

register = template.Library()

UNACCEPTABLE_WORDS = [
    'fool', 'Fool',
    'stupid', 'Stupid',
    'silly', 'Silly'
]

@register.filter()
def censor(value):
    for unw in UNACCEPTABLE_WORDS:
        value = value.replace(unw, unw[:1] + '*' * (len(unw) - 1))
        #value = value.replace(unw, '***') #замена всего слова на *
    return value



