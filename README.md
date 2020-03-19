# django_sso_service
django sso service poc


* Firefox did not like password fields in an iframe
* Safari did not like iframes coming from different domains that had input
* TODO: Next - need to see if cookies are best way to pass things from server and save to local storage.


### Setup

1. Setup django:


    pip install django
    
1. Configure /etc/hosts  add the following:

```
127.0.0.1       site1.local
127.0.0.1       site2.local
127.0.0.1       sso.mymedia.local
127.0.0.1       site1.mymedia.local
127.0.0.1       site2.mymedia.local
```

1. Run the server


    python3 manage.py runserver

   
1. Browse `http://site1.mymedia.local:8000/`, try login, see console.


## References

### Sessions how to:
https://docs.djangoproject.com/en/3.0/topics/http/sessions/#using-cookie-based-sessions

### Local storage b/w domains
https://levelup.gitconnected.com/share-localstorage-sessionstorage-between-different-domains-eb07581e9384

### Sending data b/w iframe and parent
* https://stackoverflow.com/questions/25098021/securityerror-blocked-a-frame-with-origin-from-accessing-a-cross-origin-frame
* https://stackoverflow.com/questions/9153445/how-to-communicate-between-iframe-and-the-parent-site 

### Session middleware
https://docs.djangoproject.com/en/2.2/_modules/django/contrib/sessions/middleware/

## Viafoura docs
* https://documentation.viafoura.com/docs/viafoura-custom-jwt-login
* https://documentation.viafoura.com/reference#get_-site-id-domain-aliases

### Piano dash
https://dashboard.tinypass.com/publisher/home

#### Janrain dash, docs
* https://console.janrain.com/#/login
* https://learn.akamai.com/en-us/webhelp/identity-cloud/technical-library/GUID-8E88D51A-26C7-4C2E-881F-BF7EB3A71F2E.html

