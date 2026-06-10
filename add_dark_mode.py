import re

with open('graph.html', 'r', encoding='utf-8') as f:
    content = f.read()

dark_css = """
/* ===== DARK THEME ===== */
[data-theme="dark"] {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-card: #1e293b;
  --bg-card-hover: #334155;
  --bg-code: #020617;
  --border: #334155;
  --border-light: #475569;
  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --accent-cyan: #38bdf8;
  --accent-blue: #60a5fa;
  --accent-purple: #a78bfa;
  --accent-green: #34d399;
  --accent-orange: #fbbf24;
  --accent-red: #f87171;
  --accent-pink: #f472b6;
  --glow-cyan: rgba(56, 189, 248, 0.15);
  --glow-blue: rgba(96, 165, 250, 0.15);
  --glow-purple: rgba(167, 139, 250, 0.15);
}

[data-theme="dark"] .code-block pre { color: #f8fafc; }
[data-theme="dark"] .code-block pre .kw { color: #60a5fa; }
[data-theme="dark"] .code-block pre .fn { color: #e2e8f0; }
[data-theme="dark"] .code-block pre .cm { color: #94a3b8; }
[data-theme="dark"] .code-block pre .st { color: #34d399; }
[data-theme="dark"] .code-block pre .nm { color: #fbbf24; }
[data-theme="dark"] .code-block pre .op { color: #cbd5e1; }

[data-theme="dark"] #header { background: rgba(30, 41, 59, 0.95); }
"""

# Insert right before </style>
content = content.replace('</style>', dark_css + '\n</style>')

with open('graph.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
