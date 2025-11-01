#!/bin/bash

echo "=== Accessibility Learning Hub Backend - Testing Suite ==="
echo ""
echo "Testing Server Health..."
curl -s http://localhost:5001/api/health | python3 -m json.tool

echo ""
echo ""
echo "Testing Text Simplification..."
curl -s -X POST http://localhost:5001/api/accessibility/simplify-text \
  -H "Content-Type: application/json" \
  -d '{"text": "The mitochondria is the powerhouse of the cell that produces energy through cellular respiration."}' \
  | python3 -m json.tool

echo ""
echo ""
echo "Testing Available TTS Voices..."
curl -s http://localhost:5001/api/accessibility/available-voices | python3 -m json.tool

echo ""
echo ""
echo "=== Tests Complete ==="
