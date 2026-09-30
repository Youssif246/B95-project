import os

# Define the 5 Country Silhouette SVGs with clean geometric vector styling
svg_iraq = '''<svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Iraq territory silhouette">
  <path d="M14 20 L28 12 L46 14 L52 26 L48 44 L34 54 L20 46 L12 36 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
  <path d="M22 18 L34 32 L40 48" stroke="#991B1B" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
  <path d="M28 16 L38 28 L44 42" stroke="#991B1B" stroke-width="1" stroke-dasharray="2 2" opacity="0.6"/>
  <circle cx="34" cy="32" r="2.5" fill="#991B1B"/>
</svg>'''

svg_bahrain = '''<svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Bahrain territory silhouette">
  <path d="M26 12 C34 12, 40 18, 40 26 C40 36, 34 52, 28 54 C22 52, 20 38, 20 26 C20 18, 22 12, 26 12 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
  <circle cx="28" cy="22" r="3" fill="#991B1B"/>
  <circle cx="28" cy="22" r="7" stroke="#991B1B" stroke-width="0.8" stroke-dasharray="2 2" opacity="0.7"/>
  <circle cx="44" cy="38" r="2" fill="#CBD5E1"/>
  <circle cx="46" cy="44" r="1.5" fill="#CBD5E1"/>
</svg>'''

svg_libya = '''<svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Libya territory silhouette">
  <path d="M12 22 L26 14 L42 22 L54 18 L56 36 L50 52 L16 52 L12 34 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
  <path d="M26 14 Q34 24 42 22" stroke="#991B1B" stroke-width="1.5" fill="none"/>
  <circle cx="44" cy="22" r="2.5" fill="#991B1B"/>
  <line x1="16" y1="36" x2="48" y2="36" stroke="#94A3B8" stroke-width="0.75" stroke-dasharray="2 3"/>
</svg>'''

svg_syria = '''<svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Syria territory silhouette">
  <path d="M16 26 L32 14 L52 18 L50 32 L36 44 L20 46 L14 34 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
  <path d="M24 20 L38 28 L46 26" stroke="#991B1B" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <circle cx="26" cy="22" r="2.5" fill="#991B1B"/>
  <circle cx="38" cy="28" r="2" fill="#0F172A"/>
</svg>'''

svg_turkey = '''<svg class="b95-country-silhouette" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Turkey territory silhouette">
  <path d="M10 24 L20 20 L48 18 L56 26 L54 38 L38 42 L18 40 L10 32 Z" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.2"/>
  <circle cx="20" cy="23" r="3" fill="#991B1B"/>
  <circle cx="20" cy="23" r="6.5" stroke="#991B1B" stroke-width="0.8" opacity="0.6"/>
  <line x1="20" y1="23" x2="48" y2="30" stroke="#991B1B" stroke-width="1.2" stroke-dasharray="2 2"/>
</svg>'''

print("SVGs prepared successfully!")
