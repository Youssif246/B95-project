import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the references section
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

print(f"Replacing lines from character {s_start} to {s_end}")

editorial_references_html = '''    <!-- ====================================================================
         SECTION 02: REFERENCES (ARCHITECTURAL MONOGRAPH PROJECT INDEX)
         Swiss Editorial 2-Column Ledger: Delicate Hairlines, No Boxy Cards
         ==================================================================== -->
    <section class="b95-section b95-references-editorial" id="sec-references" aria-labelledby="references-index-title">
      <div class="b95-container">
        
        <!-- Clean Monograph Section Header -->
        <header class="b95-editorial-header">
          <div class="b95-editorial-eyebrow">
            <span class="b95-eyebrow-accent">02</span> / REFERENCES &amp; REGIONAL REACH
          </div>
          <div class="b95-editorial-title-row">
            <h2 class="b95-editorial-title" id="references-index-title">Selected Works &amp; Commission Index</h2>
            <div class="b95-editorial-badge">08 REGIONAL COMMISSIONS</div>
          </div>
          <p class="b95-editorial-lead">Flagship contracting, infrastructure, and turnkey engineering commissions executed across sovereign operational territories.</p>
        </header>

        <!-- 2-Column Editorial Index Matrix (Left: 01-04 | Right: 05-08) -->
        <div class="b95-editorial-columns">
          
          <!-- Column A: Commissions 01 to 04 -->
          <div class="b95-editorial-column">
            
            <!-- Item 01: Iraq (Baghdad) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">01</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                      <clipPath id="flag-iq-01"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-iq-01)">
                        <rect width="32" height="10.66" fill="#CE1126"/>
                        <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                        <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                        <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">BAGHDAD, IRAQ</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-lightbulb b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Sports Infrastructure</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">Artificial Lighting Units for Sports Stadium Turf</h3>
              </div>
            </article>

            <!-- Item 02: Iraq (Basra - Safwan) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">02</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                      <clipPath id="flag-iq-02"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-iq-02)">
                        <rect width="32" height="10.66" fill="#CE1126"/>
                        <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                        <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                        <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">BASRA - SAFWAN, IRAQ</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-road b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Highway Infrastructure</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">Safwan International Highway Lighting Project</h3>
              </div>
            </article>

            <!-- Item 03: Iraq (Basra) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">03</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                      <clipPath id="flag-iq-03"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-iq-03)">
                        <rect width="32" height="10.66" fill="#CE1126"/>
                        <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                        <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                        <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">BASRA, IRAQ</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-plane-departure b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Aviation Facilities</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">International Basra Airport Renovation Project</h3>
              </div>
            </article>

            <!-- Item 04: Türkiye (Istanbul) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">04</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Turkey">
                      <clipPath id="flag-tr-04"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-tr-04)">
                        <rect width="32" height="32" fill="#E30A17"/>
                        <circle cx="14" cy="16" r="6.8" fill="#FFFFFF"/>
                        <circle cx="16" cy="16" r="5.4" fill="#E30A17"/>
                        <polygon points="19,16 22.8,17.2 20.3,14 20.3,18 22.8,14.8" fill="#FFFFFF"/>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">ISTANBUL, TÜRKİYE</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-city b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Commercial &amp; Fair</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">The 46th Turkish Construction Fair</h3>
              </div>
            </article>

          </div>

          <!-- Column B: Commissions 05 to 08 -->
          <div class="b95-editorial-column">
            
            <!-- Item 05: Bahrain (Manama) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">05</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Bahrain">
                      <clipPath id="flag-bh-05"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-bh-05)">
                        <rect width="32" height="32" fill="#DA291C"/>
                        <path d="M0,0 L10,0 L14,3.2 L10,6.4 L14,9.6 L10,12.8 L14,16 L10,19.2 L14,22.4 L10,25.6 L14,28.8 L10,32 L0,32 Z" fill="#FFFFFF"/>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">MANAMA, BAHRAIN</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-landmark b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Diplomatic &amp; Plenary</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">Royal-Level Diplomatic Conference Hall</h3>
              </div>
            </article>

            <!-- Item 06: Libya (Benghazi) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">06</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Libya">
                      <clipPath id="flag-ly-06"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-ly-06)">
                        <rect width="32" height="8" fill="#E70013"/>
                        <rect y="8" width="32" height="16" fill="#000000"/>
                        <rect y="24" width="32" height="8" fill="#239E46"/>
                        <circle cx="16" cy="16" r="4.8" fill="#FFFFFF"/>
                        <circle cx="17.2" cy="16" r="3.8" fill="#000000"/>
                        <polygon points="18.5,16 20.5,16.6 19.2,15 19.2,17 20.5,15.4" fill="#FFFFFF"/>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">BENGHAZI, LIBYA</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-hospital b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Healthcare Facilities</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">Finishing &amp; Furnishing of Akam Al-Sonwan Specialty Hospital</h3>
              </div>
            </article>

            <!-- Item 07: Syria (Idlib) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">07</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Syria">
                      <clipPath id="flag-sy-07"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-sy-07)">
                        <rect width="32" height="10.66" fill="#CE1126"/>
                        <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                        <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                        <polygon points="11,16 13.2,16.6 11.8,14.8 11.8,17.2 13.2,15.4" fill="#007A3D"/>
                        <polygon points="21,16 23.2,16.6 21.8,14.8 21.8,17.2 23.2,15.4" fill="#007A3D"/>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">IDLIB, SYRIA</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-people-roof b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Residential &amp; Urban</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">2000 Housing Units Design &amp; Implementation Project</h3>
              </div>
            </article>

            <!-- Item 08: Iraq (Basra) -->
            <article class="b95-editorial-strip" tabindex="0">
              <span class="b95-strip-num" aria-hidden="true">08</span>
              <div class="b95-strip-content">
                <div class="b95-strip-meta">
                  <div class="b95-meta-loc">
                    <svg class="b95-flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-label="Flag of Iraq">
                      <clipPath id="flag-iq-08"><circle cx="16" cy="16" r="16"/></clipPath>
                      <g clip-path="url(#flag-iq-08)">
                        <rect width="32" height="10.66" fill="#CE1126"/>
                        <rect y="10.66" width="32" height="10.66" fill="#FFFFFF"/>
                        <rect y="21.33" width="32" height="10.66" fill="#000000"/>
                        <text x="16" y="18" fill="#007A3D" font-size="5.5" font-weight="900" text-anchor="middle" font-family="sans-serif">الله أكبر</text>
                      </g>
                      <circle cx="16" cy="16" r="15.5" stroke="rgba(15,23,42,0.12)" stroke-width="1" fill="none"/>
                    </svg>
                    <span class="b95-loc-text">BASRA, IRAQ</span>
                  </div>
                  <span class="b95-meta-separator" aria-hidden="true">/</span>
                  <div class="b95-meta-sector">
                    <i class="fa-solid fa-tower-broadcast b95-sector-icon" aria-hidden="true"></i>
                    <span class="b95-sector-text">Municipal Infrastructure</span>
                  </div>
                </div>
                <h3 class="b95-strip-title">Sports City Road Lighting Project</h3>
              </div>
            </article>

          </div>

        </div>

      </div>
    </section>
'''

new_html = html[:s_start] + editorial_references_html + "\n\n" + html[s_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Applied editorial project index to index.html successfully!")
