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

EDUCATION ENTRY LAYOUT (each cert on its own line):
\\noindent{\\textbf{Certification Name}}\\hfill{Date}\\\\

SKILLS LAYOUT:
\\textit{Label:} content text

BULLETS:
- Use \\textbullet as the bullet marker
- itemsep=2pt, parsep=0pt, topsep=3pt, leftmargin=1.5em

SECTION HEADERS:
- Each section header is bold and centered — NO horizontal rule, no titlerule, no underline.
- Use this pattern for every section:
  \\section*{Section Name}
- Define \\section* with titlesec to be centered bold only — do NOT add any \\titlerule or rule below it.

EXPERIENCE ENTRY LAYOUT (use this exact pattern for every job):
\\vspace{18pt}
\\needspace{8\\baselineskip}
\\noindent{\\textbf{Company Name}}\\hfill{Dates}\\\\
{\\textit{Job Title}}\\hfill{Location}\\\\
\\begin{itemize}...\\end{itemize}
\\goodbreak

CRITICAL SPACING RULES:
- The \\vspace{18pt} creates two clear lines of breathing room ABOVE the company name (between jobs).
- After the Location line use \\\\ with NO extra points — just a plain line break, no \\\\[Xpt].
- The itemize topsep must be 0pt so the first bullet sits tight under the job title line.
- After \\end{itemize} place \\goodbreak — this signals to LaTeX that breaking the page HERE
  (between jobs) is preferred over breaking mid-job. This is how we minimize mid-block breaks.

BULLETS:
- Use \\textbullet as the bullet marker
- itemsep=2pt, parsep=0pt, topsep=0pt, partopsep=0pt, leftmargin=1.5em

PAGE BREAK RULES:
- \\needspace{8\\baselineskip} before each job entry keeps company name + title + first 2 bullets together.
- Before every \\section* use \\needspace{10\\baselineskip} so the section header never lands
  at the bottom of a page without at least some of its content following it.
- \\goodbreak after every \\end{itemize} encourages breaks between jobs, not inside them.

NO HORIZONTAL RULES:
- Do NOT use \\titlerule, \\hrule, \\rule, or any horizontal line anywhere in the document.
- Ignore any --- lines in the markdown source — do not render them as rules.
- Section headers are plain bold centered text only, with no decorative lines.

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
