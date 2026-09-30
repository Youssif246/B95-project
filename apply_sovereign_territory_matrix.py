import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate section 02 start and end
s_start = html.find('<!-- ====================================================================\n         SECTION 02: REFERENCES & REGIONAL REACH')
if s_start == -1:
    s_start = html.find('id="sec-references"')
    s_start = html.rfind('<!--', 0, s_start)

s_end = html.find('<!-- ====================================================================\n         SECTION 03: FEATURED CASE STUDY')
if s_end == -1:
    s_end = html.find('id="sec-featured"')
    s_end = html.rfind('<!--', 0, s_end)

print(f"References section range: {s_start} to {s_end}")

territory_matrix_html = '''    <!-- ====================================================================
         SECTION 02: SOVEREIGN TERRITORY MATRIX (REFERENCES & REGIONAL REACH)
         Innovative Editorial Cards with Stylized Country Vector Badges
         ==================================================================== -->
    <section class="b95-section b95-territory-section" id="sec-references" aria-labelledby="territory-matrix-title">
      <div class="b95-container">
        
        <!-- Section Header -->
        <header class="b95-section-header">
          <div class="b95-section-eyebrow">
            <span class="b95-eyebrow-accent">02</span> / SOVEREIGN TERRITORY MATRIX
          </div>
          <div class="b95-section-title-wrap">
            <h2 class="b95-section-title" id="territory-matrix-title">References &amp; Regional Reach</h2>
            <span class="b95-section-subtitle">Cross-Border General Contracting, High-Assurance Aviation &amp; Public Works</span>
          </div>
          <p class="b95-section-lead">
            Headquartered in Istanbul, B95 PROJECT orchestrates landmark civil infrastructure, airport modernization, diplomatic plenary halls, and specialized healthcare facilities across five sovereign territories with single-source accountability.
          </p>
        </header>

        <!-- TOP COMPONENT: Subtle Regional Vector Footprint & Operational Ribbon -->
        <div class="b95-territory-footprint-card">
          <div class="b95-footprint-topbar">
            <div class="b95-footprint-topbar__left">
              <span class="b95-pulse-dot" aria-hidden="true"></span>
              <span class="b95-footprint-topbar__label">Sovereign Theater Operational Grid</span>
            </div>
            <div class="b95-footprint-topbar__right">
              <span class="b95-coord-tag"><i class="fa-solid fa-compass"></i> ISTANBUL HQ: 41.0082° N, 28.9784° E</span>
            </div>
          </div>

          <!-- Sleek Architectural Vector Ribbon Graphic -->
          <div class="b95-territory-vector-canvas">
            <svg class="b95-vector-ribbon-svg" viewBox="0 0 1000 140" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Regional vector network">
              <!-- Technical Baseline & Grid -->
              <line x1="20" y1="70" x2="980" y2="70" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="4 4"/>
              <line x1="20" y1="30" x2="980" y2="30" stroke="#E2E8F0" stroke-width="0.75" stroke-dasharray="2 4"/>
              <line x1="20" y1="110" x2="980" y2="110" stroke="#E2E8F0" stroke-width="0.75" stroke-dasharray="2 4"/>

              <!-- HQ Node: Istanbul -->
              <g class="b95-svg-node-group">
                <circle cx="160" cy="70" r="16" fill="#991B1B" fill-opacity="0.12"/>
                <circle cx="160" cy="70" r="8" stroke="#991B1B" stroke-width="1.5" fill="#FFFFFF"/>
                <circle cx="160" cy="70" r="3.5" fill="#991B1B"/>
                <text x="160" y="48" fill="#0F172A" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="800" text-anchor="middle" letter-spacing="0.5">ISTANBUL (HQ)</text>
                <text x="160" y="96" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="8.5" text-anchor="middle">TÜRKİYE</text>
              </g>

              <!-- Node Vector Lines from Istanbul -->
              <path d="M168 70 Q 250 45 340 70" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="3 3"/>
              <path d="M168 70 Q 320 95 500 70" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="3 3"/>
              <path d="M168 70 Q 400 45 660 70" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="3 3"/>
              <path d="M168 70 Q 480 100 820 70" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="3 3"/>

              <!-- Node: Northern Syria -->
              <g class="b95-svg-node-group">
                <circle cx="340" cy="70" r="6" stroke="#0F172A" stroke-width="1.5" fill="#FFFFFF"/>
                <circle cx="340" cy="70" r="2.5" fill="#0F172A"/>
                <text x="340" y="48" fill="#0F172A" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" text-anchor="middle">N. SYRIA</text>
                <text x="340" y="96" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="8.5" text-anchor="middle">2000 HOUSING</text>
              </g>

              <!-- Node: Baghdad & Basra (Iraq) -->
              <g class="b95-svg-node-group">
                <circle cx="500" cy="70" r="14" fill="#991B1B" fill-opacity="0.08"/>
                <circle cx="500" cy="70" r="6.5" stroke="#991B1B" stroke-width="1.5" fill="#FFFFFF"/>
                <circle cx="500" cy="70" r="3" fill="#991B1B"/>
                <text x="500" y="48" fill="#0F172A" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="800" text-anchor="middle">BAGHDAD · BASRA</text>
                <text x="500" y="96" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="8.5" text-anchor="middle">IRAQ THEATER</text>
              </g>

              <!-- Node: Manama (Bahrain) -->
              <g class="b95-svg-node-group">
                <circle cx="660" cy="70" r="6" stroke="#0F172A" stroke-width="1.5" fill="#FFFFFF"/>
                <circle cx="660" cy="70" r="2.5" fill="#0F172A"/>
                <text x="660" y="48" fill="#0F172A" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" text-anchor="middle">MANAMA</text>
                <text x="660" y="96" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="8.5" text-anchor="middle">BAHRAIN</text>
              </g>

              <!-- Node: Benghazi (Libya) -->
              <g class="b95-svg-node-group">
                <circle cx="820" cy="70" r="6" stroke="#0F172A" stroke-width="1.5" fill="#FFFFFF"/>
                <circle cx="820" cy="70" r="2.5" fill="#0F172A"/>
                <text x="820" y="48" fill="#0F172A" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700" text-anchor="middle">BENGHAZI</text>
                <text x="820" y="96" fill="#64748B" font-family="'JetBrains Mono', monospace" font-size="8.5" text-anchor="middle">LIBYA</text>
              </g>
            </svg>
          </div>

          <!-- Sleek Operational Ribbon -->
          <div class="b95-operational-ribbon">
            <div class="b95-ribbon-metric">
              <span class="b95-metric-num">05</span>
              <div class="b95-metric-text">
                <strong>Sovereign Theaters</strong>
                <span>Active Regional Deployment</span>
              </div>
            </div>
            <div class="b95-ribbon-sep" aria-hidden="true"></div>
            <div class="b95-ribbon-metric">
              <span class="b95-metric-num">100%</span>
              <div class="b95-metric-text">
                <strong>On-Spec Execution</strong>
                <span>Statutory Compliance Record</span>
              </div>
            </div>
            <div class="b95-ribbon-sep" aria-hidden="true"></div>
            <div class="b95-ribbon-metric">
              <span class="b95-metric-num">Tier-1</span>
              <div class="b95-metric-text">
                <strong>EPC Accountability</strong>
                <span>Full Turnkey Governance</span>
              </div>
            </div>
            <div class="b95-ribbon-sep" aria-hidden="true"></div>
            <div class="b95-ribbon-metric">
              <span class="b95-metric-num">10+ Yrs</span>
              <div class="b95-metric-text">
                <strong>Asset Durability</strong>
                <span>Engineered Lifecycle Longevity</span>
              </div>
            </div>
          </div>
        </div>

        <!-- PROJECT SHOWCASE: The Sovereign Territory Matrix Grid (2-Column Architecture) -->
        <div class="b95-territory-matrix-grid">
          
          <!-- Card 01: Iraq (Baghdad) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Iraq territory silhouette">
                  <path d="M14 20 L28 12 L46 14 L52 26 L48 44 L34 54 L20 46 L12 36 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <path d="M22 18 L34 32 L40 48" stroke="#991B1B" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
                  <path d="M28 16 L38 28 L44 42" stroke="#991B1B" stroke-width="1" stroke-dasharray="2 2" opacity="0.6"/>
                  <circle cx="34" cy="32" r="2.5" fill="#991B1B"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">IRQ · 01</span>
                  <strong class="b95-country-name">IRAQ</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--sports">
                <i class="fa-solid fa-volleyball"></i> Sports &amp; Aviation
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Baghdad, Republic of Iraq</span>
              </div>
              <h3 class="b95-territory-title">Al-Shaab Stadium Turf Lighting Systems</h3>
              <p class="b95-territory-scope">
                Turnkey photosynthetic gantry infrastructure &amp; Philips LED array.
              </p>
              <div class="b95-territory-detail">
                Engineered mobile aluminum structural gantry with European-origin optical modules stimulating pitch chlorophyll growth without turf compaction.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">Client: Al-Emad Al-Athmal Co.</span>
            </div>
          </article>

          <!-- Card 02: Iraq (Safwan Border) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Iraq territory silhouette">
                  <path d="M14 20 L28 12 L46 14 L52 26 L48 44 L34 54 L20 46 L12 36 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <path d="M22 18 L34 32 L40 48" stroke="#991B1B" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
                  <path d="M28 16 L38 28 L44 42" stroke="#991B1B" stroke-width="1" stroke-dasharray="2 2" opacity="0.6"/>
                  <circle cx="34" cy="32" r="2.5" fill="#991B1B"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">IRQ · 02</span>
                  <strong class="b95-country-name">IRAQ</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--infra">
                <i class="fa-solid fa-road"></i> Civil Infrastructure
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Safwan Border, Iraq-Kuwait</span>
              </div>
              <h3 class="b95-territory-title">Safwan International Highway Lighting</h3>
              <p class="b95-territory-scope">
                12m double-arm decorative galvanized lighting masts.
              </p>
              <div class="b95-territory-detail">
                Civil foundation casting and mechanical erection of high-illuminance galvanized double-mast structures along strategic international transit corridor.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">Basra Governorate Partnership</span>
            </div>
          </article>

          <!-- Card 03: Iraq (Basra Airport) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Iraq territory silhouette">
                  <path d="M14 20 L28 12 L46 14 L52 26 L48 44 L34 54 L20 46 L12 36 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <path d="M22 18 L34 32 L40 48" stroke="#991B1B" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
                  <path d="M28 16 L38 28 L44 42" stroke="#991B1B" stroke-width="1" stroke-dasharray="2 2" opacity="0.6"/>
                  <circle cx="34" cy="32" r="2.5" fill="#991B1B"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">IRQ · 03</span>
                  <strong class="b95-country-name">IRAQ</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--aviation">
                <i class="fa-solid fa-plane-departure"></i> Aviation &amp; Transport
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Basra, Republic of Iraq</span>
              </div>
              <h3 class="b95-territory-title">Basra International Airport Modernization</h3>
              <p class="b95-territory-scope">
                Full terminal rehabilitation, acoustic ceiling systems &amp; flight ops fit-out.
              </p>
              <div class="b95-territory-detail">
                Architectural passenger terminal overhaul, acoustic sound baffle integration, VIP lounge finishing, and mission-critical MEP operational systems.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">Civil Aviation Authority</span>
            </div>
          </article>

          <!-- Card 04: Bahrain (Manama) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Bahrain territory silhouette">
                  <path d="M26 12 C34 12, 40 18, 40 26 C40 36, 34 52, 28 54 C22 52, 20 38, 20 26 C20 18, 22 12, 26 12 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <circle cx="28" cy="22" r="3" fill="#991B1B"/>
                  <circle cx="28" cy="22" r="7" stroke="#991B1B" stroke-width="0.8" stroke-dasharray="2 2" opacity="0.7"/>
                  <circle cx="44" cy="38" r="2" fill="#CBD5E1"/>
                  <circle cx="46" cy="44" r="1.5" fill="#CBD5E1"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">BHR · 01</span>
                  <strong class="b95-country-name">BAHRAIN</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--diplomatic">
                <i class="fa-solid fa-landmark-flag"></i> Diplomatic &amp; Civic
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Manama, Kingdom of Bahrain</span>
              </div>
              <h3 class="b95-territory-title">33rd Arab Summit Royal Conference Hall</h3>
              <p class="b95-territory-scope">
                Bespoke diplomatic interior architecture, acoustic cladding &amp; VIP plenary seating.
              </p>
              <div class="b95-territory-detail">
                Turnkey royal-tier fit-out executed for visiting heads of state with luxury architectural woodwork, custom acoustic panels, and diplomatic plenary installations.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">Royal Protocol Protocol Authority</span>
            </div>
          </article>

          <!-- Card 05: Libya (Benghazi) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Libya territory silhouette">
                  <path d="M12 22 L26 14 L42 22 L54 18 L56 36 L50 52 L16 52 L12 34 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <path d="M26 14 Q34 24 42 22" stroke="#991B1B" stroke-width="1.5" fill="none"/>
                  <circle cx="44" cy="22" r="2.5" fill="#991B1B"/>
                  <line x1="16" y1="36" x2="48" y2="36" stroke="#94A3B8" stroke-width="0.75" stroke-dasharray="2 3"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">LBY · 01</span>
                  <strong class="b95-country-name">LIBYA</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--health">
                <i class="fa-solid fa-hospital"></i> Healthcare &amp; Medical
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Benghazi, State of Libya</span>
              </div>
              <h3 class="b95-territory-title">Akam Al-Sonwan Specialty Hospital</h3>
              <p class="b95-territory-scope">
                Certified antibacterial medical fit-out, cleanrooms &amp; ICU partitioning.
              </p>
              <div class="b95-territory-detail">
                Specialized clinical finishes, certified seamless antibacterial medical vinyl flooring, sterile ICU partition enclosures, and cleanroom MEP installations.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">Healthcare Ministry Certification</span>
            </div>
          </article>

          <!-- Card 06: Syria (Northern Syria) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Syria territory silhouette">
                  <path d="M16 26 L32 14 L52 18 L50 32 L36 44 L20 46 L14 34 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <path d="M24 20 L38 28 L46 26" stroke="#991B1B" stroke-width="1.5" fill="none" stroke-linecap="round"/>
                  <circle cx="26" cy="22" r="2.5" fill="#991B1B"/>
                  <circle cx="38" cy="28" r="2" fill="#0F172A"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">SYR · 01</span>
                  <strong class="b95-country-name">SYRIA</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--urban">
                <i class="fa-solid fa-city"></i> Residential &amp; Urban
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Northern Syria Corridor</span>
              </div>
              <h3 class="b95-territory-title">2000 Sustainable Housing Units</h3>
              <p class="b95-territory-scope">
                Master-planning, modular rapid-assembly casting &amp; community civil utilities.
              </p>
              <div class="b95-territory-detail">
                Regional civil master-planning, high-durability precast structural concrete casting, community potable and stormwater grids, and turnkey unit delivery.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">Community Reconstruction Program</span>
            </div>
          </article>

          <!-- Card 07: Iraq (Basra Sports City) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Iraq territory silhouette">
                  <path d="M14 20 L28 12 L46 14 L52 26 L48 44 L34 54 L20 46 L12 36 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <path d="M22 18 L34 32 L40 48" stroke="#991B1B" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
                  <path d="M28 16 L38 28 L44 42" stroke="#991B1B" stroke-width="1" stroke-dasharray="2 2" opacity="0.6"/>
                  <circle cx="34" cy="32" r="2.5" fill="#991B1B"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">IRQ · 04</span>
                  <strong class="b95-country-name">IRAQ</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--infra">
                <i class="fa-solid fa-tower-broadcast"></i> Municipal Infrastructure
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Basra, Republic of Iraq</span>
              </div>
              <h3 class="b95-territory-title">Sports City Roadway High-Mast Illumination</h3>
              <p class="b95-territory-scope">
                Structural concrete foundation casting &amp; 96 highway luminaire masts.
              </p>
              <div class="b95-territory-detail">
                Precision civil footing casting, delivery and mechanical integration of 96 heavy-duty roadway high-masts illuminating the Basra Sports City arterial corridor.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">Municipal Infrastructure Board</span>
            </div>
          </article>

          <!-- Card 08: Türkiye (Istanbul) -->
          <article class="b95-territory-card" tabindex="0">
            <div class="b95-card-anchor-header">
              <!-- Stylized Country Silhouette Badge -->
              <div class="b95-country-badge">
                <svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Turkey territory silhouette">
                  <path d="M10 24 L20 20 L48 18 L56 26 L54 38 L38 42 L18 40 L10 32 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
                  <circle cx="20" cy="23" r="3" fill="#991B1B"/>
                  <circle cx="20" cy="23" r="6.5" stroke="#991B1B" stroke-width="0.8" opacity="0.6"/>
                  <line x1="20" y1="23" x2="48" y2="30" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="2 2"/>
                </svg>
                <div class="b95-country-badge__info">
                  <span class="b95-country-code">TUR · 01</span>
                  <strong class="b95-country-name">TÜRKİYE</strong>
                </div>
              </div>

              <!-- Sector Pill Badge -->
              <span class="b95-matrix-sector-tag b95-matrix-sector-tag--comm">
                <i class="fa-solid fa-building-columns"></i> Commercial Architecture
              </span>
            </div>

            <div class="b95-territory-card__content">
              <div class="b95-territory-location">
                <i class="fa-solid fa-location-dot b95-pin-red"></i>
                <span>Istanbul, Republic of Türkiye</span>
              </div>
              <h3 class="b95-territory-title">46th Turkeybuild International Exhibition Pavilion</h3>
              <p class="b95-territory-scope">
                Bespoke architectural pavilion design, structural steel booth &amp; dynamic lighting.
              </p>
              <div class="b95-territory-detail">
                Architectural design, engineered modular steel exhibition superstructure, integrated multi-angle illumination, and international delegate trade hospitality staging.
              </div>
            </div>

            <div class="b95-territory-footer">
              <span class="b95-delivery-status"><i class="fa-solid fa-circle-check"></i> Turnkey Handover Completed</span>
              <span class="b95-territory-client">International Trade Delegation</span>
            </div>
          </article>

        </div>
      </div>
    </section>
'''

new_html = html[:s_start] + territory_matrix_html + "\n\n" + html[s_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Applied Sovereign Territory Matrix HTML to index.html successfully!")
