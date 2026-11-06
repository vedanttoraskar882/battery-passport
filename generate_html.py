import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

# Read original page contents to verify
with open("original/index.html", 'r', encoding='utf-8') as f:
    orig_html = f.read()

# Let's craft the high quality SVG Circuit Network and Isometric Layered Battery Cell
hero_visual_html = """
    <div class="hero-visual-wrapper">
      <!-- Circuit Traces Network (Background Animation) -->
      <svg class="hero-circuits" viewBox="0 0 540 460" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <defs>
          <linearGradient id="traceGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#14D97D" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#3CF2C4" stop-opacity="0.1"/>
          </linearGradient>
          <linearGradient id="traceGrad2" x1="100%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#2E8FE0" stop-opacity="0.5"/>
            <stop offset="100%" stop-color="#14D97D" stop-opacity="0.15"/>
          </linearGradient>
          <filter id="glowLight" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur"/>
            <feComposite in="SourceGraphic" in2="blur" operator="over"/>
          </filter>
        </defs>

        <!-- Static Fine Etched Circuit Grid & Traces -->
        <path class="circuit-trace" d="M 30,120 L 140,120 L 180,160 L 320,160" />
        <path class="circuit-trace" d="M 80,60 L 220,60 L 260,100 L 380,100" />
        <path class="circuit-trace" d="M 40,280 L 160,280 L 210,230 L 340,230" />
        <path class="circuit-trace" d="M 110,380 L 240,380 L 280,340 L 410,340" />
        <path class="circuit-trace" d="M 450,110 L 480,110 L 510,140 L 510,260 L 470,300" />
        <path class="circuit-trace" d="M 280,30 L 340,30 L 370,60" />

        <!-- Nodes / Soldered Connection Pads -->
        <circle class="circuit-node" cx="30" cy="120" r="3"/>
        <circle class="circuit-node" cx="140" cy="120" r="2.5"/>
        <circle class="circuit-node" cx="80" cy="60" r="3"/>
        <circle class="circuit-node" cx="220" cy="60" r="2.5"/>
        <circle class="circuit-node" cx="40" cy="280" r="3"/>
        <circle class="circuit-node" cx="160" cy="280" r="2.5"/>
        <circle class="circuit-node" cx="110" cy="380" r="3"/>
        <circle class="circuit-node" cx="240" cy="380" r="2.5"/>
        <circle class="circuit-node" cx="510" cy="140" r="2.5"/>
        <circle class="circuit-node" cx="510" cy="260" r="2.5"/>

        <!-- Animated Traveling Pulses (Soft staggered cycle towards battery cell) -->
        <path class="circuit-pulse pulse-primary" filter="url(#glowLight)" d="M 30,120 L 140,120 L 180,160 L 320,160 L 380,160" />
        <path class="circuit-pulse pulse-secondary" filter="url(#glowLight)" d="M 80,60 L 220,60 L 260,100 L 380,100 L 420,130" />
        <path class="circuit-pulse pulse-tertiary" filter="url(#glowLight)" d="M 40,280 L 160,280 L 210,230 L 340,230 L 400,230" />
      </svg>

      <!-- Battery Pack Assembly (Layered Cells + Dashboard Card) -->
      <div class="battery-pack-assembly">
        <!-- Isometric Layered Battery Cell Artwork -->
        <svg class="battery-cells-svg" viewBox="0 0 340 260" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <!-- Metallic edge gradients & specular highlights -->
            <linearGradient id="anodeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2D3A34"/>
              <stop offset="40%" stop-color="#1B2420"/>
              <stop offset="100%" stop-color="#0F1613"/>
            </linearGradient>
            <linearGradient id="ceramicSeparator" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#E8EFEB"/>
              <stop offset="50%" stop-color="#C7D5CE"/>
              <stop offset="100%" stop-color="#9FB4AA"/>
            </linearGradient>
            <linearGradient id="cathodeFoil" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#4E5F57"/>
              <stop offset="50%" stop-color="#2A3731"/>
              <stop offset="100%" stop-color="#1A2420"/>
            </linearGradient>
            <linearGradient id="terminalCopper" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#E08A3C"/>
              <stop offset="100%" stop-color="#9C5216"/>
            </linearGradient>
            <linearGradient id="terminalNickel" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#E1E8EC"/>
              <stop offset="100%" stop-color="#7B8B94"/>
            </linearGradient>
            <linearGradient id="accentBeam" x1="20%" y1="0%" x2="80%" y2="100%">
              <stop offset="0%" stop-color="#14D97D" stop-opacity="0.45"/>
              <stop offset="50%" stop-color="#3CF2C4" stop-opacity="0.15"/>
              <stop offset="100%" stop-color="#14D97D" stop-opacity="0"/>
            </linearGradient>
            <filter id="softCellShadow" x="-10%" y="-10%" width="130%" height="130%">
              <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000" flood-opacity="0.55"/>
            </filter>
          </defs>

          <!-- Layer 1: Base Anode Substrate (Brushed Graphite) -->
          <g filter="url(#softCellShadow)">
            <polygon points="120,40 290,75 220,185 50,150" fill="url(#anodeGrad)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
            <polygon points="50,150 220,185 220,195 50,160" fill="#0C1310" stroke="rgba(255,255,255,0.06)" stroke-width="0.8"/>
            <polygon points="220,185 290,75 290,85 220,195" fill="#141C18" stroke="rgba(255,255,255,0.06)" stroke-width="0.8"/>
          </g>

          <!-- Layer 2: Ceramic Separator Layer (Pale Ceramic Surface) -->
          <g transform="translate(4, -14)">
            <polygon points="120,40 290,75 220,185 50,150" fill="url(#ceramicSeparator)" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
            <polygon points="50,150 220,185 220,190 50,155" fill="#889C92"/>
            <polygon points="220,185 290,75 290,80 220,190" fill="#ADC0B6"/>
          </g>

          <!-- Layer 3: Cathode Current Collector (Metallic Graphite/Alloy) -->
          <g transform="translate(8, -28)">
            <polygon points="120,40 290,75 220,185 50,150" fill="url(#cathodeFoil)" stroke="rgba(60,242,196,0.3)" stroke-width="1"/>
            <polygon points="50,150 220,185 220,193 50,158" fill="#131B17"/>
            <polygon points="220,185 290,75 290,83 220,193" fill="#1C2722"/>

            <!-- Current Collector Electrode Tabs -->
            <polygon points="100,55 125,48 115,22 90,29" fill="url(#terminalNickel)" stroke="rgba(255,255,255,0.4)" stroke-width="0.8"/>
            <polygon points="140,64 165,57 155,31 130,38" fill="url(#terminalCopper)" stroke="rgba(255,255,255,0.3)" stroke-width="0.8"/>

            <!-- Single Focused Accent Light Beam sweeping across top edge -->
            <polygon points="120,40 290,75 260,110 90,75" fill="url(#accentBeam)"/>
            <line x1="120" y1="40" x2="290" y2="75" stroke="#3CF2C4" stroke-width="1.5" stroke-opacity="0.8"/>
          </g>
        </svg>

        <!-- Preserved Original Hero Primary Visual: BPN Dashboard Card -->
        <div class="dash-card">
          <div class="dash-top">
            <div>
              <div class="dash-lbl">BPN Dashboard</div>
              <div class="dash-title">Today's Battery Risk Snapshot</div>
            </div>
            <div class="live-wrap"><span class="live-dot"></span> LIVE</div>
          </div>
          <div class="score-row">
            <div class="s-icon si-c"><i class="fas fa-shield-halved"></i></div>
            <div class="score-lbl">BPN Classification</div>
            <div class="score-val">BPN-B · Verified</div>
          </div>
          <div class="score-row">
            <div class="s-icon si-g"><i class="fas fa-chart-line"></i></div>
            <div class="score-lbl">Residual Commercial Life</div>
            <div class="score-val">14 months</div>
          </div>
          <div class="score-row">
            <div class="s-icon si-e"><i class="fas fa-triangle-exclamation"></i></div>
            <div class="score-lbl">Replacement Risk Flagged</div>
            <div class="score-val">2 devices</div>
          </div>
          <div class="score-big">
            <div class="sb-num">£1,180</div>
            <div class="sb-info">
              <div class="lbl">Estimated Weekly Margin Protected</div>
              <div class="sub">↑ from reduced post-sale returns</div>
            </div>
          </div>
        </div>
      </div>
    </div>
"""

