#!/bin/bash

echo "🗄️  Setting up PostgreSQL Database for Accessibility Learning Hub"
echo "================================================================"
echo ""

# Check if PostgreSQL is installed (check both PATH and Homebrew location)
PSQL_CMD=""

if command -v psql &> /dev/null; then
    PSQL_CMD="psql"
    echo "✅ PostgreSQL is installed (in PATH)"
elif [ -f "/opt/homebrew/opt/postgresql@15/bin/psql" ]; then
    PSQL_CMD="/opt/homebrew/opt/postgresql@15/bin/psql"
    echo "✅ PostgreSQL is installed (Homebrew keg-only)"
    export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"
elif [ -f "/usr/local/opt/postgresql@15/bin/psql" ]; then
    PSQL_CMD="/usr/local/opt/postgresql@15/bin/psql"
    echo "✅ PostgreSQL is installed (Homebrew keg-only - Intel)"
    export PATH="/usr/local/opt/postgresql@15/bin:$PATH"
else
    echo "❌ PostgreSQL is not installed!"
    echo ""
    echo "To install PostgreSQL on macOS:"
    echo "  brew install postgresql@15"
    echo "  brew services start postgresql@15"
    echo ""
    echo "To install on Ubuntu/Debian:"
    echo "  sudo apt update"
    echo "  sudo apt install postgresql postgresql-contrib"
    echo "  sudo systemctl start postgresql"
    echo ""
    exit 1
fi

echo ""

# Database configuration
DB_NAME="skillsetai_db"
DB_USER="${DB_USER:-postgres}"
DB_PASSWORD="${DB_PASSWORD:-}"
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"

echo "📋 Database Configuration:"
echo "  Database: $DB_NAME"
echo "  User: $DB_USER"
echo "  Host: $DB_HOST"
echo "  Port: $DB_PORT"
echo ""

# Create database
echo "🔨 Creating database..."
if [ -z "$DB_PASSWORD" ]; then
    $PSQL_CMD -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -c "CREATE DATABASE $DB_NAME;" 2>/dev/null
else
    PGPASSWORD="$DB_PASSWORD" $PSQL_CMD -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -c "CREATE DATABASE $DB_NAME;" 2>/dev/null
fi

if [ $? -eq 0 ]; then
    echo "✅ Database '$DB_NAME' created successfully!"
else
    echo "⚠️  Database might already exist or check your credentials"
fi

echo ""

# Update .env file
echo "📝 Updating .env file..."
ENV_FILE=".env"

if [ ! -f "$ENV_FILE" ]; then
    touch "$ENV_FILE"
fi

# Build DATABASE_URL
if [ -z "$DB_PASSWORD" ]; then
    DATABASE_URL="postgresql://$DB_USER@$DB_HOST:$DB_PORT/$DB_NAME"
else
    DATABASE_URL="postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"
fi

# Check if DATABASE_URL already exists in .env
if grep -q "DATABASE_URL=" "$ENV_FILE"; then
    # Update existing line
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s|^DATABASE_URL=.*|DATABASE_URL=$DATABASE_URL|" "$ENV_FILE"
    else
        sed -i "s|^DATABASE_URL=.*|DATABASE_URL=$DATABASE_URL|" "$ENV_FILE"
    fi
    echo "✅ Updated DATABASE_URL in .env"
else
    # Add new line
    echo "" >> "$ENV_FILE"
    echo "# PostgreSQL Database" >> "$ENV_FILE"
    echo "DATABASE_URL=$DATABASE_URL" >> "$ENV_FILE"
    echo "✅ Added DATABASE_URL to .env"
fi

echo ""
echo "🔧 Installing Python dependencies..."
pip install psycopg2-binary Flask-SQLAlchemy Flask-Migrate

echo ""
echo "🏗️  Initializing database tables..."

# Create Python script to initialize database
python3 << 'EOF'
from app import create_app
from models import db

app = create_app()
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
EOF

echo ""
echo "================================================================"
echo "✅ PostgreSQL Database Setup Complete!"
echo ""
echo "📊 Database Connection String:"
echo "   $DATABASE_URL"
echo ""
echo "🚀 Next Steps:"
echo "   1. Start your Flask backend: python app.py"
echo "   2. The database will be ready to use!"
echo ""
echo "💡 Useful Commands:"
echo "   Connect to database: psql -U $DB_USER -d $DB_NAME"
echo "   List tables: \\dt"
echo "   Describe table: \\d table_name"
echo "================================================================"
