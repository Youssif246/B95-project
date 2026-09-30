# Build and append the complete pure CSS
css_additions = '''
/* ==========================================================================
   B95 PROJECT — PRINCIPAL ARCHITECTURAL DESIGN SYSTEM & COMPONENT MODULES
   Pure CSS3: Variables, Flexbox, CSS Grid, Media Queries, Zero Frameworks
   Sections: Services (2-Spread) · References (Elevated Footprint) · Case Study
   ========================================================================== */

:root {
  /* Extended Architectural Monograph Tokens */
  --b95-accent: #B91C1C;
  --b95-accent-dark: #991B1B;
  --b95-accent-subtle: rgba(185, 28, 28, 0.08);
  --b95-accent-glow: rgba(185, 28, 28, 0.25);
  
  --b95-slate-900: #0F172A;
  --b95-slate-800: #1E293B;
  --b95-slate-700: #334155;
  --b95-slate-600: #475569;
  --b95-slate-500: #64748B;
  --b95-slate-400: #94A3B8;
  --b95-slate-200: #E2E8F0;
  --b95-slate-100: #F1F5F9;
  --b95-slate-50:  #F8FAFC;
  
  --b95-border: #E2E8F0;
  --b95-border-strong: #CBD5E1;
  --b95-border-dark: #1E293B;
  
  --b95-ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --b95-transition-fast: all 0.2s var(--b95-ease-out);
  --b95-transition-card: transform 0.3s var(--b95-ease-out), border-color 0.3s ease, box-shadow 0.3s ease;
}

/* ==========================================================================
   SECTION 1: SERVICES (2-SPREAD ARCHITECTURE)
   ========================================================================== */
.b95-services-spread {
  background-color: #FFFFFF;
}

.b95-services-spread--alt {
  background-color: var(--b95-slate-50);
  border-top: 1px solid var(--b95-border);
}

.b95-services-spread-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

.b95-service-spread-card {
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: var(--b95-transition-card);
  cursor: pointer;
  outline: none;
}

.b95-service-spread-card:hover,
.b95-service-spread-card:focus-visible {
  transform: translateY(-6px);
  border-color: var(--b95-border-strong);
  box-shadow: 0 20px 35px -10px rgba(15, 23, 42, 0.08);
}

.b95-card-media-thumb {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 8;
  overflow: hidden;
  background-color: var(--b95-slate-900);
}

.b95-card-media-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s var(--b95-ease-out);
}

.b95-service-spread-card:hover .b95-card-media-thumb img {
  transform: scale(1.05);
}

.b95-card-badge-top {
  position: absolute;
  top: 1rem;
  left: 1rem;
  right: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 2;
}

.b95-card-num {
  font-family: var(--b95-font-mono);
  font-size: 1.15rem;
  font-weight: 800;
  color: #FFFFFF;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  padding: 0.3rem 0.75rem;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.b95-card-cat {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #FFFFFF;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  padding: 0.35rem 0.8rem;
  border: 1px solid rgba(255, 255, 255, 0.15);
  display: flex;
  align-items: center;
  gap: 0.45rem;
}

.b95-card-cat i {
  color: var(--b95-accent);
}

.b95-card-body {
  padding: 2.25rem 2rem 1.85rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.b95-card-title {
  font-family: var(--b95-font-main);
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -0.02em;
  color: var(--b95-slate-900);
  margin-bottom: 0.85rem;
  transition: color 0.2s ease;
}

.b95-service-spread-card:hover .b95-card-title {
  color: var(--b95-accent);
}

.b95-card-desc {
  font-size: 0.95rem;
  line-height: 1.65;
  color: var(--b95-slate-700);
  margin-bottom: 1.75rem;
  flex-grow: 1;
}

.b95-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--b95-border);
  padding-top: 1rem;
}

.b95-card-phase {
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--b95-slate-500);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.b95-card-arrow {
  color: var(--b95-slate-400);
  font-size: 0.85rem;
  transition: transform 0.25s var(--b95-ease-out), color 0.25s ease;
}

.b95-service-spread-card:hover .b95-card-arrow {
  transform: translateX(5px);
  color: var(--b95-accent);
}

/* ==========================================================================
   SECTION 2: REFERENCES & REGIONAL REACH (ELEVATED GLOBAL FOOTPRINT)
   ========================================================================== */
.b95-references-elevated {
  background-color: #FFFFFF;
}

.b95-footprint-showcase {
  margin-bottom: 3.5rem;
}

.b95-footprint-graphic-box {
  background-color: var(--b95-slate-900);
  border: 1px solid var(--b95-slate-800);
  overflow: hidden;
  box-shadow: 0 20px 40px -15px rgba(15, 23, 42, 0.4);
}

.b95-footprint-graphic-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.15rem 1.75rem;
  background-color: rgba(15, 23, 42, 0.95);
  border-bottom: 1px solid var(--b95-slate-800);
}

.b95-graphic-indicator {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #E2E8F0;
}

.b95-pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--b95-accent);
  box-shadow: 0 0 10px var(--b95-accent);
  animation: b95-pulse-glow 2s infinite;
}

@keyframes b95-pulse-glow {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(185, 28, 28, 0.7); }
  70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(185, 28, 28, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(185, 28, 28, 0); }
}

.b95-svg-pulse-ring {
  transform-origin: center;
  animation: b95-ring-expand 2.5s cubic-bezier(0.25, 1, 0.5, 1) infinite;
}

@keyframes b95-ring-expand {
  0% { r: 6; opacity: 0.9; }
  100% { r: 24; opacity: 0; }
}

.b95-graphic-coords {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  color: var(--b95-slate-400);
  letter-spacing: 0.05em;
}

.b95-map-canvas-container {
  padding: 1.5rem 1rem;
  background: radial-gradient(circle at 30% 30%, #1E293B 0%, #0F172A 70%);
}

.b95-elevated-map-svg {
  width: 100%;
  height: auto;
  display: block;
}

/* Quick Metrics Ribbon */
.b95-metrics-ribbon {
  display: grid;
  grid-template-columns: 1fr auto 1fr auto 1fr;
  align-items: center;
  background-color: #0B1120;
  border-top: 1px solid var(--b95-slate-800);
  padding: 1.5rem 2.5rem;
}

.b95-ribbon-item {
  display: flex;
  align-items: baseline;
  gap: 0.85rem;
}

.b95-ribbon-val {
  font-family: var(--b95-font-main);
  font-size: 1.85rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: #FFFFFF;
}

.b95-ribbon-label {
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--b95-slate-400);
}

.b95-ribbon-divider {
  width: 1px;
  height: 28px;
  background-color: var(--b95-slate-800);
}

/* Architectural Project Rows Table */
.b95-projects-rows-wrap {
  border: 1px solid var(--b95-border);
  background-color: #FFFFFF;
}

.b95-projects-table-header {
  display: grid;
  grid-template-columns: 210px 180px 320px 1fr;
  gap: 1.5rem;
  padding: 1rem 1.75rem;
  background-color: var(--b95-slate-100);
  border-bottom: 1px solid var(--b95-border);
  font-family: var(--b95-font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--b95-slate-500);
}

.b95-project-row {
  display: grid;
  grid-template-columns: 210px 180px 320px 1fr;
  gap: 1.5rem;
  align-items: center;
  padding: 1.45rem 1.75rem;
  border-bottom: 1px solid var(--b95-border);
  border-left: 3px solid transparent;
  transition: all 0.2s var(--b95-ease-out);
  cursor: default;
}

.b95-project-row:last-child {
  border-bottom: none;
}

.b95-project-row:hover {
  background-color: var(--b95-slate-50);
  border-left-color: var(--b95-accent);
  box-shadow: 0 4px 15px rgba(15, 23, 42, 0.03);
}

.b95-row-loc {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  font-family: var(--b95-font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--b95-slate-900);
}

.b95-pin-red {
  color: var(--b95-accent);
  font-size: 0.85rem;
}

.b95-sector-tag {
  display: inline-block;
  font-family: var(--b95-font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.3rem 0.65rem;
  border-radius: 2px;
  background-color: var(--b95-slate-100);
  color: var(--b95-slate-700);
  border: 1px solid var(--b95-border);
}

.b95-sector-tag--sports { background: #FEF2F2; color: #991B1B; border-color: #FCA5A5; }
.b95-sector-tag--infra { background: #F0FDF4; color: #166534; border-color: #86EFAC; }
.b95-sector-tag--aviation { background: #EFF6FF; color: #1E40AF; border-color: #93C5FD; }
.b95-sector-tag--diplomatic { background: #FAF5FF; color: #6B21A8; border-color: #D8B4FE; }
.b95-sector-tag--health { background: #ECFDF5; color: #065F46; border-color: #6EE7B7; }
.b95-sector-tag--urban { background: #FFFBEB; color: #92400E; border-color: #FDE68A; }
.b95-sector-tag--comm { background: #F8FAFC; color: #334155; border-color: #CBD5E1; }

.b95-row-title h3 {
  font-family: var(--b95-font-main);
  font-size: 1.05rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--b95-slate-900);
  letter-spacing: -0.01em;
}

.b95-row-deliverable span {
  font-size: 0.88rem;
  line-height: 1.55;
  color: var(--b95-slate-600);
}

/* ==========================================================================
   SECTION 3: FEATURED PROJECT / CASE STUDY (MONOGRAPH SPEC)
   ========================================================================== */
.b95-case-study-monograph {
  background-color: var(--b95-slate-50);
}

.b95-case-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 2rem;
  padding-bottom: 2.25rem;
  border-bottom: 1px solid var(--b95-border);
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.b95-case-headline {
  font-family: var(--b95-font-main);
  font-size: 2.75rem;
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: var(--b95-slate-900);
  margin: 0.35rem 0 0.65rem;
}

.b95-case-sublocation {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--b95-font-mono);
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--b95-slate-600);
}

.b95-case-seals {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.b95-seal-pill {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.85rem 1.25rem;
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
}

.b95-seal-pill i {
  font-size: 1.35rem;
  color: var(--b95-slate-700);
}

.b95-seal-pill--commend {
  border-color: rgba(185, 28, 28, 0.3);
  background-color: #FEF2F2;
}

.b95-seal-pill--commend i {
  color: var(--b95-accent);
}

.b95-seal-sub {
  display: block;
  font-family: var(--b95-font-mono);
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--b95-slate-500);
}

.b95-seal-bold {
  display: block;
  font-family: var(--b95-font-main);
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--b95-slate-900);
}

/* Wide Hero Display */
.b95-case-hero-stage {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  border: 1px solid var(--b95-border);
  background-color: #000;
  overflow: hidden;
  margin-bottom: 3.5rem;
  box-shadow: 0 20px 45px -15px rgba(15, 23, 42, 0.15);
}

.b95-case-hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.b95-case-hero-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(15, 23, 42, 0.95) 0%, rgba(15, 23, 42, 0.4) 65%, transparent 100%);
  padding: 2.25rem 2.5rem 1.75rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  color: #FFFFFF;
  flex-wrap: wrap;
  gap: 1rem;
}

.b95-hero-kicker {
  display: block;
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: #94A3B8;
  margin-bottom: 0.35rem;
}

.b95-hero-status {
  display: block;
  font-family: var(--b95-font-main);
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.b95-hero-coords span {
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  color: #CBD5E1;
  background: rgba(15, 23, 42, 0.75);
  padding: 0.35rem 0.85rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Two-Column Engineering Breakdown */
.b95-case-breakdown-grid {
  display: grid;
  grid-template-columns: 1.25fr 1fr;
  gap: 3.5rem;
  margin-bottom: 4rem;
  align-items: start;
}

.b95-case-narrative-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  font-family: var(--b95-font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--b95-accent);
  background-color: var(--b95-accent-subtle);
  padding: 0.4rem 0.85rem;
  margin-bottom: 1.5rem;
}

.b95-story-lead {
  font-size: 1.15rem;
  line-height: 1.7;
  font-weight: 500;
  color: var(--b95-slate-900);
  margin-bottom: 1.25rem;
}

.b95-story-text {
  font-size: 0.96rem;
  line-height: 1.75;
  color: var(--b95-slate-700);
  margin-bottom: 1.25rem;
}

.b95-specs-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.b95-spec-card {
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  padding: 1.85rem 1.6rem;
  display: flex;
  flex-direction: column;
  transition: var(--b95-transition-card);
}

.b95-spec-card:hover {
  transform: translateY(-4px);
  border-color: var(--b95-accent);
  box-shadow: 0 12px 28px -8px rgba(15, 23, 42, 0.08);
}

.b95-spec-stat {
  font-family: var(--b95-font-main);
  font-size: 2.25rem;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.04em;
  color: var(--b95-accent);
  margin-bottom: 0.5rem;
}

.b95-spec-name {
  font-family: var(--b95-font-main);
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--b95-slate-900);
  margin-bottom: 0.45rem;
}

.b95-spec-desc {
  font-size: 0.82rem;
  line-height: 1.6;
  color: var(--b95-slate-500);
  margin: 0;
}

/* Bottom Gallery Strip (3-Image Sequence) */
.b95-case-gallery-strip {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.b95-strip-item {
  background-color: #FFFFFF;
  border: 1px solid var(--b95-border);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: var(--b95-transition-card);
}

.b95-strip-item:hover {
  transform: translateY(-4px);
  border-color: var(--b95-border-strong);
  box-shadow: 0 14px 30px -10px rgba(15, 23, 42, 0.08);
}

.b95-strip-frame {
  width: 100%;
  aspect-ratio: 16 / 11;
  overflow: hidden;
  background-color: var(--b95-slate-900);
}

.b95-strip-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s var(--b95-ease-out);
}

.b95-strip-item:hover .b95-strip-frame img {
  transform: scale(1.05);
}

.b95-strip-meta {
  padding: 1rem 1.15rem;
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
  background-color: #FFFFFF;
  border-top: 1px solid var(--b95-border);
}

.b95-strip-num {
  font-family: var(--b95-font-mono);
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--b95-accent);
}

.b95-strip-caption {
  font-family: var(--b95-font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--b95-slate-700);
  line-height: 1.4;
}

/* ==========================================================================
   MEDIA QUERIES & RESPONSIVE BEHAVIOR
   ========================================================================== */
@media (max-width: 1024px) {
  .b95-services-spread-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .b95-metrics-ribbon {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .b95-ribbon-divider {
    display: none;
  }

  .b95-projects-table-header {
    display: none;
  }

  .b95-project-row {
    grid-template-columns: 1fr;
    gap: 0.65rem;
    padding: 1.5rem 1.25rem;
  }

  .b95-case-breakdown-grid {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }

  .b95-case-gallery-strip {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }
}

@media (max-width: 640px) {
  .b95-case-headline {
    font-size: 2rem;
  }

  .b95-specs-grid {
    grid-template-columns: 1fr;
  }

  .b95-card-media-thumb {
    aspect-ratio: 16 / 10;
  }
}
'''

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)

print("Successfully added architectural CSS rules to styles.css!")
