from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, JSON

Base = declarative_base()


class Projects(Base):
    __tablename__ = 'projects'
    id = Column(String, primary_key=True)
    name = Column(String)


class ProjectDocuments(Base):
    __tablename__ = 'project_documents'
    _dummy = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    document_id = Column(String)


class PreparedStatements(Base):
    __tablename__ = 'prepared_statements'
    _dummy = Column(Integer, primary_key=True)
    document_id = Column(String)
    reader = Column(String)
    reader_version = Column(String)
    indra_version = Column(String)
    stmt = Column(JSON)


class Curations(Base):
    __tablename__ = 'curations'
    _dummy = Column(Integer, primary_key=True)
    project_id = Column(String)
    curation = Column(JSON)