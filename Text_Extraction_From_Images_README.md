
# Text Extraction From Images Application

This project is a Python-based application designed to extract text from images using Optical Character Recognition (OCR) techniques. The application is suitable for a wide range of use cases, including document digitization, automated data entry, and information retrieval from scanned documents or photos.

## Features

- **Image Upload**: Upload images in various formats (JPG, PNG, etc.) for text extraction.
- **OCR Processing**: Extract text from images using the powerful Tesseract OCR engine.
- **Multiple Language Support**: Supports text extraction in multiple languages.
- **Preprocessing Tools**: Includes image preprocessing features such as noise removal and binarization to enhance OCR accuracy.
- **Output Options**: Save extracted text as plain text or export to formats such as PDF or CSV.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/text-extraction-from-images.git
   cd text-extraction-from-images
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR on your system:
   - **Linux**: `sudo apt-get install tesseract-ocr`
   - **Windows/Mac**: Download and install from [Tesseract's GitHub page](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Start the application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000`.

3. Upload an image and extract text.

## Folder Structure

```
text-extraction-from-images/
├── app.py                # Main application file
├── templates/            # HTML templates for the web interface
├── static/               # Static files (CSS, JavaScript, images)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── example_images/       # Example images for testing
```

## Dependencies

- Python 3.7+
- Flask (for the web interface)
- pytesseract (Python wrapper for Tesseract OCR)
- OpenCV (for image preprocessing)

## Screenshots

### Home Page
![Home Page](static/screenshots/homepage.png)

### Extracted Text
![Extracted Text](static/screenshots/extracted_text.png)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m 'Add a new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for providing the OCR engine.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
