territory_css = '''
/* ==========================================================================
   SOVEREIGN TERRITORY MATRIX (REFERENCES & REGIONAL REACH REDESIGN)
   Pure CSS System: 2-Column Responsive Grid, Silhouette Badges, Vector Ribbon
   ========================================================================== */

.b95-territory-section {
  background-color: #FFFFFF;
}

/* Top Component: Footprint Card & Operational Ribbon */
.b95-territory-footprint-card {
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  box-shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.05);
  margin-bottom: 3.5rem;
  overflow: hidden;
}

.b95-footprint-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.85rem 1.75rem;
  background-color: var(--b95-slate-50);
  border-bottom: 1px solid var(--b95-border);
}

.b95-footprint-topbar__left {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.b95-footprint-topbar__label {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--b95-slate-700);
}

.b95-coord-tag {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  color: var(--b95-slate-500);
  letter-spacing: 0.04em;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.b95-coord-tag i {
  color: var(--b95-accent);
}

.b95-territory-vector-canvas {
  padding: 1rem 1.5rem;
  background-color: #FFFFFF;
}

.b95-vector-ribbon-svg {
  width: 100%;
  height: auto;
  display: block;
}

/* Sleek Operational Ribbon */
.b95-operational-ribbon {
  display: grid;
  grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
  align-items: center;
  background-color: var(--b95-slate-900);
  padding: 1.35rem 2rem;
  border-top: 1px solid var(--b95-border);
}

.b95-ribbon-metric {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.b95-metric-num {
  font-family: var(--b95-font-main);
  font-size: 2rem;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.04em;
  color: #FFFFFF;
}

.b95-metric-text strong {
  display: block;
  font-family: var(--b95-font-main);
  font-size: 0.88rem;
  font-weight: 700;
  color: #FFFFFF;
  line-height: 1.25;
}

.b95-metric-text span {
  display: block;
  font-family: var(--b95-font-mono);
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--b95-slate-400);
}

.b95-ribbon-sep {
  width: 1px;
  height: 32px;
  background-color: var(--b95-slate-800);
}

/* ==========================================================================
   SOVEREIGN TERRITORY MATRIX GRID & PROJECT CARDS
   ========================================================================== */
.b95-territory-matrix-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.85rem;
}

.b95-territory-card {
  position: relative;
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  padding: 2.25rem 2rem 1.85rem;
  display: flex;
  flex-direction: column;
  transition: var(--b95-transition-card);
  outline: none;
  cursor: default;
}

.b95-territory-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 0;
  height: 3px;
  background-color: var(--b95-accent);
  transition: width 0.3s var(--b95-ease-out);
}

.b95-territory-card:hover,
.b95-territory-card:focus-visible {
  transform: translateY(-5px);
  border-color: var(--b95-border-strong);
  box-shadow: 0 18px 36px -10px rgba(15, 23, 42, 0.08);
}

.b95-territory-card:hover::before {
  width: 100%;
}

/* Card Anchor Header */
.b95-card-anchor-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-bottom: 1.35rem;
  padding-bottom: 1.15rem;
  border-bottom: 1px solid var(--b95-border);
}

.b95-country-badge {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.b95-country-silhouette {
  width: 48px;
  height: 48px;
  flex-shrink: 0;
  border: 1px solid var(--b95-border);
  background-color: var(--b95-slate-50);
  padding: 4px;
  border-radius: 2px;
  transition: transform 0.3s var(--b95-ease-out), border-color 0.3s ease;
}

.b95-territory-card:hover .b95-country-silhouette {
  transform: scale(1.06);
  border-color: var(--b95-accent);
}

.b95-country-badge__info {
  display: flex;
  flex-direction: column;
}

.b95-country-code {
  font-family: var(--b95-font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: var(--b95-slate-500);
  line-height: 1.2;
}

.b95-country-name {
  font-family: var(--b95-font-main);
  font-size: 1.05rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  color: var(--b95-slate-900);
  line-height: 1.2;
}

/* Sector Pill Badges */
.b95-matrix-sector-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--b95-font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.35rem 0.75rem;
  border-radius: 2px;
  border: 1px solid transparent;
}

.b95-matrix-sector-tag--sports { background: #FEF2F2; color: #991B1B; border-color: #FCA5A5; }
.b95-matrix-sector-tag--infra { background: #F0FDF4; color: #166534; border-color: #86EFAC; }
.b95-matrix-sector-tag--aviation { background: #EFF6FF; color: #1E40AF; border-color: #93C5FD; }
.b95-matrix-sector-tag--diplomatic { background: #FAF5FF; color: #6B21A8; border-color: #D8B4FE; }
.b95-matrix-sector-tag--health { background: #ECFDF5; color: #065F46; border-color: #6EE7B7; }
.b95-matrix-sector-tag--urban { background: #FFFBEB; color: #92400E; border-color: #FDE68A; }
.b95-matrix-sector-tag--comm { background: #F8FAFC; color: #334155; border-color: #CBD5E1; }

/* Card Content */
.b95-territory-card__content {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.b95-territory-location {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-family: var(--b95-font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--b95-slate-700);
  margin-bottom: 0.5rem;
}

.b95-territory-title {
  font-family: var(--b95-font-main);
  font-size: 1.25rem;
  font-weight: 800;
  line-height: 1.35;
  letter-spacing: -0.02em;
  color: var(--b95-slate-900);
  margin-bottom: 0.65rem;
  transition: color 0.2s ease;
}

.b95-territory-card:hover .b95-territory-title {
  color: var(--b95-accent);
}

.b95-territory-scope {
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.55;
  color: var(--b95-slate-900);
  margin-bottom: 0.65rem;
  border-left: 2px solid var(--b95-accent);
  padding-left: 0.75rem;
}

.b95-territory-detail {
  font-size: 0.88rem;
  line-height: 1.65;
  color: var(--b95-slate-600);
  margin-bottom: 1.75rem;
  flex-grow: 1;
}

/* Card Footer */
.b95-territory-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1rem;
  border-top: 1px solid var(--b95-border);
  flex-wrap: wrap;
  gap: 0.5rem;
}

.b95-delivery-status {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #166534;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.b95-territory-client {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  color: var(--b95-slate-500);
}

/* Responsive Behavior */
@media (max-width: 1024px) {
  .b95-operational-ribbon {
    grid-template-columns: 1fr 1fr;
    gap: 1.25rem;
    padding: 1.5rem;
  }

  .b95-ribbon-sep {
    display: none;
  }

  .b95-territory-matrix-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

@media (max-width: 640px) {
  .b95-operational-ribbon {
    grid-template-columns: 1fr;
  }

  .b95-territory-card {
    padding: 1.75rem 1.25rem;
  }

  .b95-card-anchor-header {
    flex-direction: column;
    align-items: flex-start;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(territory_css)

print("Appended Sovereign Territory Matrix CSS to styles.css successfully!")
