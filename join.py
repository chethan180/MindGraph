import pandas as pd
import json

df1 = pd.read_csv('Metadata.csv')
df2 = pd.read_csv('F_club_linked.csv')
df3 = pd.read_csv('F_org_linked.csv')
df4 = pd.read_csv('F_fest_linked.csv')


data = []

for row in df1.iterrows():
    # print(row[1].ID)
    # print(df3.loc[df3['ID'] == row[1].ID])
    fest_org = df3.loc[df3['ID'] == row[1].ID]
    fest_part = df4.loc[df4['ID'] == row[1].ID]
    clubs = df2.loc[df2['ID'] == row[1].ID] 
    # fest_org = df3.loc[df3['ID'] == '17XJ1A0303']
    # fest_part = df4.loc[df4['ID'] == '17XJ1A0303']
    # clubs = df2.loc[df2['ID'] == '17XJ1A0303'] 
    # print(clubs)
    # print(fest_part)
    record = {
        'name' : row[1].Name,
        'id' : row[1].ID,
        'clubs':{
                'club_1' : {
                    'isOrganiser' : '',
                    'club_1_event_1' : {
                    'participated' : False
                    },
                    'club_1_event_2' : {
                    'participated' : False
                    },
                    'club_1_event_3' : {
                    'participated' : False
                    }
                },
                'club_2' : {
                    'isOrganiser' : '',
                    'club_2_event_1' : {
                    'participated' : False
                    },
                    'club_2_event_2' : {
                    'participated' : False
                    },
                    'club_2_event_3' : {
                    'participated' : False
                    }
                },
                'club_3' : {
                    'isOrganiser' : '',
                    'club_3_event_1' : {
                    'participated' : False
                    },
                    'club_3_event_2' : {
                    'participated' : False
                    },
                    'club_3_event_3' : {
                    'participated' : False
                    }
                }

        },
        'fests':{
                'fest_1' : {
                    'isOrganiser' : '',
                    'fest_1_event_1' : {
                    'participated' : False
                    },
                    'fest_1_event_2' : {
                    'participated' : False
                    },
                    'fest_1_event_3' : {
                    'participated' : False
                    },
                    'fest_1_event_4' : {
                    'participated' : False
                    },
                    'fest_1_event_5' : {
                    'participated' : False
                    },
                    'fest_1_event_6' : {
                    'participated' : False
                    },
                    'fest_1_event_7' : {
                    'participated' : False
                    },
                    'fest_1_event_8' : {
                    'participated' : False
                    },
                    'fest_1_event_9' : {
                    'participated' : False
                    },
                    'fest_1_event_10' : {
                    'participated' : False
                    },
                    'fest_1_event_11' : {
                    'participated' : False
                    },
                    'fest_1_event_12' : {
                    'participated' : False
                    },
                    'fest_1_event_13' : {
                    'participated' : False
                    },
                    'fest_1_event_14' : {
                    'participated' : False
                    },
                    'fest_1_event_15' : {
                    'participated' : False
                    },
                    
            },
            'fest_2' : {
                    'isOrganiser' : '',
                    'fest_2_event_1' : {
                    'participated' : False
                    },
                    'fest_2_event_2' : {
                    'participated' : False
                    },
                    'fest_2_event_3' : {
                    'participated' : False
                    },
                    'fest_2_event_4' : {
                    'participated' : False
                    },
                    'fest_2_event_5' : {
                    'participated' : False
                    },
                    'fest_2_event_6' : {
                    'participated' : False
                    },
                    'fest_2_event_7' : {
                    'participated' : False
                    },
                    'fest_2_event_8' : {
                    'participated' : False
                    },
                    'fest_2_event_9' : {
                    'participated' : False
                    },
                    'fest_2_event_10' : {
                    'participated' : False
                    },
                    'fest_2_event_11' : {
                    'participated' : False
                    },
                    'fest_2_event_12' : {
                    'participated' : False
                    },
                    'fest_2_event_13' : {
                    'participated' : False
                    },
                    'fest_2_event_14' : {
                    'participated' : False
                    },
                    'fest_2_event_15' : {
                    'participated' : False
                    },
                    
            },
        }
    }


    # record["clubs"] = {}
    # x = record["clubs"]
    # x["hell"] = {"fe" : "dd"}

    # z.append({"name" : "d"})

    # print(clubs)
    for row_club in clubs.iterrows():
        # record = recordformat
        # print("x=" , row_club[1].Club_Name)
        clubname = row_club[1].Club_Name
        # print("len = ",len(clubname))
        clubevent = row_club[1].Event
        role = row_club[1].Role
        # row_club[1].
        # record.clubs 
        # print(record)
        # print("")
        clu = record["clubs"]
        # clu[clubname] = {}
        x = clu[clubname]
        # print(role[:11])
        if(role[:9] == "organiser"):
            x['isOrganiser'] = 'Organiser'
        else:
            # part = x[clubevent]
            # part['participated'] = True
            part = {'participated': True}
            x[clubevent] = part
            # print("true")


    for row_fest in fest_part.iterrows():
        # record = recordformat
        # print("x=" , row_fest[1])
        clubname = row_fest[1].Fest_Name
        # print("len = ",len(clubname))
        clubevent = row_fest[1].Event
        # role = row_fest[1].Role
        # row_fest[1].
        # record.clubs 
        # print(record)
        # print("")
        clu = record["fests"]
        # clu[clubname] = {}
        x = clu[clubname]
        # print(role[:11])
            # part = x[clubevent]
            # part['participated'] = True
        part = {'participated': True}
        x[clubevent] = part

    for row_org in fest_org.iterrows():
        # record = recordformat
        # print("x=" , row_org[1])
        clubname = row_org[1].Fest_Name
        # print("len = ",len(clubname))
        # clubevent = row_org[1].Event
        # role = row_org[1].Role
        # row_org[1].
        # record.clubs 
        # print(record)
        # print("")
        clu = record["fests"]
        # clu[clubname] = {}
        x = clu[clubname]
        # print(role[:11])
            # part = x[clubevent]
            # part['participated'] = True
        # part = {'participated': True}
        # x[clubevent] = part
        x['isOrganiser'] = 'Organiser'
            # print("true")
    data.append(record)
    # break
    # data.append(record)

