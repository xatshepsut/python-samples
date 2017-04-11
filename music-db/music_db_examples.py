import datetime

import sqlalchemy as sql
from sqlalchemy import Column, \
    String, Integer, Date, \
    ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = sql.create_engine("sqlite:///music.db", echo=True)
Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    release_date = Column(Date)
    tracks_number = Column(Integer)

    artist_id = Column(Integer, ForeignKey("artists.id"))
    artist = relationship("Artist", backref=backref("albums", order_by=id))

    def __init__(self, title, genre, release_date, tracks_number):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.tracks_number = tracks_number


Base.metadata.create_all(engine)


# Session = sqlalchemy.orm.sessionmaker(bind=engine)
# session = Session()
#
# # Create an artist
# new_artist = Artist("Newsboys")
# new_artist.albums = [Album("Read All About It", "unknown", datetime.date(1988, 12, 01), 12)]
#
# more_albums = [Album("Hell Is for Wimps", "unknown", datetime.date(1990, 07, 31), 12),
#                Album("Love Liberty Disco", "unknown", datetime.date(1999, 11, 16), 12),
#                Album("Thrive", "unknown", datetime.date(2002, 03, 26), 12)]
# new_artist.albums.extend(more_albums)
#
# session.add(new_artist)
# session.commit()
#
# session.add_all([
#     Artist("MXPX"),
#     Artist("Kutless"),
#     Artist("Thousand Foot Krutch")
#     ])
# session.commit()
#
# bred = Artist("Bred")
# bred.albums.append(more_albums[1])
# session.commit()
#
# bred2 = Artist("Bred2")
# bred2.albums.append(more_albums[1])
# session.commit()


# Session = sqlalchemy.orm.sessionmaker(bind=engine)
# session = Session()
#
# artist = session.query(Artist).filter(Artist.name=="Bred2").first()
# if artist is not None:
#     print artist.name
#     artist.name = "Bob"
#     session.commit()
#
#
# artist, album = session.query(Artist, Album).filter(Artist.id==Album.artist_id).filter(Album.title=="Love Liberty Disco").first()
# print artist.name
# print album.title

Session = sql.orm.sessionmaker(bind=engine)
session = Session()

artist = session.query(Artist).filter(Artist.name=="Bob").first()
session.delete(artist)
session.rollback()
session.commit()


result = session.query(Artist).order_by(Artist.name).all()
for artist in result:
    print artist.name

try:
    res = session.query(Artist).filter(Artist.name.like("B%n")).one()
    print res.name
except sql.orm.exc.NoResultFound:
    print "No results!!!"

query = session.query(Artist, Album).filter(Artist.id==Album.artist_id)
art, album = query.filter(Artist.name.like("%")).first()
print art.name