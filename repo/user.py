from sqlalchemy.orm import Session

from src.user import User


class UserRepository:
    def get_all_login_username(sess: Session, u: str) -> User:
        return sess.query(User).filter(User.user == u).one_or_none()
