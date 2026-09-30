import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Font Awesome 6 if not already present
if 'font-awesome' not in html:
    html = html.replace(
        '<link rel="stylesheet" href="styles.css">',
        '<!-- Font Awesome 6 Free CDN -->\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n  <link rel="stylesheet" href="styles.css">'
    )

# Section 1: Services (2-Page / 2-Spread Structure)
services_markup = '''    <!-- ====================================================================
         SECTION 01: SERVICES — 2-SPREAD ARCHITECTURAL STRUCTURE
         Spread 01: Pre-Construction & Sourcing | Spread 02: Fabrication & Handover
         ==================================================================== -->
    
    <!-- SPREAD 01: SERVICES 01 - 04 -->
    <section class="b95-section b95-services-spread" id="sec-services" aria-labelledby="services-spread1-title">
      <div class="b95-container">
        <header class="b95-section-header">
          <div class="b95-section-eyebrow">
            <span class="b95-eyebrow-accent">01</span> / TURNKEY SOLUTIONS — SPREAD I
          </div>
          <div class="b95-section-title-wrap">
            <h2 class="b95-section-title" id="services-spread1-title">From Feasibility to Procurement</h2>
            <span class="b95-section-subtitle">Multidisciplinary Engineering, Regulatory Governance &amp; Global Sourcing</span>
          </div>
          <p class="b95-section-lead">
            Initiating high-complexity capital infrastructure through advanced structural simulations, statutory legal underwriting under Turkish and regional jurisdictions, and value-engineered international material acquisition.
          </p>
        </header>

        <!-- 2x2 Rich Interactive Cards Grid -->
        <div class="b95-services-spread-grid">
          <!-- Card 01 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/generated/services_engineering_planning_1790715742990.jpg" alt="Engineering planning and structural modeling at Istanbul headquarters" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">01</span>
                <span class="b95-card-cat"><i class="fa-solid fa-drafting-compass"></i> CONSULTANCY</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Planning &amp; Engineering Consultancy</h3>
              <p class="b95-card-desc">
                Multidisciplinary feasibility, advanced structural modeling, and strategic execution roadmaps mitigating risk and optimizing capital expenditure.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 01 · Pre-Construction</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>

          <!-- Card 02 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/extracted/p06_img1_13.png" alt="Material specifications quantification and BOQ scheduling" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">02</span>
                <span class="b95-card-cat"><i class="fa-solid fa-boxes-packing"></i> PROCUREMENT</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Material Specifications &amp; Procurement</h3>
              <p class="b95-card-desc">
                Rigorous BOQ quantification, global material sourcing, and value-engineering ensuring highest tier certifications within budget.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 02 · Specification Schedule</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>

          <!-- Card 03 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/extracted/p08_img2_41.png" alt="Legal governance and contract administration documents" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">03</span>
                <span class="b95-card-cat"><i class="fa-solid fa-scale-balanced"></i> GOVERNANCE</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Legal Governance &amp; Contract Administration</h3>
              <p class="b95-card-desc">
                Turnkey regulatory alignment, statutory compliance under Turkish &amp; regional jurisdictions, and risk-proofed commercial contracts.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 03 · Statutory Alignment</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>

          <!-- Card 04 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/extracted/p09_img1_58.png" alt="Supply chain orchestration and vendor vetting" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">04</span>
                <span class="b95-card-cat"><i class="fa-solid fa-truck-fast"></i> SUPPLY CHAIN</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Supply Chain &amp; Vendor Management</h3>
              <p class="b95-card-desc">
                Strategic vendor vetting, enterprise-grade brand procurement, and transparent tracking from origin to staging.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 04 · Vendor Vetting</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- SPREAD 02: SERVICES 05 - 08 -->
    <section class="b95-section b95-services-spread b95-services-spread--alt" id="sec-services-part2" aria-labelledby="services-spread2-title">
      <div class="b95-container">
        <header class="b95-section-header">
          <div class="b95-section-eyebrow">
            <span class="b95-eyebrow-accent">01</span> / TURNKEY SOLUTIONS — SPREAD II
          </div>
          <div class="b95-section-title-wrap">
            <h2 class="b95-section-title" id="services-spread2-title">From Fabrication to Handover</h2>
            <span class="b95-section-subtitle">Manufacturing Audits, Multimodal Logistics, Erection &amp; Facility Lifecycle</span>
          </div>
          <p class="b95-section-lead">
            Translating engineered specifications into reality through strict on-site factory quality verification, cross-border multimodal transport, turnkey MEP and structural execution, and permanent operational handover.
          </p>
        </header>

        <!-- 2x2 Rich Interactive Cards Grid -->
        <div class="b95-services-spread-grid">
          <!-- Card 05 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/generated/featured_stadium_engineers_1790715921480.jpg" alt="Quality assurance and factory inspection audits by B95 Project engineers" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">05</span>
                <span class="b95-card-cat"><i class="fa-solid fa-vial-circle-check"></i> QA / QC AUDIT</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Quality Assurance &amp; Factory Inspection</h3>
              <p class="b95-card-desc">
                Rigorous QA/QC protocols, on-site manufacturing audits, and strict compliance verification prior to dispatch.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 05 · Factory Inspection</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>

          <!-- Card 06 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/generated/sector_infrastructures_1790715761734.jpg" alt="Multimodal international freight forwarding and customs clearance" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">06</span>
                <span class="b95-card-cat"><i class="fa-solid fa-ship"></i> GLOBAL LOGISTICS</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Global Freight &amp; Customs Logistics</h3>
              <p class="b95-card-desc">
                End-to-end multimodal transport (air/sea/land), streamlined customs clearance, and precision site delivery.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 06 · Transit &amp; Customs</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>

          <!-- Card 07 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/extracted/p10_img1_88.png" alt="Turnkey construction, MEP installations and structural erection" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">07</span>
                <span class="b95-card-cat"><i class="fa-solid fa-trowel-bricks"></i> GENERAL CONTRACTING</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Execution &amp; General Contracting</h3>
              <p class="b95-card-desc">
                Turnkey structural erection, electro-mechanical (MEP) installations, high-spec interior fit-outs, and architectural finishing.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 07 · On-Site Delivery</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>

          <!-- Card 08 -->
          <article class="b95-service-spread-card" tabindex="0">
            <div class="b95-card-media-thumb">
              <img src="assets/generated/sector_sports_1790715802924.jpg" alt="Post-completion warranty enforcement, facility maintenance, and operational readiness" loading="lazy">
              <div class="b95-card-badge-top">
                <span class="b95-card-num">08</span>
                <span class="b95-card-cat"><i class="fa-solid fa-screwdriver-wrench"></i> LIFECYCLE HANDOVER</span>
              </div>
            </div>
            <div class="b95-card-body">
              <h3 class="b95-card-title">Lifecycle Handover &amp; Facility Maintenance</h3>
              <p class="b95-card-desc">
                Post-completion warranty enforcement, technical operations handover, and continuous operational readiness training.
              </p>
              <div class="b95-card-footer">
                <span class="b95-card-phase">Phase 08 · Lifetime Guarantee</span>
                <i class="fa-solid fa-arrow-right b95-card-arrow" aria-hidden="true"></i>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>
'''

