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
7. Importing the package
```
from pkgUdit import generatePass
```

# Publishing the Package
To publish the package to PyPI, follow these steps:

Ensure you are in the root directory of the password-generator project.

Manually trigger the GitHub Actions workflow to publish the package. To do this:

* Go to the "Actions" tab in your GitHub repository.
* Click on the "Publish Package" under "All workflows."
* Click on the "Run workflow" button.
* You will be prompted to enter the new package version.

The GitHub Actions workflow will then automatically update the package version in the version.py file, build the distribution, and publish the package to PyPI with the specified version.