import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate section 02
start_marker = '<!-- ====================================================================\n         SECTION 02: REFERENCES'
if start_marker not in html:
    start_marker = 'id="sec-references"'
    s_start = html.find(start_marker)
    s_start = html.rfind('<!--', 0, s_start)
else:
    s_start = html.find(start_marker)

end_marker = '<!-- ====================================================================\n         SECTION 03: FEATURED'
if end_marker not in html:
    end_marker = 'id="sec-featured"'
    s_end = html.find(end_marker)
    s_end = html.rfind('<!--', 0, s_end)
else:
    s_end = html.find(end_marker)

print(f"Replacing lines from {s_start} to {s_end}")

master_index_html = '''    <!-- ====================================================================
         SECTION 02: REFERENCES (ARCHITECTURAL MASTER INDEX LEDGER)
         Swiss Full-Bleed Master Ledger: 8 Horizontal Rows, 4 Strict Columns
         ==================================================================== -->
    <section class="b95-section b95-master-index-section" id="sec-references" aria-labelledby="master-index-title">
      <div class="b95-container">
        
        <!-- Wide Top Header & Context Integration -->
        <header class="b95-master-header">
          <div class="b95-master-eyebrow">
            <span class="b95-eyebrow-accent">02</span> / REFERENCES &amp; REGIONAL FOOTPRINT
          </div>
          <h2 class="b95-master-title" id="master-index-title">Selected Works &amp; Regional Commissions</h2>
          
          <!-- Integrated Operational Meta Strip -->
          <div class="b95-master-meta-strip" role="region" aria-label="Operational Summary">
            <div class="b95-meta-segment">
              <span class="b95-meta-dot"></span>
              <strong>HQ:</strong> Istanbul, Türkiye
            </div>
            <div class="b95-meta-divider" aria-hidden="true">|</div>
            <div class="b95-meta-segment">
              <span class="b95-meta-highlight">08</span> Sovereign Commissions
            </div>
            <div class="b95-meta-divider" aria-hidden="true">|</div>
            <div class="b95-meta-segment">
              <strong>5 Regional Territories:</strong> Iraq, Türkiye, Bahrain, Libya, Syria
            </div>
          </div>
        </header>

        <!-- Master Index Ledger (Full-Width Architectural Rows) -->
        <div class="b95-master-ledger" role="table" aria-label="Regional Project Index">
          
          <!-- Ledger Column Header -->
          <div class="b95-ledger-table-header" role="row" aria-hidden="true">
            <span class="b95-th-cell b95-th-num">INDEX</span>
            <span class="b95-th-cell b95-th-node">SOVEREIGN NODE</span>
            <span class="b95-th-cell b95-th-title">COMMISSION TITLE</span>
            <span class="b95-th-cell b95-th-sector">CLASSIFICATION</span>
          </div>

          <!-- Row 01: Iraq (Baghdad) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">01</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                <clipPath id="flag-row-01"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-01)">
                  <rect width="32" height="10.66" fill="#CE1126"/>
                  <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                  <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                  <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">BAGHDAD, IRAQ</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">Artificial Lighting Units for Sports Stadium Turf</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-lightbulb b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Sports Infrastructure</span>
              </span>
            </div>
          </article>

          <!-- Row 02: Iraq (Basra - Safwan) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">02</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                <clipPath id="flag-row-02"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-02)">
                  <rect width="32" height="10.66" fill="#CE1126"/>
                  <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                  <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                  <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">BASRA - SAFWAN, IRAQ</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">Safwan International Highway Lighting Project</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-road b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Highway Infrastructure</span>
              </span>
            </div>
          </article>

          <!-- Row 03: Iraq (Basra) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">03</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                <clipPath id="flag-row-03"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-03)">
                  <rect width="32" height="10.66" fill="#CE1126"/>
                  <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                  <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                  <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">BASRA, IRAQ</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">International Basra Airport Renovation Project</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-plane-departure b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Aviation Facilities</span>
              </span>
            </div>
          </article>

          <!-- Row 04: Türkiye (Istanbul) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">04</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Turkey">
                <clipPath id="flag-row-04"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-04)">
                  <rect width="32" height="32" fill="#E30A17"/>
                  <circle cx="14" cy="16" r="6.8" fill="#FFFFFF"/>
                  <circle cx="16" cy="16" r="5.4" fill="#E30A17"/>
                  <polygon points="19,16 22.8,17.2 20.3,14 20.3,18 22.8,14.8" fill="#FFFFFF"/>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">ISTANBUL, TÜRKİYE</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">The 46th Turkish Construction Fair</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-city b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Commercial &amp; Fair</span>
              </span>
            </div>
          </article>

          <!-- Row 05: Bahrain (Manama) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">05</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Bahrain">
                <clipPath id="flag-row-05"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-05)">
                  <rect width="32" height="32" fill="#DA291C"/>
                  <path d="M0,0 L10,0 L14,3.2 L10,6.4 L14,9.6 L10,12.8 L14,16 L10,19.2 L14,22.4 L10,25.6 L14,28.8 L10,32 L0,32 Z" fill="#FFFFFF"/>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">MANAMA, BAHRAIN</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">Royal-Level Diplomatic Conference Hall</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-landmark b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Diplomatic &amp; Plenary</span>
              </span>
            </div>
          </article>

          <!-- Row 06: Libya (Benghazi) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">06</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Libya">
                <clipPath id="flag-row-06"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-06)">
                  <rect width="32" height="8" fill="#E70013"/>
                  <rect y="8" width="32" height="16" fill="#000000"/>
                  <rect y="24" width="32" height="8" fill="#239E46"/>
                  <circle cx="16" cy="16" r="4.8" fill="#FFFFFF"/>
                  <circle cx="17.2" cy="16" r="3.8" fill="#000000"/>
                  <polygon points="18.5,16 20.5,16.6 19.2,15 19.2,17 20.5,15.4" fill="#FFFFFF"/>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">BENGHAZI, LIBYA</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">Finishing &amp; Furnishing of Akam Al-Sonwan Specialty Hospital</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-hospital b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Healthcare Facilities</span>
              </span>
            </div>
          </article>

          <!-- Row 07: Syria (Idlib) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">07</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Syria">
                <clipPath id="flag-row-07"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-07)">
                  <rect width="32" height="10.66" fill="#CE1126"/>
                  <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                  <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                  <polygon points="11,16 13.2,16.6 11.8,14.8 11.8,17.2 13.2,15.4" fill="#007A3D"/>
                  <polygon points="21,16 23.2,16.6 21.8,14.8 21.8,17.2 23.2,15.4" fill="#007A3D"/>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">IDLIB, SYRIA</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">2000 Housing Units Design &amp; Implementation Project</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-people-roof b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Residential &amp; Urban</span>
              </span>
            </div>
          </article>

          <!-- Row 08: Iraq (Basra) -->
          <article class="b95-ledger-row" role="row" tabindex="0">
            <div class="b95-col-num" role="cell">08</div>
            <div class="b95-col-node" role="cell">
              <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                <clipPath id="flag-row-08"><circle cx="16" cy="16" r="16"/></clipPath>
                <g clip-path="url(#flag-row-08)">
                  <rect width="32" height="10.66" fill="#CE1126"/>
                  <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                  <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                  <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                </g>
                <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
              </svg>
              <span class="b95-node-text">BASRA, IRAQ</span>
            </div>
            <div class="b95-col-title" role="cell">
              <h3 class="b95-row-title">Sports City Road Lighting Project</h3>
            </div>
            <div class="b95-col-sector" role="cell">
              <span class="b95-sector-pill">
                <i class="fa-solid fa-tower-broadcast b95-sector-icon" aria-hidden="true"></i>
                <span class="b95-sector-name">Municipal Infrastructure</span>
              </span>
            </div>
          </article>

        </div>

      </div>
    </section>
'''

new_html = html[:s_start] + master_index_html + "\n\n" + html[s_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Applied architectural master index to index.html successfully!")
