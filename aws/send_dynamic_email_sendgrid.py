import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

# from address we pass to our Mail object, edit with your name
FROM_EMAIL = 'iuc@iu.edu'

# update to your dynamic template id from the UI
TEMPLATE_ID = 'd-dec40c9d6b324aa7b248ee63fef787e2'

# list of emails and preheader names, update with yours


def send_dynamic_email(email, date, id, title, theme, name, phone, secondary_authors):
    """ Send a dynamic email to a list of email addresses

    :returns API response code
    :raises Exception e: raises an exception """
    # create Mail object and populate
    TO_EMAILS = [(email)]

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAILS)
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = {
        'date': date,
        'number': id,
        'title': title,
        'theme': theme,
        'name': name,
        'email': email,
        'phone': phone,
        'secondary_authors': secondary_authors
    }
    message.template_id = TEMPLATE_ID
    # create our sendgrid client object, pass it our key, then send and return our response objects
    try:
        sg = SendGridAPIClient("")
        response = sg.send(message)
        code, body, headers = response.status_code, response.body, response.headers
        print(f"Response code: {code}")
        print(f"Response headers: {headers}")
        print(f"Response body: {body}")
        print("Dynamic Messages Sent!")
    except Exception as e:
        print("Error: {0}".format(e))
    return str(response.status_code)


# if __name__ == "__main__":
#     SendDynamic()
