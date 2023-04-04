from datetime import timedelta, datetime
from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel

from src.user import User
from src.user import UserReq

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
SECRET_KEY = "fe3c19aff3338ffba9a6f230476323e98896b3bacc721fcc863058606473e2c0"
ALGORITHM = "HS256"


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


def verify_password(plain_pw, hashed_pw):
    return pwd_context.verify(plain_pw, hashed_pw)


# the_user is the correct info from the database
def authenticate(username, password, the_user: User):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if username != the_user.user or username is None:
        raise credential_exception
    if not verify_password(password, the_user.pw):
        raise credential_exception
    return the_user.user


def create_access_token(data: dict, expire_delta: timedelta | None = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    if token_data.username != "anne" | token_data.username is None:
        raise credentials_exception
    return token_data
