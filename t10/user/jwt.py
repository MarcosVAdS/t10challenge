import json
import base64
import os
import datetime

class Jwt():
    def createJWT(data=[], expire_time=3600):
        header = [
            'alg' = 'HS256',
            'typ' = 'JWT'
        ]
        header = json.dumps(header)

        tokenid = base64.b64encode(os.urandom(32))
        createdTime = datetime.datetime.now()
        notExpireBefore = createdTime + 60
        

        payload = [

        ]