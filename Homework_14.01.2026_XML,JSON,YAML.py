# import json
#
# results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}
#
# with open('test_results.json', 'w',encoding="utf-8")  as file_object:
#     json.dump(results, file_object,indent=2, ensure_ascii=False)
#
# with open('test_results.json', 'r', encoding="utf-8") as file_object:
#     data = json.load(file_object)
#     data_total = data['total']
#     data_passed = data['passed']
#     percent =  data_passed / data_total * 100
#     print(f"Процент успешно пройденных тестов {percent} %")
#
# results = [{"id": 1, "name": "Sasha", "role": "admin"}]
#
# with open('users.json', 'w',encoding="utf-8") as file_user:
#     json.dump(results, file_user,indent=2, ensure_ascii=False)
#
# with open('users.json', 'r', encoding="utf-8") as file_user:
#     all_users = json.load(file_user)
#     new_user = {'Drako': 'Serge'}
#     all_users.append(new_user)
#     print(all_users)
#
# with open('users.json', 'w', encoding="utf-8") as file_user:
#     json.dump(all_users, file_user,indent=2, ensure_ascii=False)

import yaml

results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}

with open ('results', 'w', encoding="utf-8") as file_text:
    yaml.safe_dump(results, file_text, default_flow_style=False,sort_keys=False)

with open ('results', 'r', encoding="utf-8") as file_text:
    data = yaml.safe_load(file_text)
    data_total = data['total']
    data_passed = data['passed']
    percent =  data_passed / data_total * 100
    print(f"Процент успешно пройденных тестов {percent} %")

results = [{"id": 1, "name": "Sasha", "role": "admin"}]

with open ('users.yaml', 'w', encoding="utf-8") as file_users:
    yaml.safe_dump(results, file_users, default_flow_style=False,sort_keys=False)

with open ('users.yaml', 'r', encoding="utf-8") as file_users:
    all_users = yaml.safe_load(file_users)
    new_user = {'Cat':'Nec'}
    all_users.append(new_user)
    print(all_users)

with open ('users.yaml', 'w', encoding="utf-8") as file_users:
    yaml.safe_dump(all_users,file_users, default_flow_style=False,sort_keys=False)




