import time
# import logging
import datetime

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt

from identity.forms import LoginForm


def home(request):
    user_session = request.COOKIES.get('user_session')
    return render(request, 'home.html', {'user_session': user_session})


def login(request):
    """
    Login view

    :param request: POST.request (form)
    :return: render, response with login template
    """
    form = LoginForm(request.POST or None)
    session = request.session
    max_age = expires = None
    session_key = session.session_key
    janrain_cookie = None
    if request.method == 'POST':
        if form.is_valid():
            # TODO: Call api to log user in (janrain). For now mock if form valid set.
            janrain_cookie = 'this-is-a-test'

            # Store whatever we want in the session
            session['last_login'] = time.time()
            session['user_email'] = form.cleaned_data['email']
            session['some_key'] = 'some value'
            session.save()
            session_key = session.session_key

            max_age = 8 * 24 * 60 * 60  # session expiry, x days
            expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                                 "%a, %d-%b-%Y %H:%M:%S GMT")

    # TODO: We can only get the cookie in js once its set by server? seems so.
    response = render(request, 'login.html', {'form': form, 'user_session': session.session_key})
    response.set_cookie('user_session', session_key or '', max_age=max_age, expires=expires)

    # Set additional login cookies
    if janrain_cookie:
        response.set_cookie('janrainCaptureToken', janrain_cookie, max_age=max_age, expires=expires)
    return response


def logout(request):
    """
    logout endpoint, clearing the cookie which
    will in turn clear local storage in fe
    :param request:
    :return:
    """
    response = redirect(reverse('sso_login'))
    response.set_cookie(settings.SESSION_COOKIE_NAME, '')
    response.delete_cookie('user_session')
    response.delete_cookie('janrainCaptureToken')
    return response


@csrf_exempt
@xframe_options_exempt
def hidden(request):
    return render(request, 'hidden.html')
