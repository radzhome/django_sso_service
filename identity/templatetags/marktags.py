from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def cookie(context, cookie_name):  # could feed in additional argument to use as default value
    """
    For getting a cookie in template
    :param context:
    :param cookie_name:
    :return:
    """
    request = context['request']
    result = request.COOKIES.get(cookie_name, '')  # I use blank as default value
    return result
