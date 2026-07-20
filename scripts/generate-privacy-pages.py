#!/usr/bin/env python3
"""Generate product privacy pages from shared template."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PRIVACY_SHELL = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Privacy Policy — {name_plain}</title>
    <meta name="description" content="{meta}" />
    <link rel="icon" href="../../images/logo/favicon.ico" type="image/x-icon" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
    <link rel="stylesheet" href="../../style.css" />
</head>

<body>

    <header class="site-header scrolled" id="siteHeader">
        <div class="container header-inner">
            <a href="/" class="logo">
                <img src="../../images/logo/gradientlogo.webp" alt="QAYHAM" class="logo-img" />
                <span class="logo-text">QAYHAM</span>
            </a>
            <nav class="nav" id="mainNav">
                <ul class="nav-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/#products">Products</a></li>
                    <li><a href="/#services">Services</a></li>
                    <li><a href="/#contact">Contact</a></li>
                </ul>
                <a href="/cloudnotes/" class="btn btn-sm btn-primary nav-cta">Cloud Notes</a>
            </nav>
            <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <main>
        <div class="page-hero">
            <div class="container">
                <span class="section-tag">Legal</span>
                <h1>Privacy Policy</h1>
                <p>{name_plain} · Last updated: {updated}</p>
            </div>
        </div>

        <section class="policy-section">
            <div class="container">
                <div class="policy-content">
{body}
                    <p class="policy-back"><a href="/privacy.html">&larr; QAYHAM master privacy policy</a></p>
                </div>
            </div>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="/" class="logo">
                        <img src="../../images/logo/gradientlogo.webp" alt="QAYHAM" class="logo-img" />
                        <span class="logo-text">QAYHAM</span>
                    </a>
                    <p>Building mobile apps and web tools that people actually use.</p>
                </div>
                <div class="footer-col">
                    <h4>Navigate</h4>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/#products">Products</a></li>
                        <li><a href="/#services">Services</a></li>
                        <li><a href="/#contact">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>This app</h4>
                    <ul>
                        <li><a href="/products/{slug}/">App page</a></li>
                        <li><a href="https://play.google.com/store/apps/details?id={play_id}" target="_blank" rel="noopener noreferrer">Google Play</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="/privacy.html">QAYHAM Privacy</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 QAYHAM · {name_plain}. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/919682318133" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
        <i class="fab fa-whatsapp"></i>
    </a>

    <button class="back-to-top" id="backToTop" aria-label="Back to top">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
    </button>

    <script src="../../app.js"></script>
</body>

</html>
"""

CONTACT = """
                    <h3>{contact_heading}</h3>
                    <p>If you have questions about this Privacy Policy, contact us:</p>
                    <div class="policy-contact">
                        <strong>QAYHAM — {name_plain}</strong><br />
                        Email: <a href="mailto:parraybilal34@gmail.com">parraybilal34@gmail.com</a><br />
                        WhatsApp: <a href="https://wa.me/919682318133">+91 96823 18133</a><br />
                        App ID: <code>{play_id}</code>
                    </div>
"""

