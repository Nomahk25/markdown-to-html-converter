# 🔄 Markdown to HTML Converter (Python CLI)

A simple Python script that converts basic **Markdown (.md)** files into **HTML (.html)** format.  
Supports headings, bold, italic, lists, and paragraphs.

---

## ✨ Features

- Converts:
  - `#`, `##`, `###` headings → `<h1>`, `<h2>`, `<h3>`
  - `**bold**` → `<b>`
  - `*italic*` → `<i>`
  - `- list item` → `<ul><li>`
  - Plain text → `<p>`
- Auto-wraps HTML in `<html><body>...</body></html>`
- CLI-based and easy to use

---

## 🚀 How to Use

### 1. Save the Script

Save the file as `converter.py`.

### 2. Prepare Your Markdown File

Create a simple `input.md` file with content like:

```markdown
# My Title
Some *italic* and **bold** text.

## Subheading

- Item 1
- Item 2
```
---

### 3. Run the Converter

python converter.py input.md output.html
You’ll get a output.html file with formatted HTML.

---

📁 Example Output

```
<html>
<body>
<h1>My Title</h1>
<p>Some <i>italic</i> and <b>bold</b> text.</p>
<h2>Subheading</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
</body>
</html>
```

---

🔧 Requirements

Python 3.x
No external libraries needed

---

📦 File Structure

markdown-to-html/
│
├── converter.py        # Main script
├── input.md            # Sample markdown input
├── output.html         # Generated HTML file
└── README.md

---

🛠 Limitations

Basic support only (no nested lists or advanced formatting)
Simplified bold/italic handling
Does not handle code blocks, links, or images

---

📄 License
Open-source under the MIT License.

---

🙋 Author
Created by Nomanguni Khumalo
Simple tools for clean results.
