# django_sso_service
django sso service poc


# TODO: Does not work in safari, iframe does not load


### Setup

1. setup django:
    pip install django
    
1. configure /etc/hosts  add the following:

    127.0.0.1       site1.local
    127.0.0.1       site2.local
    127.0.0.1       sso.postmedia.local
    127.0.0.1       site1.postmedia.local
    127.0.0.1       site2.postmedia.local

1. Browse `http://site1.local:8000/`

### Sessions how to:
https://docs.djangoproject.com/en/3.0/topics/http/sessions/#using-cookie-based-sessions

### Local storage b/w domains
https://levelup.gitconnected.com/share-localstorage-sessionstorage-between-different-domains-eb07581e9384



