 # test_detect_lowercase_words.py
 
from detect_lowercase_words import detect_lowercase_words
from unittest.mock import patch
import io

def test_detect_lowercase_words():
    """Test the detect_lowercase_words function"""
    # Simulate user input
    user_inputs = ["word", "California", "hello", "Python", "exit"]
    expected_output = "word detected\nhello detected\n"
    
    with patch('builtins.input', side_effect=user_inputs):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            detect_lowercase_words()
            output = mock_stdout.getvalue()
            assert "word detected" in output
            assert "hello detected" in output
            assert "California" not in output
            assert "Python" not in output