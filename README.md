# Count Words

## Overview

This project is a Django web application that allows users to submit text and view the total word count of their submission. The application is built using Django and SQLite3 with Python 3.

## Features

- Submit text through a form.
- Display the total word count of the submitted text.
- Handle form validation and display errors on the same page.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/moreiralucas/count-words.git
   cd count-words
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

   Your application will be available at `http://127.0.0.1:8000/`.

## Usage

1. Navigate to the application's URL in your browser.
2. Enter your text into the form and submit.
3. View the total word count on the same page.

## Requirements

- Python 3.x

Dependencies are listed in `requirements.txt`.
