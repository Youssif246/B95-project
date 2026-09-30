import re

css_to_add = """/* ==========================================================================
   SECTION 02: REFERENCES & REGIONAL FOOTPRINT (ARCHITECTURAL MASTER INDEX)
   Swiss Full-Bleed Master Ledger: 8 Horizontal Rows, 4 Strict Columns
   ========================================================================== */

.b95-master-index-section {
  background-color: #FFFFFF;
  padding: 6.5rem 0;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
  position: relative;
}

/* Header & Context Integration */
.b95-master-header {
  margin-bottom: 2.75rem;
}

.b95-master-eyebrow {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #64748B;
  margin-bottom: 0.65rem;
}

.b95-master-eyebrow .b95-eyebrow-accent {
  color: #991B1B;
  font-weight: 800;
}

.b95-master-title {
  font-size: clamp(2.15rem, 3.5vw, 2.85rem);
  font-weight: 800;
  color: #0F172A;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin: 0 0 1.35rem 0;
}

/* Integrated Operational Meta Strip */
.b95-master-meta-strip {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.85rem 1.25rem;
  padding: 0.95rem 1.35rem;
  background-color: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 4px;
  font-size: 0.85rem;
  color: #475569;
}

.b95-meta-segment {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.b95-meta-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: #991B1B;
  display: inline-block;
  box-shadow: 0 0 0 2px rgba(153, 27, 27, 0.2);
}

.b95-meta-highlight {
  font-weight: 800;
  color: #991B1B;
}

.b95-meta-divider {
  color: #CBD5E1;
  font-weight: 300;
  user-select: none;
}

/* Master Index Ledger */
.b95-master-ledger {
  width: 100%;
  border-top: 2px solid #0F172A;
  display: flex;
  flex-direction: column;
}

/* Table Header Row */
.b95-ledger-table-header {
  display: grid;
  grid-template-columns: 85px 230px 1fr 220px;
  align-items: center;
  padding: 0.85rem 1.35rem;
  background-color: #FAFAFA;
  border-bottom: 1px solid #E2E8F0;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #64748B;
  user-select: none;
}

.b95-th-sector {
  text-align: right;
}

/* Architectural Row Strip (Zero Box Containers) */
.b95-ledger-row {
  display: grid;
  grid-template-columns: 85px 230px 1fr 220px;
  align-items: center;
  padding: 1.35rem 1.35rem;
  border-bottom: 1px solid #E2E8F0;
  border-left: 3px solid transparent;
  background-color: transparent;
  transition: background-color 0.2s ease, border-left-color 0.2s ease;
  cursor: default;
  outline: none;
}

/* Row Hover State: Background tint & crimson indicator */
.b95-ledger-row:hover,
.b95-ledger-row:focus-visible {
  background-color: #F1F5F9;
  border-left-color: #991B1B;
}

/* Column 1: Typographic Anchor (~10%) */
.b95-col-num {
  font-size: 1.5rem;
  font-weight: 800;
  color: #991B1B;
  font-family: 'Space Grotesk', 'Plus Jakarta Sans', monospace, sans-serif;
  letter-spacing: -0.04em;
  line-height: 1;
  user-select: none;
}

/* Column 2: Sovereign Node (~22%) */
.b95-col-node {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
}

.b95-col-node .b95-flag-svg {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  flex-shrink: 0;
  display: inline-block;
  vertical-align: middle;
  box-shadow: 0 0 0 1px rgba(15, 23, 42, 0.1);
}

.b95-node-text {
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #334155;
  white-space: nowrap;
}

/* Column 3: Project Title (~48%) */
.b95-col-title {
  padding-right: 1.5rem;
}

.b95-row-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.4;
  letter-spacing: -0.015em;
  margin: 0;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), color 0.2s ease;
}

.b95-ledger-row:hover .b95-row-title,
.b95-ledger-row:focus-visible .b95-row-title {
  transform: translateX(6px);
  color: #0F172A;
}

/* Column 4: Sector Classification (~20%) */
.b95-col-sector {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.b95-sector-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.4rem 0.85rem;
  background-color: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #64748B;
  white-space: nowrap;
  transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
}

.b95-sector-pill .b95-sector-icon {
  color: #991B1B;
  font-size: 0.75rem;
}

.b95-ledger-row:hover .b95-sector-pill,
.b95-ledger-row:focus-visible .b95-sector-pill {
  background-color: #FEF2F2;
  border-color: rgba(153, 27, 27, 0.25);
  color: #991B1B;
}

/* Responsive Adaptations */
@media (max-width: 1040px) {
  .b95-ledger-table-header {
    grid-template-columns: 65px 190px 1fr 190px;
    padding: 0.75rem 1rem;
  }

  .b95-ledger-row {
    grid-template-columns: 65px 190px 1fr 190px;
    padding: 1.25rem 1rem;
  }

  .b95-node-text {
    font-size: 0.775rem;
  }

  .b95-row-title {
    font-size: 1.05rem;
  }

  .b95-sector-pill {
    padding: 0.35rem 0.7rem;
    font-size: 0.7rem;
  }
}

@media (max-width: 820px) {
  .b95-ledger-table-header {
    display: none;
  }

  .b95-ledger-row {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.65rem;
    padding: 1.25rem 1rem;
  }

  .b95-col-num {
    display: none;
  }

  .b95-col-node {
    width: 100%;
    justify-content: flex-start;
  }

  .b95-col-title {
    padding-right: 0;
  }

  .b95-col-sector {
    width: 100%;
    justify-content: flex-start;
  }

  .b95-master-meta-strip {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .b95-meta-divider {
    display: none;
  }

  .b95-master-title {
    font-size: 1.85rem;
  }
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace any previous .b95-commission-spread or .b95-references-editorial
marker = '.b95-commission-spread'
pos = css.find(marker)
if pos == -1:
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

print("Applied architectural master index CSS to styles.css successfully!")
