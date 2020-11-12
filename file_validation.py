import pandas as pd
import logging
import cx_Oracle

from lib.db_connections import DBconnections
from lib.rule_check import RuleCheck

sql = "SELECT column_name,rule FROM file_validation_rule WHERE file_name='employees_new.csv'"
config_sql="SELECT FILE_NAME,FILE_TYPE,FILE_LOCATION,ACTIVE_IND FROM FILE_CONFIG WHERE ACTIVE_IND='Y'"

db= DBconnections('ORACLE')
config_result = db.query_result_set(config_sql)


def rule_valiation():
    rule_result = ''
    comments = ''
    final_result = ''
    for rule_config in result:
        column_name = rule_config[0]
        rules = rule_config[1].split(';')
        for setrules in rules:
            if setrules == 'unique':
                rule_result = rule.is_unique_calc(column_name)
                comments = column_name + ' ' + ' ' + 'rule ' + setrules + ' result' + ':' + str(
                    rule_result) + '\n' + comments
                final_result = str(rule_result) + final_result
            elif setrules == 'notnull':
                rule_result = rule.not_null_calc(column_name)
                comments = column_name + ' ' + ' ' + 'rule ' + setrules + ' result' + ':' + str(
                    rule_result) + '\n' + comments
                final_result = str(rule_result) + final_result
            elif "len>" in setrules:
                rule_result = rule.char_length_less_calc(column_name, setrules[4:])
                comments = column_name + ' ' + ' ' + 'rule ' + setrules + ' result' + ':' + str(
                    rule_result) + '\n' + comments
                final_result = str(rule_result) + final_result
            elif "len>" in setrules:
                rule_result = rule.char_length_greater_calc(column_name, setrules[4:])
                comments = column_name + ' ' + ' ' + 'rule ' + setrules + ' result' + ':' + str(
                    rule_result) + '\n' + comments
                final_result = str(rule_result) + final_result
            else:
                rule_result = setrules + ' ' + ' ' + 'rules does not exists...add rules'
                comments = column_name + ' ' + ' ' + 'rule ' + setrules + ' result' + ':' + str(
                    rule_result) + '\n' + comments
                final_result = 'False' + ' ' + final_result + ' '
    return comments, final_result

def capture_request(file_name,row_number,status,comments,error_code):
        conn = db.oracle_set_connections()
        cur = conn.cursor()
        rows = [file_name,row_number,status,comments,error_code]
        cur.execute(
            "insert into file_valiation_request(file_name, no_of_records,status,rule_comments,error_message) "
            "values (:1, :2, :3, :4,:5)",
            rows)
        conn.commit()

def file_config_update(active_status,file_name):
    conn = db.oracle_set_connections()
    cur = conn.cursor()
    rows = [active_status,file_name]
    print(rows)
    cur.execute(
        "update FILE_CONFIG set active_ind = :1"
        "where file_name = :2",
        rows)
    conn.commit()

for file_config in config_result:
    try:
        print(file_config)
        file_name=file_config[0]
        file_path=file_config[2]
        print(file_name)
        print(file_path)
        file_df = pd.read_csv(file_path + file_name)

        rule = RuleCheck(file_df)
        result = db.query_result_set(sql)

        if __name__ == "__main__":
            rule_comments,final_result=rule_valiation()
            if 'False' in final_result:
                status='Failed'
            else:
                status='Success'

            capture_request('employees_new.csv', len(file_df), status, rule_comments,' ')
            file_config_update('C','employees_new.csv')
    except Exception as e:
        capture_request('employees_new.csv', len(file_df), 'Error', rule_comments, e.message + ' ' + e.code)
