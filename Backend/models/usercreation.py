from sqlmodel import Session ,select
from .model import User, Group, Status
from .app import engine
from .passwdmanager import PasswordManager,JwtToken


class UserCreationManager:
    def create_user(firstname, lastname, phone, email, password, group_id, status_id):
        with Session(engine) as session:
            encrypted_password = PasswordManager.encrypt_password(password)
            new_user = User(first_name=firstname, last_name=lastname, phone_no=phone, email=email, group=group_id, status=status_id, password=encrypted_password)
            session.add(new_user)
            session.commit()
            return firstname,True
    def update_user(user_id, firstname, lastname, phone, email, group_id, status_id):
        with Session(engine) as session:
            user = session.query(User).filter(User.id == user_id).first()
            user.first_name = firstname
            user.lastname = lastname
            user.phone_no = phone
            user.email = email
            user.group = group_id
            user.status = status_id
            session.commit()
    def delete_user(user_id):
        with Session(engine) as session:
            user = session.query(User).filter(User.id == user_id).first()
            session.delete(user)
            session.commit()
    def get_user(user_id):
        with Session(engine) as session:
            user = session.query(User).filter(User.id == user_id).first()
            return user
    
    def update_user_password(user_id, new_password):
        with Session(engine) as session:
            encrypted_password = PasswordManager.encrypt_password(new_password)
            user = session.query(User).filter(User.id == user_id).first()
            user.password = encrypted_password
            session.commit()
    def update_user_group(user_id, group_id):
        with Session(engine) as session:
            user = session.query(User).filter(User.id == user_id).first()
            user.group = group_id
            session.commit()
    
    def get_all_users():
        with Session(engine) as session:
            
            # Execute a query to fetch all records from the Hello table
            query = select(User)
            result = session.exec(query).all()

            # Convert each record to a dictionary
            records = [record.dict() for record in result]
            
            return records
            # return users
    def update_user_status(user_id, status_id):
        with Session(engine) as session:
            user = session.query(User).filter(User.id == user_id).first()
            user.status = status_id
            session.commit()
   
    def get_user_by_email(email):
        with Session(engine) as session:
            user = session.query(User).filter(User.email == email).first()
            return user
    

  
            
    
class UserGroupManager:
    def add_group(groupname):
        with Session(engine) as session:
            new_group = Group(groupname=groupname)
            session.add(new_group)
            session.commit()
    
    def add_statustype(statustype):
        with Session(engine) as session:
            new_status = Status(statustype=statustype)
            session.add(new_status)
            session.commit()

class Login:
    def __init__(self , email, password):
        self.email = email
        self.password = password
    def login(self):
        user = UserCreationManager.get_user_by_email(self.email)
        if user:
            decrypted_password = PasswordManager.decrypt_password(user.password)
            if self.password == decrypted_password:
                token=JwtToken.generate_token(user.id)
                
                return token
            else:
                print("Incorrect Password")
                return False
        else:
            print("User not found")
            return False
    
    def isAdmin(self,user):
        if user.group == 3:
            return True
        else:
            return False
    def isActive(self,user):
        if user.status == 1:
            return True
        else:
            return False
    def isMerchant(self,user):
            if user.group == 2:
                return True
            else:
                return False
    def isUser(self,user):
        if user.group == 1:
            return True
        else:
            return False
    
        
class auth:
    def authenticate(token):
        payload=JwtToken.verify_token(token)
        print(payload)
        if payload:
            user=UserCreationManager.get_user(payload['user_id'])
            if user:
                return user
        else:
            return False

