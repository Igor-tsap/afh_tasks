from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import Error
from pydantic import BaseModel


class Animal(BaseModel):
    name: str = None
    price: float = None
    quantity: int = None
    img: str = None


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return mysql.connector.connect(
    user = 'root',
    password = 'aKp1haay2iEs394W',
    host = 'localhost',
    port = 8889,
    database = '2nd',
    raise_on_warnings = True,
    )


@app.get("/api/animals")
def index():
    conn = None
    cursor = None
    try:
        conn=get_connection()
        cursor=conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM animals ORDER BY id")
        return cursor.fetchall()

    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.post("/api/animals", status_code=201)
def create(animal: Animal):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "INSERT INTO animals (name, price, quantity, img) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (animal.name, animal.price, animal.quantity, animal.img))
        conn.commit()

        cursor.execute("SELECT * FROM animals WHERE id = %s", (cursor.lastrowid,))
        return cursor.fetchone()

    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.get("/api/animals/{id}")
def the_object(id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM animals WHERE id = %s", (id,))
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data


