from generate import generate_pdf
import click
from pathlib import Path

@click.command()
@click.argument('length', type=click.IntRange(5))

@click.option('--count', default=1, type=click.IntRange(1), show_default=True,
              help='Number of PDF files to create.')

@click.option('--sections', default=1, type=click.IntRange(1), show_default=True,
              help='Number of sections in each PDF.')

@click.option('--locale', type=str, 
              help='Locale used for generated names and text.')

@click.option('--output-dir', type=click.Path(file_okay=False, path_type=Path),
              help='Directory where PDF files are saved.')

@click.option('--seed', type=int,
              help='Seed for reproducible generated content.')

def gen(length, count, sections, locale, output_dir, seed):
    """Generate random PDF files.

    LENGTH is the approximate amount of text in each file.
    """
    if sections > length // 5:
        raise click.BadParameter(
            'length must allow at least 5 characters per section',
            param_hint='--sections',
        )

    for index in range(count):
        document_seed = seed + index if seed is not None else None
        generate_pdf(length, sections, locale, output_dir, document_seed)

if (__name__ == "__main__"):
    gen()