with open("sample.json", "w") as outfile:
    json.dump(data, outfile)


# print(data)
# print(record)


#      Unnamed: 0 Club_Name           Event         Role               Name          ID
# 630         630    club_2  club_2_event_1  organiser_5  Guillermo Hackney  17XJ1A0296
# 631         631    club_3  club_3_event_1  Participant  Guillermo Hackney  17XJ1A0296
# 632         632    club_2  club_2_event_2  Participant  Guillermo Hackney  17XJ1A0296
# 633         633    club_3  club_3_event_2  Participant  Guillermo Hackney  17XJ1A0296
# 634         634    club_1  club_1_event_2  Participant  Guillermo Hackney  17XJ1A0296
# 635         635    club_2  club_2_event_3  organiser_5  Guillermo Hackney  17XJ1A0296
# 636         636    club_2  club_2_event_1  Participant  Guillermo Hackney  17XJ1A0296



        # 'clubs' : {
        #     'club_1': {
        #         'isOrganiser' : "",
        #         'club_1_event_1' : {
        #             'participated' : ""
        #         }
        #     },
        #     'club_2': {
        #         'isOrganiser' : "",
        #         'club_1_event' : {
        #             'participated' : ""
        #         }
        #     },
        #     'club_3': {
        #         'isOrganiser' : "",
        #         'club_1_event' : {
        #             'participated' : ""
        #         }
        #     },  
        # }


# [
#     {
#         'name': 'Dummy',
#         'id': 'id000',
#         'clubs': {
#             'club_i': {
#                 'isOrganiser': 'Organiser',
#                 'club_i_event_j': {
#                     'participated': False
#                     },
#             },
#         },
#         'fests': {
#             'fest_i': {
#                 'isOrganiser': '',
#                 'fest_i_event_j': {
#                     'participated': True
#                     },
#             },
#         }
#     }
# ]