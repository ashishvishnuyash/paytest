from sqlmodel import SQLModel, Field, ForeignKey, create_engine
from typing import Optional 
import datetime

class Group(SQLModel, table=True):
    id:  Optional[int] = Field(primary_key=True)
    groupname: str

class Status(SQLModel, table=True):
    id:  Optional[int] = Field(primary_key=True)
    statustype: str

class User(SQLModel, table=True):
    id:  Optional[int] = Field(primary_key=True)
    first_name: str
    last_name: str
    phone_no: str
    email: str = Field(unique=True)
    group:  Optional[int] = Field(default=None, foreign_key="group.id")
    password: str
    status: Optional[int] = Field(default=2, foreign_key="status.id")
    
class TransactionType(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    typename: str

class TransactionCurrency(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    currencyname: str
    symbool: str
    value: float

class TransactionStatuses(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    status: str

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user: Optional[int] = Field(foreign_key="user.id")
    datetime:float = Field(default=datetime.datetime.now().timestamp(), nullable=False)
    type: Optional[int] = Field(foreign_key="transactiontype.id")
    amount: float = Field(default=0)
    fees: float = Field(default=0)
    total: float = Field(default=0)
    currency: Optional[int] = Field(foreign_key="transactioncurrency.id")
    receiveruser: Optional[int] = Field(foreign_key="user.id")
    status: Optional[int] = Field(foreign_key="transactionstatuses.id")
    

class Addressproof(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user: Optional[int] = Field(foreign_key="user.id")
    address: str
    state : str
    city: str
    postal_code: str
    nationality: str
    

class IDproof(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    user: Optional[int] = Field(foreign_key="user.id")
    id_type: str
    id_number: str
    id_erpiry_date: str
    id_upload: str
    


class Fees(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    user : int = Field(foreign_key="user.id" ,default=0 )
    setup_fee: float
    yearly_fee: float
    monthly_fee: float
    
    credit_mdr_percentage: float
    credit_min_fee: float
    
    debit_mdr_percentage: float
    debit_min_fee: float
