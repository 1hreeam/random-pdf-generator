from markdown_pdf import MarkdownPdf, Section
from faker import Faker
from random import randint
from pathlib import Path

def generate_pdf(length: int, sections=1, locale="en_US"):
    f = Faker(locale)
    pdf = MarkdownPdf(optimize=True, toc_level=0)

    author = f.name()
    title = f.sentence(2, True)[:-1]
    
    pdf.add_section(Section(f"# {title}\n {author}", toc=False))
    for i in range(sections):
        s_length = randint(5,length)
        pdf.add_section(Section(f"## {f.sentence(3, True)[:-1]}\n {f.text(s_length)}"))
        length = length - s_length
        if length <= 0:
            break

    output_path = Path(__file__).resolve().parent / "output" / f"{title}.pdf"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.save(str(output_path))
    print("Document saved ✅")