# Message Encoder & Decoder

This Python script can **encode** and **decode** a given message by rearranging characters and adding random letters for obfuscation.

## Features
- Splits the input message into words.
- **Encoding mode (`codin=True`)**:
  - For words with length ≥ 3:
    - Adds 3 random letters at the start and 3 random letters at the end.
    - Moves the first letter of the word to the end.
  - For words with length < 3:
    - Simply reverses the word.
- **Decoding mode (`codin=False`)**:
  - For words with length ≥ 3:
    - Removes the first and last 3 characters (random letters).
    - Moves the last letter back to the start.
  - For words with length < 3:
    - Reverses the word back to original.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/username/repo-name.git
   ```
2. Run the script:
   ```bash
   python script.py
   ```
3. Enter a message when prompted.
4. Set the `codin` variable in the code to:
   - `True` for encoding.
   - `False` for decoding.

## Example
### Encoding:
Input:
```
hello world
```
Output (example):
```
AbXellohYz PdQorldwLmN
```

### Decoding:
Input:
```
AbXellohYz PdQorldwLmN
```
Output:
```
hello world
```

## Requirements
- Python 3.x

## Note
Since random letters are generated during encoding, every encoded result will be different even for the same input message.

