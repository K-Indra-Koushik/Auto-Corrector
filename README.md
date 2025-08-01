# Auto-Corrector

A Python-based autocorrect application that helps correct spelling mistakes in text. This project includes both a command-line interface and a web-based Streamlit application.

## Features

- **Command Line Interface**: Simple text input and correction
- **Web Interface**: Modern Streamlit web application with a user-friendly interface
- **Real-time Correction**: Instant spelling correction using the pyspellchecker library
- **Side-by-side Comparison**: View original and corrected text simultaneously

## Installation

1. Clone the repository:
```bash
git clone https://github.com/K-Indra-Koushik/Auto-Corrector.git
cd Auto-Corrector
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Run the command-line version:
```bash
python autocorrect.py
```

Enter your text when prompted and see the corrected version.

### Web Interface (Streamlit)

Run the Streamlit web application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Features of the Web Interface

- **Modern UI**: Clean and intuitive interface
- **Text Area**: Large text input area for easy text entry
- **Real-time Processing**: Shows a loading spinner during correction
- **Side-by-side Display**: Compare original and corrected text
- **Responsive Design**: Works on different screen sizes

## Dependencies

- `pyspellchecker`: For spell checking and correction
- `streamlit`: For the web interface

## Project Structure

```
Auto-Corrector/
├── autocorrect.py      # Command-line version
├── app.py             # Streamlit web application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## How it Works

The application uses the `pyspellchecker` library to:
1. Split input text into words
2. Clean each word by removing punctuation
3. Check for spelling errors
4. Suggest corrections using the library's correction algorithm
5. Return the corrected text

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
