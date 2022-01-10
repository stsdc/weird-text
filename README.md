# Weird Text

![Lint](https://github.com/stsdc/weird-text/actions/workflows/pylint.yml/badge.svg)
![Lint](https://github.com/stsdc/weird-text/actions/workflows/pytest.yml/badge.svg)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


#### Weird Text will encode and decode text preserving all formatting and punctuation.

**Check Frontend at: https://kkjijk-fe.herokuapp.com/**

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt # for development purposes only
```

## Usage

### Directly in code

Run `./example.py`:

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

    decoder = Decoder()
    decoder.word_list = encoder.word_list

    decoded_text = decoder.decode(ENCODED_TEXT)
    print(decoded_text)
```

### As API requests

You may try and test using this URL:

* https://kkjijk.herokuapp.com/v1/encode
* https://kkjijk.herokuapp.com/v1/decode

#### Create a POST request to `/v1/encode` with the text to encode:

```json
{
    "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
}
```
It will return the encoded text:

```json
{
    "encoded_text": "\n-weird-\noremL mIups si ilmyps mdmyu ttxe fo het ringntpi nad tepgnesytti tsirduyn.\n-weird-\n"
}
```

#### Create a POST request to `/v1/decode` with the text to decode:

```json
{
    "encoded_text": "\n-weird-\noremL mIups si ilmyps mdmyu ttxe fo het ringntpi nad tepgnesytti tsirduyn.\n-weird-\n"
}
```
It will return the encoded text:

```json
{
    "decoded_text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
}
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

## Deploying to Heroku

```bash
$ heroku create
$ git push heroku main
$ heroku open
```

or 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
