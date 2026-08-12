from markdown_pdf import MarkdownPdf, Section
import time as t

def generate_pdf(markdown_text):
    print("Generating PDF docunent...")
    t.sleep(1)

    pdf = MarkdownPdf(optimize=True)
    pdf.add_section(Section("# Lorem Ipsum\n", toc=False))
    pdf.add_section(Section(markdown_text))

    try:
        pdf.save("./output/file1.pdf")
        print("Document saved ✅")
    except:
        print("Task Failed")



