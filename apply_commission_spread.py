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

new_section_html = '''    <!-- ====================================================================
         SECTION 02: REFERENCES (ARCHITECTURAL COMMISSION LEDGER)
         Asymmetric Editorial Spread: Left Pillar (28%) + Right Ledger (72%)
         ==================================================================== -->
    <section class="b95-section b95-commission-spread" id="sec-references" aria-labelledby="commission-spread-title">
      <div class="b95-container">
        
        <div class="b95-spread-layout">
          
          <!-- LEFT PILLAR: Editorial Context Panel (approx 28%) -->
          <aside class="b95-spread-pillar">
            <div class="b95-pillar-sticky">
              
              <div class="b95-pillar-eyebrow">
                <span class="b95-eyebrow-accent">02</span> / REGIONAL MONOGRAPH
              </div>
              
              <h2 class="b95-pillar-title" id="commission-spread-title">
                Architectural Commission Ledger
              </h2>
              
              <p class="b95-pillar-lead">
                A verified index of sovereign turnkey general contracting, civil engineering, and specialized infrastructure commissions delivered across regional hubs.
              </p>

              <!-- Operational HQ Coordinates -->
              <div class="b95-pillar-hq">
                <div class="b95-hq-badge">
                  <span class="b95-hq-dot"></span>
                  <span class="b95-hq-label">HQ: ISTANBUL, TÜRKİYE</span>
                </div>
                <span class="b95-hq-coords">41.0082° N, 28.9784° E</span>
              </div>

              <!-- Typographic Metric Box -->
              <div class="b95-pillar-stat-box">
                <div class="b95-stat-huge">08</div>
                <div class="b95-stat-meta">
                  <span class="b95-stat-title">Sovereign Projects</span>
                  <span class="b95-stat-desc">Executed across Turkey, Iraq, Bahrain, Libya &amp; Syria</span>
                </div>
              </div>

              <!-- Territory Pill Badges -->
              <div class="b95-pillar-territories">
                <span class="b95-terr-tag">IRAQ</span>
                <span class="b95-terr-tag">TÜRKİYE</span>
                <span class="b95-terr-tag">BAHRAIN</span>
                <span class="b95-terr-tag">LIBYA</span>
                <span class="b95-terr-tag">SYRIA</span>
              </div>

            </div>
          </aside>

          <!-- RIGHT LEDGER: The 8 Projects in an Alternating Architectural Grid (approx 72%) -->
          <main class="b95-spread-ledger">
            
            <div class="b95-ledger-grid">
              
              <!-- Item 01: Iraq (Baghdad) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">01</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                        <clipPath id="f-clip-iq1"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-iq1)">
                          <rect width="32" height="10.66" fill="#CE1126"/>
                          <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                          <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                          <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">BAGHDAD, IRAQ</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-lightbulb b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Sports Infrastructure</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">Artificial Lighting Units for Sports Stadium Turf</h3>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Item 02: Iraq (Basra - Safwan) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">02</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                        <clipPath id="f-clip-iq2"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-iq2)">
                          <rect width="32" height="10.66" fill="#CE1126"/>
                          <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                          <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                          <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">BASRA - SAFWAN, IRAQ</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-road b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Highway Infrastructure</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">Safwan International Highway Lighting Project</h3>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Item 03: Iraq (Basra) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">03</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                        <clipPath id="f-clip-iq3"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-iq3)">
                          <rect width="32" height="10.66" fill="#CE1126"/>
                          <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                          <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                          <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">BASRA, IRAQ</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-plane-departure b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Aviation Facilities</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">International Basra Airport Renovation Project</h3>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Item 04: Türkiye (Istanbul) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">04</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Turkey">
                        <clipPath id="f-clip-tr4"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-tr4)">
                          <rect width="32" height="32" fill="#E30A17"/>
                          <circle cx="14" cy="16" r="6.8" fill="#FFFFFF"/>
                          <circle cx="16" cy="16" r="5.4" fill="#E30A17"/>
                          <polygon points="19,16 22.8,17.2 20.3,14 20.3,18 22.8,14.8" fill="#FFFFFF"/>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">ISTANBUL, TÜRKİYE</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-city b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Commercial &amp; Fair</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">The 46th Turkish Construction Fair</h3>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Item 05: Bahrain (Manama) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">05</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Bahrain">
                        <clipPath id="f-clip-bh5"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-bh5)">
                          <rect width="32" height="32" fill="#DA291C"/>
                          <path d="M0,0 L10,0 L14,3.2 L10,6.4 L14,9.6 L10,12.8 L14,16 L10,19.2 L14,22.4 L10,25.6 L14,28.8 L10,32 L0,32 Z" fill="#FFFFFF"/>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">MANAMA, BAHRAIN</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-landmark b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Diplomatic &amp; Plenary</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">Royal-Level Diplomatic Conference Hall</h3>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Item 06: Libya (Benghazi) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">06</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Libya">
                        <clipPath id="f-clip-ly6"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-ly6)">
                          <rect width="32" height="8" fill="#E70013"/>
                          <rect y="8" width="32" height="16" fill="#000000"/>
                          <rect y="24" width="32" height="8" fill="#239E46"/>
                          <circle cx="16" cy="16" r="4.8" fill="#FFFFFF"/>
                          <circle cx="17.2" cy="16" r="3.8" fill="#000000"/>
                          <polygon points="18.5,16 20.5,16.6 19.2,15 19.2,17 20.5,15.4" fill="#FFFFFF"/>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">BENGHAZI, LIBYA</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-hospital b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Healthcare Facilities</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">Finishing &amp; Furnishing of Akam Al-Sonwan Specialty Hospital</h3>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Item 07: Syria (Idlib) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">07</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Syria">
                        <clipPath id="f-clip-sy7"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-sy7)">
                          <rect width="32" height="10.66" fill="#CE1126"/>
                          <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                          <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                          <polygon points="11,16 13.2,16.6 11.8,14.8 11.8,17.2 13.2,15.4" fill="#007A3D"/>
                          <polygon points="21,16 23.2,16.6 21.8,14.8 21.8,17.2 23.2,15.4" fill="#007A3D"/>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">IDLIB, SYRIA</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-people-roof b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Residential &amp; Urban</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">2000 Housing Units Design &amp; Implementation Project</h3>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Item 08: Iraq (Basra) -->
              <article class="b95-ledger-item" tabindex="0">
                <span class="b95-ledger-watermark" aria-hidden="true">08</span>
                <div class="b95-item-inner">
                  <div class="b95-item-topbar">
                    <div class="b95-item-country">
                      <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                        <clipPath id="f-clip-iq8"><circle cx="16" cy="16" r="16"/></clipPath>
                        <g clip-path="url(#f-clip-iq8)">
                          <rect width="32" height="10.66" fill="#CE1126"/>
                          <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                          <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                          <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                        </g>
                        <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                      </svg>
                      <span class="b95-country-name">BASRA, IRAQ</span>
                    </div>
                    <div class="b95-item-sector">
                      <i class="fa-solid fa-tower-broadcast b95-fa-sector" aria-hidden="true"></i>
                      <span class="b95-sector-name">Municipal Infrastructure</span>
                    </div>
                  </div>
                  <div class="b95-item-body">
                    <div class="b95-title-wrap">
                      <h3 class="b95-item-title">Sports City Road Lighting Project</h3>
                    </div>
                  </div>
                </div>
              </article>

            </div>

          </main>

        </div>

      </div>
    </section>
'''

new_html = html[:s_start] + new_section_html + "\n\n" + html[s_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Applied architectural commission spread to index.html successfully!")
