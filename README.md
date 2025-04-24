# Calculator Application

A modern calculator application built with FastAPI backend and Gradio frontend.

## Features
- Addition
- Subtraction
- Multiplication
- Division
- Clean and intuitive user interface
- Error handling for invalid operations
- Division by zero protection

## Tech Stack
- Backend: FastAPI
- Frontend: Gradio
- Data Validation: Pydantic
- API Documentation: Swagger UI (automatically generated)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/NikhilSetiya/calculator-app.git
cd calculator-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the backend server:
```bash
python backend.py
```

5. In a new terminal, start the frontend:
```bash
python frontend.py
```

6. Open your web browser and navigate to the URL shown in the Gradio output (typically http://localhost:7860)

## API Documentation
Once the backend server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Usage
1. Enter two numbers in the input fields
2. Select the operation you want to perform
3. Click the "Calculate" button
4. View the result in the output field

## Error Handling
The application handles various error cases:
- Division by zero
- Invalid operations
- Network errors
- Input validation

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is licensed under the MIT License - see the LICENSE file for details. 