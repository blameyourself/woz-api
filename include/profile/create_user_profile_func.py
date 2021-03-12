from include.config import connect
from psycopg2 import sql
from include.filter import attribute
import psycopg2
import uuid

def addUserCredential(fullname:str, email:str, password:str, birtdate:str, gender:str, address:str, country:str):
    data = []
    try:
        user_id = str(uuid.uuid4().hex)
        conn = connect()
        cur = conn.cursor()

        stmt = sql.SQL(""" INSERT INTO
                                public.useraccount(idaccount, email, password)

                            SELECT '{user_id}', '{email}', '{password}'
                            WHERE
                                NOT EXISTS (
                                    SELECT email FROM public.useraccount WHERE email = '{email}'
                                );
                            """.format(user_id = user_id,
                                       email = email,
                                       password = password))
        cur.execute(stmt)
        conn.commit()
        result = cur.rowcount
       

        if result:

            stmt1 = sql.SQL( """INSERT INTO
                                public.userprofile(idaccount, fullname, birthdate, gender, address, country)

                            SELECT '{user_id}', '{fullname}', '{birtdate}', '{gender}', '{address}', '{country}'
                            WHERE
                                NOT EXISTS (
                                    SELECT fullname, address, country FROM public.userprofile WHERE fullname = '{fullname}' AND address = '{address}' AND country = '{country}'
                                );
                            """.format(user_id = user_id,
                                        fullname = fullname,
                                        birtdate = birtdate,
                                        gender = gender,
                                        address = address,
                                        country = country))
            cur.execute(stmt1)
            conn.commit()
            result1 = cur.rowcount
            cur.close()

        if result:
            data.append({"status": 200,"message": "Successfullly added"})
        else:
            data.append({"status": 403,"message": "Data already Exist"})
            
        return data    

    except (Exception,psycopg2.DatabaseError) as error:
        data.append({"status": 500,"message": "Server internal error"})
        print("Failed to add parent, error: ", error)
        return data

