from ninja import Schema
from pydantic import EmailStr
from datetime import datetime
from typing import List

class WaitListEntryCreateSchema(Schema):
    email: EmailStr = None

class ErrorWaitListEntryCreateSchema(Schema):
    email: List[dict]
    # non_field_errors: List[dict] = []

class WaitlistEntryCreateResponseSchema(Schema):
    email: EmailStr
    message: str = None

class WaitListEntryDetailSchema(Schema):
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime

class WaitListEntryListSchema(Schema):
    id: int
    email: EmailStr

class WaitlistEntryUpdateSchema(Schema):
    # Put -> Data
    # WaitlistEntryOut
    # id: int
    description: str = ""