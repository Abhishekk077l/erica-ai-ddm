#!/bin/bash

# This script installs the Node.js dependencies for the voice processing module.
# It includes workarounds for the uv_cwd error that can occur in some environments.

set -e

# --- Configuration ---
NODE_VERSION_MAJOR=18
NPM_VERSION_MAJOR=8

# --- Helper Functions ---
function info {
  echo "[INFO] $1"
}

function warn {
  echo "[WARN] $1"
}

function error {
  echo "[ERROR] $1" >&2
  exit 1
}

# --- Pre-flight Checks ---
info "Changing to script directory..."
cd "$(dirname "$0")"

info "Checking prerequisites..."

# Check if running as root
if [ "$(id -u)" -eq 0 ]; then
  warn "Running this script as root is not recommended and can cause permission issues."
fi

# Check ownership of ~/.npm directory
if [ -d "$HOME/.npm" ] && [ "$(stat -c '%u' "$HOME/.npm")" -eq 0 ]; then
    warn "The ~/.npm directory is owned by root. This can cause permission issues."
    warn "To fix this, run: sudo chown -R $(whoami) $HOME/.npm"
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
  error "Node.js is not installed. Please install Node.js version $NODE_VERSION_MAJOR or higher."
fi

# Check Node.js version
CURRENT_NODE_VERSION=$(node -v)
CURRENT_NODE_MAJOR=$(echo "$CURRENT_NODE_VERSION" | cut -d'.' -f1 | sed 's/v//')
if [ "$CURRENT_NODE_MAJOR" -lt "$NODE_VERSION_MAJOR" ]; then
  error "Node.js version $CURRENT_NODE_VERSION is not supported. Please install Node.js version $NODE_VERSION_MAJOR or higher."
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
  error "npm is not installed. Please install npm version $NPM_VERSION_MAJOR or higher."
fi

# Check npm version
CURRENT_NPM_VERSION=$(npm -v)
CURRENT_NPM_MAJOR=$(echo "$CURRENT_NPM_VERSION" | cut -d'.' -f1)
if [ "$CURRENT_NPM_MAJOR" -lt "$NPM_VERSION_MAJOR" ]; then
  error "npm version $CURRENT_NPM_VERSION is not supported. Please install npm version $NPM_VERSION_MAJOR or higher."
fi

# Check if package.json exists
if [ ! -f "package.json" ]; then
    error "package.json not found in '$(pwd)'."
fi

# --- Installation ---
info "Starting Node.js dependency installation in '$(pwd)'..."

info "Cleaning installation directory..."
npm cache clean --force
rm -rf node_modules

info "Installing dependencies using npx workaround..."
# Use npx to avoid the uv_cwd error.
# The --yes flag automatically accepts any prompts from npx.
if ! npx --yes npm install; then
  error "npm install failed. Please check the logs for more details."
fi

info "Node.js dependencies installed successfully."
