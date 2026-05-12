# Zootopia API Project

This project generates an animal website using data from the API Ninjas Animals API.

The user enters the name of an animal, the program fetches the data from the API, and automatically generates an HTML website displaying information about the animal.

## Features

- Fetch animal data from an API
- Generate a dynamic HTML website
- Handle missing animals with an error message
- Use environment variables with dotenv
- Multi-file project architecture

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python animals_web_generator.py
```

Enter the name of an animal when prompted.

The program will generate an `animals.html` file.

## Technologies

- Python
- Requests
- Dotenv
- HTML

## Project Structure

```text
animals_web_generator.py -> website generator
data_fetcher.py -> API communication
requirements.txt -> project dependencies
.env -> environment variables
```

## Author

Derya Sarikaya