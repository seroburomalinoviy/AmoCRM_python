from pprint import pprint
import requests
import smtplib
from email.message import EmailMessage


def send_mes(textfile, rec_mail):
  my_email = 'vanya104@gmail.com'
  passw = input(str("Password: "))
  with open(textfile) as fp:
      msg = EmailMessage()
      msg.set_content(fp.read())

  msg['Subject'] = 'Notification from AmoCRM'
  msg['From'] = my_email
  msg['To'] = rec_mail

  # Send the message via gmail
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(my_email, passw)
  print("login success")
  server.send_message(msg)
  server.quit()
  print('sent')

def print_res(res):
  if res.status_code == 200:
      data = res.json()
      pprint(data)
  else:
    pprint(res.content)

def contacts_post(amo_domain, contacts, headers):
  res = requests.post(amo_domain + "/api/v2/contacts", json=contacts, headers=headers)
  print_res(res)

def leads_post(amo_domain, leads, headers):
  res = requests.post(amo_domain + "/api/v2/leads", json=leads, headers=headers)
  print_res(res)

def data_post(amo_domain, textfile, rec_mail, upd_leads, tasks, notes, headers):
  # Get the id of Lead Stages to update one
  # res = requests.get(amo_domain + "/api/v2/pipelines",headers=headers)
  res = requests.post(amo_domain + "/api/v2/leads", json=upd_leads, headers=headers)
  print_res(res)
  res = requests.post(amo_domain + "/api/v2/tasks", json=tasks, headers=headers)
  print_res(res)
  send_mes(textfile, rec_mail)
  res = requests.post(amo_domain + "/api/v2/notes", json=notes, headers=headers)
  print_res(res)