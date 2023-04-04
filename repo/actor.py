from typing import Dict, Any, List

from sqlalchemy.orm import Session

from src import actor


class ActorRepository:
    def insert_actor(sess: Session, actor: actor.Actor) -> bool:
        try:
            sess.add(actor)
            sess.commit()

        except:
            return False
        return True

    def insert_nation(sess: Session, n: actor.Nation) -> bool:
        try:
            sess.add(n)
            sess.commit()
        except:
            return False
        return True

    def insert_gender(sess: Session, g: actor.Gender) -> bool:
        try:
            sess.add(g)
            sess.commit()
        except:
            return False
        return True

    def insert_actor_verksam(sess: Session, av: actor.ActorActive) -> bool:
        try:
            sess.add(av)
            sess.commit()
        except:
            return False
        return True

    def update_actor(sess: Session, id: int, details: Dict[str, Any]) -> bool:
        try:
            sess.query(actor.Actor).filter(actor.Actor.id == id).upate(details)
            sess.commit()
        except:
            return False
        return True

    def update_nation(sess: Session, id: int, details: Dict[str, Any]) -> bool:
        try:
            sess.query(actor.Nation).filter(actor.Nation.id == id).update(details)
            sess.commit()
        except:
            return False
        return True

    def update_gender(sess: Session, id: int, details: Dict[str, Any]) -> bool:
        try:
            sess.query(actor.Gender).filter(actor.Gender.id == id).update(details)
            sess.commit()
        except:
            return False
        return True

    def update_actor_verksam(sess: Session, a_id: int, nation_id: int,
                             details: Dict[str, Any]) -> bool:
        try:
            sess.query(actor.ActorActive).filter(
                actor.ActorActive.actor_idtor_id == a_id,
                actor.ActorActive.nation_id == nation_id).update(details)
            sess.commit()
        except:
            return False
        return True

    def get_all_actor(sess: Session) -> List[actor.ActorReq]:
        return sess.query(actor.Actor).order_by(actor.Actor.id).all()

    def get_all_nation(sess: Session) -> List[actor.Nation]:
        return sess.query(actor.Nation).order_by(actor.Nation.name).all()

    def get_all_gender(sess: Session) -> List[actor.Gender]:
        return sess.query(actor.Gender).order_by(actor.Gender.id).all()

    def get_all_isntrument(sess) -> List[actor.Instrument]:
        return sess.query(actor.Instrument).order_by(actor.Instrument.id).all()


class ActorJoinRepository():

    def join_actor_nation(sess: Session):
        return sess.query(actor.Actor, actor.Nation).filter(actor.Actor.id == actor.Nation.id).all()

    def join_actor_instrument(sess: Session):
        return sess.query(actor.Actor, actor.Instrument).filter(actor.Actor.id == actor.Instrument.id).all()

    def join_actor_type(sess: Session):
        return sess.query(actor.Actor, actor.Gender).filter(actor.Actor.id == actor.Gender.id).all()

    def join_actor_verksam_nation(sess: Session):
        return sess.query(actor.Actor, actor.Nation).filter(actor.ActorActive.actor_id == actor.Actor.id,
                                                            actor.ActorActive.nation_id == actor.Nation.id).order_by(
            actor.Actor.id, actor.Nation.id).all()

    def join_actor_all(sess: Session) -> List[actor.ActorJointReq]:
        return sess.query(actor.Actor, actor.Nation, actor.Instrument,
                          actor.Gender).join(actor.Nation).join(
            actor.Instrument).join(actor.Gender).order_by(actor.Actor.id).all()