# Let's read all other sections from our preserved original page chunks
with open("original_page-home.html", 'r', encoding='utf-8') as f:
    orig_home = f.read()

# Replace the hero portion in home with our redesigned hero (which includes original text and buttons + visual wrapper)
# Let's inspect where hero section ends in orig_home
hero_end = orig_home.find('</section>') + 10
home_after_hero = orig_home[hero_end:]

home_redesigned = f"""<div class="page active" id="page-home">
<section class="hero">
  <div class="hero-inner">
    <div>
      <div class="hero-badge"><span class="hero-bdot"></span> AI-Driven Battery Risk Intelligence</div>
      <h1>Certify Trust. <span class="blue">Protect Every Margin.</span></h1>
      <div class="hero-rule"></div>
      <p class="hero-body">Battery Passport Network is an AI-driven battery-risk intelligence and certification platform for the UK's secondary consumer electronics industry. We unify electrochemical diagnostics, replacement authenticity forensics and post-sale outcome data into one commercial trust identity  so refurbishers know exactly which batteries are safe to resell, before the device ever leaves the warehouse.</p>
      <div class="hero-btns">
        <button class="btn-p" onclick="showPage('contact')">Book a Demo <i class="fas fa-arrow-right" style="margin-left:6px"></i></button>
        <button class="btn-s" onclick="showPage('platform')">Explore the Platform</button>
      </div>
    </div>
{hero_visual_html}
  </div>
</section>
{home_after_hero}
"""

