"""Original illustrative storefront for the opening question; no real site implied."""
from pathlib import Path
import subprocess
D=Path(__file__).resolve().parent
s='''<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="190" viewBox="0 0 1040 190">
<rect x="1" y="1" width="1038" height="188" rx="16" fill="#fff" stroke="#cbdce7" stroke-width="2"/>
<path d="M1 45 H1039" stroke="#cbdce7"/>
<g fill="#bacbd7"><circle cx="24" cy="24" r="5"/><circle cx="42" cy="24" r="5"/><circle cx="60" cy="24" r="5"/></g>
<text x="87" y="31" font-family="Arial,sans-serif" font-size="19" fill="#536b7b">Ilustrativna trgovina</text>
<text x="30" y="88" font-family="Arial,sans-serif" font-size="27" font-weight="700" fill="#20384d">Proizvodi</text>
<rect x="30" y="107" width="980" height="57" rx="10" fill="#f3f8fb"/>
<circle cx="59" cy="136" r="11" fill="none" stroke="#d0e2ed" stroke-width="4"/>
<path d="M59 125 A11 11 0 0 1 70 136" fill="none" stroke="#3886ad" stroke-width="4" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" from="0 59 136" to="360 59 136" dur="0.9s" repeatCount="indefinite"/></path>
<text x="85" y="144" font-family="Arial,sans-serif" font-size="23" fill="#536b7b">Učitavanje…</text>
</svg>'''
p=D/'loading-example.hr.svg';p.write_text(s)
subprocess.run(['rsvg-convert','-f','pdf','-o',str(p.with_suffix('.pdf')),str(p)],check=True)
