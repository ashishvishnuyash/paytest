from sqlmodel import SQLModel, Field, ForeignKey, create_engine ,Session
from .model import User , Group, Status
from .passwdmanager import PasswordManager


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)



# SQLModel.metadata.create_all(engine)

def createModal():
    SQLModel.metadata.create_all(engine)
        


