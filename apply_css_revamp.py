css_code = '''
/* ==========================================================================
   B95 PROJECT — INDUSTRIAL LUXURY / ARCHITECTURAL MONOGRAPH REVAMP
   Turnkey Solutions (Services) · References & Footprint · Featured Case Study
   Color Palette & Mathematical Rhythm: Pure CSS / No Frameworks
   ========================================================================== */

:root {
  /* Industrial Luxury / Monograph Variables */
  --b95-bg-primary: #FFFFFF;
  --b95-bg-subtle: #F8FAFC;
  --b95-surface-secondary: #F1F5F9;
  --b95-text-primary: #0F172A;
  --b95-text-secondary: #334155;
  --b95-text-muted: #64748B;
  --b95-border: #E2E8F0;
  --b95-border-subtle: rgba(226, 232, 240, 0.7);
  --b95-border-strong: #CBD5E1;
  --b95-accent: #B91C1C;
  --b95-accent-dark: #991B1B;
  --b95-accent-subtle: rgba(185, 28, 28, 0.08);

  /* Typography Scale */
  --b95-font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --b95-font-mono: 'JetBrains Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace;

  /* Animation & Transition */
  --b95-ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --b95-transition: all 0.25s var(--b95-ease-out);
  --b95-transition-transform: transform 0.25s var(--b95-ease-out), border-color 0.25s ease, box-shadow 0.25s ease;
}

/* Base Wrapper for Redesigned Sections */
.b95-section {
  position: relative;
  background-color: var(--b95-bg-primary);
  color: var(--b95-text-primary);
  padding: 6.5rem 0;
  border-bottom: 1px solid var(--b95-border);
}

.b95-section:nth-of-type(even) {
  background-color: var(--b95-bg-subtle);
}

.b95-container {
  width: 100%;
  max-width: 1360px;
  margin: 0 auto;
  padding: 0 2.5rem;
}

/* Architectural Monograph Header */
.b95-section-header {
  margin-bottom: 3.75rem;
  border-bottom: 1px solid var(--b95-border);
  padding-bottom: 2.25rem;
}

.b95-section-eyebrow {
  font-family: var(--b95-font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--b95-text-muted);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.b95-eyebrow-accent {
  color: var(--b95-accent);
}

.b95-section-title-wrap {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

.b95-section-title {
  font-family: var(--b95-font-main);
  font-size: 2.75rem;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.03em;
  color: var(--b95-text-primary);
}

.b95-section-subtitle {
  font-family: var(--b95-font-main);
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--b95-text-muted);
  letter-spacing: -0.01em;
}

.b95-section-lead {
  font-size: 1.05rem;
  line-height: 1.68;
  color: var(--b95-text-secondary);
  max-width: 860px;
  margin: 0;
}

/* ==========================================================================
   1. SECTION: OUR SERVICES (01 TO 08)
   ========================================================================== */
.b95-services-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.b95-service-card {
  position: relative;
  background-color: var(--b95-bg-primary);
  border: 1px solid var(--b95-border);
  padding: 2.5rem 1.85rem 2.25rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  transition: var(--b95-transition-transform);
  cursor: default;
  outline: none;
}

.b95-service-card:hover,
.b95-service-card:focus-visible {
  transform: translateY(-4px);
  border-color: var(--b95-border-strong);
  box-shadow: 0 12px 28px -8px rgba(15, 23, 42, 0.07);
}

.b95-service-card__top {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 2rem;
  border-bottom: 1px solid var(--b95-border-subtle);
  padding-bottom: 1rem;
}

.b95-service-card__number {
  font-family: var(--b95-font-mono);
  font-size: 2rem;
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.04em;
  color: var(--b95-text-primary);
  transition: color 0.2s ease;
}

.b95-service-card:hover .b95-service-card__number {
  color: var(--b95-accent);
}

.b95-service-card__badge {
  font-family: var(--b95-font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--b95-text-muted);
  background-color: var(--b95-surface-secondary);
  padding: 0.25rem 0.55rem;
  border-radius: 2px;
}

.b95-service-card__title {
  font-family: var(--b95-font-main);
  font-size: 1.15rem;
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -0.02em;
  color: var(--b95-text-primary);
  margin-bottom: 1rem;
}

.b95-service-card__desc {
  font-size: 0.92rem;
  line-height: 1.65;
  color: var(--b95-text-secondary);
  margin: 0;
}

.b95-service-card__accent-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 2px;
  background-color: var(--b95-accent);
  transition: width 0.3s var(--b95-ease-out);
}

.b95-service-card:hover .b95-service-card__accent-bar {
  width: 100%;
}

/* ==========================================================================
   2. SECTION: REFERENCES & REGIONAL REACH
   ========================================================================== */
.b95-references-layout {
  display: grid;
  grid-template-columns: 380px 1fr;
  gap: 2.25rem;
  align-items: flex-start;
}

.b95-footprint-panel {
  position: sticky;
  top: 6rem;
}

.b95-footprint-card {
  background-color: var(--b95-bg-primary);
  border: 1px solid var(--b95-border);
  padding: 2.25rem;
}

.b95-footprint-card__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem;
  padding-bottom: 0.85rem;
  border-bottom: 1px solid var(--b95-border-subtle);
}

.b95-footprint-tag {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--b95-accent);
}

.b95-footprint-coords {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  color: var(--b95-text-muted);
}

.b95-footprint-card__title {
  font-family: var(--b95-font-main);
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--b95-text-primary);
  letter-spacing: -0.02em;
  margin-bottom: 0.75rem;
}

.b95-footprint-card__desc {
  font-size: 0.92rem;
  line-height: 1.65;
  color: var(--b95-text-secondary);
  margin-bottom: 1.75rem;
}

.b95-footprint-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  padding: 1.25rem 0;
  border-top: 1px solid var(--b95-border-subtle);
  border-bottom: 1px solid var(--b95-border-subtle);
  margin-bottom: 1.5rem;
}

.b95-stat-value {
  display: block;
  font-family: var(--b95-font-main);
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--b95-text-primary);
  line-height: 1;
  margin-bottom: 0.35rem;
}

.b95-stat-label {
  display: block;
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--b95-text-muted);
  line-height: 1.35;
}

.b95-footprint-map-wrap {
  width: 100%;
  border: 1px solid var(--b95-border-subtle);
  background-color: var(--b95-surface-secondary);
  padding: 1rem;
}

.b95-footprint-map {
  width: 100%;
  height: auto;
  display: block;
}

/* References Data Matrix Grid */
.b95-matrix-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.b95-ref-card {
  background-color: var(--b95-bg-primary);
  border: 1px solid var(--b95-border);
  padding: 2rem 1.85rem;
  display: flex;
  flex-direction: column;
  transition: var(--b95-transition-transform);
  cursor: default;
  outline: none;
}

.b95-ref-card:hover,
.b95-ref-card:focus-visible {
  transform: translateY(-4px);
  border-color: var(--b95-border-strong);
  box-shadow: 0 12px 28px -8px rgba(15, 23, 42, 0.07);
}

.b95-ref-card__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.15rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--b95-border-subtle);
}

.b95-ref-card__location {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--b95-font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--b95-accent);
}

.b95-icon-pin {
  width: 12px;
  height: 12px;
  flex-shrink: 0;
}

.b95-ref-card__badge {
  font-family: var(--b95-font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--b95-text-secondary);
  background-color: var(--b95-surface-secondary);
  padding: 0.25rem 0.55rem;
  border-radius: 2px;
}

.b95-ref-card__title {
  font-family: var(--b95-font-main);
  font-size: 1.18rem;
  font-weight: 700;
  line-height: 1.35;
  letter-spacing: -0.02em;
  color: var(--b95-text-primary);
  margin-bottom: 0.85rem;
}

.b95-ref-card__scope {
  font-size: 0.9rem;
  line-height: 1.62;
  color: var(--b95-text-muted);
  margin: 0;
}

/* ==========================================================================
   3. SECTION: FEATURED PROJECT / CASE STUDY
   ========================================================================== */
.b95-case-study-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3.5rem;
  align-items: start;
}

.b95-case-meta-bar {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 1.75rem;
}

.b95-meta-pill {
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.35rem 0.8rem;
  border: 1px solid var(--b95-border);
  background-color: var(--b95-surface-secondary);
  color: var(--b95-text-secondary);
  border-radius: 2px;
}

.b95-meta-pill--endorse {
  border-color: rgba(185, 28, 28, 0.35);
  background-color: var(--b95-accent-subtle);
  color: var(--b95-accent-dark);
  font-weight: 700;
}

.b95-case-lead {
  font-size: 1.12rem;
  line-height: 1.68;
  font-weight: 500;
  color: var(--b95-text-primary);
  margin-bottom: 1.25rem;
}

.b95-case-body {
  font-size: 0.96rem;
  line-height: 1.7;
  color: var(--b95-text-secondary);
  margin-bottom: 2.5rem;
}

/* Technical Specification Callout Metrics Grid (2x2) */
.b95-metrics-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.25rem;
  border-top: 1px solid var(--b95-border);
  padding-top: 2rem;
}

.b95-metric-card {
  background-color: var(--b95-surface-secondary);
  border: 1px solid var(--b95-border);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  transition: var(--b95-transition);
}

.b95-metric-card:hover {
  background-color: var(--b95-bg-primary);
  border-color: var(--b95-accent);
  transform: translateY(-2px);
}

.b95-metric-card__value {
  font-family: var(--b95-font-main);
  font-size: 2.1rem;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.04em;
  color: var(--b95-accent);
  margin-bottom: 0.4rem;
}

.b95-metric-card__title {
  font-family: var(--b95-font-main);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--b95-text-primary);
  margin-bottom: 0.35rem;
  line-height: 1.3;
}

.b95-metric-card__desc {
  font-size: 0.82rem;
  line-height: 1.55;
  color: var(--b95-text-muted);
  margin: 0;
}

/* Case Study Media Gallery (Hero View + Subgrid) */
.b95-case-study-media {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.b95-media-hero {
  position: relative;
  border: 1px solid var(--b95-border);
  background-color: #000;
  overflow: hidden;
}

.b95-media-hero .b95-media-img {
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
  display: block;
  transition: transform 0.6s var(--b95-ease-out);
}

.b95-media-hero:hover .b95-media-img {
  transform: scale(1.025);
}

.b95-media-badge {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(15, 23, 42, 0.92) 0%, rgba(15, 23, 42, 0.4) 65%, transparent 100%);
  padding: 1.75rem 1.5rem 1.25rem;
  color: #FFFFFF;
}

.b95-media-badge span {
  display: block;
  font-family: var(--b95-font-mono);
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: #E2E8F0;
  margin-bottom: 0.25rem;
}

.b95-media-badge strong {
  display: block;
  font-family: var(--b95-font-main);
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -0.01em;
}

.b95-media-subgrid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.b95-media-subcard {
  border: 1px solid var(--b95-border);
  background-color: var(--b95-bg-primary);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.b95-media-subcard .b95-media-img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  display: block;
  transition: transform 0.5s var(--b95-ease-out);
}

.b95-media-subcard:hover .b95-media-img {
  transform: scale(1.04);
}

.b95-media-caption {
  font-family: var(--b95-font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--b95-text-muted);
  padding: 0.75rem 0.65rem;
  background-color: var(--b95-surface-secondary);
  border-top: 1px solid var(--b95-border);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ==========================================================================
   RESPONSIVENESS (BREAKPOINTS: 1024px & 640px)
   ========================================================================== */
@media (max-width: 1024px) {
  .b95-services-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .b95-references-layout {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }

  .b95-footprint-panel {
    position: static;
  }

  .b95-case-study-layout {
    grid-template-columns: 1fr;
    gap: 2.75rem;
  }
}

@media (max-width: 640px) {
  .b95-section {
    padding: 4.5rem 0;
  }

  .b95-container {
    padding: 0 1.25rem;
  }

  .b95-section-title {
    font-size: 2.1rem;
  }

  .b95-services-grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .b95-matrix-grid {
    grid-template-columns: 1fr;
  }

  .b95-metrics-grid {
    grid-template-columns: 1fr;
  }

  .b95-media-subgrid {
    grid-template-columns: 1fr;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

print("Appended Pure CSS rules to styles.css successfully!")
