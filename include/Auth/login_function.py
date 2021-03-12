from include.config import connect
from include.filedir import dirFile
import psycopg2
import jwt
import datetime
import json

config = dirFile()

def LoginFunction(email:str, password:str):
    data = []
    payload = {}
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(""" SELECT idaccount, email, password
                        FROM public.useraccount
                        WHERE (email = %s or email= %s) and password = %s and status<>'true';
                    """, (email, email, password, ))
        conn.commit()
        result = cur.rowcount
        fetchdata = cur.fetchall()
        if result:
            for row in fetchdata:
                payload = {"id": row[0], "email": row[1]}
            
            token = jwt.encode({'payload':payload,
                               'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)}, 
                               config.get('secretKey'), 
                               algorithm='HS256')

            data.append({"status": 200,
                         "message": "Successfully login", 
                         "body": {"token": token.decode(),
                                  "data": payload}})
        else:
            data.append({"status": 403,"message": "Invalid username or password", "body":{}})
        
        cur.close()
        return data
    except (Exception, psycopg2.DatabaseError) as error:
        print("Failed to signin, error: ", error)
        data.append({"status": 500,"message": "Internal Server Error", "body":{}})
        return data