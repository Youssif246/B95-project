css = '''
/* ==========================================================================
   ULTRA-MINIMALIST SWISS PROJECT INDEX (REFERENCES SECTION REDESIGN)
   Pure Swiss Typography · Massive Whitespace · Zero Clutter
   ========================================================================== */

.b95-references-minimal {
  background-color: #FFFFFF;
  padding: 6.5rem 0;
  border-bottom: 1px solid var(--b95-border);
}

.b95-minimal-header {
  margin-bottom: 4rem;
  padding-bottom: 2.25rem;
  border-bottom: 1px solid var(--b95-border);
}

.b95-minimal-eyebrow {
  font-family: var(--b95-font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--b95-slate-500);
  margin-bottom: 0.75rem;
}

.b95-minimal-eyebrow .b95-eyebrow-accent {
  color: var(--b95-accent);
}

.b95-minimal-title {
  font-family: var(--b95-font-main);
  font-size: 2.85rem;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.035em;
  color: var(--b95-slate-900);
  margin-bottom: 0.65rem;
}

.b95-minimal-subtitle {
  font-size: 1.05rem;
  color: var(--b95-slate-600);
  line-height: 1.6;
}

/* 2-Column Minimal Index Grid */
.b95-project-index-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.75rem;
}

.b95-project-index-card {
  position: relative;
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  padding: 2.75rem 2.5rem 2.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 220px;
  transition: transform 0.25s var(--b95-ease-out), border-color 0.25s ease, box-shadow 0.25s ease;
  outline: none;
  cursor: default;
}

.b95-project-index-card:hover,
.b95-project-index-card:focus-visible {
  transform: translateY(-4px);
  border-color: var(--b95-border-strong);
  box-shadow: 0 16px 32px -8px rgba(15, 23, 42, 0.06);
}

.b95-index-card__top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 2rem;
  padding-bottom: 1.25rem;
  border-bottom: 1px solid rgba(226, 232, 240, 0.7);
}

.b95-index-card__num {
  font-family: var(--b95-font-mono);
  font-size: 2.75rem;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.04em;
  color: var(--b95-border-strong);
  transition: color 0.25s ease;
}

.b95-project-index-card:hover .b95-index-card__num {
  color: var(--b95-accent);
}

.b95-index-card__loc {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--b95-slate-600);
}

.b95-loc-bullet {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--b95-accent);
  display: inline-block;
}

.b95-index-card__title {
  font-family: var(--b95-font-main);
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -0.02em;
  color: var(--b95-slate-900);
  margin: 0;
  transition: color 0.2s ease;
}

.b95-project-index-card:hover .b95-index-card__title {
  color: var(--b95-accent);
}

/* Responsive Breakpoints */
@media (max-width: 1024px) {
  .b95-project-index-grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }
}

@media (max-width: 640px) {
  .b95-references-minimal {
    padding: 4.5rem 0;
  }

  .b95-minimal-title {
    font-size: 2.1rem;
  }

  .b95-project-index-card {
    padding: 2rem 1.5rem;
    min-height: auto;
  }

  .b95-index-card__num {
    font-size: 2.1rem;
  }

  .b95-index-card__title {
    font-size: 1.15rem;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Appended ultra-minimalist project index CSS successfully!")
