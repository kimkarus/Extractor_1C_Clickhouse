import sys
import psycopg2

debug = False
pg_requests_0 = ""
if debug:
    argv_filepath_requests = "C://Users//Ilya//AppData//Local//Temp//cc3b0fb3-9280-4c19-8ea5-c5fdbef0f242.txt"
    argv_filepath_results = "C://Users//Ilya//AppData//Local//Temp//3fbaa1ed-db38-44d9-8483-9cb5b51dc8fe.txt"
    argv_dbname = 'argv_dbname'
    argv_user = 'argv_user'
    argv_password = 'argv_password'
    argv_host = 'argv_host'
    argv_type = 'post'
    pg_requests = "SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'bp_documents1'"
else:
    argv_filepath_requests = sys.argv[1]
    argv_filepath_results = sys.argv[2]
    argv_dbname = sys.argv[3]
    argv_user = sys.argv[4]
    argv_password = sys.argv[5]
    argv_host = sys.argv[6]
    argv_type = sys.argv[7]
#
pg_commited = 0
#
with open(argv_filepath_requests, 'r', encoding="utf-8-sig") as file:
    pg_requests = file.read()
pg_requests = pg_requests.replace("\n", "")
pg_requests = pg_requests.replace("\ufeff", "")

pg_requests_0 = pg_requests_0 + "" + pg_requests + ""
conn = psycopg2.connect(dbname=argv_dbname, user=argv_user, password=argv_password, host=argv_host)
response_json = ""
#
if argv_type == 'get':
    # run pg_requests
    try:
        cursor = conn.cursor()
        cursor.execute(pg_requests_0)
        # run transaction
        records = cursor.fetchall()
        for row in records:
            pg_commited = 1
        cursor.close()
    except Exception as e:
        cursor.close()
        #wait = input("Press Enter to continue.")
        results_file = open(argv_filepath_results, "w", encoding="utf-8")
        results_file.write(str(e))
        results_file.close()

    conn.close()
if argv_type == 'get_json':
    from psycopg2.extras import DictCursor
    cursor = conn.cursor(cursor_factory=DictCursor)
    # run pg_requests
    try:
        cursor.execute(pg_requests_0)
        # run transaction
        response_json_arr = []
        records = cursor.fetchall()
        for row in records:
            response_json_arr.append(dict(row))
        response_json = str(response_json_arr)
        response_json = response_json.replace("' '", '')
        response_json = response_json.replace("::", "")
        response_json = response_json.replace("'", "\"")
        response_json = response_json.replace("None,", '"None",')
        cursor.close()
        pg_commited = 1
    except Exception as e:
        cursor.close()
        #wait = input("Press Enter to continue.")
        results_file = open(argv_filepath_results, "w", encoding="utf-8")
        results_file.write(str(e))
        results_file.close()

    conn.close()
if argv_type == 'post':
    try:
        cursor = conn.cursor()
        # run pg_requests
        cursor.execute(pg_requests_0)
        # run transaction
        conn.commit()
        #
        pg_commited = 1
        cursor.close()
    except Exception as e:
        cursor.close()
        #wait = input("Press Enter to continue.")
        results_file = open(argv_filepath_results, "w", encoding="utf-8")
        results_file.write(str(e))
        results_file.close()

    conn.close()

if pg_commited == 1:
    results_file = open(argv_filepath_results, "w", encoding="utf-8")
    if argv_type == 'post' or argv_type == 'get':
        results_file.write("OK")
    else:
        results_file.write(str(response_json))
    results_file.close()
else:
    results_file = open(argv_filepath_results, "w", encoding="utf-8")
    results_file.write("ERROR")
    results_file.close()