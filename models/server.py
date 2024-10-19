from pydantic import BaseModel
from typing import Generic, TypeVar, Optional
from models.types import UpdatedFormat

A = TypeVar("A")


class ServerInfo(BaseModel):
    version: str = "product"


class UserAuth(BaseModel):
    uid: int
    dbid: int
    authCode: str
    version: str
    synchronousDataVersion: int


class RequestPacket(BaseModel, Generic[A]):
    userAuth: UserAuth
    parameters: A


class ResponsePacket(BaseModel, Generic[A]):
    serverInfo: ServerInfo = ServerInfo()
    state: str = "ok"
    updated: Optional[UpdatedFormat] = None
    result: A
