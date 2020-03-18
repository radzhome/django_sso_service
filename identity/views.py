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
    return render(request, 'home.html')


@csrf_exempt
@xframe_options_exempt
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

    if request.method == 'POST':
        if form.is_valid():
            # TODO: Call api to log user in (janrain)

            # Store whatever we want in the session
            session['last_login'] = time.time()
            session['user_email'] = form.cleaned_data['email']
            session['some_key'] = 'some value'
            session.save()
            session_key = session.session_key

            max_age = 8 * 24 * 60 * 60  # session expiry, x days
            expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                                 "%a, %d-%b-%Y %H:%M:%S GMT")

    # TODO: We need to set cookie each time to get in js?
    response = render(request, 'login.html', {'form': form, 'user_session': session.session_key})
    response.set_cookie('user_session', session_key, max_age=max_age, expires=expires)

    return response


def logout(request):
    """
    logout endpoint, clearing the cookie which
    will in turn clear local storage in fe
    :param request:
    :return:
    """
    response = redirect(reverse('sso_login'))
    # response.set_cookie('user_session', '')
    response.set_cookie(settings.SESSION_COOKIE_NAME, '')
    return response


# OLD WAY, but we can use session middleware to do the lifting for us
# from django.contrib.sessions.models import Session
# from django.contrib.sessions.backends.db import SessionStore
# @csrf_exempt
# @xframe_options_exempt
# def login(request):
#     """
#     Login view
#     :param request: POST.request (form)
#     :return: render, response with login template
#     """
#     form = LoginForm(request.POST or None)
#
#     max_age = expires = None
#     user_session = ''
#     if request.method == 'POST':
#         if form.is_valid():
#             # TODO: Call api to log user in (janrain)
#
#             # Create or restore session
#             try:
#                 user_session = request.COOKIES.get('user_session')
#                 session = Session.objects.get(pk=user_session)
#             except Session.DoesNotExist:
#                 session = None
#
#             if not session:
#                 max_age = 8 * 24 * 60 * 60  # session expiry, x days
#                 expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
#                                                      "%a, %d-%b-%Y %H:%M:%S GMT")
#
#                 # Store what we want in our session here
#                 session_store = SessionStore()
#                 session_store['last_login'] = time.time()
#                 session_store['user_email'] = form.cleaned_data['email']
#                 session_store['expires'] = expires
#                 session_store.create()
#
#                 # Set cookie here, same expiry as session
#                 user_session = session_store.session_key
#     else:
#         try:
#             user_session = request.COOKIES.get('user_session')
#             session = Session.objects.get(pk=user_session)
#         except Session.DoesNotExist:
#             session = None
#
#         if session:
#             # Do we need to Check expire date if valid, if not delete cookie?
#             logging.error(session.session_key)
#             logging.error(session.get_decoded())
#             logging.error(session.expire_date)
#
#     response = render(request, 'login.html', {'form': form, 'user_session': user_session})
#     response.set_cookie('user_session', user_session, max_age=max_age, expires=expires)
#     return response