POLICIES = [
    {
        "slug": "trainerflow",
        "name_plain": "Trainer Flow",
        "meta": "Privacy Policy for Trainer Flow by QAYHAM — client and workout management for personal trainers.",
        "play_id": "com.qayham.trainerflow",
        "updated": "June 10, 2026",
        "filename": "privacy.html",
        "body": """
                    <p>
                        This Privacy Policy describes how <strong>QAYHAM</strong> handles information when you use
                        <strong>Trainer Flow</strong> (the &ldquo;App&rdquo;). Trainer Flow helps personal trainers
                        manage clients, workouts, and schedules.
                    </p>

                    <div class="policy-highlight">
                        <strong>The short version:</strong> Trainer Flow stores the training data you enter to provide
                        app features. We do not sell your personal information. Contact us to request access or deletion.
                    </div>

                    <h3>1. Information we collect</h3>
                    <p>Depending on how you use the App, we may process:</p>
                    <ul>
                        <li>Account information if you sign in (such as email, name, or profile details)</li>
                        <li>Client names, workout plans, schedules, and notes you enter in the App</li>
                        <li>App settings and preferences stored on your device or synced to our backend, if enabled</li>
                        <li>Basic usage or crash data to keep the App reliable, if analytics or crash reporting is enabled</li>
                    </ul>

                    <h3>2. How we use information</h3>
                    <ul>
                        <li>To provide client, workout, and scheduling features</li>
                        <li>To sync your data across devices when cloud sync is available</li>
                        <li>To improve stability, security, and performance</li>
                        <li>To respond to support requests</li>
                    </ul>
                    <p>We do not sell your personal information.</p>

                    <h3>3. Third-party services</h3>
                    <p>The App may use third-party services such as:</p>
                    <ul>
                        <li><strong>Google Play</strong> — app distribution and in-app purchases, if applicable</li>
                        <li><strong>Google Firebase or similar cloud services</strong> — if sign-in or sync is enabled</li>
                    </ul>

                    <h3>4. Permissions</h3>
                    <p>The App may request permissions only as needed for features you use, such as notifications for reminders or storage for exports.</p>

                    <h3>5. Data retention and your choices</h3>
                    <p>We retain data for as long as needed to provide the App. You may delete content in the App where supported, or contact us to request account or data deletion.</p>

                    <h3>6. Children&rsquo;s privacy</h3>
                    <p>The App is not directed at children under 13. We do not knowingly collect personal information from children.</p>

                    <h3>7. Changes to this policy</h3>
                    <p>We may update this Privacy Policy from time to time. Continued use of the App after changes means you accept the updated policy.</p>
""" + CONTACT.format(contact_heading="8. Contact us", name_plain="Trainer Flow", play_id="com.qayham.trainerflow"),
    },
    {
        "slug": "quickunits",
        "name_plain": "Quick Units",
        "meta": "Privacy Policy for Quick Units by QAYHAM — instant unit and currency conversion.",
        "play_id": "com.qayham.quickunits",
        "updated": "June 10, 2026",
        "filename": "privacy.html",
        "body": """
                    <p>
                        This Privacy Policy explains how <strong>Quick Units</strong> (the &ldquo;App&rdquo;), published by
                        <strong>QAYHAM</strong>, handles your information when you convert units and currencies.
                    </p>

                    <div class="policy-highlight">
                        <strong>The short version:</strong> Quick Units is a utility app. Conversions you perform stay on
                        your device. The App may fetch public exchange rates from the internet but does not require an account.
                    </div>

                    <h3>1. Information we collect</h3>
                    <p>Quick Units is designed to collect minimal personal information:</p>
                    <ul>
                        <li>We do <strong>not</strong> require you to create an account</li>
                        <li>Conversion inputs you enter are processed on your device</li>
                        <li>We do <strong>not</strong> sell your personal information</li>
                    </ul>

                    <h3>2. Network use</h3>
                    <p>
                        For live currency rates, the App may request public rate data from third-party APIs or services
                        over the internet. Those requests may include basic technical data such as your IP address as
                        handled by the rate provider, not by QAYHAM directly operating a separate tracking service.
                    </p>

                    <h3>3. Local storage</h3>
                    <p>The App may store preferences (such as favorite units or recent conversions) locally on your device.</p>

                    <h3>4. Advertising and analytics</h3>
                    <p>
                        If the App displays ads or uses analytics, those providers may collect device or usage information
                        under their own policies. Check the Google Play Data safety section for the current disclosure.
                    </p>

                    <h3>5. Children&rsquo;s privacy</h3>
                    <p>The App is not directed at children under 13. We do not knowingly collect personal information from children.</p>

                    <h3>6. Changes to this policy</h3>
                    <p>We may update this Privacy Policy from time to time. Continued use of the App after changes means you accept the updated policy.</p>
""" + CONTACT.format(contact_heading="7. Contact us", name_plain="Quick Units", play_id="com.qayham.quickunits"),
    },
    {
        "slug": "compoundcalculator",
        "name_plain": "Compound Calculator",
        "meta": "Privacy Policy for Compound Calculator by QAYHAM — compound interest calculations.",
        "play_id": "com.bilalparray07.compoundingcalculator",
        "updated": "June 10, 2026",
        "filename": "privacy.html",
        "body": """
                    <p>
                        This Privacy Policy explains how <strong>Compound Calculator</strong> (the &ldquo;App&rdquo;),
                        published by <strong>QAYHAM</strong>, handles your information when you use the calculator.
                    </p>

                    <div class="policy-highlight">
                        <strong>The short version:</strong> Compound Calculator performs calculations on your device.
                        We do not require an account and do not collect the financial figures you enter on QAYHAM servers.
                    </div>

                    <h3>1. Information we collect</h3>
                    <ul>
                        <li>We do <strong>not</strong> require you to create an account</li>
                        <li>Calculation inputs are processed locally on your device</li>
                        <li>We do <strong>not</strong> sell your personal information</li>
                    </ul>

                    <h3>2. Local storage</h3>
                    <p>The App may store preferences or recent calculations locally on your device for convenience.</p>

                    <h3>3. Advertising</h3>
                    <p>
                        The App may display advertisements through third-party ad networks. Those networks may collect
                        information about your device or ad interactions under their own privacy policies. See the Google Play
                        Data safety section for current disclosures.
                    </p>

                    <h3>4. Children&rsquo;s privacy</h3>
                    <p>The App is not directed at children under 13. We do not knowingly collect personal information from children.</p>

                    <h3>5. Changes to this policy</h3>
                    <p>We may update this Privacy Policy from time to time. Continued use of the App after changes means you accept the updated policy.</p>
""" + CONTACT.format(contact_heading="6. Contact us", name_plain="Compound Calculator", play_id="com.bilalparray07.compoundingcalculator"),
    },
]


def main() -> None:
    for policy in POLICIES:
        html = PRIVACY_SHELL.format(
            name_plain=policy["name_plain"],
            meta=policy["meta"],
            updated=policy["updated"],
            slug=policy["slug"],
            play_id=policy["play_id"],
            body=policy["body"],
        )
        out_dir = ROOT / "products" / policy["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / policy["filename"]
        out_path.write_text(html, encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
