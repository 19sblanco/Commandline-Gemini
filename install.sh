#!/bin/bash

# Get the absolute path of the directory where this script is living
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo $CURRENT_DIR

echo "Installing in directory: $CURRENT_DIR"

# 2. Update apt and install python3-venv
echo "Updating apt and installing python3-venv..."
sudo apt update
sudo apt install -y python3-venv  

echo "Creating python virtual environment..."
# Create venv inside that current directory
python3 -m venv "$CURRENT_DIR/venv"

# 3. Install rich to display markdown
echo "Installing rich..."
"$CURRENT_DIR/venv/bin/pip" install rich

# 4. Create context.txt file
echo "Creating context.txt..."
touch "$CURRENT_DIR/context.txt"

# 5. Add bash alias to .bashrc dynamically
echo "Adding gemini alias to ~/.bashrc..."

# We wrap the paths in quotes inside the alias just in case your folder path has spaces
ALIAS_CMD="alias gemini='\"$CURRENT_DIR/venv/bin/python\" \"$CURRENT_DIR/gemini.py\"'"

# Check if the alias already exists to avoid adding duplicates if you run the script twice
if grep -q "alias gemini=" ~/.bashrc; then
    echo "Alias 'gemini' already exists in ~/.bashrc. Please remove it manually if you want to update it."
else
    echo "$ALIAS_CMD" >> ~/.bashrc
    echo "Successfully added alias."
fi

echo ""
echo "Setup complete!"
echo "Please run 'source ~/.bashrc' or restart your terminal to use the new 'gemini' alias."

