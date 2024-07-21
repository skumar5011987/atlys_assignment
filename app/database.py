from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "sqlite:///./atlys.db"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(String,)
    image_url = Column(String, unique=True)
    path_to_image = Column(String, nullable=True)

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency for database session management
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
