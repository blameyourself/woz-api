from include.config import connect
from include.filter import attribute
from include.filedir import dirFile
from psycopg2 import sql
import psycopg2
import uuid
import jwt
import json


config = dirFile()
def addUserFileUpload(token: str, fileUpload: str):
	data = []
	try:
		id_docs = str(uuid.uuid4().hex)
		decoded = jwt.decode(token, key=config.get('secretKey'))
		decoded = json.dumps(decoded)
		decoded = json.loads(decoded)

		idaccount = decoded['payload']['id']
		email = decoded['payload']['email']

		
		conn = connect()
		cur = conn.cursor()

		if fileUpload:
			stmt = sql.SQL(""" INSERT INTO
							public.userdocument(id,idaccount, filephoto, status)

						SELECT '{id_docs}','{idaccount}', '{fileUpload}', '{status}'
						WHERE
							NOT EXISTS (
								SELECT id FROM public.userdocument WHERE   idaccount= '{idaccount}'
							);
						""".format(id_docs = id_docs,
									idaccount = idaccount, 
									fileUpload =  fileUpload,
									status = 'true'))
			cur.execute(stmt)
			conn.commit()
			result = cur.rowcount
			cur.close()

		if result:
			data.append({"status": 200,"message": "File Successfully Upload"})
		else:
			data.append({"status": 403,"message": "File Already Exist"})

		return data

	except (Exception,psycopg2.DatabaseError) as error:
		data.append({"status": 500,"message": "Server internal error"})
		print("Failed to add parent, error: ", error)
		return data