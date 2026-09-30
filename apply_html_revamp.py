import os

# 1. READ HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Section 1: Services HTML
services_html = '''    <!-- ====================================================================
         SECTION 01: OUR SERVICES (01 TO 08 TURNKEY SOLUTIONS)
         Industrial Luxury / Architectural Monograph Grid
         ==================================================================== -->
    <section class="b95-section b95-services" id="sec-services" aria-labelledby="services-title">
      <div class="b95-container">
        <header class="b95-section-header">
          <div class="b95-section-eyebrow">
            <span class="b95-eyebrow-accent">01</span> / TURNKEY SOLUTIONS
          </div>
          <div class="b95-section-title-wrap">
            <h2 class="b95-section-title" id="services-title">Our Services</h2>
            <span class="b95-section-subtitle">Multidisciplinary Engineering &amp; General Contracting</span>
          </div>
          <p class="b95-section-lead">
            An integrated execution framework managing every operational tier from advanced feasibility analysis and statutory regulatory governance to precision procurement, turnkey erection, and lifecycle facility handover.
          </p>
        </header>

        <!-- Modern CSS Grid (4 Columns Desktop / 2 Columns Tablet / 1 Column Mobile) -->
        <div class="b95-services-grid">
          <!-- 01 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">01</span>
              <span class="b95-service-card__badge">Consultancy</span>
            </div>
            <h3 class="b95-service-card__title">Planning &amp; Engineering Consultancy</h3>
            <p class="b95-service-card__desc">
              Multidisciplinary feasibility, advanced structural modeling, and strategic execution roadmaps mitigating risk and optimizing capital expenditure.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>

          <!-- 02 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">02</span>
              <span class="b95-service-card__badge">Procurement</span>
            </div>
            <h3 class="b95-service-card__title">Material Specifications &amp; Procurement</h3>
            <p class="b95-service-card__desc">
              Rigorous BOQ quantification, global material sourcing, and value-engineering ensuring highest tier certifications within budget.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>

          <!-- 03 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">03</span>
              <span class="b95-service-card__badge">Governance</span>
            </div>
            <h3 class="b95-service-card__title">Legal Governance &amp; Contract Administration</h3>
            <p class="b95-service-card__desc">
              Turnkey regulatory alignment, statutory compliance under Turkish &amp; regional jurisdictions, and risk-proofed commercial contracts.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>

          <!-- 04 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">04</span>
              <span class="b95-service-card__badge">Supply Chain</span>
            </div>
            <h3 class="b95-service-card__title">Supply Chain &amp; Vendor Management</h3>
            <p class="b95-service-card__desc">
              Strategic vendor vetting, enterprise-grade brand procurement, and transparent tracking from origin to staging.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>

          <!-- 05 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">05</span>
              <span class="b95-service-card__badge">QA / QC</span>
            </div>
            <h3 class="b95-service-card__title">Quality Assurance &amp; Factory Inspection</h3>
            <p class="b95-service-card__desc">
              Rigorous QA/QC protocols, on-site manufacturing audits, and strict compliance verification prior to dispatch.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>

          <!-- 06 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">06</span>
              <span class="b95-service-card__badge">Logistics</span>
            </div>
            <h3 class="b95-service-card__title">Global Freight &amp; Customs Logistics</h3>
            <p class="b95-service-card__desc">
              End-to-end multimodal transport (air/sea/land), streamlined customs clearance, and precision site delivery.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>

          <!-- 07 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">07</span>
              <span class="b95-service-card__badge">Contracting</span>
            </div>
            <h3 class="b95-service-card__title">Execution &amp; General Contracting</h3>
            <p class="b95-service-card__desc">
              Turnkey structural erection, electro-mechanical (MEP) installations, high-spec interior fit-outs, and architectural finishing.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>

          <!-- 08 -->
          <article class="b95-service-card" tabindex="0">
            <div class="b95-service-card__top">
              <span class="b95-service-card__number">08</span>
              <span class="b95-service-card__badge">Lifecycle</span>
            </div>
            <h3 class="b95-service-card__title">Lifecycle Handover &amp; Facility Maintenance</h3>
            <p class="b95-service-card__desc">
              Post-completion warranty enforcement, technical operations handover, and continuous operational readiness training.
            </p>
            <div class="b95-service-card__accent-bar" aria-hidden="true"></div>
          </article>
        </div>
      </div>
    </section>
'''

