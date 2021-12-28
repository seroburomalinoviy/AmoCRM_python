import datetime
td = datetime.timedelta(hours=1)

import time
t = str(time.time()).split('.')


def contacts():
    contacts = {
        "add": [
            {
                "name": "Naruto",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Rassengan, Djubi",
                "custom_fields": [  # создаем нвоое поле email в контактаз в рездаеле Set up
                    {
                        "id": 327723,
                        "values": [
                            {
                                "value": "vanya104@gmail.com",
                                "subtype": "email"
                            }
                        ]
                    }
                ]

            },
            {
                "name": "Sasuke",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Chidory, Sharingan",
                "custom_fields": [  # создаем нвоое поле email в контактаз в рездаеле Set up
                    {
                        "id": 327723,
                        "values": [
                            {
                                "value": "vanya104@gmail.com",
                                "subtype": "email"
                            }
                        ]
                    }
                ]

            },
            {
                "name": "Sakura",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Regeneration, Strong",
                "custom_fields": [  # создаем нвоое поле email в контактаз в рездаеле Set up
                    {
                        "id": 327723,
                        "values": [
                            {
                                "value": "vanya104@gmail.com",
                                "subtype": "email"
                            }
                        ]
                    }
                ]

            },
            {
                "name": "Kakashi",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Raikiri, Thousand techniques",
                "custom_fields": [  # создаем нвоое поле email в контактаз в рездаеле Set up
                    {
                        "id": 327723,
                        "values": [
                            {
                                "value": "vanya104@gmail.com",
                                "subtype": "email"
                            }
                        ]
                    }
                ]

            },
            {
                "name": "Shikamaru",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Shadow, Brain",

            },
            {
                "name": "FirstHokage",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Wood Style",

            },
            {
                "name": "2ndHokage",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Speed style, resurrection from the dead",

            },
            {
                "name": "3d Hokage",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "5 styles, Enma",

            },
            {
                "name": "4th Hokage",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Fastest, sealing techniques",

            },
            {
                "name": "5th Hokage",
                "responsible_user_id": "29901778",
                "created_by": "29901778",
                "tags": "Power, Healing",

            }
        ]
    }
    return contacts
def leads(lst_id):
    leads = {
        "add": [
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "5000",
                "tags": "pencil, buy",
                "contacts_id": lst_id[0]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "100",
                "tags": "buy",
                "contacts_id": lst_id[1]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "500",
                "tags": "buy",
                "contacts_id": lst_id[2]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "200",
                "tags": "buy",
                "contacts_id": lst_id[3]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "120",
                "tags": "buy",
                "contacts_id": lst_id[4]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "0",
                "tags": "organization",
                "contacts_id": lst_id[5]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "2000",
                "tags": "order",
                "contacts_id": lst_id[6]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "220",
                "tags": "buy",
                "contacts_id": lst_id[7]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "110",
                "tags": "buy",
                "contacts_id": lst_id[8]
            },
            {
                "name": "Sergeev ID",
                "responsible_user_id": "29901778",
                "sale": "800",
                "tags": "debt",
                "contacts_id": lst_id[9]
            },
        ]
    }
    return leads
