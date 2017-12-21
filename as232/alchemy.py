from datetime import datetime, date


from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

from hornstone.alchemy import compile_query
from hornstone.alchemy import SerialBase, TimeStampMixin
    

class AnnexKeyMixin(SerialBase):
    @property
    def dirname_lower(self):
        return os.path.join(self.hashdirlower, self.key)
    @property
    def filename_lower(self):
        return os.path.join(self.hashdirlower, self.key, self.key)
    @property
    def dirname_mixed(self):
        return os.path.join(self.hashdirmixed, self.key)
    @property
    def filename_mixed(self):
        return os.path.join(self.hashdirmixed, self.key, self.key)
    
    
def _make_db_session(dburl, create_all=False, baseclass=None):
    settings = {'sqlalchemy.url' : dburl}
    engine = engine_from_config(settings)
    if create_all:
        baseclass.metadata.create_all(engine)
    session_class = sessionmaker()
    session_class.configure(bind=engine)
    return session_class

def make_sqlite_session(filename=None, create_all=False, baseclass=None):
    dburl = "sqlite://"
    if filename is not None:
        dburl = "sqlite:///%s" % filename
    return _make_db_session(dburl, create_all=create_all,
                            baseclass=baseclass)

def make_postgresql_session(dburl, create_all=False, baseclass=None):
    return _make_db_session(dburl, create_all=create_all,
                            baseclass=baseclass)

