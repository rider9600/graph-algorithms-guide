import re

with open('graph.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS Variables for a clean educational theme
new_vars = """/* ===== CSS VARIABLES ===== */
:root {
  --bg-primary: #f8fafc;
  --bg-secondary: #f1f5f9;
  --bg-card: #ffffff;
  --bg-card-hover: #ffffff;
  --bg-code: #f1f5f9;
  --border: #e2e8f0;
  --border-light: #cbd5e1;
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  --accent-cyan: #0284c7;
  --accent-blue: #2563eb;
  --accent-purple: #7c3aed;
  --accent-green: #059669;
  --accent-orange: #d97706;
  --accent-red: #dc2626;
  --accent-pink: #db2777;
  --glow-cyan: rgba(2, 132, 199, 0.1);
  --glow-blue: rgba(37, 99, 235, 0.1);
  --glow-purple: rgba(124, 58, 237, 0.1);
  --beginner: #059669;
  --intermediate: #d97706;
  --advanced: #dc2626;
  --sidebar-width: 280px;
  --header-height: 64px;
  --font-mono: 'JetBrains Mono', monospace;
  --font-ui: 'Inter', sans-serif;
  --font-display: 'Space Grotesk', sans-serif;
  --radius: 12px;
  --radius-sm: 6px;
  --transition: 0.2s ease;
}
[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-secondary: #f1f5f9;
  --bg-card: #ffffff;
  --bg-card-hover: #ffffff;
  --bg-code: #f1f5f9;
  --border: #e2e8f0;
  --border-light: #cbd5e1;
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  --accent-cyan: #0284c7;
  --glow-cyan: rgba(2, 132, 199, 0.1);
  --glow-blue: rgba(37, 99, 235, 0.1);
}"""

content = re.sub(r'/\* ===== CSS VARIABLES ===== \*/[\s\S]*?}\n\[data-theme="light"\] {[\s\S]*?}', new_vars, content)

# 2. Fix specific hardcoded dark gradients and transparency that look vibrant
content = content.replace('background:linear-gradient(180deg,rgba(15,22,40,0.98),rgba(10,14,26,0.94));', 'background:var(--bg-card);')
content = content.replace('background:linear-gradient(180deg,rgba(19,28,51,0.96),rgba(10,14,26,0.98));', 'background:var(--bg-card);')
content = content.replace('background:linear-gradient(135deg,rgba(8,13,26,0.96),rgba(19,28,51,0.92));', 'background:var(--bg-card);')
content = content.replace('background:rgba(19,28,51,0.88);', 'background:var(--bg-primary);')
content = content.replace('background:rgba(10,14,26,0.92);backdrop-filter:blur(16px);', 'background:rgba(255,255,255,0.95);backdrop-filter:blur(16px);')
content = content.replace('background:radial-gradient(ellipse at 80% 50%,var(--glow-purple),transparent 60%)', 'background:none')
content = content.replace('background:linear-gradient(135deg,var(--bg-secondary) 0%,var(--bg-card) 100%);', 'background:var(--bg-card);')

# 3. Increase shadow/border-radius on cards for educational feel
content = content.replace('box-shadow:0 4px 24px rgba(0,0,0,0.2)', 'box-shadow:0 4px 12px rgba(0,0,0,0.08)')
content = content.replace('box-shadow:0 18px 44px rgba(0,0,0,0.18)', 'box-shadow:0 10px 25px rgba(0,0,0,0.05)')
content = content.replace('box-shadow:0 24px 56px rgba(0,0,0,0.26)', 'box-shadow:0 20px 40px rgba(0,0,0,0.08)')
content = content.replace('box-shadow:0 8px 28px rgba(0,0,0,0.22)', 'box-shadow:0 8px 20px rgba(0,0,0,0.06)')
content = content.replace('border:1px solid rgba(255,255,255,0.1)', 'border:1px solid var(--border)')
content = content.replace('background:rgba(255,255,255,0.04)', 'background:var(--bg-secondary)')
content = content.replace('background:rgba(255,255,255,0.03)', 'background:var(--bg-secondary)')
content = content.replace('background:rgba(255,255,255,0.05)', 'background:var(--bg-secondary)')
content = content.replace('background:rgba(255,255,255,0.06)', 'background:var(--bg-secondary)')
content = content.replace('border:1px solid rgba(255,255,255,0.06)', 'border:1px solid var(--border)')
content = content.replace('border:1px solid rgba(255,255,255,0.05)', 'border:1px solid var(--border)')
content = content.replace('box-shadow:inset 0 1px 0 rgba(255,255,255,0.03)', 'box-shadow:none')

# 4. Code blocks need a dark text color
code_style = """.code-block pre{padding:16px;overflow-x:auto;font-size:0.82rem;line-height:1.7;color:#334155}
.code-block pre .kw{color:#2563eb;font-weight:600}
.code-block pre .fn{color:#0f172a;font-weight:600}
.code-block pre .cm{color:#64748b;font-style:italic}
.code-block pre .st{color:#059669}
.code-block pre .nm{color:#d97706}
.code-block pre .op{color:#334155}"""
content = re.sub(r'\.code-block pre\{padding:16px;.*?\n\.code-block pre \.op\{.*?\}', code_style, content, flags=re.DOTALL)

# 5. Make HTML default to light mode
content = content.replace('<html lang="en" data-theme="dark">', '<html lang="en" data-theme="light">')

with open('graph.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
