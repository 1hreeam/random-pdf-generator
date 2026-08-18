from markdown_pdf import MarkdownPdf, Section
from faker import Faker
from pathlib import Path
from random import Random
import re

_WINDOWS_RESERVED_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{index}" for index in range(1, 10)),
    *(f"LPT{index}" for index in range(1, 10)),
}


def _safe_filename(title: str) -> str:
    filename = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", title).strip(" .")
    if not filename:
        return "document"
    if filename.upper() in _WINDOWS_RESERVED_NAMES:
        return f"_{filename}"
    return filename


def _unique_path(output_dir: Path, filename: str) -> Path:
    output_path = output_dir / f"{filename}.pdf"
    suffix = 1
    while output_path.exists():
        output_path = output_dir / f"{filename}-{suffix}.pdf"
        suffix += 1
    return output_path


def generate_pdf(
    length: int,
    sections: int = 1,
    locale: str = "en_US",
    output_dir: Path | str | None = None,
    seed: int | None = None,
) -> Path:
    if length < 5:
        raise ValueError("length must be at least 5")
    if sections < 1:
        raise ValueError("sections must be at least 1")
    if sections > length // 5:
        raise ValueError("length must allow at least 5 characters per section")

    random = Random(seed)
    f = Faker(locale)
    if seed is not None:
        f.seed_instance(seed)
    pdf = MarkdownPdf(optimize=True, toc_level=0)

    author = f.name()
    title = f.sentence(2, True)[:-1]
    
    pdf.add_section(Section(f"# {title}\n {author}", toc=False))
    for section_index in range(sections):
        remaining_sections = sections - section_index - 1
        max_length = length - (remaining_sections * 5)
        s_length = random.randint(5, max_length)
        pdf.add_section(Section(f"## {f.sentence(3, True)[:-1]}\n {f.text(s_length)}"))
        length = length - s_length

    output_root = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "output"
    output_root = output_root.expanduser().resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    output_path = _unique_path(output_root, _safe_filename(title))
    pdf.save(str(output_path))
    print(f"Document saved: {output_path}")
    return output_path