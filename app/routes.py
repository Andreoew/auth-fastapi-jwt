from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.auth_user import UserUseCases
from app.schemas import UserRegister, UserLogin
 
user_router = APIRouter(prefix='/user')

@user_router.post('/register')
def user_register(
    user: UserRegister,
    db_session: Session = Depends(get_db_session),
):
    uc = UserUseCases(db_session=db_session)
    uc.user_register(user=user)
    return JSONResponse(
        content={'msg': 'success'},
        status_code=status.HTTP_201_CREATED
    )
    


@user_router.post('/login')
def user_login(
    login_request_form: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session)
):
    uc = UserUseCases(db_session=db_session)
    
    user = UserLogin(
        username=login_request_form.username,
        password=login_request_form.password
    )
    
    auth_data = uc.user_login(user=user)
    
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )