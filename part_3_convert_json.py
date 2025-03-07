import cc_classes
import cc_dat_utils
import json


#Part 3
#Load your custom JSON file
input_json_file = "data/kpitcair_cc1.json"

with open(input_json_file, "r") as file:
    jsd = json.load(file)


#Convert JSON data to CCLevelPack

#Save converted data to DAT fil

def make_level_pack_from_json(json_data):

    level_pack = cc_classes.CCLevelPack()

    for level_data in json_data["level_pack"]["levels"]:
        level = cc_classes.CCLevel()

        #reqs
        level.level_number = level_data["level_number"]
        level.time = level_data["time"]
        level.num_chips = level_data["num_chips"]
        level.upper_layer = level_data["upper_layer"]

        #fields 3, 6, 7, 10
        level.add_field(cc_classes.CCMapTitleField(level_data["map_title"]))
        level.add_field(cc_classes.CCEncodedPasswordField(level_data["password"]))
        level.add_field(cc_classes.CCMapHintField(level_data["hint_text"]))

        monster_list = []
        if "monsters" in level_data and len(level_data["monsters"]) >= 1:
            for monster in level_data["monsters"]:
                coords = cc_classes.CCCoordinate(monster[0], monster[1])
                monster_list.append(coords)
            level.add_field(cc_classes.CCMonsterMovementField(monster_list))

        level_pack.levels.append(level)

    return level_pack





level_pack = make_level_pack_from_json(jsd)

cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "data/kpitcair_cc1.dat")

print(level_pack)