# ERICA v2.0 - Revolutionary AI Assistant with HRM Integration

This project is the development of ERICA v2.0, a next-generation AI desktop assistant.

## Features

- **HRM (Hierarchical Reasoning Model):** A novel reasoning model designed for high-speed, complex problem-solving, replacing traditional LLMs.
- **Advanced Computer Vision:** A powerful module for universal GUI control across any application.
- **Desktop Assistant Framework:** The core application that integrates the above components and provides a user interface.

## Project Structure

```
.
├── README.md
├── src
│   ├── main.py
│   ├── hrm
│   │   └── __init__.py
│   ├── computer_vision
│   │   └── __init__.py
│   └── voice_processing
│       ├── install_node_deps.sh
│       └── package.json
└── tests
    ├── test_hrm.py
    └── test_computer_vision.py
```

## Voice Processing Module

The voice processing module uses Node.js and requires a separate installation step for its dependencies. The main application will automatically install these dependencies when it is run for the first time.

If you encounter any issues with the Node.js dependency installation, you can run the installation script manually:

```bash
bash src/voice_processing/install_node_deps.sh
```

The script includes checks for common issues, such as incorrect Node.js/npm versions and permission problems.
