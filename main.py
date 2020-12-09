from fastapi import FastAPI, HTTPException
import db


app = FastAPI()


@app.get("/ordenes/")
async def obtener_ordenes():
    ordenes = db.obtener_ordenes()
    return ordenes