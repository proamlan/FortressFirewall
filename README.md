# Protecting Your API with IP-Based Blocking and Rate Limiting

This project demonstrates techniques to safeguard your API against malicious activity and excessive usage by:

Blocking API calls from specific IP addresses
Implementing rate limiting to control the frequency of requests from individual IPs

## Technologies Used

Python
Django
django-ratelimit (for rate limiting)

## Usage

Run your Django application.
Attempt excessive or unauthorized API calls from a specific IP.
Observe IP-based blocking and rate limiting in action.

```
@ratelimit(key='ip', rate='50/h')
def index(request):
return HttpResponse("Hello, world. You're at the polls index.")
```
