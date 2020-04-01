from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(r"", "config.visitor_urls", name="visitor"),
    host(r"dashboard", "config.member_urls", name="member"),
)
