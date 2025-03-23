# Author: Peter
# Ver 0.1
# Append massive list to a existent JSON

import sys
import json


def createJson(argv) -> None:
    # ARGV 1 read the origin file backup
    # ARGV 2 read the list to append to the JSON
    json_input = argv[1]
    subdomains_input = argv[2]

    with open(subdomains_input, "r", encoding="utf-8") as f:
        raw_subdomains = f.read()
        subdomains_list = raw_subdomains.split("\n")

    with open(json_input, "r", encoding="utf-8") as f:
        dict_json = json.loads(f.read())
        main_key = "monitorList"
        tag_key = "tags"
        sub_keys = {
            "id": 1,
            "name": "",
            "pathName": "",
            "accepted_statuscodes": ["200-299", "300-399", "400-499"],
            "url": "",
            "tags": [
                {
                    "id": 1,
                    "monitor_id": 1,
                    "tag_id": 1,
                    "value": "",
                    "name": "Primera Division",
                    "color": "#cc4b00",
                }
            ],
        }

        replace_name = ["name", "url"]
        increment_tags = ["id", "monitor_id"]
        last_tag = ["tag_id"]

        parent_id = 22

        len_monitor_list = len(dict_json[main_key])

        copy_dict = {}
        if len_monitor_list > 0:
            copy_dict = dict_json[main_key][0].copy()
        else:
            raise (Exception("This dict is empty"))

        latest_id = 0
        latest_monitor_id = 0
        latest_tag_id = 0

        for dict in dict_json[main_key]:
            tags_dict = dict[tag_key]
            l_tag_dict = len(tags_dict)

            if l_tag_dict > 1:
                last_tag = tags_dict[l_tag_dict - 1]
            elif l_tag_dict == 1:
                last_tag = tags_dict[l_tag_dict - 1]
            else:
                if dict["name"] == "Cloudflare":
                    group_location = dict

                continue

            if last_tag["id"] > latest_id:
                latest_id = last_tag["id"]

            if last_tag["monitor_id"] > latest_monitor_id:
                latest_monitor_id = last_tag["monitor_id"]

            if last_tag["tag_id"] > latest_tag_id:
                latest_tag_id = last_tag["tag_id"]

        print(latest_id, latest_monitor_id, latest_tag_id)
        latest_id += 1
        latest_monitor_id += 1
        latest_tag_id += 1

        sub_keys["tags"][0]["tag_id"] = latest_tag_id

        for subdomain in subdomains_list:
            actual_copy = copy_dict.copy()
            for key, value in sub_keys.items():
                if type(actual_copy[key]) is str and key in replace_name:
                    actual_copy[key] = "https://" + subdomain
                elif type(actual_copy[key]) is int and key == "parent":
                    actual_copy[key] = parent_id

                elif type(actual_copy[key]) is list and key == "accepted_statuscodes":
                    actual_copy[key] = value
                elif type(actual_copy[key]) is list and key == "tags":
                    for inc in increment_tags:
                        if key == "id":
                            actual_copy[key][0][inc] = sub_keys[key][0][inc] + latest_id
                        elif key == "monitor_id":
                            actual_copy[key][0][inc] = (
                                sub_keys[key][0][inc] + latest_monitor_id
                            )
                elif type(actual_copy[key]) is int and key == "id":
                    actual_copy[key] = actual_copy[key] + latest_monitor_id
                elif key == "accepted_statuscodes" or key == "pathName":
                    actual_copy[key] = sub_keys[key]

            group_location["childrenIDs"].append(latest_monitor_id)

            latest_monitor_id += 1
            latest_id += 1
            dict_json[main_key].append(actual_copy)

        with open("out.json", "w") as out:
            out.write(json.dumps(dict_json))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        createJson(sys.argv)
    elif len(sys.argv) == 2 and sys.argv[1] == '-i':
        
    else:
        print(f"Error please do: ")
        print(f"${sys.argv[0]} <json> <list>")
