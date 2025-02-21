from sqlmodel import SQLModel, create_engine

# Define your database URL
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)

# Drop all tables (WARNING: This deletes all data!)
SQLModel.metadata.drop_all(engine)

# Recreate all tables
SQLModel.metadata.create_all(engine)

print("Database reset successfully!")
