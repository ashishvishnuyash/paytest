from models.usercreation import UserCreationManager , UserGroupManager , Login ,auth
import json as jsn
from models.model import User , Group, Status, TransactionType, TransactionCurrency, TransactionStatuses, Transaction
from models.app import engine 
from sqlmodel import Session ,select
from blacksheep import Application, get , post ,FromJSON ,text ,route ,json ,Request
from blacksheep.cookies import Cookie
# from blacksheep.server import json_response


app = Application()
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

@route('/userdetail',methods=['GET'])    
async def userdetail(request:Request):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        return json({"message": user})
    else:
        return json({"message": "Unauthorized"})
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
    
@route('/deposit',methods=['POST'])
async def deposit(request:Request,expense_model: FromJSON[dict]):
    token = request.cookies.get("token")
    print(token)
    user = auth.authenticate(token)
    if user:
        data = expense_model.value
        with Session(engine) as session:
            money=Transaction(user=user.id,type=3,amount=data['amount'],fees=["fees"],total=data["total"],currency=data['currency'],receiveruser=user.id,status=1)
            session.add(money)
            session.commit()
        return json({"message": "Transaction Successful"})
    else:
        return json({"message": "Unauthorized"})
    
    

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="localhost", port=44777, log_level="debug")
    