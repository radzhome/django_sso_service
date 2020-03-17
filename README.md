# django_sso_service
django sso service poc


# TODO: Does not work in safari, iframe does not load


### Setup

1. Setup django:


    pip install django
    
1. Configure /etc/hosts  add the following:


    127.0.0.1       site1.local
    127.0.0.1       site2.local
    127.0.0.1       sso.mymedia.local
    127.0.0.1       site1.mymedia.local
    127.0.0.1       site2.mymedia.local

1. Browse `http://site1.local:8000/`, try login, see console.


## References

### Sessions how to:
https://docs.djangoproject.com/en/3.0/topics/http/sessions/#using-cookie-based-sessions

### Local storage b/w domains
* https://levelup.gitconnected.com/share-localstorage-sessionstorage-between-different-domains-eb07581e9384

### Sending data b/w iframe and parent
* https://stackoverflow.com/questions/25098021/securityerror-blocked-a-frame-with-origin-from-accessing-a-cross-origin-frame
* https://stackoverflow.com/questions/9153445/how-to-communicate-between-iframe-and-the-parent-site 



