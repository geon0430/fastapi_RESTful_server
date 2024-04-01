from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class APIstruct(BaseModel):
    id: int
    name: str
    rtsp: str
    codec: str
    model: str
    fps: float
    in_width: int
    in_height: int
    out_width: int
    out_height: int
    on_time: str
    off_time: str
    post_time: str
    update_time: str
    status: str
    button: bool
    random_seed: int

json_list: List[APIstruct] = []

class DB(BaseModel):
    id: int
    name: str
    rtsp: str
    codec: str
    model: str
    fps: float
    in_width: int
    in_height: int
    out_width: int
    out_height: int
    on_time: str
    off_time: str
    post_time: str
    update_time: str
    status: str
    button: bool
    random_seed: int
    gpu: int
    moniter: bool

db_list: List[DB] = []