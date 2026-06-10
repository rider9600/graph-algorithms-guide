import re

with open('graph.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_vars = """/* ===== CSS VARIABLES ===== */
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f4f4f4;
  --bg-card: #ffffff;
  --bg-card-hover: #fafafa;
  --bg-code: #f8f8f8;
  --border: #cccccc;
  --border-light: #e0e0e0;
  --text-primary: #000000;
  --text-secondary: #333333;
  --text-muted: #666666;
  --accent-cyan: #000000;
  --accent-blue: #000000;
  --accent-purple: #000000;
  --accent-green: #000000;
  --accent-orange: #000000;
  --accent-red: #000000;
  --accent-pink: #000000;
  --glow-cyan: transparent;
  --glow-blue: transparent;
  --glow-purple: transparent;
  --beginner: #000000;
  --intermediate: #000000;
  --advanced: #000000;
  --sidebar-width: 260px;
  --header-height: 60px;
  --font-mono: 'JetBrains Mono', monospace;
  --font-ui: 'Inter', sans-serif;
  --font-display: 'Space Grotesk', sans-serif;
  --radius: 0px;
  --radius-sm: 0px;
  --transition: 0s;
}
[data-theme="light"] {
  --bg-primary: #ffffff;
  --bg-secondary: #f4f4f4;
  --bg-card: #ffffff;
  --bg-card-hover: #fafafa;
  --bg-code: #f8f8f8;
  --border: #cccccc;
  --border-light: #e0e0e0;
  --text-primary: #000000;
  --text-secondary: #333333;
  --text-muted: #666666;
  --accent-cyan: #000000;
  --glow-cyan: transparent;
  --glow-blue: transparent;
}"""

# Replace the variables block
content = re.sub(r'/\* ===== CSS VARIABLES ===== \*/[\s\S]*?}\n\[data-theme="light"\] {[\s\S]*?}', new_vars, content)

# Replace dark backgrounds and gradients
content = re.sub(r'background:linear-gradient\([^)]+\)', 'background:var(--bg-card)', content)
content = re.sub(r'background:rgba\([^)]+\)', 'background:var(--bg-card)', content)

# Fix code block syntax highlighting for light background
code_style = """.code-block pre{padding:16px;overflow-x:auto;font-size:0.82rem;line-height:1.7;color:#000000}
.code-block pre .kw{color:#0000ff;font-weight:bold}
.code-block pre .fn{color:#000000;font-weight:bold}
.code-block pre .cm{color:#666666;font-style:italic}
.code-block pre .st{color:#008000}
.code-block pre .nm{color:#000000}
.code-block pre .op{color:#000000}"""

content = re.sub(r'\.code-block pre\{padding:16px;.*?\n\.code-block pre \.op\{.*?\}', code_style, content, flags=re.DOTALL)

# Also fix the data-theme on the html tag to light so we don't rely on OS preferences if we missed any specific dark overrides. Actually we overrode the dark theme variables directly, so it's fine.
content = content.replace('<html lang="en" data-theme="dark">', '<html lang="en" data-theme="light">')

with open('graph.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