# Section 2: References & Regional Reach
references_markup = '''    <!-- ====================================================================
         SECTION 02: REFERENCES & REGIONAL REACH
         Elevated Global Footprint · Dark Pulse Graphic & Modern Architectural Rows
         ==================================================================== -->
    <section class="b95-section b95-references-elevated" id="sec-references" aria-labelledby="references-elevated-title">
      <div class="b95-container">
        
        <!-- Header -->
        <header class="b95-section-header">
          <div class="b95-section-eyebrow">
            <span class="b95-eyebrow-accent">02</span> / OPERATIONAL FOOTPRINT
          </div>
          <div class="b95-section-title-wrap">
            <h2 class="b95-section-title" id="references-elevated-title">References &amp; Regional Reach</h2>
            <span class="b95-section-subtitle">Sovereign Corridors · Strategic Infrastructure · Diplomatic Fit-Outs</span>
          </div>
          <p class="b95-section-lead">
            Headquartered in Istanbul, B95 PROJECT orchestrates high-assurance civil, aviation, and healthcare projects across five sovereign theaters, maintaining single-source accountability from concept to operational certification.
          </p>
        </header>

        <!-- PART A: Elevated Dark Regional Graphic with Glowing Pulse Nodes -->
        <div class="b95-footprint-showcase">
          <div class="b95-footprint-graphic-box">
            <div class="b95-footprint-graphic-topbar">
              <div class="b95-graphic-indicator">
                <span class="b95-pulse-dot"></span>
                <span>Active Geopolitical Footprint · Live Node Network</span>
              </div>
              <div class="b95-graphic-coords">HQ ISTANBUL: 41.0082° N, 28.9784° E</div>
            </div>

            <!-- Stylized Dark/Monochrome Regional Map with Animated Nodes -->
            <div class="b95-map-canvas-container">
              <svg class="b95-elevated-map-svg" viewBox="0 0 960 420" fill="none" xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <!-- Glowing Pulse Filters -->
                  <radialGradient id="hq-glow" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stop-color="#B91C1C" stop-opacity="0.8"/>
                    <stop offset="60%" stop-color="#B91C1C" stop-opacity="0.25"/>
                    <stop offset="100%" stop-color="#B91C1C" stop-opacity="0"/>
                  </radialGradient>
                  <radialGradient id="node-glow" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.7"/>
                    <stop offset="100%" stop-color="#38BDF8" stop-opacity="0"/>
                  </radialGradient>
                  <linearGradient id="route-gradient-iq" x1="280" y1="120" x2="620" y2="230" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#B91C1C" stop-opacity="0.8"/>
                    <stop offset="100%" stop-color="#B91C1C" stop-opacity="0.15"/>
                  </linearGradient>
                </defs>

                <!-- Grid Matrix Background -->
                <line x1="40" y1="80" x2="920" y2="80" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 4"/>
                <line x1="40" y1="180" x2="920" y2="180" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 4"/>
                <line x1="40" y1="280" x2="920" y2="280" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 4"/>
                <line x1="40" y1="360" x2="920" y2="360" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 4"/>

                <line x1="200" y1="30" x2="200" y2="390" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 4"/>
                <line x1="440" y1="30" x2="440" y2="390" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 4"/>
                <line x1="680" y1="30" x2="680" y2="390" stroke="#1E293B" stroke-width="0.8" stroke-dasharray="3 4"/>

                <!-- Stylized Landmass & Continental Coastline Geometry -->
                <path d="M120 110 C 190 90, 260 100, 310 130 C 370 170, 480 180, 560 170 C 640 160, 720 190, 800 240 C 850 270, 880 320, 910 350" stroke="#334155" stroke-width="1.2" stroke-dasharray="2 3" fill="none" opacity="0.45"/>
                <path d="M80 260 C 140 240, 210 260, 270 290 C 350 330, 470 340, 580 330 C 680 320, 770 340, 850 370" stroke="#334155" stroke-width="1.2" stroke-dasharray="2 3" fill="none" opacity="0.35"/>

                <!-- Active Inter-City Connection Beams -->
                <!-- Istanbul -> Idlib -->
                <path d="M 280 110 Q 360 140 440 190" stroke="url(#route-gradient-iq)" stroke-width="1.8" fill="none"/>
                <!-- Istanbul -> Baghdad -->
                <path d="M 280 110 Q 420 140 590 220" stroke="url(#route-gradient-iq)" stroke-width="2" fill="none"/>
                <!-- Istanbul -> Basra -->
                <path d="M 280 110 Q 460 170 710 290" stroke="url(#route-gradient-iq)" stroke-width="1.8" fill="none"/>
                <!-- Istanbul -> Manama (Bahrain) -->
                <path d="M 280 110 Q 520 200 810 320" stroke="url(#route-gradient-iq)" stroke-width="1.6" fill="none"/>
                <!-- Istanbul -> Benghazi (Libya) -->
                <path d="M 280 110 Q 210 210 160 300" stroke="url(#route-gradient-iq)" stroke-width="1.6" fill="none"/>

                <!-- ISTANBUL HQ (Dominant Radiant Red Node) -->
                <circle cx="280" cy="110" r="32" fill="url(#hq-glow)"/>
                <circle cx="280" cy="110" r="14" stroke="#B91C1C" stroke-width="1.5" fill="none" class="b95-svg-pulse-ring"/>
                <circle cx="280" cy="110" r="6" fill="#B91C1C"/>
                <circle cx="280" cy="110" r="2.5" fill="#FFFFFF"/>
                <text x="280" y="80" fill="#FFFFFF" font-family="var(--b95-font-main)" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1">ISTANBUL · TÜRKİYE</text>
                <text x="280" y="96" fill="#94A3B8" font-family="var(--b95-font-mono)" font-size="9" text-anchor="middle" letter-spacing="0.5">GLOBAL HEADQUARTERS &amp; DESIGN</text>

                <!-- BAGHDAD NODE -->
                <circle cx="590" cy="220" r="22" fill="url(#hq-glow)" opacity="0.6"/>
                <circle cx="590" cy="220" r="9" stroke="#B91C1C" stroke-width="1.2" fill="none" class="b95-svg-pulse-ring"/>
                <circle cx="590" cy="220" r="4.5" fill="#B91C1C"/>
                <text x="590" y="202" fill="#FFFFFF" font-family="var(--b95-font-main)" font-size="11" font-weight="700" text-anchor="middle">BAGHDAD · IRAQ</text>
                <text x="590" y="244" fill="#94A3B8" font-family="var(--b95-font-mono)" font-size="8.5" text-anchor="middle">Al-Shaab Stadium Systems</text>

                <!-- BASRA NODE -->
                <circle cx="710" cy="290" r="20" fill="url(#hq-glow)" opacity="0.6"/>
                <circle cx="710" cy="290" r="8" stroke="#B91C1C" stroke-width="1.2" fill="none" class="b95-svg-pulse-ring"/>
                <circle cx="710" cy="290" r="4" fill="#B91C1C"/>
                <text x="710" y="274" fill="#FFFFFF" font-family="var(--b95-font-main)" font-size="11" font-weight="700" text-anchor="middle">BASRA · IRAQ</text>
                <text x="710" y="312" fill="#94A3B8" font-family="var(--b95-font-mono)" font-size="8.5" text-anchor="middle">Airport &amp; Highway Infrastructure</text>

                <!-- MANAMA NODE (Bahrain) -->
                <circle cx="810" cy="320" r="16" fill="url(#hq-glow)" opacity="0.5"/>
                <circle cx="810" cy="320" r="4" fill="#E2E8F0"/>
                <text x="810" y="304" fill="#FFFFFF" font-family="var(--b95-font-main)" font-size="10.5" font-weight="700" text-anchor="middle">MANAMA · BAHRAIN</text>
                <text x="810" y="342" fill="#94A3B8" font-family="var(--b95-font-mono)" font-size="8.5" text-anchor="middle">33rd Arab Summit Royal Hall</text>

                <!-- BENGHAZI NODE (Libya) -->
                <circle cx="160" cy="300" r="18" fill="url(#hq-glow)" opacity="0.5"/>
                <circle cx="160" cy="300" r="4" fill="#E2E8F0"/>
                <text x="160" y="284" fill="#FFFFFF" font-family="var(--b95-font-main)" font-size="10.5" font-weight="700" text-anchor="middle">BENGHAZI · LIBYA</text>
                <text x="160" y="322" fill="#94A3B8" font-family="var(--b95-font-mono)" font-size="8.5" text-anchor="middle">Akam Al-Sonwan Specialty Hospital</text>

                <!-- IDLIB / NORTH SYRIA NODE -->
                <circle cx="440" cy="190" r="16" fill="url(#hq-glow)" opacity="0.5"/>
                <circle cx="440" cy="190" r="4" fill="#E2E8F0"/>
                <text x="440" y="174" fill="#FFFFFF" font-family="var(--b95-font-main)" font-size="10.5" font-weight="700" text-anchor="middle">NORTHERN SYRIA</text>
                <text x="440" y="212" fill="#94A3B8" font-family="var(--b95-font-mono)" font-size="8.5" text-anchor="middle">2000 Housing Units &amp; Utilities</text>
              </svg>
            </div>

            <!-- Quick Metrics Ribbon -->
            <div class="b95-metrics-ribbon">
              <div class="b95-ribbon-item">
                <span class="b95-ribbon-val">05</span>
                <span class="b95-ribbon-label">Active Sovereign Theaters</span>
              </div>
              <div class="b95-ribbon-divider" aria-hidden="true"></div>
              <div class="b95-ribbon-item">
                <span class="b95-ribbon-val">100%</span>
                <span class="b95-ribbon-label">On-Spec Completion Record</span>
              </div>
              <div class="b95-ribbon-divider" aria-hidden="true"></div>
              <div class="b95-ribbon-item">
                <span class="b95-ribbon-val">Tier-1</span>
                <span class="b95-ribbon-label">Turnkey International Accountability</span>
              </div>
            </div>
          </div>
        </div>

        <!-- PART B: Modern Architectural Project Rows (8 Projects Matrix) -->
        <div class="b95-projects-rows-wrap">
          <div class="b95-projects-table-header">
            <span>Location &amp; Jurisdiction</span>
            <span>Sector / Classification</span>
            <span>Project Designation</span>
            <span>Key Execution Deliverable</span>
          </div>

          <!-- Project Row 01 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Baghdad, Iraq</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--sports">Sports &amp; Aviation</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>Al-Shaab Stadium Turf Lighting Systems</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Engineered mobile aluminum gantry structures with 9 European Philips LED units for specialized pitch chlorophyll photosynthetic stimulation.</span>
            </div>
          </article>

          <!-- Project Row 02 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Safwan Highway, Iraq-Kuwait</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--infra">Civil Infrastructure</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>Dual-Mast Highway Lighting Infrastructure</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Full-corridor supply and mechanical foundation erection of 12-meter double-arm decorative high-illuminance galvanized masts along strategic international border.</span>
            </div>
          </article>

          <!-- Project Row 03 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Basra International Airport</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--aviation">Aviation &amp; Transport</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>Terminal Rehabilitation &amp; Modernization</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Complete civil modernization, structural acoustic ceilings, passenger circulation refurbishment, and integrated flight operations MEP systems.</span>
            </div>
          </article>

          <!-- Project Row 04 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Manama, Kingdom of Bahrain</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--diplomatic">Diplomatic &amp; Civic</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>33rd Arab Summit Royal Conference Hall</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Royal-tier interior architectural execution, bespoke acoustic cladding, diplomatic plenary staging, and luxury finishes for heads of state.</span>
            </div>
          </article>

          <!-- Project Row 05 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Benghazi, Libya</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--health">Healthcare Fit-Out</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>Akam Al-Sonwan Specialty Hospital</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Turnkey clinical outfitting, certified antibacterial medical vinyl flooring, sterile ICU enclosures, and cleanroom architectural partitions.</span>
            </div>
          </article>

          <!-- Project Row 06 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Northern Syria</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--urban">Residential &amp; Urban</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>2000 Sustainable Housing Units &amp; Civil Utilities</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Civil master-planning, pre-cast modular structural casting, community potable and stormwater grids, and turnkey residential unit construction.</span>
            </div>
          </article>

          <!-- Project Row 07 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Basra, Iraq</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--infra">Municipal Infrastructure</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>Basra Sports City Roadway High-Mast Illumination</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Precision fabrication, civil footing casting, and electrical grid energization of 96 roadway masts serving the international sports complex.</span>
            </div>
          </article>

          <!-- Project Row 08 -->
          <article class="b95-project-row" tabindex="0">
            <div class="b95-row-col b95-row-loc">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Istanbul, Türkiye</span>
            </div>
            <div class="b95-row-col b95-row-badge">
              <span class="b95-sector-tag b95-sector-tag--comm">Commercial Architecture</span>
            </div>
            <div class="b95-row-col b95-row-title">
              <h3>46th Turkeybuild International Exhibition Pavilion</h3>
            </div>
            <div class="b95-row-col b95-row-deliverable">
              <span>Architectural design, bespoke modular exhibition pavilion engineering, dynamic illumination systems, and international trade delegate staging.</span>
            </div>
          </article>
        </div>
      </div>
    </section>
'''

