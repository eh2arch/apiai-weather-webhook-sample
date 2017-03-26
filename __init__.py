import json

global_subj_list = 0

with open('global_subj_list.json') as json_data:
    global_subj_list = json.load(json_data)