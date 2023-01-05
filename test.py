import pandas as pd
import json


def make_clickable_monster_name(idx, name):
    return f'<a target="_blank" href="monster_detail?id={idx}">{name}</a>'


data = json.load(open('json_test_files/breeding_combo_example.json'))
df = data
monster_page_id = 6

reformat_list = []
for combo in data:
    entry = {}
    if combo['pedigree_id']:
        name_x = combo['pedigree']['old_name']
        if combo['pedigree_id'] == monster_page_id:
            entry['PEDIGREE'] = name_x
        else:
            temp_id_x = combo['pedigree_id']
            entry['PEDIGREE'] = make_clickable_monster_name(temp_id_x, name_x)
    else:
        entry['PEDIGREE'] = combo['pedigree_family']['family_eng'] + " FAMILY"

    if combo['parent2_id']:
        name_y = combo['parent2']['old_name']
        if combo['parent2_id'] == monster_page_id:
            entry['PARTNER'] = name_y
        else:
            temp_id_y = combo['parent2_id']
            entry['PARTNER'] = make_clickable_monster_name(temp_id_y, name_y)
    else:
        entry['PARTNER'] = combo['family2']['family_eng'] + " FAMILY"

    if combo['child_id'] == monster_page_id:
        entry['OFFSPRING'] = combo['child']['old_name']
    else:
        temp_id_z = combo['child_id']
        name_z = combo['child']['old_name']
        entry['OFFSPRING'] = make_clickable_monster_name(temp_id_z, name_z)

    reformat_list.append(entry)
# print(df.columns)
# print(reformat_list)

return_df = pd.DataFrame(reformat_list)
print(return_df)
