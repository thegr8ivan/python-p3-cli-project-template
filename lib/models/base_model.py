from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///teketeke.db"

# Initialize the base for ORM models
Base = declarative_base()

# Create engine and session
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialize the database by importing all model modules.
    This function will create all tables if they do not exist yet.
    """
    # Import models to register them with the Base
    import lib.models.customer  
    import lib.models.order
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
