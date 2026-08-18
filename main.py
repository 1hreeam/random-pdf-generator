from generate import generate_pdf
import click

@click.command()
@click.argument('length', type=click.IntRange(5))

@click.option('--count', default=1, type=click.IntRange(1), show_default=True,
              help='Number of PDF files to create.')

@click.option('--sections', default=1, type=click.IntRange(1), show_default=True,
              help='Number of sections in each PDF.')

@click.option('--locale', type=str, 
              help='Locale used for generated names and text.')

def gen(length, count, sections, locale):
    """Generate random PDF files.

    LENGTH is the approximate amount of text in each file.
    """
    for i in range(0, count):
        generate_pdf(length, sections, locale)

if (__name__ == "__main__"):
    gen()