def tasks(lst_id_leads):
    tasks = {
        'add': [
            {
                'element_id': lst_id_leads[0],  # Naruto id
                'element_type': 2,  # 1 - contact, 2 - leads, 3 - company, 12 - customer
                'complete_till_at': str(datetime.datetime.now()+td),
                'task_type': 1,  # 1 - CALL, 2 - meeting, 3 - write an email
                'text': "Work out",
                'created_at': str(datetime.datetime.now()),
                'updated_at': str(datetime.datetime.now()),
                'responsible_user_id': 29901778,
                'created_by': 29901778
            },
            {
                'element_id': lst_id_leads[1],
                'element_type': 2,  # 1 - contact, 2 - leads, 3 - company, 12 - customer
                'complete_till_at': str(datetime.datetime.now()+td),
                'task_type': 1,  # 1 - CALL, 2 - meeting, 3 - write an email
                'text': "Find brother",
                'created_at': str(datetime.datetime.now()),
                'updated_at': str(datetime.datetime.now()),
                'responsible_user_id': 29901778,
                'created_by': 29901778
            },
            {
                'element_id': lst_id_leads[2],
                'element_type': 2,  # 1 - contact, 2 - leads, 3 - company, 12 - customer
                'complete_till_at': str(datetime.datetime.now()+td),
                'task_type': 1,  # 1 - CALL, 2 - meeting, 3 - write an email
                'text': "Love Sasuke",
                'created_at': str(datetime.datetime.now()),
                'updated_at': str(datetime.datetime.now()),
                'responsible_user_id': 29901778,
                'created_by': 29901778
            },
            {
                'element_id': lst_id_leads[3],
                'element_type': 2,  # 1 - contact, 2 - leads, 3 - company, 12 - customer
                'complete_till_at': str(datetime.datetime.now()+td),
                'task_type': 1,  # 1 - CALL, 2 - meeting, 3 - write an email
                'text': "Buy new Paradise Game",
                'created_at': str(datetime.datetime.now()),
                'updated_at': str(datetime.datetime.now()),
                'responsible_user_id': 29901778,
                'created_by': 29901778
            },
            {
                'element_id': lst_id_leads[4],
                'element_type': 2,  # 1 - contact, 2 - leads, 3 - company, 12 - customer
                'complete_till_at': str(datetime.datetime.now()+td),
                'task_type': 1,  # 1 - CALL, 2 - meeting, 3 - write an email
                'text': "Buy sigarets",
                'created_at': str(datetime.datetime.now()),
                'updated_at': str(datetime.datetime.now()),
                'responsible_user_id': 29901778,
                'created_by': 29901778,
            }

        ]
    }
    return tasks

def upd_leads(lst_id_leads):
    upd_leads = {
        "update": [
            {
                "id": lst_id_leads[0],
                "updated_at": 1640725378,
                "status_id": 45000979

            },
            {
                "id": lst_id_leads[1],
                "updated_at": 1640725378,
                "status_id": 45000979
            },
            {
                "id": lst_id_leads[2],
                "updated_at": 1640725378,
                "status_id": 45000979
            },
            {
                "id": lst_id_leads[3],
                "updated_at": 1640725378,
                "status_id": 45000979
            },
            {
                "id": lst_id_leads[4],
                "updated_at": 1640725378,
                "status_id": 45000979
            }
        ]
    }
    return upd_leads

def notes(lst_id_cont):
    notes = {
        "add": [
            {
                "element_id": lst_id_cont[0],
                "element_type": 1,
                "text": "Note after post email",
                "note_type": 4,
                "created_at": str(datetime.datetime.now()),
                "responsible_user_id": 29901778,
                "created_by": 29901778
            },
            {
                "element_id": lst_id_cont[1],
                "element_type": 1,
                "text": "Note after post email",
                "note_type": 4,
                "created_at": str(datetime.datetime.now()),
                "responsible_user_id": 29901778,
                "created_by": 29901778
            },
            {
                "element_id": lst_id_cont[2],
                "element_type": 1,
                "text": "Note after post email",
                "note_type": 4,
                "created_at": str(datetime.datetime.now()),
                "responsible_user_id": 29901778,
                "created_by": 29901778
            },
            {
                "element_id": lst_id_cont[3],
                "element_type": 1,
                "text": "Note after post email",
                "note_type": 4,
                "created_at": str(datetime.datetime.now()),
                "responsible_user_id": 29901778,
                "created_by": 29901778
            },
            {
                "element_id": lst_id_cont[4],
                "element_type": 1,
                "text": "Note after post email",
                "note_type": 4,
                "created_at": str(datetime.datetime.now()),
                "responsible_user_id": 29901778,
                "created_by": 29901778
            }
        ]
    }
    return notes