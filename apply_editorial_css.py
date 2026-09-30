import re

css_to_add = """/* ==========================================================================
   SECTION 02: REFERENCES & REGIONAL REACH (ARCHITECTURAL MONOGRAPH INDEX)
   Swiss Editorial 2-Column Ledger: Hairline Dividers, Elegant Indicators
   ========================================================================== */

.b95-references-editorial {
  background-color: #FFFFFF;
  padding: 6rem 0;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
  position: relative;
}

.b95-editorial-header {
  margin-bottom: 3.5rem;
}

.b95-editorial-eyebrow {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #64748B;
  margin-bottom: 0.75rem;
}

.b95-editorial-title-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 1.25rem;
  margin-bottom: 0.85rem;
}

.b95-editorial-title {
  font-size: clamp(2rem, 3.2vw, 2.75rem);
  font-weight: 800;
  color: #0F172A;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin: 0;
}

.b95-editorial-badge {
  display: inline-flex;
  align-items: center;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #991B1B;
  background-color: #FEF2F2;
  padding: 0.35rem 0.85rem;
  border-radius: 9999px;
  border: 1px solid rgba(153, 27, 27, 0.18);
  white-space: nowrap;
}

.b95-editorial-lead {
  font-size: 1.05rem;
  color: #475569;
  max-width: 720px;
  line-height: 1.6;
  margin: 0;
  font-weight: 400;
}

/* 2-Column Swiss Monograph Layout */
.b95-editorial-columns {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  column-gap: 4rem;
  align-items: start;
}

.b95-editorial-column {
  display: flex;
  flex-direction: column;
}

/* Editorial Project Strip (No Boxy Cards) */
.b95-editorial-strip {
  display: grid;
  grid-template-columns: 44px 1fr;
  gap: 1.5rem;
  align-items: start;
  padding: 1.85rem 1.25rem 1.85rem 1.25rem;
  border-bottom: 1px solid #E2E8F0;
  position: relative;
  background-color: transparent;
  transition: background-color 0.22s ease;
  cursor: default;
  outline: none;
}

.b95-editorial-strip:first-child {
  border-top: 1px solid #E2E8F0;
}

/* Left Hairline Indicator Accent on Hover (Swiss Monograph Interaction) */
.b95-editorial-strip::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background-color: #991B1B;
  transform: scaleY(0);
  transform-origin: center;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.b95-editorial-strip:hover::before,
.b95-editorial-strip:focus-visible::before {
  transform: scaleY(1);
}

.b95-editorial-strip:hover,
.b95-editorial-strip:focus-visible {
  background-color: #F8FAFC;
}

/* Typographic Project Index Number */
.b95-strip-num {
  font-size: 1.35rem;
  font-weight: 700;
  font-family: 'Space Grotesk', 'Plus Jakarta Sans', monospace, sans-serif;
  color: #94A3B8;
  line-height: 1;
  padding-top: 0.25rem;
  letter-spacing: -0.03em;
  transition: color 0.22s ease;
  user-select: none;
}

.b95-editorial-strip:hover .b95-strip-num,
.b95-editorial-strip:focus-visible .b95-strip-num {
  color: #991B1B;
}

/* Strip Content Container */
.b95-strip-content {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

/* Top Meta Row (Flags, Country, Sector) */
.b95-strip-meta {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.65rem 0.85rem;
  line-height: 1;
}

.b95-meta-loc {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.b95-flag-svg {
  width: 17px;
  height: 17px;
  border-radius: 50%;
  flex-shrink: 0;
  display: inline-block;
  vertical-align: middle;
  box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.1);
}

.b95-loc-text {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #334155;
}

.b95-meta-separator {
  color: #CBD5E1;
  font-weight: 300;
  font-size: 0.75rem;
  user-select: none;
}

.b95-meta-sector {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
}

.b95-sector-icon {
  color: #991B1B;
  font-size: 0.75rem;
}

.b95-sector-text {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #64748B;
}

/* Project Title */
.b95-strip-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.4;
  letter-spacing: -0.015em;
  margin: 0;
  transition: color 0.2s ease;
}

.b95-editorial-strip:hover .b95-strip-title,
.b95-editorial-strip:focus-visible .b95-strip-title {
  color: #0F172A;
}

/* Responsive Breakpoints */
@media (max-width: 1024px) {
  .b95-editorial-columns {
    grid-template-columns: 1fr;
    gap: 0;
  }

  .b95-editorial-column + .b95-editorial-column .b95-editorial-strip:first-child {
    border-top: none;
  }
}

@media (max-width: 768px) {
  .b95-references-editorial {
    padding: 4rem 0;
  }

  .b95-editorial-header {
    margin-bottom: 2.25rem;
  }

  .b95-editorial-title {
    font-size: 1.85rem;
  }

  .b95-editorial-strip {
    grid-template-columns: 36px 1fr;
    gap: 1rem;
    padding: 1.4rem 0.75rem;
  }

  .b95-strip-num {
    font-size: 1.15rem;
  }

  .b95-strip-title {
    font-size: 1.05rem;
  }
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check if previously added .b95-references-elevated-index exists
elev_pos = css.find('.b95-references-elevated-index')
if elev_pos != -1:
    css = css[:elev_pos].rstrip() + "\n\n" + css_to_add
else:
    css = css + "\n\n" + css_to_add

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied editorial project index CSS to styles.css successfully!")
