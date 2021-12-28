
import json
from functions import contacts_post, leads_post, data_post
from data import contacts, leads, upd_leads, tasks, notes
from auth import auth

amo_domain = 'https://antidirt.amocrm.com'
textfile = 'notification_text.txt'
rec_mail = 'mr.vanya1998@yandex.ru'

#           AUTH
# auth(amo_domain)

with open('tokens.txt') as tok:
    data = json.load(tok)
    access_token = str(data['access_token'])
    refresh_token = str(data['refresh_token'])
headers = {
    "Authorization": f"Bearer {access_token}",
}

#           ADD CONTACTS

resp_contacts = contacts_post(amo_domain, contacts(), headers)

lst_id_cont = []
for i in range(len(resp_contacts['_embedded']['items'])):
  lst_id_cont.append(resp_contacts['_embedded']['items'][i]['id'])

#           ADD LEADS

resp_leads = leads_post(amo_domain,leads(lst_id_cont), headers)

lst_id_leads = []
for i in range(5):
  lst_id_leads.append(resp_leads['_embedded']['items'][i]['id'])

#           ADD TASKS, NOTES  UPDATE LEADS  SEND MES

data_post(amo_domain, textfile, rec_mail, upd_leads(lst_id_leads), tasks(lst_id_leads), notes(lst_id_cont[5:]), headers)
