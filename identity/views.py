import time
import datetime

from django.shortcuts import render
# from django.shortcuts import redirect
# from django.urls import reverse
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from identity.forms import LoginForm


import logging


def login(request):
    """
    Login view
    :param request: POST.request (form)
    :return: render, response with login template
    """
    form = LoginForm(request.POST or None)

    response = render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        if form.is_valid():
            # TODO: Call api to log user in

            # Create or restore session
            session = Session.objects.get(pk=request.COOKIES['user_session'])
            if not session:
                max_age = 8 * 24 * 60 * 60  # x days
                expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                                     "%a, %d-%b-%Y %H:%M:%S GMT")

                session_store = SessionStore()
                session_store['last_login'] = time.time()
                session_store['user_email'] = form.cleaned_data['email']
                session_store['expires'] = expires
                session_store.create()

                # Set cookie here
                response.set_cookie('user_session', session_store.session_key, max_age=max_age, expires=expires)

            # return redirect(reverse('home'))
    else:
        session = Session.objects.get(pk=request.COOKIES['user_session'])
        if session:
            # TODO: check expire date if valid, if not delete cookie
            # logging.error(session['expires'])
            logging.error(session.session_key)
            # logging.error(session.session_data)
            logging.error(session.get_decoded())
            logging.error(session.expire_date)
            # logging.error(dir(session))
        else:
            pass
            # TODO: delete cookie

    return response

