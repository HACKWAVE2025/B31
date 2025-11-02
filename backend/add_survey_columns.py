#!/usr/bin/env python3
"""
Add survey columns to users table
"""

import psycopg2
import os

# Database connection
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/skillsetai_db')

try:
    # Parse DATABASE_URL
    if DATABASE_URL.startswith('postgresql://'):
        # For local development
        dbname = DATABASE_URL.split('/')[-1]
        conn = psycopg2.connect(
            dbname=dbname,
            user=os.getenv('DB_USER', 'postgres'),
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432')
        )
    else:
        conn = psycopg2.connect(DATABASE_URL)
    
    cursor = conn.cursor()
    
    # Check if columns exist
    cursor.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = 'users' 
        AND column_name IN ('survey_data', 'survey_completed');
    """)
    
    existing_columns = [row[0] for row in cursor.fetchall()]
    print(f"Existing survey columns: {existing_columns}")
    
    # Add survey_data column if missing
    if 'survey_data' not in existing_columns:
        print("Adding survey_data column...")
        cursor.execute("ALTER TABLE users ADD COLUMN survey_data JSON;")
        print("✅ survey_data column added")
    else:
        print("✓ survey_data column already exists")
    
    # Add survey_completed column if missing
    if 'survey_completed' not in existing_columns:
        print("Adding survey_completed column...")
        cursor.execute("ALTER TABLE users ADD COLUMN survey_completed BOOLEAN DEFAULT FALSE;")
        print("✅ survey_completed column added")
    else:
        print("✓ survey_completed column already exists")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print("\n✅ Migration complete!")
    
except Exception as e:
    print(f"❌ Migration failed: {e}")
    import traceback
    traceback.print_exc()
