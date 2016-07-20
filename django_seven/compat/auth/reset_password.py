import django


def reset_password_uidb_context(user_id):
    if django.VERSION < (1, 6):
        base = 36
    else:
        base = 64
    uidb_key = 'uidb' + str(base)
    return {uidb_key: int_to_base(user_id, base)}


def int_to_base(user_id, base):
    if base == 36:
        from django.utils.http import int_to_base36
        return int_to_base36(user_id)
    elif base == 64:
        # Logic extracted from django.contrib.auth.forms.PasswordResetForm in Django 1.6+
        from django.utils.encoding import force_bytes
        from django.utils.http import urlsafe_base64_encode
        return urlsafe_base64_encode(force_bytes(user_id))
