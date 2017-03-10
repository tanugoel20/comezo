from django import template

register = template.Library()


@register.filter(name='chr')
def chr_(value):
    return chr(value + 64)


@register.filter()
def to_int(value):
    return int(value)


@register.filter(name='strng')
def str_(value):
    return str(value)


@register.filter(name='flag_reverse')
def flag_reverse_(boolean):
    flag = not boolean
    #return not boolean
    return flag
