css = '''
/* ==========================================================================
   ELEVATED MINIMAL PROJECT CARDS (REFERENCES SECTION)
   Pure CSS System: Sector FA6 Icons, Country Flag Badges, Smooth Transitions
   ========================================================================== */

.b95-references-elevated-index {
  background-color: #FFFFFF;
  padding: 6.5rem 0;
  border-bottom: 1px solid var(--b95-border);
}

.b95-elevated-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.85rem;
}

.b95-elevated-card {
  position: relative;
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  padding: 2.25rem 2rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 240px;
  transition: transform 0.25s var(--b95-ease-out), border-color 0.25s ease, box-shadow 0.25s ease;
  outline: none;
  cursor: default;
}

.b95-elevated-card:hover,
.b95-elevated-card:focus-visible {
  transform: translateY(-4px);
  border-color: var(--b95-accent); /* #991B1B */
  box-shadow: 0 18px 36px -10px rgba(15, 23, 42, 0.08);
}

/* Top Row: Number & Country Flag Pill */
.b95-card-top-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.75rem;
  padding-bottom: 1.15rem;
  border-bottom: 1px solid rgba(226, 232, 240, 0.8);
}

.b95-card-num {
  font-family: var(--b95-font-mono);
  font-size: 2.25rem;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.04em;
  color: var(--b95-border-strong);
  transition: color 0.25s ease;
}

.b95-elevated-card:hover .b95-card-num {
  color: var(--b95-accent);
}

.b95-country-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.35rem 0.85rem 0.35rem 0.45rem;
  background-color: var(--b95-slate-50);
  border: 1px solid var(--b95-border);
  border-radius: 9999px;
  transition: border-color 0.2s ease, background-color 0.2s ease;
}

.b95-elevated-card:hover .b95-country-pill {
  border-color: var(--b95-border-strong);
  background-color: var(--b95-slate-100);
}

.b95-flag-svg {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: block;
  flex-shrink: 0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.b95-country-label {
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--b95-slate-700);
}

/* Middle Section: Sector Icon Badge + Category Label */
.b95-card-middle {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  margin-bottom: 1.15rem;
}

.b95-sector-icon-badge {
  width: 36px;
  height: 36px;
  border-radius: 6px;
  background-color: #FEF2F2;
  border: 1px solid #FEE2E2;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--b95-accent);
  font-size: 0.95rem;
  flex-shrink: 0;
  transition: all 0.25s ease;
}

.b95-elevated-card:hover .b95-sector-icon-badge {
  background-color: var(--b95-accent);
  color: #FFFFFF;
  border-color: var(--b95-accent);
  transform: scale(1.05);
}

.b95-sector-label {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--b95-slate-500);
}

/* Bottom Section: Bold Project Title */
.b95-card-title {
  font-family: var(--b95-font-main);
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -0.02em;
  color: var(--b95-slate-900);
  margin: 0;
  transition: color 0.2s ease;
}

.b95-elevated-card:hover .b95-card-title {
  color: var(--b95-accent);
}

/* Responsive Breakpoints */
@media (max-width: 1024px) {
  .b95-elevated-cards-grid {
    grid-template-columns: 1fr;
    gap: 1.35rem;
  }
}

@media (max-width: 640px) {
  .b95-references-elevated-index {
    padding: 4.5rem 0;
  }

  .b95-elevated-card {
    padding: 1.75rem 1.35rem;
    min-height: auto;
  }

  .b95-card-top-row {
    flex-wrap: wrap;
    gap: 0.75rem;
  }

  .b95-card-num {
    font-size: 1.85rem;
  }

  .b95-card-title {
    font-size: 1.15rem;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Appended elevated cards CSS to styles.css successfully!")
