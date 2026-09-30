import re

css_to_add = """/* ==========================================================================
   SECTION 02: REFERENCES (ARCHITECTURAL COMMISSION LEDGER)
   Asymmetric Editorial Spread: Left Pillar (28%) + Right Ledger (72%)
   ========================================================================== */

.b95-commission-spread {
  background-color: #F8FAFC;
  padding: 6.5rem 0;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
  position: relative;
}

/* Asymmetric 28% / 72% Editorial Layout */
.b95-spread-layout {
  display: grid;
  grid-template-columns: 310px 1fr;
  gap: 3.5rem;
  align-items: start;
}

/* Left Pillar: Editorial Context Panel */
.b95-spread-pillar {
  width: 100%;
}

.b95-pillar-sticky {
  position: sticky;
  top: 96px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.b95-pillar-eyebrow {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #64748B;
}

.b95-eyebrow-accent {
  color: #991B1B;
  font-weight: 800;
}

.b95-pillar-title {
  font-size: clamp(2rem, 2.5vw, 2.45rem);
  font-weight: 800;
  color: #0F172A;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin: 0;
}

.b95-pillar-lead {
  font-size: 0.95rem;
  color: #475569;
  line-height: 1.65;
  margin: 0;
}

/* Operational HQ Coordinates */
.b95-pillar-hq {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  padding: 1rem 1.15rem;
  background-color: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 4px;
}

.b95-hq-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.b95-hq-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: #991B1B;
  display: inline-block;
  box-shadow: 0 0 0 3px rgba(153, 27, 27, 0.15);
}

.b95-hq-label {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #0F172A;
}

.b95-hq-coords {
  font-family: monospace;
  font-size: 0.72rem;
  color: #64748B;
  letter-spacing: 0.05em;
  padding-left: 1.1rem;
}

/* Typographic Metric Box */
.b95-pillar-stat-box {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 1.25rem;
  background-color: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}

.b95-pillar-stat-box::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background-color: #991B1B;
}

.b95-stat-huge {
  font-size: 3.25rem;
  font-weight: 900;
  color: #991B1B;
  line-height: 1;
  letter-spacing: -0.04em;
  font-family: 'Space Grotesk', 'Plus Jakarta Sans', monospace, sans-serif;
  user-select: none;
}

.b95-stat-meta {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.b95-stat-title {
  font-size: 0.9rem;
  font-weight: 800;
  color: #0F172A;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.b95-stat-desc {
  font-size: 0.775rem;
  color: #64748B;
  line-height: 1.4;
}

/* Territory Pill Badges */
.b95-pillar-territories {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.b95-terr-tag {
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.3rem 0.65rem;
  background-color: #FFFFFF;
  color: #475569;
  border-radius: 3px;
  border: 1px solid #E2E8F0;
}

/* Right Ledger: 4 rows x 2 columns Architectural Grid */
.b95-spread-ledger {
  width: 100%;
}

.b95-ledger-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.25rem;
}

/* Ledger Item (Anti-Boring Architectural Monograph Tile) */
.b95-ledger-item {
  position: relative;
  background-color: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 4px;
  padding: 1.65rem 1.5rem;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);
  transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1), 
              box-shadow 0.22s ease, 
              border-color 0.22s ease,
              background-color 0.22s ease;
  cursor: default;
  outline: none;
  overflow: hidden;
}

/* Left Hairline Indicator Accent on Hover */
.b95-ledger-item::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background-color: #991B1B;
  transform: scaleY(0);
  transform-origin: center;
  transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 3;
}

.b95-ledger-item:hover::before,
.b95-ledger-item:focus-visible::before {
  transform: scaleY(1);
}

.b95-ledger-item:hover,
.b95-ledger-item:focus-visible {
  border-color: #CBD5E1;
  box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.07);
}

/* Large Typographic Watermark (Paper Architecture Look) */
.b95-ledger-watermark {
  position: absolute;
  right: 1.15rem;
  bottom: 0.65rem;
  font-size: 3.6rem;
  font-weight: 900;
  color: rgba(15, 23, 42, 0.04);
  font-family: 'Space Grotesk', 'Plus Jakarta Sans', monospace, sans-serif;
  line-height: 1;
  letter-spacing: -0.05em;
  user-select: none;
  pointer-events: none;
  transition: color 0.25s ease, transform 0.25s ease;
  z-index: 1;
}

.b95-ledger-item:hover .b95-ledger-watermark,
.b95-ledger-item:focus-visible .b95-ledger-watermark {
  color: rgba(153, 27, 27, 0.08);
  transform: translateY(-2px);
}

/* Item Inner Content */
.b95-item-inner {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

/* Top Bar: Country Flag + Location + Sector Tag */
.b95-item-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid #F1F5F9;
}

.b95-item-country {
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

.b95-country-name {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #334155;
}

.b95-item-sector {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.72rem;
  font-weight: 600;
  color: #64748B;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.b95-fa-sector {
  color: #991B1B;
  font-size: 0.75rem;
}

/* Project Title with Architectural Red Tick */
.b95-title-wrap {
  border-left: 2px solid #991B1B;
  padding-left: 0.75rem;
}

.b95-item-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.4;
  letter-spacing: -0.015em;
  margin: 0;
}

/* Responsive Adaptations */
@media (max-width: 1120px) {
  .b95-spread-layout {
    grid-template-columns: 280px 1fr;
    gap: 2.5rem;
  }
}

@media (max-width: 960px) {
  .b95-spread-layout {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .b95-pillar-sticky {
    position: static;
  }

  .b95-ledger-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .b95-commission-spread {
    padding: 4rem 0;
  }

  .b95-ledger-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .b95-ledger-item {
    padding: 1.35rem 1.25rem;
  }

  .b95-ledger-watermark {
    font-size: 2.85rem;
  }

  .b95-pillar-title {
    font-size: 1.85rem;
  }
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace any previous .b95-references-editorial or .b95-references-elevated-index
marker = '.b95-references-editorial'
pos = css.find(marker)
if pos == -1:
    marker = '.b95-references-elevated-index'
    pos = css.find(marker)

if pos != -1:
    css = css[:pos].rstrip() + "\n\n" + css_to_add
else:
    css = css + "\n\n" + css_to_add

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied architectural commission spread CSS to styles.css successfully!")
