def icon(size=56, bracket="#5B3A70", g="#16141A", line="#16141A"):
    h = size * 64 / 56
    return f'''<svg width="{size}" height="{h:.1f}" viewBox="0 0 56 64" aria-hidden="true"><path d="M17 6H7v44h10" fill="none" stroke="{bracket}" stroke-width="6"/><path d="M39 6h10v44H39" fill="none" stroke="{bracket}" stroke-width="6"/><text x="28" y="37" text-anchor="middle" font-family="Newsreader, Georgia, serif" font-weight="600" font-size="26" fill="{g}">G</text><rect x="0" y="57" width="56" height="6" fill="{line}"/></svg>'''
