# Tone Teller

Tone Teller is a web application that performs sentiment analysis on user-provided text in real-time using the Transformers library by Hugging Face. The app is built with Flask, a Python web framework, and utilises jQuery for handling user input and updating the results dynamically.

## Features

- Real-time sentiment analysis of user-provided text
- Utilises the Transformers library for accurate sentiment analysis
- Simple and intuitive user interface
- Displays the sentiment label and confidence score

## Requirements

- Python 3.6 or higher
- Flask
- Transformers

## Installation

1. Clone the repository:

```
git clone https://github.com/stephen-a-nicholson/tone-teller.git
```

2. Navigate to the project directory:

```
cd tone-teller
```

3. Install Poetry if you haven't already:

```
pip install poetry
```

4. Install the project dependencies using Poetry:

```
poetry install
```

## Usage

1. Activate the Poetry virtual environment:

```
poetry shell
```

2. Run the Flask application:

```
python app.py
```

3. Open your web browser and navigate to `http://localhost:5000`.

4. Type or paste the text you want to analyse in the provided text area.

5. The sentiment analysis results will be displayed in real-time below the text area, showing the sentiment label (e.g., "POSITIVE" or "NEGATIVE") and the confidence score.

## How it Works

- The web app is built using Flask, which handles the routing and rendering of the HTML template.
- The HTML template contains a text area where the user can input their text.
- jQuery is used to listen for changes in the text area and send an AJAX request to the Flask backend with the user's input.
- The Flask backend receives the user's text and passes it through the sentiment analysis pipeline from the Transformers library.
- The sentiment analysis results are then sent back to the frontend as a JSON response.
- jQuery updates the HTML with the received sentiment label and confidence score, providing real-time feedback to the user.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Licence

This project is licensed under the MIT Licence. See the [LICENCE](LICENCE) file for details.