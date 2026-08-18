# Random PDF Generator

Generate PDF files with random names and text.

## Installation

```bash
git clone https://github.com/1hreeam/random-pdf-generator.git
cd random-pdf-generator
python -m pip install -r requirements.txt
```

## Usage

Run the script with a required text length:

```bash
python main.py LENGTH [OPTIONS]
```

`LENGTH` must be at least 5. It controls the approximate amount of text in each PDF.

### Options

- `--count INTEGER`: Number of PDF files to create. Default: `1`.
- `--sections INTEGER`: Number of sections in each PDF. Default: `1`.
- `--locale TEXT`: Locale used for generated names and text.
- `--help`: Show the help message.

Examples:

```bash
python main.py 3000
python main.py 3000 --count 3 --sections 2
python main.py 3000 --locale en_US
```

Files are saved in the `output` directory.

## Development

- absolute paths
- AI real pdfs generator
