#!/usr/bin/env bash
set -e

# 1. Git identity (wiped on logout)
git config --global user.name "Ayande Wuese Joy"
git config --global user.email "your-github-email@example.com"

# 2. Install uv if missing
if ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi
source "$HOME/.local/bin/env"

# 3. Clone YOUR fork (blobless) if missing
cd ~
if [ ! -d ai-engineering-from-scratch ]; then
  git clone --filter=blob:none https://github.com/YOUR-USERNAME/ai-engineering-from-scratch.git
fi
cd ai-engineering-from-scratch

# 4. Connect upstream if missing, and switch to your branch
git remote get-url upstream >/dev/null 2>&1 || \
  git remote add upstream https://github.com/rohitg00/ai-engineering-from-scratch.git
git checkout my-progress

# 5. Python environment
if [ ! -d .venv ]; then
  uv venv
fi
uv pip install numpy matplotlib

echo ""
echo "Setup done. Now run in your terminal:"
echo "  source \$HOME/.local/bin/env"
echo "  cd ~/ai-engineering-from-scratch && source .venv/bin/activate"