# Section 3: References HTML
references_html = '''    <!-- ====================================================================
         SECTION 03: REFERENCES & OPERATIONAL FOOTPRINT
         Asymmetric Split Layout & Clean Project Matrix
         ==================================================================== -->
    <section class="b95-section b95-references" id="sec-references" aria-labelledby="references-title">
      <div class="b95-container">
        <header class="b95-section-header">
          <div class="b95-section-eyebrow">
            <span class="b95-eyebrow-accent">02</span> / OPERATIONAL FOOTPRINT
          </div>
          <div class="b95-section-title-wrap">
            <h2 class="b95-section-title" id="references-title">References &amp; Regional Reach</h2>
            <span class="b95-section-subtitle">Cross-Border Infrastructure, Civic &amp; Healthcare Portfolios</span>
          </div>
          <p class="b95-section-lead">
            With corporate headquarters anchored in Istanbul, B95 PROJECT delivers mission-critical general contracting, aviation infrastructure, and diplomatic-grade engineering across key operational theaters in Türkiye, Iraq, Bahrain, Libya, and Syria.
          </p>
        </header>

        <!-- 2-Column Asymmetric Split: Left Architectural Footprint / Right Project Data Matrix -->
        <div class="b95-references-layout">
          <!-- Left Column: Regional Reach Overview & Spatial Diagram -->
          <aside class="b95-footprint-panel">
            <div class="b95-footprint-card">
              <div class="b95-footprint-card__header">
                <span class="b95-footprint-tag">Regional Vector</span>
                <span class="b95-footprint-coords">41.0082° N, 28.9784° E</span>
              </div>
              <h3 class="b95-footprint-card__title">Strategic Operations Hub</h3>
              <p class="b95-footprint-card__desc">
                Centralized project governance, procurement orchestration, and engineering design directed from Istanbul HQ, executing across regional hubs in the Middle East &amp; North Africa.
              </p>

              <!-- Regional Nodes Matrix -->
              <div class="b95-footprint-stats">
                <div class="b95-footprint-stat">
                  <span class="b95-stat-value">05</span>
                  <span class="b95-stat-label">Active Sovereign Theaters</span>
                </div>
                <div class="b95-footprint-stat">
                  <span class="b95-stat-value">100%</span>
                  <span class="b95-stat-label">On-Spec Delivery Track</span>
                </div>
              </div>

              <!-- Stylized Regional Architectural Map -->
              <div class="b95-footprint-map-wrap" aria-label="Geographic project footprint diagram">
                <svg class="b95-footprint-map" viewBox="0 0 360 260" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <!-- Subtle Grid System -->
                  <line x1="20" y1="65" x2="340" y2="65" stroke="var(--b95-border)" stroke-width="0.75" stroke-dasharray="2 3"/>
                  <line x1="20" y1="130" x2="340" y2="130" stroke="var(--b95-border)" stroke-width="0.75" stroke-dasharray="2 3"/>
                  <line x1="20" y1="195" x2="340" y2="195" stroke="var(--b95-border)" stroke-width="0.75" stroke-dasharray="2 3"/>

                  <!-- Architectural Trajectories from Istanbul HQ -->
                  <line x1="100" y1="55" x2="160" y2="115" stroke="var(--b95-text-secondary)" stroke-width="0.8" opacity="0.3"/>
                  <line x1="100" y1="55" x2="220" y2="130" stroke="var(--b95-text-secondary)" stroke-width="0.8" opacity="0.3"/>
                  <line x1="100" y1="55" x2="260" y2="175" stroke="var(--b95-text-secondary)" stroke-width="0.8" opacity="0.3"/>
                  <line x1="100" y1="55" x2="300" y2="195" stroke="var(--b95-text-secondary)" stroke-width="0.8" opacity="0.3"/>
                  <line x1="100" y1="55" x2="55" y2="185" stroke="var(--b95-text-secondary)" stroke-width="0.8" opacity="0.3"/>

                  <!-- Istanbul HQ Point -->
                  <circle cx="100" cy="55" r="4.5" fill="var(--b95-accent)"/>
                  <circle cx="100" cy="55" r="9" stroke="var(--b95-accent)" stroke-width="0.75" opacity="0.4"/>
                  <text x="100" y="42" fill="var(--b95-text-primary)" font-family="var(--b95-font-main)" font-weight="700" font-size="9" text-anchor="middle" letter-spacing="0.5">ISTANBUL (HQ)</text>

                  <!-- Baghdad Node -->
                  <circle cx="220" cy="130" r="4" fill="var(--b95-accent)"/>
                  <text x="220" y="120" fill="var(--b95-text-primary)" font-family="var(--b95-font-main)" font-weight="700" font-size="8" text-anchor="middle">BAGHDAD</text>

                  <!-- Basra Node -->
                  <circle cx="260" cy="175" r="4" fill="var(--b95-accent)"/>
                  <text x="260" y="193" fill="var(--b95-text-primary)" font-family="var(--b95-font-main)" font-weight="700" font-size="8" text-anchor="middle">BASRA</text>

                  <!-- Manama Node -->
                  <circle cx="300" cy="195" r="3.5" fill="var(--b95-text-secondary)"/>
                  <text x="300" y="213" fill="var(--b95-text-muted)" font-family="var(--b95-font-main)" font-weight="600" font-size="7.5" text-anchor="middle">MANAMA</text>

                  <!-- Benghazi Node -->
                  <circle cx="55" cy="185" r="3.5" fill="var(--b95-text-secondary)"/>
                  <text x="55" y="203" fill="var(--b95-text-muted)" font-family="var(--b95-font-main)" font-weight="600" font-size="7.5" text-anchor="middle">BENGHAZI</text>

                  <!-- Northern Syria Node -->
                  <circle cx="160" cy="115" r="3.5" fill="var(--b95-text-secondary)"/>
                  <text x="160" y="105" fill="var(--b95-text-muted)" font-family="var(--b95-font-main)" font-weight="600" font-size="7.5" text-anchor="middle">N. SYRIA</text>
                </svg>
              </div>
            </div>
          </aside>

          <!-- Right Column: Clean Data Matrix / Minimalist Cards -->
          <div class="b95-matrix-grid">
            <!-- Reference 01 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Baghdad, Iraq
                </span>
                <span class="b95-ref-card__badge">Sports &amp; Aviation</span>
              </div>
              <h3 class="b95-ref-card__title">Al-Shaab Stadium Turf Lighting Systems</h3>
              <p class="b95-ref-card__scope">Turnkey engineering, structural aluminum mobile truss fabrication, and 9-unit Philips horticultural optical systems deployment.</p>
            </article>

            <!-- Reference 02 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Safwan Highway, Iraq-Kuwait Border
                </span>
                <span class="b95-ref-card__badge">Infrastructure &amp; Civil</span>
              </div>
              <h3 class="b95-ref-card__title">Dual-Mast Highway Lighting Infrastructure</h3>
              <p class="b95-ref-card__scope">Installation of 12-meter double-arm decorative and high-illuminance galvanized masts for international strategic transit corridor.</p>
            </article>

            <!-- Reference 03 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Basra International Airport
                </span>
                <span class="b95-ref-card__badge">Aviation &amp; Transport</span>
              </div>
              <h3 class="b95-ref-card__title">Terminal Rehabilitation &amp; Architectural Modernization</h3>
              <p class="b95-ref-card__scope">Civil renovation, acoustic and structural ceiling systems, passenger terminal finishes, and technical MEP integration.</p>
            </article>

            <!-- Reference 04 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Manama, Kingdom of Bahrain
                </span>
                <span class="b95-ref-card__badge">Diplomatic &amp; Civic</span>
              </div>
              <h3 class="b95-ref-card__title">33rd Arab Summit Royal Diplomatic Conference Hall Fit-Out</h3>
              <p class="b95-ref-card__scope">Execution of royal-standard interior architecture, custom luxury woodwork, executive VIP acoustics, and diplomatic plenary installations.</p>
            </article>

            <!-- Reference 05 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Benghazi, Libya
                </span>
                <span class="b95-ref-card__badge">Healthcare &amp; Medical</span>
              </div>
              <h3 class="b95-ref-card__title">Akam Al-Sonwan Specialty Hospital</h3>
              <p class="b95-ref-card__scope">Turnkey clinical fit-out, certified antibacterial medical flooring, clinical partition panels, ICU finishing, and sterile environments.</p>
            </article>

            <!-- Reference 06 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Northern Syria
                </span>
                <span class="b95-ref-card__badge">Residential &amp; Urban</span>
              </div>
              <h3 class="b95-ref-card__title">2000 Sustainable Housing Units &amp; Civil Infrastructure Development</h3>
              <p class="b95-ref-card__scope">Master-planning, modular structural casting, community utility infrastructure networks, and turnkey residential unit construction.</p>
            </article>

            <!-- Reference 07 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Basra, Iraq
                </span>
                <span class="b95-ref-card__badge">Municipal Infrastructure</span>
              </div>
              <h3 class="b95-ref-card__title">Basra Sports City Roadway High-Mast Illumination (96 Units)</h3>
              <p class="b95-ref-card__scope">Civil foundation casting, delivery, and high-performance luminaire integration of 96 roadway masts serving the Sports City complex.</p>
            </article>

            <!-- Reference 08 -->
            <article class="b95-ref-card" tabindex="0">
              <div class="b95-ref-card__header">
                <span class="b95-ref-card__location">
                  <svg class="b95-icon-pin" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C4.7 0 2 2.7 2 6c0 4.5 6 10 6 10s6-5.5 6-10c0-3.3-2.7-6-6-6zm0 8.5c-1.4 0-2.5-1.1-2.5-2.5S6.6 3.5 8 3.5 10.5 4.6 10.5 6 9.4 8.5 8 8.5z"/></svg>
                  Istanbul, Türkiye
                </span>
                <span class="b95-ref-card__badge">Commercial Architecture</span>
              </div>
              <h3 class="b95-ref-card__title">46th Turkeybuild International Exhibition Pavilion</h3>
              <p class="b95-ref-card__scope">Conceptual architectural design, bespoke structural booth fabrication, dynamic lighting, and international delegate hospitality staging.</p>
            </article>
          </div>
        </div>
      </div>
    </section>
'''

