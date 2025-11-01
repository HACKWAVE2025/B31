#!/bin/bash

# Accessibility Learning Hub - Backend Setup Script

echo "🚀 Setting up Accessibility Learning Hub Backend..."

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Download NLP models
echo "🧠 Downloading NLP models..."
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your credentials!"
else
    echo "✅ .env file already exists"
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads
mkdir -p generated
mkdir -p temp
mkdir -p logs

echo ""
echo "✅ Setup complete!"
echo ""
echo "📌 Next steps:"
echo "1. Edit .env file with your Firebase and API credentials"
echo "2. Download Firebase Admin SDK credentials JSON"
echo "3. Run: python app.py"
echo ""
echo "🔗 API will be available at: http://localhost:5000"
echo ""
