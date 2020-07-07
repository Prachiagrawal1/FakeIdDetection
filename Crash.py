import os
import signal
import sys
from sentry_sdk import configure_scope
from sentry_sdk import add_breadcrumb
import sentry_sdk
sentry_sdk.init("https://412c14178bf94be187693e247fb502fd@o417232.ingest.sentry.io/5316059",
	release="Crash_app@0.0.2",
	environment="production" 
	)
# sentry_sdk.init(release="Crash_app@0.0.2")

with configure_scope() as scope:
    scope.user = {"email": "prachi@example.com", "username":"prachi_agrawal"}
    scope.user = {"email": "john.doe@example.com"}
    scope.level = 'fatal'
    scope.set_context("my_cool_data", {"foo": "bar"})
    scope.set_tag("page_locale", "de-at")

add_breadcrumb(
    category='auth',
    message='Authenticated user %s' % user.email,
    level='info',
)

os.kill(os.getpid(), signal.SIGABRT)

planet = "32 ascii char string (=32 bytes)"
blackhole = []
while True:
	blackhole.append(planet)



division_by_zero = 1 / 0
print(division_by_zero)
l={1,3,4}
print(l[4])
