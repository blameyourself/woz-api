from include.config import connect
from psycopg2 import sql
import psycopg2

def emailVerification(code: str, email: str):
    data = []
    try:
        conn = connect()
        cur = conn.cursor()

        if code == 'true':
            stmt = sql.SQL('''UPDATE public.useraccount
                          SET is_email_verified = '{email_value}' WHERE email = '{email}';
                          '''.format(email_value = code,
                                     email = email))
        cur.execute(stmt)
        conn.commit()
        result = cur.rowcount
        cur.close()

        if result:
            data.append({"status": 200,"message": "Successfullly Verified"})
        else:
            data.append({"status": 400,"message": "Could Not Verify"})
        
        return data    

    except (Exception,psycopg2.DatabaseError) as error:
        data.append({"status": 500,"message": "Server internal error"})
        print("Failed to add parent, error: ", error)
        return data
