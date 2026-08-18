# Random PDF Generator

Generate PDF files with random names and text.

## Installation

```bash
git clone https://github.com/1hreeam/random-pdf-generator.git
cd random-pdf-generator
python -m pip install -r requirements.txt
```

To install the script as a command, run:

```bash
python -m pip install .
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
- `--output-dir DIRECTORY`: Directory where PDF files are saved.
- `--seed INTEGER`: Seed for reproducible generated content.
- `--help`: Show the help message.

Examples:

```bash
python main.py 3000
python main.py 3000 --count 3 --sections 2
python main.py 3000 --locale en_US
python main.py 3000 --output-dir ./pdfs --seed 7
```

Files are saved in the `output` directory by default.

To run the tests:

```bash
python -m pytest -q
```

## Development

The following improvements are implemented:

- Input validation for length and sections.
- Safe and unique generated filenames.
- Custom output directory with `--output-dir`.
- Reproducible output with `--seed`.
- Pinned dependencies.
- Tests and continuous integration.
- Installation as a command.

### Future Ideas

- Add more PDF templates and content styles.
- Add support for custom fonts and themes.
- Add an option to generate content with an AI service.
