import psycopg2
import psycopg2.extras
from datetime import datetime

# DB Credential
HOST     = "192.168.1.211"
PORT     = "5432"
DBNAME   = "postgres"
USER     = "postgres"
PASSWORD = os.environ['postgres_pass']
 
CREDENTIAL = "host={h} port={p} dbname={db} user={u} password={pa}"\
	.format(h=HOST,p=PORT,db=DBNAME,u=USER,pa=PASSWORD)


def logout(str,log_f):
	with open(log_f,"a") as f:
		print(str)
		f.write(str)
		f.write("\n")
	


"""/**************************************************/
   /*         1.をファイルから読み込む               */
   /**************************************************/"""
def read_file_query(path):
    f = open(path,'r')
    query = f.read()
    f.close()	
    return query

"""/**************************************************/
   /*         2.クエリを実行                         */
   /**************************************************/"""
 
def exe_query(_query, _credential):

    with psycopg2.connect(_credential) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            
            # クエリ実行
            cur.execute(_query)
 
def exe_process(_proc_nm,_query, _credential,log_f):
	
	logout( "Process = " + _proc_nm, log_f)
	logout( "Process Start   DateTime => " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"), log_f)
	
	try:
		result = exe_query(_query, _credential)
	except Exception as e:
		print( str(e) )
		log_msg = "ERROR OCCURED IN exe_query"
		logout( log_msg , log_f)
		logout( "ERROR MESSAGE = " + str(e) , log_f)
	logout( "Process Finish  DateTime => " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"), log_f)
 
 
