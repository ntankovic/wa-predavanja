"""Shared visual style for original Croatian course diagrams (SVG/PDF)."""
from html import escape
import textwrap
BLUE = '#3886ad'
INK = '#20384d'
RED = '#b63842'

def text(x, y, value, size=24, color=INK, weight=400):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>')

def box(x, y, w, h, label, sub=''):
    title_size = 25 if w >= 230 else 23
    sub_size = 18
    # Keep explicit inner margins, wrapping descriptions rather than shrinking text.
    max_chars = max(12, int((w - 42) / (sub_size * .52)))
    lines = textwrap.wrap(sub, width=max_chars, break_long_words=False, break_on_hyphens=False)
    title_height = title_size * 1.15
    subtitle_height = max(2, len(lines)) * 24 if lines else 0
    group_height = title_height + (12 + subtitle_height if lines else 0)
    top = y + (h - group_height) / 2
    radius = 16
    result = (f'<rect x="{x+1}" y="{y+5}" width="{w-2}" height="{h}" rx="{radius}" fill="#24445c" opacity=".035"/>'
              f'<rect x="{x}" y="{y+2}" width="{w}" height="{h}" rx="{radius}" fill="#24445c" opacity=".025"/>'
              f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="#f8fbfd" '
              f'stroke="#c6dbe8" stroke-width="1.2"/>'
              f'<rect x="{x+12}" y="{y+min(28,h*.28)}" width="7" height="{h-2*min(28,h*.28)}" rx="3.5" fill="#3886ad"/>')
    result += text(x+w/2, top+title_size*.82, label, title_size, INK, 600)
    for i, line in enumerate(lines):
        result += text(x+w/2, top+title_height+12+(subtitle_height-len(lines)*24)/2+sub_size*.82+i*24, line, sub_size, '#536b7b')
    return result

def markers():
    return '<defs>' + ''.join(
        f'<marker id="arrow-{name}" markerWidth="18" markerHeight="18" refX="14" refY="9" orient="auto" markerUnits="userSpaceOnUse"><path d="M2,2 L18,9 L2,16 Z" fill="{color}"/></marker>'
        for name, color in [('blue', BLUE), ('red', RED)]) + '</defs>'

def arrow(x, y, x2, y2, label='', color=BLUE, dash=False):
    marker = 'red' if color == RED else 'blue'
    result = (f'<path d="M{x},{y} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="3.2" '
              f'stroke-linecap="round" '+('stroke-dasharray="7 6" ' if dash else '')+
              f'marker-end="url(#arrow-{marker})"/>')
    return result + (text((x+x2)/2, (y+y2)/2-13, label, 19, color) if label else '')
