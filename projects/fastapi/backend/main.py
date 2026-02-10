from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import mysql.connector
from mysql.connector import Error
from pydantic import BaseModel


class Animal(BaseModel):
    name: str
    price: float
    quantity: int
    img: str = None

class AnimalUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    img: Optional[str] = None

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
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
        cursor = conn.cursor()

        sql = "INSERT INTO animals (name, price, quantity, img) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (animal.name, animal.price, animal.quantity, animal.img))
        conn.commit()

        cursor.close()

        cursor = conn.cursor(dictionary=True)
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
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM animals WHERE id = %s", (id,))
        return cursor.fetchone()

    except Error as e:
        raise HTTPException(status_code=404, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.put("/api/animals/{id}")
def edit_the_object(id: int, animal: Animal):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "UPDATE animals SET name = %s, price = %s, quantity = %s, img = %s WHERE id = %s"
        cursor.execute(sql, (animal.name, animal.price, animal.quantity, animal.img, id))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Animal not found")

        cursor.close()

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM animals WHERE id = %s", (id,))
        return cursor.fetchone()

    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()




@app.patch("/api/animals/{id}")
def update_animal(id: int, data: AnimalUpdate):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        fields = []
        values = []

        for key, value in data.model_dump(exclude_none=True).items():
            fields.append(f"{key} = %s")
            values.append(value)

        if not fields:
            raise HTTPException(status_code=400, detail="no fields to update")

        values.append(id)

        sql = f"UPDATE animals SET {', '.join(fields)} WHERE id = %s"

        cursor.execute(sql, values)
        conn.commit()

        cursor.execute("SELECT * FROM animals WHERE id = %s", (id,))
        animal = cursor.fetchone()

        if not animal:
            raise HTTPException(status_code=404, detail="animal not found")

        return animal

    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.delete("/api/animals/{id}")
def delete_the_object(id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM animals WHERE id = %s", (id,))
        conn.commit()
        return {"message": "data deleted"}

    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()






