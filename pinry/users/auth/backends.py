
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from pinry.core.models import Pin
from pinry.users.models import User


def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class CombinedAuthBackend(object):
    def authenticate(self, username=None, password=None):
        is_email = validateEmail(username)
        if is_email:
            qs = User.objects.filter(email=username)
        else:
            qs = User.objects.filter(username=username)

        try:
            user = qs.get()
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def has_perm(self, user, perm, obj=None):
        """
        A very simplistic authorization mechanism for now. Basically a pin owner can do anything with the pin.
        """
        if obj and isinstance(obj, Pin):
            return obj.submitter == user
        return False
