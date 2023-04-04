from datetime import timedelta
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database.connection import sess_db
from repo.actor import ActorRepository, ActorJoinRepository
from repo.user import UserRepository
from security.secure import authenticate, create_access_token, get_current_user

DIR_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(DIR_PATH / "../templates"))
user_router = APIRouter()


@user_router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), sess: Session = Depends(sess_db)):
    user = UserRepository.get_all_login_username(sess, form_data.username)
    login_user = authenticate(form_data.username, form_data.password, user)
    if not login_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=420)
    access_token = create_access_token(data={"sub": login_user},
                                       expire_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/admin", response_class=HTMLResponse)
async def admin(request: Request,
                username: Annotated[str, Depends(get_current_user)],
                sess: Session = Depends(sess_db)):
    """

    :type sess: object
    """
    if username:
        actor_table = ActorRepository.get_all_actor(sess)
        actor_joint_table = ActorJoinRepository.join_actor_all(sess)
        for actor, nation, instrument, gender in actor_joint_table:
            print(actor.name, nation.name, instrument.instrument_namn,
                  gender.description)
        return templates.TemplateResponse("admin.html", {"request": request,
                                                         "actors": actor_table,
                                                         "actor_joint_table": actor_joint_table})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You need to login again",
        )
