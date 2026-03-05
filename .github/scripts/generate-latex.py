#!/usr/bin/env python3
import os
import sys
import anthropic

# Load .env file if present (local development)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

STYLE_INSTRUCTIONS = """
You are a LaTeX expert. Convert the resume markdown below into a complete, compilable LaTeX document.

STRICT FORMATTING REQUIREMENTS:
- Font: Times New Roman via \\usepackage{mathptmx}
- Document class: \\documentclass[11pt,letterpaper]{article}
- Margins: top=0.5in, bottom=0.5in, left=0.75in, right=0.75in
- No page numbers (\\pagestyle{empty})
- No paragraph indentation

FONT SIZES:
- Candidate name: \\Large\\bfseries, centered
- Contact line: \\normalsize, centered
- Section headers: \\normalsize\\bfseries, centered
- Company names and certification names: \\normalsize\\bfseries (same as body but bold)
- Job titles: \\normalsize\\itshape
- Bullet text: \\normalsize (11pt)

SECTION HEADERS:
- Each section header is bold, centered, with a full-width rule immediately below it
- Use this pattern for every section:
  \\section*{Section Name}
- Define \\section* with titlesec to be centered bold with a rule below

EXPERIENCE ENTRY LAYOUT (use this exact pattern for every job):
\\vspace{12pt}
\\needspace{6\\baselineskip}
\\noindent{\\textbf{Company Name}}\\hfill{Dates}\\\\
{\\textit{Job Title}}\\hfill{Location}\\\\[2pt]
\\begin{itemize}...\\end{itemize}

The \\vspace{12pt} MUST appear before every company name, including the first one in a section.
This creates two clear lines of breathing room between the bullet list above and the next company name.

EDUCATION ENTRY LAYOUT (each cert on its own line):
\\noindent{\\textbf{Certification Name}}\\hfill{Date}\\\\

SKILLS LAYOUT:
\\textit{Label:} content text

BULLETS:
- Use \\textbullet as the bullet marker
- itemsep=2pt, parsep=0pt, topsep=3pt, leftmargin=1.5em

PAGE BREAK RULES:
- The \\needspace{6\\baselineskip} before each job entry prevents orphaned company names
- Section headers (\\section*) must also have extra space before them when following a bullet list
- Add \\vspace{12pt} before every \\section* call so sections never feel glued to the content above

HORIZONTAL RULES between sections:
- The rule comes from the section header formatting, not from \\hrule or --- in markdown
- Ignore any --- lines in the markdown; they are not separators in the output

Return ONLY the raw LaTeX source. No explanation. No markdown code fences. No triple backticks.
"""

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    md_path = "resume/main/resume.md"
    if not os.path.exists(md_path):
        print(f"ERROR: Resume file not found at {md_path}", file=sys.stderr)
        sys.exit(1)

    with open(md_path, "r") as f:
        markdown_content = f.read()

    client = anthropic.Anthropic(api_key=api_key)

    print("Calling Claude API to generate LaTeX...")
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f"{STYLE_INSTRUCTIONS}\n\nRESUME MARKDOWN:\n{markdown_content}",
            }
        ],
    )

    latex = message.content[0].text.strip()

    # Strip markdown code fences if Claude wrapped the output
    if latex.startswith("```"):
        lines = latex.splitlines()
        # Drop first line (```latex or ```) and last line (```)
        latex = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

    os.makedirs("build", exist_ok=True)
    out_path = "build/resume.tex"
    with open(out_path, "w") as f:
        f.write(latex)

    print(f"LaTeX written to {out_path}")


if __name__ == "__main__":
    main()
