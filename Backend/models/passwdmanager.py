
from cryptography.fernet import Fernet
import jwt
import datetime

key ="_EoMIDJMMo-FK60K0GyYfMnkGF5EsTwFQzbpGEy8z1w="

auth_key="QGfGIpHLt8DDHjdPmecRGbPeKubTHNx_QOsXdGZvJYs="


class PasswordManager:
    
    def encrypt_password(password):
        try:
            cipher_suite = Fernet(key)
            encrypted_password = cipher_suite.encrypt(password.encode())
            return encrypted_password
        except Exception as e:
            print("Error encrypting password:", e)
            return None

    def decrypt_password(encrypted_password):
        try:
            cipher_suite = Fernet(key)
            decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
            return decrypted_password
        except Exception as e:
            print("Error decrypting password:", e)
            return None



class JwtToken:
    def generate_token(user_id):
        try:
            payload = {
                'user_id': user_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=1)}
            token = jwt.encode(payload, auth_key,algorithm='HS256')
            return token
        except Exception as e:
            print("Error generating token:", e)
            return None
        
    def verify_token(token):
        try:
            payload = jwt.decode(token, auth_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return False
        

# print(JwtToken.generate_token(1))
# print(jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTE1MjcyNTl9.c0IoMsNVeDydQvHL_KGA8AUYLgC7pRCKCuEURGUaf2o"))