# Now let's gather all pages:
pages_dict = {
    'home': home_redesigned,
    'about': open("original_page-about.html", 'r', encoding='utf-8').read(),
    'platform': open("original_page-platform.html", 'r', encoding='utf-8').read(),
    'process': open("original_page-process.html", 'r', encoding='utf-8').read(),
    'market': open("original_page-market.html", 'r', encoding='utf-8').read(),
    'pricing': open("original_page-pricing.html", 'r', encoding='utf-8').read(),
    'faq': open("original_page-faq.html", 'r', encoding='utf-8').read(),
    'contact': open("original_page-contact.html", 'r', encoding='utf-8').read(),
    'privacy': open("original_page-privacy.html", 'r', encoding='utf-8').read(),
    'terms': open("original_page-terms.html", 'r', encoding='utf-8').read(),
    'fsa': open("original_page-fsa.html", 'r', encoding='utf-8').read()
}

# Navbar and Footer from original
footer_start = orig_html.find('<footer>')
footer_end = orig_html.find('</footer>') + 9
orig_footer = orig_html[footer_start:footer_end]

# Compose full index.html
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Battery Passport Network | AI-Driven Battery Risk Intelligence for UK Circular Economy</title>
  
  <!-- Google Fonts: Barlow Semi Condensed (Headings), Inter (Body & Controls), IBM Plex Mono (Technical Data) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:ital,wght@0,500;0,600;0,700;1,600&family=IBM+Plex+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  
  <!-- Chart.js for Market Analytics -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
  
  <!-- Redesigned Industrial Design Stylesheet -->
  <link rel="stylesheet" href="styles.css">
  
  <!-- Application Logic -->
  <script src="app.js" defer></script>
</head>
<body>

  <!-- Navigation Bar -->
  <nav class="navbar">
    <a class="nav-logo" onclick="showPage('home')">
      <div class="nav-logo-icon"><i class="fas fa-battery-full"></i></div>
      <div class="nav-logo-text">Battery Passport Network<span>Battery Risk Intelligence</span></div>
    </a>
    <ul class="nav-links">
      <li><button id="nav-home" class="active" onclick="showPage('home')">Home</button></li>
      <li><button id="nav-about" onclick="showPage('about')">About</button></li>
      <li><button id="nav-platform" onclick="showPage('platform')">Platform</button></li>
      <li><button id="nav-process" onclick="showPage('process')">How It Works</button></li>
      <li><button id="nav-market" onclick="showPage('market')">Market</button></li>
      <li><button id="nav-pricing" onclick="showPage('pricing')">Pricing</button></li>
      <li><button id="nav-faq" onclick="showPage('faq')">FAQ</button></li>
    </ul>
    
    <div class="nav-right">
      <button class="btn-demo-nav" onclick="showPage('contact')">Book a Demo</button>
      <button class="hamburger" id="hamburger" aria-label="Toggle navigation menu"><span></span><span></span><span></span></button>
    </div>
  </nav>

  <!-- Mobile Drawer Navigation -->
  <div class="mobile-nav" id="mobileNav">
    <button onclick="showPage('home');closeMob()">Home</button>
    <button onclick="showPage('about');closeMob()">About</button>
    <button onclick="showPage('platform');closeMob()">Platform</button>
    <button onclick="showPage('process');closeMob()">How It Works</button>
    <button onclick="showPage('market');closeMob()">Market</button>
    <button onclick="showPage('pricing');closeMob()">Pricing</button>
    <button onclick="showPage('faq');closeMob()">FAQ</button>
    <button class="mob-cta" onclick="showPage('contact');closeMob()">Book a Demo</button>
  </div>

  <!-- Page Containers -->
  {pages_dict['home']}
  {pages_dict['about']}
  {pages_dict['platform']}
  {pages_dict['process']}
  {pages_dict['market']}
  {pages_dict['pricing']}
  {pages_dict['faq']}
  {pages_dict['contact']}
  {pages_dict['privacy']}
  {pages_dict['terms']}
  {pages_dict['fsa']}

  <!-- Footer -->
  {orig_footer}

</body>
</html>
"""

output_path = os.path.join("battery-passport-redesign", "index.html")
with open(output_path, 'w', encoding='utf-8') as out:
    out.write(full_html)

print("Generated battery-passport-redesign/index.html successfully.")
print(f"File size: {os.path.getsize(output_path)} bytes")