# Section 3: Featured Project / Case Study
case_study_markup = '''    <!-- ====================================================================
         SECTION 03: FEATURED CASE STUDY — BAGHDAD STADIUM TURF LIGHTING
         Elite Architectural Monograph · Executive Commendation & Spec Grid
         ==================================================================== -->
    <section class="b95-section b95-case-study-monograph" id="sec-featured" aria-labelledby="case-study-monograph-title">
      <div class="b95-container">
        
        <!-- Executive Header & Ministerial Commendation Seal -->
        <header class="b95-case-header">
          <div class="b95-case-header-left">
            <div class="b95-section-eyebrow">
              <span class="b95-eyebrow-accent">03</span> / FEATURED ARCHITECTURAL CASE STUDY
            </div>
            <h2 class="b95-case-headline" id="case-study-monograph-title">
              Artificial Turf Photosynthesis Lighting Units
            </h2>
            <div class="b95-case-sublocation">
              <i class="fa-solid fa-location-dot b95-pin-red"></i>
              <span>Al-Shaab International Stadium · Baghdad, Republic of Iraq</span>
            </div>
          </div>

          <!-- Executive Seals -->
          <div class="b95-case-seals">
            <div class="b95-seal-pill">
              <i class="fa-solid fa-building-shield"></i>
              <div>
                <span class="b95-seal-sub">Commissioning Client</span>
                <strong class="b95-seal-bold">Al-Emad Al-Athmal Co.</strong>
              </div>
            </div>
            <div class="b95-seal-pill b95-seal-pill--commend">
              <i class="fa-solid fa-award"></i>
              <div>
                <span class="b95-seal-sub">Official Sovereign Commendation</span>
                <strong class="b95-seal-bold">Iraqi Ministry of Youth &amp; Sports</strong>
              </div>
            </div>
          </div>
        </header>

        <!-- Wide High-Impact Hero Display (Night Photosynthesis Illumination) -->
        <div class="b95-case-hero-stage">
          <img src="assets/generated/featured_stadium_wide_1790715873921.jpg" alt="12-meter artificial lighting units deployed across sports stadium pitch turf in Baghdad at night" class="b95-case-hero-img" loading="lazy">
          <div class="b95-case-hero-overlay">
            <div class="b95-hero-meta-badge">
              <span class="b95-hero-kicker">Deployment Milestone</span>
              <strong class="b95-hero-status">First High-Output Photosynthetic System Deployed in Iraq</strong>
            </div>
            <div class="b95-hero-coords">
              <span>STADIUM SECTOR: NORTH &amp; SOUTH PITCH GOAL AREAS</span>
            </div>
          </div>
        </div>

        <!-- Two-Column Engineering Breakdown -->
        <div class="b95-case-breakdown-grid">
          <!-- Left Column: The Challenge & Turnkey Solution -->
          <div class="b95-case-story-col">
            <div class="b95-case-narrative-tag">
              <i class="fa-solid fa-microscope"></i>
              <span>The Engineering Challenge &amp; Turnkey Solution</span>
            </div>
            
            <p class="b95-story-lead">
              International stadium architecture routinely suffers from profound solar shade deficits during winter months. Massive grandstand cantilever roofs block natural sunlight, starving natural Bermuda and Rye grasses of critical photosynthetic radiation, resulting in rapid turf root death and unsafe match pitch conditions.
            </p>

            <p class="b95-story-text">
              Following strategic consultations at our Istanbul headquarters with the executive leadership of <strong>Al-Emad Al-Athmal Company</strong>, B95 PROJECT conceived, designed, and manufactured bespoke mobile illumination rigs. Each unit delivers balanced <strong>Photosynthetically Active Radiation (PAR)</strong> at ground level, acting as a scientifically validated replacement for sunlight without thermal scorching.
            </p>

            <p class="b95-story-text">
              Engineered exclusively from lightweight marine-grade structural aluminum alloys, the rigs provide expansive turf coverage while completely avoiding root compaction through high-flotation pneumatic multi-wheel running gear. The successful commissioning was officially praised by the <strong>Iraqi Ministry of Youth and Sports</strong> for setting a benchmark in national sporting infrastructure.
            </p>
          </div>

          <!-- Right Column: Technical Specifications Grid (4 High-Contrast Key-Stat Cards) -->
          <div class="b95-case-specs-col">
            <div class="b95-specs-grid">
              <!-- Spec 01 -->
              <div class="b95-spec-card">
                <div class="b95-spec-stat">12m</div>
                <div class="b95-spec-name">Ultra-Lightweight Marine Aluminum Gantry</div>
                <p class="b95-spec-desc">Engineered structural truss delivering maximal ground coverage span with complete resistance to humidity and seasonal atmospheric corrosion.</p>
              </div>

              <!-- Spec 02 -->
              <div class="b95-spec-card">
                <div class="b95-spec-stat">9 Units</div>
                <div class="b95-spec-name">Philips Horticultural PAR Spectrum LEDs</div>
                <p class="b95-spec-desc">European-origin high-output optical units calibrated for targeted 450nm and 660nm chlorophyll activation wavelengths.</p>
              </div>

              <!-- Spec 03 -->
              <div class="b95-spec-card">
                <div class="b95-spec-stat">0%</div>
                <div class="b95-spec-name">Compaction Pneumatic Multi-Axis Chassis</div>
                <p class="b95-spec-desc">High-flotation rolling chassis engineered to glide across delicate grass surfaces without turf depression or subsurface root shearing.</p>
              </div>

              <!-- Spec 04 -->
              <div class="b95-spec-card">
                <div class="b95-spec-stat">40%+</div>
                <div class="b95-spec-name">Accelerated Root Regeneration</div>
                <p class="b95-spec-desc">Empirically validated biological recovery cycle restoring damaged turf fibers between premier league fixtures in sub-optimal climates.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Gallery Strip: 3-Image Sequence with Technical Captions -->
        <div class="b95-case-gallery-strip">
          <div class="b95-strip-item">
            <div class="b95-strip-frame">
              <img src="assets/generated/featured_stadium_closeup_1790715897409.jpg" alt="Structural aluminum gantry fabrication and truss connection detail" loading="lazy">
            </div>
            <div class="b95-strip-meta">
              <span class="b95-strip-num">01</span>
              <span class="b95-strip-caption">Structural Aluminum Fabrication &amp; Gantry Trussing</span>
            </div>
          </div>

          <div class="b95-strip-item">
            <div class="b95-strip-frame">
              <img src="assets/generated/featured_manufacturing_1790715972624.jpg" alt="Factory quality assurance, optical testing and assembly in Istanbul" loading="lazy">
            </div>
            <div class="b95-strip-meta">
              <span class="b95-strip-num">02</span>
              <span class="b95-strip-caption">Factory QA &amp; Optical PAR Spectrum Testing</span>
            </div>
          </div>

          <div class="b95-strip-item">
            <div class="b95-strip-frame">
              <img src="assets/generated/featured_stadium_engineers_1790715921480.jpg" alt="Live pitch commissioning and turf sensor calibration by B95 Project engineers" loading="lazy">
            </div>
            <div class="b95-strip-meta">
              <span class="b95-strip-num">03</span>
              <span class="b95-strip-caption">Live Pitch Commissioning &amp; Turf Sensor Calibration</span>
            </div>
          </div>
        </div>

      </div>
    </section>
'''

