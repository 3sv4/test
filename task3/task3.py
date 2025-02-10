import sys
import json
values = sys.argv[1] #Объявление путей к файлам
tests = sys.argv[2]
report = sys.argv[3]
def update_report(data, value_dict): #Рекурсивная функция с вставкой "value"
    if isinstance(data, list):
        for item in data:
            update_report(item, value_dict)
    elif isinstance(data, dict):
        if "id" in data and data["id"] in value_dict:
            data["value"] = value_dict[data["id"]]
        if "values" in data:
            update_report(data["values"], value_dict)
with open(values, "r" ,encoding='utf-8') as fp: #Чтение и запись файла(в переменную) с результатами прохождения теста
    data_values = json.load(fp)
with open(tests, "r" ,encoding='utf-8') as fp: #Чтение и запись файла(в переменную) с структурой построения отчета
    data_tests = json.load(fp)
value_dict = {item["id"]: item["value"] for item in data_values["values"]} #Запись "id" и "value" в переменный массив
update_report(data_tests["tests"], value_dict) #Вызов функции для составления "report"
with open(report, "w" ,encoding='utf-8') as fp: 
    json.dump(data_tests, fp, indent=4) #Запись отчёта в report.json 