# Translation Tool

## Overview
The Translation Tool is a user-friendly application designed to facilitate language translation. Inspired by the cozy aesthetics of Studio Ghibli, this tool provides a visually appealing interface for users to input text and select languages for translation.

## Project Structure
```
translation-tool
├── src
│   ├── main.py          # Entry point of the application
│   ├── translator.py    # Functions to interact with the translation API
│   └── ui
│       ├── __init__.py  # Marks the ui directory as a package
│       └── interface.py  # Defines the user interface components
├── templates
│   ├── layout.html      # HTML structure for the user interface
│   └── style.css        # CSS styles for the user interface
├── tests
│   ├── __init__.py      # Marks the tests directory as a package
│   └── test_translator.py # Unit tests for the translator functions
├── data
│   ├── languages.json   # List of supported languages
│   └── context.txt      # Tracks changes made to the project
├── requirements.txt      # Lists project dependencies
├── .gitignore            # Specifies files to ignore by Git
└── README.md             # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd translation-tool
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Contribution Guidelines
- Fork the repository and create a new branch for your feature or bug fix.
- Ensure that your code adheres to the project's coding standards.
- Write unit tests for any new functionality.
- Submit a pull request with a clear description of your changes.

## Maintaining `context.txt`
To track changes made to the project, please follow these instructions:
- For each significant change, add a new entry to `context.txt` with the following format:
  ```
  [Date] - [Description of the change] - [Author]
  ```
- Ensure that the entries are clear and concise for future reference.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.