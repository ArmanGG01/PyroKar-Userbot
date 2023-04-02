# Kata Gua Lu Anjing

from . import BASE, SESSION
from sqlalchemy import Column, Numeric, String, UnicodeText


class Filters(BASE):
    __tablename__ = "filters"
    user_id = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True, nullable=False)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def __init__(self, user_id, chat_id, keyword, reply, f_mesg_id):
        self.user_id = str(user_id)
        self.chat_id = str(chat_id)
        self.keyword = keyword
        self.reply = reply
        self.f_mesg_id = f_mesg_id

    def __eq__(self, other):
        return bool(
            isinstance(other, Filters)
            and self.user_id == other.user_id
            and self.chat_id == other.chat_id
            and self.keyword == other.keyword
        )


Filters.__table__.create(checkfirst=True)


def get_filter(user_id, chat_id, keyword):
    try:
        return SESSION.query(Filters).get((str(user_id), chat_id, keyword))
    finally:
        SESSION.close()


def get_filters(user_id, chat_id):
    try:
        return SESSION.query(Filters).filter(Filters.user_id == str(user_id), Filters.chat_id == str(chat_id)).all()
    finally:
        SESSION.close()


def add_filter(user_id, chat_id, keyword, reply, f_mesg_id):
    lu_babi = get_filter(user_id, chat_id, keyword)
    if not lu_babi:
        bangsat = Filters(str(user_id), chat_id, keyword, reply, f_mesg_id)
        SESSION.add(bangsat)
        SESSION.commit()
        return True
    else:
        onyet = SESSION.query(Filters).get((str(user_id), chat_id, keyword))
        SESSION.delete(onyet)
        SESSION.commit()
        bangsat = Filters(str(user_id), chat_id, keyword, reply, f_mesg_id)
        SESSION.add(bangsat)
        SESSION.commit()
        return False


def remove_filter(user_id, chat_id, keyword):
    tai = get_filter(user_id, chat_id, keyword)
    if not tai:
        return False
    else:
        SESSION.delete(tai)
        SESSION.commit()
        return True
