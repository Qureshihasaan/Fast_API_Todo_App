from sqlalchemy import create_engine , Column , String , Integer , Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

sql_alchemy = f"postgresql://hasaanqureshi150:Rh1x3yCHvLSr@ep-round-shadow-12558671.us-east-2.aws.neon.tech/neondb?sslmode=require"


enigne = create_engine(sql_alchemy)

Sessionlocal = sessionmaker(autocommit = False , autoflush= False , bind= enigne)

Base = declarative_base()

class Todo_app(Base):
    __tablename__ = "Todo-App"
    id = Column(Integer , primary_key=True , index=True)
    title = Column(String , index= True)
    description = Column(String , index= True)


