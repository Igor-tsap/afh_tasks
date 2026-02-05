from fastapi import FastAPI, HTTPException
import mysql.connector
from mysql.connector import Error
from pydantic import BaseModel

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
    user = 'root',
    password = 'aKp1haay2iEs394W',
    host = 'localhost',
    port = 8889,
    database = '2nd',
    raise_on_warnings = True,
    )


# class Item(BaseModel):
#     name: str = None
#     price: float = None
#     quantity: int = None
#
#
#
# items = []

# @app.get("/api/animals", response_model=list[Item])
# def index(limit: int = 10):
#     return items[0:limit]

@app.get("/api/animals")
def index():
    try:
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM animals ORDER BY id")
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data

    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))



# @app.post("/api/animals")
# def create(item: Item):
#     items.append(item)
#     return items
#
#
# @app.get("/api/animals/{id}", response_model=Item)
# def the_object(id: int) -> Item:
#     if id < len(items):
#         return items[id]
#     else:
#         raise HTTPException(status_code=404,detail=f"Item {id} not found")

