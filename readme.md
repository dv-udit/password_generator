# Password Generator

This is a simple password generator that generates a random password of length between 6 to 12 characters. The generated password will always contain at least one uppercase letter, one lowercase letter, and one number.

## Features

- Generates a random password with the specified criteria.
- Checks if the generated password is already present in a CSV file to prevent Dictionary attacks.

## Getting Started

Follow the steps below to set up and run the password generator:

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/password-generator.git

2. Navigate to the project directory
```bash
cd password-generator
 ```


3. Create a virtual environment
```
python -m venv venv
```
4. Activate the virtual environment
#### On Windows
```
venv\Scripts\activate
```
5. On macOS/Linux
```
source venv/bin/activate
```
6. Install the Package
```
pip install pkgUdit
```
7. from pkgUdit import generatePass