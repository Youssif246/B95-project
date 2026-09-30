import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_start = html.find('<!-- ====================================================================\n         SECTION 02: REFERENCES (ULTRA-MINIMALIST')
if s_start == -1:
    s_start = html.find('id="sec-references"')
    s_start = html.rfind('<!--', 0, s_start)

s_end = html.find('<!-- ====================================================================\n         SECTION 03: FEATURED CASE STUDY')
if s_end == -1:
    s_end = html.find('id="sec-featured"')
    s_end = html.rfind('<!--', 0, s_end)

print(f"Replacing lines {s_start} to {s_end}")

elevated_section_html = '''    <!-- ====================================================================
         SECTION 02: REFERENCES (ELEVATED MINIMAL PROJECT CARDS)
         Features: Sector FA6 Icons, Circular Country Flag Badges, Clean Layout
         ==================================================================== -->
    <section class="b95-section b95-references-elevated-index" id="sec-references" aria-labelledby="references-index-title">
      <div class="b95-container">
        
        <!-- Clean, Quiet Section Header -->
        <header class="b95-minimal-header">
          <div class="b95-minimal-eyebrow">
            <span class="b95-eyebrow-accent">02</span> / REFERENCES
          </div>
          <h2 class="b95-minimal-title" id="references-index-title">Selected Regional Works</h2>
          <p class="b95-minimal-subtitle">Flagship contracting and engineering projects executed across the region.</p>
        </header>

        <!-- Elevated 2-Column Minimal Index Grid -->
        <div class="b95-elevated-cards-grid">
          
          <!-- Card 01: Iraq (Baghdad) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">01</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                  <clipPath id="flag-clip-01"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-01)">
                    <rect width="32" height="10.66" fill="#CE1126"/>
                    <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                    <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                    <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">BAGHDAD, IRAQ</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-lightbulb"></i>
              </span>
              <span class="b95-sector-label">Sports Infrastructure</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">Artificial Lighting Units for Sports Stadium Turf</h3>
          </article>

          <!-- Card 02: Iraq (Basra - Safwan) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">02</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                  <clipPath id="flag-clip-02"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-02)">
                    <rect width="32" height="10.66" fill="#CE1126"/>
                    <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                    <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                    <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">BASRA - SAFWAN, IRAQ</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-road"></i>
              </span>
              <span class="b95-sector-label">Highway Infrastructure</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">Safwan International Highway Lighting Project</h3>
          </article>

          <!-- Card 03: Iraq (Basra Airport) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">03</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                  <clipPath id="flag-clip-03"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-03)">
                    <rect width="32" height="10.66" fill="#CE1126"/>
                    <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                    <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                    <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">BASRA, IRAQ</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-plane-departure"></i>
              </span>
              <span class="b95-sector-label">Aviation Facilities</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">International Basra Airport Renovation Project</h3>
          </article>

          <!-- Card 04: Türkiye (Istanbul) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">04</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Turkey">
                  <clipPath id="flag-clip-04"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-04)">
                    <rect width="32" height="32" fill="#E30A17"/>
                    <circle cx="14" cy="16" r="6.8" fill="#FFFFFF"/>
                    <circle cx="16" cy="16" r="5.4" fill="#E30A17"/>
                    <polygon points="19,16 22.8,17.2 20.3,14 20.3,18 22.8,14.8" fill="#FFFFFF"/>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">ISTANBUL, TÜRKİYE</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-city"></i>
              </span>
              <span class="b95-sector-label">Commercial &amp; Fair</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">The 46th Turkish Construction Fair</h3>
          </article>

          <!-- Card 05: Bahrain (Manama) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">05</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Bahrain">
                  <clipPath id="flag-clip-05"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-05)">
                    <rect width="32" height="32" fill="#DA291C"/>
                    <path d="M0,0 L10,0 L14,3.2 L10,6.4 L14,9.6 L10,12.8 L14,16 L10,19.2 L14,22.4 L10,25.6 L14,28.8 L10,32 L0,32 Z" fill="#FFFFFF"/>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">MANAMA, BAHRAIN</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-landmark"></i>
              </span>
              <span class="b95-sector-label">Diplomatic &amp; Plenary</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">Royal-Level Diplomatic Conference Hall</h3>
          </article>

          <!-- Card 06: Libya (Benghazi) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">06</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Libya">
                  <clipPath id="flag-clip-06"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-06)">
                    <rect width="32" height="8" fill="#E70013"/>
                    <rect y="8" width="32" height="16" fill="#000000"/>
                    <rect y="24" width="32" height="8" fill="#239E46"/>
                    <circle cx="16" cy="16" r="4.8" fill="#FFFFFF"/>
                    <circle cx="17.2" cy="16" r="3.8" fill="#000000"/>
                    <polygon points="18.5,16 20.5,16.6 19.2,15 19.2,17 20.5,15.4" fill="#FFFFFF"/>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">BENGHAZI, LIBYA</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-hospital"></i>
              </span>
              <span class="b95-sector-label">Healthcare Facilities</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">Finishing &amp; Furnishing of Akam Al-Sonwan Specialty Hospital</h3>
          </article>

          <!-- Card 07: Syria (Idlib) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">07</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Syria">
                  <clipPath id="flag-clip-07"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-07)">
                    <rect width="32" height="10.66" fill="#CE1126"/>
                    <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                    <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                    <polygon points="11,16 13.2,16.6 11.8,14.8 11.8,17.2 13.2,15.4" fill="#007A3D"/>
                    <polygon points="21,16 23.2,16.6 21.8,14.8 21.8,17.2 23.2,15.4" fill="#007A3D"/>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">IDLIB, SYRIA</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-people-roof"></i>
              </span>
              <span class="b95-sector-label">Residential &amp; Urban</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">2000 Housing Units Design &amp; Implementation Project</h3>
          </article>

          <!-- Card 08: Iraq (Basra Sports City) -->
          <article class="b95-elevated-card" tabindex="0">
            <!-- Top Row: Number + Country Pill -->
            <div class="b95-card-top-row">
              <span class="b95-card-num">08</span>
              <div class="b95-country-pill">
                <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                  <clipPath id="flag-clip-08"><circle cx="16" cy="16" r="16"/></clipPath>
                  <g clip-path="url(#flag-clip-08)">
                    <rect width="32" height="10.66" fill="#CE1126"/>
                    <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                    <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                    <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                  </g>
                  <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                </svg>
                <span class="b95-country-label">BASRA, IRAQ</span>
              </div>
            </div>

            <!-- Middle Section: Sector Icon Badge + Category Label -->
            <div class="b95-card-middle">
              <span class="b95-sector-icon-badge" aria-hidden="true">
                <i class="fa-solid fa-tower-broadcast"></i>
              </span>
              <span class="b95-sector-label">Municipal Infrastructure</span>
            </div>

            <!-- Bottom Section: Bold Project Title -->
            <h3 class="b95-card-title">Sports City Road Lighting Project</h3>
          </article>

        </div>
      </div>
    </section>
'''

new_html = html[:s_start] + elevated_section_html + "\n\n" + html[s_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Applied elevated cards to index.html successfully!")
