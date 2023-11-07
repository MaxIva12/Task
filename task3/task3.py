import sys
import json

def fill_insert_values(tests, values):
    for test in tests:
        test_id = test['id']
        for value in values['values']:
            if value['id'] == test_id and 'value' in test:
                test['value'] = value['value']
        if 'values' in test:
            fill_insert_values(test['values'], values)

def fill_values(tests, values):
    for test in tests['tests']:
        test_id = test['id']
        for value in values['values']:
            if value['id'] == test_id:
                test['value'] = value['value']
        if 'values' in test:
            fill_insert_values(test['values'], values)

def generate_report(tests_file, values_file, report_file):
    with open(tests_file, 'r') as f:
        tests = json.load(f)
    with open(values_file, 'r') as f:
        values = json.load(f)
    
    fill_values(tests, values)
    
    with open(report_file, 'w') as f:
        json.dump(tests, f, indent=4)

# Получаем параметры файлов из аргументов командной строки
file1 = sys.argv[1]
file2 = sys.argv[2]

report_file = 'report.json'

generate_report(file1, file2, report_file)
