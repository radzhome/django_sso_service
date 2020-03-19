# django_sso_service
django sso service poc


* Firefox did not like password fields in an iframe
* Safari did not like iframes coming from different domains that had input
* Server passes cookies which are saved in local storage on login
* logout - remove cookies + local storage
* TODO: Next - janrain traditional login working + jwt token saved to local torage


### Setup

1. Setup django:


    pip install -r requirements.txt
    
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

## Viafoura dash, docs
* https://auth.viafoura.co/login?response_type=code&scope=56696166-6f75-7261-0000-000000000000&site=0&client_id=4499c2bf-9a85-4e9f-b875-e23e352da524&redirect_uri=https%3A%2F%2Fadmin.viafoura.co%2Foauth2%2Fcode&state=pdp959cc5shems96hfppdtd08h.admin
* https://documentation.viafoura.com/docs/viafoura-custom-jwt-login
* https://documentation.viafoura.com/reference#get_-site-id-domain-aliases

### Piano dash, docs
* https://dashboard.tinypass.com/publisher/home
* https://docs.piano.io/implementing-janrain/

#### Janrain dash, docs
* https://console.janrain.com/#/login
* https://learn.akamai.com/en-us/webhelp/identity-cloud/technical-library/GUID-8E88D51A-26C7-4C2E-881F-BF7EB3A71F2E.html

