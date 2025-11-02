"""
Database Migration - Add survey fields to User model
Run this once to update the database schema
"""
from app import create_app, db
from models import User

app = create_app()

with app.app_context():
    # Add new columns to users table if they don't exist
    try:
        from sqlalchemy import text
        
        # Check if columns exist
        result = db.session.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='users' AND column_name IN ('survey_data', 'survey_completed')
        """))
        
        existing_columns = [row[0] for row in result]
        
        # Add survey_data column if missing
        if 'survey_data' not in existing_columns:
            print("Adding survey_data column...")
            db.session.execute(text("""
                ALTER TABLE users 
                ADD COLUMN survey_data JSON
            """))
            db.session.commit()
            print("✅ survey_data column added")
        else:
            print("✓ survey_data column already exists")
        
        # Add survey_completed column if missing
        if 'survey_completed' not in existing_columns:
            print("Adding survey_completed column...")
            db.session.execute(text("""
                ALTER TABLE users 
                ADD COLUMN survey_completed BOOLEAN DEFAULT FALSE
            """))
            db.session.commit()
            print("✅ survey_completed column added")
        else:
            print("✓ survey_completed column already exists")
        
        print("\n🎉 Database migration completed successfully!")
        
    except Exception as e:
        print(f"❌ Migration error: {e}")
        db.session.rollback()