# Section 4: Featured Project / Case Study HTML
featured_html = '''    <!-- ====================================================================
         SECTION 04: FEATURED PROJECT / CASE STUDY
         Two-Column Editorial Monograph & Spec Callouts
         ==================================================================== -->
    <section class="b95-section b95-case-study" id="sec-featured" aria-labelledby="case-study-title">
      <div class="b95-container">
        <header class="b95-section-header">
          <div class="b95-section-eyebrow">
            <span class="b95-eyebrow-accent">03</span> / FEATURED CASE STUDY
          </div>
          <div class="b95-section-title-wrap">
            <h2 class="b95-section-title" id="case-study-title">Artificial Turf Photosynthesis Lighting Units</h2>
            <span class="b95-section-subtitle">Al-Shaab International Stadium · Baghdad, Iraq</span>
          </div>
        </header>

        <!-- Two-Column Editorial Layout -->
        <div class="b95-case-study-layout">
          <!-- Left Column: Editorial Copy & Technical Spec Metrics -->
          <div class="b95-case-study-narrative">
            <div class="b95-case-meta-bar">
              <span class="b95-meta-pill">Client: Al-Emad Al-Athmal Co.</span>
              <span class="b95-meta-pill b95-meta-pill--endorse">Endorsed by Iraqi Ministry of Youth &amp; Sports</span>
            </div>

            <p class="b95-case-lead">
              Commissioned as the first specialized turf photosynthesis enhancement deployment in the Republic of Iraq, B95 PROJECT engineered, fabricated, and delivered mobile high-output illumination rigs designed to overcome acute winter solar deficiency and severe architectural stadium shading.
            </p>

            <p class="b95-case-body">
              Following direct consultations at our Istanbul headquarters with the executive management of Al-Emad Al-Athmal Company, our multidisciplinary engineering teams developed a specialized mobile structural framework. Each system stimulates chlorophyll photosynthetic radiation at turf level without inducing thermal stress or soil compaction, guaranteeing premier international match-readiness throughout extreme seasonal temperature deltas.
            </p>

            <!-- Technical Spec Metrics Data Callouts -->
            <div class="b95-metrics-grid">
              <div class="b95-metric-card">
                <span class="b95-metric-card__value">12m</span>
                <span class="b95-metric-card__title">Marine-Grade Aluminum Truss</span>
                <p class="b95-metric-card__desc">Ultra-lightweight structural span maximizing illumination area with total weatherproofing.</p>
              </div>

              <div class="b95-metric-card">
                <span class="b95-metric-card__value">9 Units</span>
                <span class="b95-metric-card__title">Philips High-Output Modules</span>
                <p class="b95-metric-card__desc">European-origin horticultural LEDs calibrated for balanced Photosynthetically Active Radiation (PAR).</p>
              </div>

              <div class="b95-metric-card">
                <span class="b95-metric-card__value">0% Compaction</span>
                <span class="b95-metric-card__title">Ground-Clearance Mobility</span>
                <p class="b95-metric-card__desc">Engineered multi-axis pneumatic rolling chassis guaranteeing zero root degradation during transit.</p>
              </div>

              <div class="b95-metric-card">
                <span class="b95-metric-card__value">Gov. Praise</span>
                <span class="b95-metric-card__title">Ministry Commendation</span>
                <p class="b95-metric-card__desc">Officially commended by the Iraqi Ministry of Youth &amp; Sports for operational speed and excellence.</p>
              </div>
            </div>
          </div>

          <!-- Right Column: Image Grid / Gallery Showcasing Stadium Deployment & Assembly -->
          <div class="b95-case-study-media">
            <!-- Main Hero View: Stadium Deployment -->
            <div class="b95-media-hero">
              <img src="assets/generated/featured_stadium_wide_1790715873921.jpg" alt="12-meter artificial lighting units deployed across the sports stadium turf in Baghdad" class="b95-media-img" loading="lazy">
              <div class="b95-media-badge">
                <span>Deployment Stage</span>
                <strong>Baghdad Stadium Field Operations</strong>
              </div>
            </div>

            <!-- Sub Grid: Detail Assembly & QA/QC Inspections -->
            <div class="b95-media-subgrid">
              <div class="b95-media-subcard">
                <img src="assets/generated/featured_stadium_closeup_1790715897409.jpg" alt="Close-up detail of the precision aluminum truss and Philips optical module array" class="b95-media-img" loading="lazy">
                <div class="b95-media-caption">01 · Structural Truss &amp; Optical Modules</div>
              </div>

              <div class="b95-media-subcard">
                <img src="assets/generated/featured_manufacturing_1790715972624.jpg" alt="Precision structural welding and factory fabrication audit in Istanbul" class="b95-media-img" loading="lazy">
                <div class="b95-media-caption">02 · Factory Fabrication &amp; Assembly</div>
              </div>

              <div class="b95-media-subcard">
                <img src="assets/generated/featured_stadium_engineers_1790715921480.jpg" alt="B95 Project engineering leadership conducting on-turf photometric validation audits" class="b95-media-img" loading="lazy">
                <div class="b95-media-caption">03 · Photometric &amp; Safety Audit</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

# Find boundaries and replace in index.html
# 1. Services
s1_start = html.find('<!-- ====================================================================\n         02: SERVICES')
if s1_start == -1:
    s1_start = html.find('id="sec-services"')
    # backup to the preceding comment
    s1_start = html.rfind('<!--', 0, s1_start)

s2_start = html.find('<!-- ====================================================================\n         03: RANGE OF PROJECTS')
if s2_start == -1:
    s2_start = html.find('id="sec-range"')
    s2_start = html.rfind('<!--', 0, s2_start)

# 2. References
s3_start = html.find('<!-- ====================================================================\n         04: OUR REFERENCES')
if s3_start == -1:
    s3_start = html.find('id="sec-references"')
    s3_start = html.rfind('<!--', 0, s3_start)

s4_start = html.find('<!-- ====================================================================\n         05: FEATURED PROJECT')
if s4_start == -1:
    s4_start = html.find('id="sec-featured"')
    s4_start = html.rfind('<!--', 0, s4_start)

# 3. Footer
s5_start = html.find('<!-- ====================================================================\n         06: FOOTER')
if s5_start == -1:
    s5_start = html.find('id="sec-footer"')
    s5_start = html.rfind('<!--', 0, s5_start)

print(f"Indices: s1={s1_start}, s2={s2_start}, s3={s3_start}, s4={s4_start}, s5={s5_start}")

# Rebuild HTML
new_html = (
    html[:s1_start] +
    services_html + "\n\n" +
    html[s2_start:s3_start] +
    references_html + "\n\n" +
    featured_html + "\n\n" +
    html[s5_start:]
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully updated index.html with new semantic sections!")
