import os
import pytest
from main import generate_qr_code

def test_generate_qr_code():
    # Create a test directory
    test_dir = "test_qr_codes"
    test_filename = "test_qr.png"
    
    # Generate a QR code for testing
    path = generate_qr_code(
        "https://github.com/sowmika-avula", 
        output_dir=test_dir,
        filename=test_filename
    )
    
    # Check if the file was created
    assert os.path.exists(path)
    assert path.endswith(test_filename)
    
    # Clean up after test
    if os.path.exists(path):
        os.remove(path)
    if os.path.exists(test_dir):
        os.rmdir(test_dir)
        