has_account = True
email_verified = False

can_login = has_account and email_verified

email = 'wahl@gmail.com'
is_email_valid = '@' in email 

user_age = 17
is_age_valid = user_age > 17

can_login_final = has_account and email_verified and is_email_valid and is_age_valid

print(can_login, is_email_valid, is_age_valid, can_login_final )

print("has_account is True")