# Find boundaries in index.html
s1_start = html.find('<!-- ====================================================================\n         SECTION 01: OUR SERVICES')
if s1_start == -1:
    s1_start = html.find('id="sec-services"')
    s1_start = html.rfind('<!--', 0, s1_start)

s2_start = html.find('<!-- ====================================================================\n         03: RANGE OF PROJECTS')
if s2_start == -1:
    s2_start = html.find('id="sec-range"')
    s2_start = html.rfind('<!--', 0, s2_start)

s3_start = html.find('<!-- ====================================================================\n         SECTION 03: REFERENCES')
if s3_start == -1:
    s3_start = html.find('id="sec-references"')
    s3_start = html.rfind('<!--', 0, s3_start)

s4_start = html.find('<!-- ====================================================================\n         SECTION 04: FEATURED PROJECT')
if s4_start == -1:
    s4_start = html.find('id="sec-featured"')
    s4_start = html.rfind('<!--', 0, s4_start)

s5_start = html.find('<!-- ====================================================================\n         06: FOOTER')
if s5_start == -1:
    s5_start = html.find('id="sec-footer"')
    s5_start = html.rfind('<!--', 0, s5_start)

print(f"Indices: s1={s1_start}, s2={s2_start}, s3={s3_start}, s4={s4_start}, s5={s5_start}")

# Construct updated HTML
updated_html = (
    html[:s1_start] +
    services_markup + "\n\n" +
    html[s2_start:s3_start] +
    references_markup + "\n\n" +
    case_study_markup + "\n\n" +
    html[s5_start:]
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Successfully written revamped sections into index.html!")
