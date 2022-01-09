# Weird Text

![Lint](https://github.com/stsdc/weird-text/actions/workflows/pylint.yml/badge.svg)
![Lint](https://github.com/stsdc/weird-text/actions/workflows/pytest.yml/badge.svg)


#### Weird Text will encode and decode text preserving all formatting and punctuation.

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt # for development purposes only
```

## Usage

```python
from encoder import Encoder
from decoder import Decoder

if __name__ == '__main__':
    encoder = Encoder()

    ENCODED_TEXT = encoder.encode('''
    Lorem Ipsum is simply dummy text of 
    the printing and typesetting industry.
    ''')

    print(ENCODED_TEXT)
    print(encoder.word_list)

    decoder = Decoder(encoder.word_list)

    decoded_text = decoder.decode(ENCODED_TEXT)
    print(decoded_text)
```

## Tests

Run the tests: 

```bash
pytest ./test_*
```

## Linting

```bash
pylint *.py
```