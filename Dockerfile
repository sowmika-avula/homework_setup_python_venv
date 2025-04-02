FROM python:3.12.3

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Create a directory for the QR codes
RUN mkdir -p qr_codes

# Set environment variables with default values
ENV QR_DATA_URL=https://github.com/sowmika-avula
ENV QR_CODE_DIR=qr_codes
ENV QR_CODE_FILENAME=github_qr.png
ENV FILL_COLOR=black
ENV BACK_COLOR=white

# Run the application
CMD ["python", "main.py"]
