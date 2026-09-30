import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_start = html.find('<!-- ====================================================================\n         SECTION 02: SOVEREIGN TERRITORY MATRIX')
if s_start == -1:
    s_start = html.find('id="sec-references"')
    s_start = html.rfind('<!--', 0, s_start)

s_end = html.find('<!-- ====================================================================\n         SECTION 03: FEATURED CASE STUDY')
if s_end == -1:
    s_end = html.find('id="sec-featured"')
    s_end = html.rfind('<!--', 0, s_end)

print(f"Replacing lines between {s_start} and {s_end}")

minimal_index_html = '''    <!-- ====================================================================
         SECTION 02: REFERENCES (ULTRA-MINIMALIST SWISS PROJECT INDEX)
         Strictly adhering to core items: Number, Location, Project Title
         ==================================================================== -->
    <section class="b95-section b95-references-minimal" id="sec-references" aria-labelledby="references-index-title">
      <div class="b95-container">
        
        <!-- Clean, Quiet Section Header -->
        <header class="b95-minimal-header">
          <div class="b95-minimal-eyebrow">
            <span class="b95-eyebrow-accent">02</span> / REFERENCES
          </div>
          <h2 class="b95-minimal-title" id="references-index-title">Selected Regional Works</h2>
          <p class="b95-minimal-subtitle">Flagship contracting and engineering projects executed across the region.</p>
        </header>

        <!-- Ultra-Minimalist Project Index Grid (2-Column Architecture) -->
        <div class="b95-project-index-grid">
          
          <!-- Item 01 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">01</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                BAGHDAD, IRAQ
              </div>
            </div>
            <h3 class="b95-index-card__title">Artificial Lighting Units for Sports Stadium Turf</h3>
          </article>

          <!-- Item 02 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">02</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                BASRA, IRAQ
              </div>
            </div>
            <h3 class="b95-index-card__title">Safwan International Highway Lighting Project</h3>
          </article>

          <!-- Item 03 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">03</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                BASRA, IRAQ
              </div>
            </div>
            <h3 class="b95-index-card__title">International Basra Airport Renovation Project</h3>
          </article>

          <!-- Item 04 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">04</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                ISTANBUL, TÜRKİYE
              </div>
            </div>
            <h3 class="b95-index-card__title">The 46th Turkish Construction Fair</h3>
          </article>

          <!-- Item 05 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">05</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                MANAMA, BAHRAIN
              </div>
            </div>
            <h3 class="b95-index-card__title">Royal-Level Diplomatic Conference Hall</h3>
          </article>

          <!-- Item 06 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">06</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                BENGHAZI, LIBYA
              </div>
            </div>
            <h3 class="b95-index-card__title">Finishing &amp; Furnishing of Akam Al-Sonwan Specialty Hospital</h3>
          </article>

          <!-- Item 07 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">07</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                IDLIB, SYRIA
              </div>
            </div>
            <h3 class="b95-index-card__title">2000 Housing Units Design &amp; Implementation Project</h3>
          </article>

          <!-- Item 08 -->
          <article class="b95-project-index-card" tabindex="0">
            <div class="b95-index-card__top">
              <span class="b95-index-card__num">08</span>
              <div class="b95-index-card__loc">
                <span class="b95-loc-bullet" aria-hidden="true"></span>
                BASRA, IRAQ
              </div>
            </div>
            <h3 class="b95-index-card__title">Sports City Road Lighting Project</h3>
          </article>

        </div>
      </div>
    </section>
'''

updated_html = html[:s_start] + minimal_index_html + "\n\n" + html[s_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Applied ultra-minimalist project index HTML successfully!")
