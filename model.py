from fastapi import FastAPI , HTTPException , Depends
from sqlalchemy.orm import Session
from database import Sessionlocal , enigne , Todo_app


app = FastAPI()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/")
async def greet():
    return {"message " : "add todo"}
@app.get("/hi")
async def greeting():
    return {"message" : "Hi"}

@app.get("/Todo")
async def create_todo(todo = Todo_app , db : Session = Depends(get_db)):
    db.add(todo)
    db.commit()
    db.refresh()
    return todo


@app.put("/Todo/{Todo_id}")
async def  update_todo(Todo_id : int , update_todo = Todo_app , db : Session = Depends(get_db)):
    db_Todo = db.query(Todo_app).filter(Todo_app.id == Todo_id).first()
    if db_Todo is None:
        raise HTTPException(status_code= 404 , detail= "Todo Not found")
    for key , value in update_todo.dict().items():
        setattr(db_Todo , key , value )
    db.commit()
    return db_Todo

@app.delete("/Todo/{Todo_id}")
async def delete_todo(Todo_id : int , db : Session = Depends(get_db)):
    db_todo = db.query(Todo_app).filter(Todo_app.id == Todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code= 404 , detail = "Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message" : "Todo is deleted successfully"}