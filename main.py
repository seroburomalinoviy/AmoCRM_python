
import json

amo_domain = 'https://antidirt.amocrm.com'

# Авторизация в amoCRM
# auth(amo_domain)

with open('tokens.txt') as tok:
    data = json.load(tok)
    access_token = str(data['access_token'])
    refresh_token = str(data['refresh_token'])

headers = {
    "Authorization": f"Bearer {access_token}",
}

textfile = 'notification_text.txt'
rec_mail = 'mr.ivandmi@yandex.ru'

# contacts_post(amo_domain, contacts, headers):

# leads_post(amo_domain, leads, headers):

# data_post(amo_domain, textfile, rec_mail, upd_leads, tasks, notes, headers):
