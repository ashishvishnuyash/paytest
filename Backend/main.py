"""
API routes for user registration, login, transactions, and account management.

Includes routes for:

- Registering a new user account
- Logging in with email and password
- Getting user details
- Sending money to another user  
- Receiving money from another user
- Getting list of transactions
- Withdrawing funds
- Depositing funds
- Setting a user's address
- Setting a user's ID proof

Uses SQLAlchemy and Pydantic models for data validation and database interactions.
"""
from models.usercreation import UserCreationManager , UserGroupManager , Login ,auth
import json as jsn
from models.utiliti import save_media_file
from models.model import User , Group, Status, TransactionType, TransactionCurrency, TransactionStatuses, Transaction , Addressproof ,IDproof
from models.app import engine 
from sqlmodel import Session ,select
from blacksheep import Application, get , post ,FromJSON ,text ,route ,json ,Request
from blacksheep.cookies import Cookie
# from blacksheep.server import json_response


app = Application()
app.use_cors()
cors = app.cors

app.add_cors_policy(
    "one",
    allow_methods="GET POST PUT DELETE",
    allow_origins="*",
    allow_headers="Authorization",
    allow_credentials=True,
)

@app.cors("one")
@route('/register', methods=['POST'])
async def registernewuser(expense_model: FromJSON[dict]):
    data=expense_model.value
    firstname = data["first_name"]
    lastname = data["last_name"]
    phone = data["phone"]
    email = data["email"]
    groupid = data["group_id"]
    password = data["password"]
    # Validate user details
    statusid = data["status_id"]
    # Create user
    user = UserCreationManager.create_user(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password,group_id=groupid,status_id=statusid)
    

    return text(f"User {user} created successfully.")
@app.cors("one")
@route('/login', methods=['POST'])
async def login(expense_model: FromJSON[dict]):
    
    data=expense_model.value
    email = data["email"]
    password = data["password"]
    
    
    user = Login(email, password).login()
    if user:
        
        r =json({"message": "Login Successful", "user":
            user})
        r.set_cookie(Cookie(name="token", value=user))
        return r
    else:
        return json({"message": "Login failed"})
@app.cors("one")
@route('/userdetail',methods=['GET'])    
async def userdetail(request:Request):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        #get address data
        with Session(engine) as session:
            address=session.query(Addressproof).filter(Addressproof.user==user.id).first()
            idproof=session.query(IDproof).filter(IDproof.user==user.id).first()
            return json({"message": "Login Successful", "user":
            user,"address":address,"idproof":idproof})
            
        
    else:
        return json({"message": "Unauthorized"})

@app.cors("one")
@route('/send',methods=['POST'])
async def sendmoney(request:Request,expense_model: FromJSON[dict]):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        data = expense_model.value
        with Session(engine) as session:
            reciverid=UserCreationManager.get_user_by_email(data['reciver_email']).id
            money=Transaction(user=user.id,type=1,amount=data['amount'],fees=["fees"],total=data["total"],currency=data['currency'],receiveruser=reciverid,status=1).save()
            session.add(money)
            session.commit()
        return json({"message": "Transaction Successful"})
    else:
        return json({"message": "Unauthorized"})

@app.cors("one")
@route('/receive',methods=['POST'])
async def receive(request:Request,expense_model: FromJSON[dict]):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        data = expense_model.value
        with Session(engine) as session:
            reciverid=UserCreationManager.get_user_by_email(data['reciver_email']).id
            money=Transaction(user=user.id,type=2,amount=data['amount'],fees=["fees"],total=data["total"],currency=data['currency'],receiveruser=reciverid,status=1).save()
            session.add(money)
            session.commit()
     
        return json({"message": "Transaction Successful"})
    else:
        return json({"message": "Unauthorized"})
    
@app.cors("one")
@route('/transactions',methods=['GET'])
async def transactions(request:Request):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        with Session(engine) as session:
            transactions=select(Transaction).where(Transaction.user==user.id).execute()
            return json({"message": transactions})
    else:
        return json({"message": "Unauthorized"})

@app.cors("one")
@route('/withdraw',methods=['POST'])
async def withdraw(request:Request,expense_model: FromJSON[dict]):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        data = expense_model.value
        with Session(engine) as session:
            money=Transaction(user=user.id,type=4,amount=data['amount'],fees=["fees"],total=data["total"],currency=data['currency'],receiveruser=user.id,status=1)
            session.add(money)
            session.commit()
        return json({"message": "Transaction Successful"})
    else:
        return json({"message": "Unauthorized"})

@app.cors("one") 
@route('/deposit',methods=['POST'])
async def deposit(request:Request,expense_model: FromJSON[dict]):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        data = expense_model.value
        with Session(engine) as session:
            money=Transaction(user=user.id,type=3,amount=data['amount'],fees=data["fees"],total=data["total"],currency=1,receiveruser=user.id,status=1)
            session.add(money)
            session.commit()
        return json({"message": "Transaction Successful"})
    else:
        return json({"message": "Unauthorized"})

@app.cors("one") 
@route('/set_address',methods=['POST'])
async def set_address(request:Request,expense_model: FromJSON[dict]):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        data = expense_model.value
        with Session(engine) as session:
            address=Addressproof(user=user.id,address=data['address'],state=data['state'],city=data['city'],postal_code=data['postal_code'],nationality=data['nationality'])
            session.add(address)
            session.commit()
            return json({"message": "address added"})
    else:
        return json({"message": "Unauthorized"})

@app.cors("one")
@route('/set_id',methods=['POST'])
async def set_id(request:Request,expense_model: FromJSON[dict]):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        data = expense_model.value
        with Session(engine) as session:
            idproof=IDproof(user=user.id,id_no=data['id_no'],id_type=data['id_type'],id_expiry=data['id_expiry'],id_upload=save_media_file(data['id_upload']))
            
        return json({"message": "id added"})
    else:
        return json({"message": "Unauthorized"})
        
    



if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="localhost", port=44777, log_level="debug")
    