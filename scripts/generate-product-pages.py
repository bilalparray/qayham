#!/usr/bin/env python3
"""Generate premium product landing pages."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def stat(value: str, label: str) -> dict:
    return {"value": value, "label": label}


def card(icon: str, title: str, desc: str) -> dict:
    return {"icon": icon, "title": title, "desc": desc}


def step(title: str, desc: str) -> dict:
    return {"title": title, "desc": desc}


APPS = [
    {
        "slug": "tradejournal",
        "name": "Trade Journal",
        "category": "Finance · Productivity",
        "tagline": "The trading journal built for discipline, clarity, and daily P&amp;L.",
        "overview": "Trade Journal helps you log every session, track profit and loss, and review what actually works — not what you wish worked. From quick daily entries to deep strategy reviews, it keeps your edge sharp and your data organized across devices.",
        "icon": "tradejournal.png",
        "play_id": "com.qayham.tradejournal",
        "privacy": "privacy-policy.html",
        "stats": [stat("4.8★", "User rating"), stat("Cloud sync", "Cross-device"), stat("Pro", "Upgrade available")],
        "trust": ["Google Play verified", "Firebase secure sync", "Google Sign-In", "Export-friendly workflow"],
        "pills": [("Daily P&amp;L", "fa-chart-line"), ("Strategies", "fa-chess"), ("Cloud sync", "fa-cloud")],
        "highlights": [
            card("fa-book", "Structured trade logging", "Capture dates, P&amp;L, market type, tags, psychology notes, and screenshots in one place."),
            card("fa-bullseye", "Goals that keep you honest", "Set monthly targets and track progress so emotions do not rewrite your results."),
            card("fa-layer-group", "Strategies &amp; analytics", "Group trades by strategy, review performance, and spot patterns over time."),
        ],
        "features": [
            card("fa-pen-to-square", "Rich trade entries", "Notes, tags, mood ratings, and attachments for complete context."),
            card("fa-calendar-days", "Calendar &amp; history", "Browse sessions by day and month with a clear timeline view."),
            card("fa-file-csv", "CSV import &amp; export", "Bring existing data in and export when you need a backup."),
            card("fa-bell", "Smart reminders", "Optional notifications to build a consistent journaling habit."),
            card("fa-user-shield", "Secure cloud backup", "Sync with Google Sign-In via Firebase when you are signed in."),
            card("fa-gem", "Pro features", "Unlock advanced sync, storage, and premium tools with a subscription."),
        ],
        "steps": [
            step("Log your session", "Record trades, P&amp;L, and notes right after the market — while details are fresh."),
            step("Review with context", "Use tags, strategies, and analytics to see what is working over weeks and months."),
            step("Improve deliberately", "Adjust goals, refine rules, and trade with a clearer picture of your edge."),
        ],
        "privacy_points": [
            "Account and journal data stored when you sign in with Google",
            "Firebase security rules protect your documents",
            "You can delete entries or request account removal by email",
            "We do not sell your personal information",
        ],
    },
    {
        "slug": "whatsappgallery",
        "name": "WhatsApp Gallery",
        "category": "Utilities · Media",
        "tagline": "Your WhatsApp media, organized — private, fast, and fully on-device.",
        "overview": "WhatsApp Gallery turns scattered status downloads and chat media into a clean, searchable gallery. Browse photos and videos saved by WhatsApp, preview instantly, share anywhere, and optionally save to your camera roll — without uploading anything to our servers.",
        "icon": "whatsappgallery.png",
        "play_id": "com.qayham.whatsappgallery",
        "privacy": "privacy.html",
        "stats": [stat("On-device", "No uploads"), stat("Fast", "Thumbnail cache"), stat("Private", "Your phone only")],
        "trust": ["No analytics SDKs", "No cloud storage", "Google Play Billing for purchases", "Independent app — not affiliated with Meta"],
        "pills": [("Browse", "fa-images"), ("Preview", "fa-play"), ("Share", "fa-share-nodes")],
        "highlights": [
            card("fa-folder-open", "Instant media discovery", "Find WhatsApp photos, videos, and documents already stored on your device."),
            card("fa-eye", "Beautiful previews", "Scroll a clean grid with fast thumbnails and full-screen previews."),
            card("fa-lock", "Privacy by design", "Media stays on your phone. QAYHAM does not operate upload servers for your files."),
        ],
        "features": [
            card("fa-table-cells", "Grid &amp; theme options", "Adjust layout and appearance to suit how you browse."),
            card("fa-share-from-square", "Share anywhere", "Send media to other apps you choose — only when you tap share."),
            card("fa-download", "Save to gallery", "Unlock one-time purchase to copy files to your camera roll."),
            card("fa-bolt", "Cached thumbnails", "Indexed locally for speed — clear cache anytime in settings."),
            card("fa-mobile-screen", "Built for Android", "Optimized for modern storage permissions and large libraries."),
            card("fa-shield-halved", "Transparent permissions", "Storage access is used only to read WhatsApp media folders."),
        ],
        "steps": [
            step("Grant media access", "Allow the app to read WhatsApp folders on your device — nothing leaves your phone."),
            step("Browse &amp; preview", "Scroll your library, open photos and videos, and find what you need quickly."),
            step("Share or save", "Send to another app or save to gallery when you explicitly choose to."),
        ],
        "privacy_points": [
            "No personal data uploaded to QAYHAM servers",
            "No ads or analytics SDKs in the app",
            "Purchases handled by Google Play Billing",
            "Clear disclaimer: not affiliated with WhatsApp or Meta",
        ],
    },
    {
        "slug": "trainerflow",
        "name": "Trainer Flow",
        "category": "Fitness · Business",
        "tagline": "Run your coaching business from one focused mobile workspace.",
        "overview": "Trainer Flow is built for personal trainers who need less admin and more time with clients. Manage rosters, plan workouts, track sessions, and keep schedules organized — with a clean interface designed for daily use in the gym or on the go.",
        "icon": "trainerflow.png",
        "play_id": "com.qayham.trainerflow",
        "privacy": "privacy.html",
        "stats": [stat("Coaches", "Built for PTs"), stat("Mobile-first", "Daily workflow"), stat("Free", "On Play Store")],
        "trust": ["Published by QAYHAM", "Privacy policy available", "Regular updates", "Support via email"],
        "pills": [("Clients", "fa-users"), ("Workouts", "fa-dumbbell"), ("Schedule", "fa-calendar")],
        "highlights": [
            card("fa-user-group", "Client management", "Keep client details, notes, and progress in one structured place."),
            card("fa-list-check", "Workout planning", "Build and reuse workout templates without messy spreadsheets."),
            card("fa-clock", "Scheduling clarity", "See what is coming up and stay on top of your coaching calendar."),
        ],
        "features": [
            card("fa-id-card", "Client profiles", "Names, goals, and session history at a glance."),
            card("fa-repeat", "Reusable plans", "Save workout structures you use every week."),
            card("fa-chart-simple", "Progress tracking", "Monitor consistency and client engagement over time."),
            card("fa-mobile", "Gym-ready UI", "Large tap targets and readable layouts for active environments."),
            card("fa-cloud", "Sync when available", "Keep data accessible across devices where cloud features are enabled."),
            card("fa-headset", "QAYHAM support", "Reach us by email for help, feedback, or privacy requests."),
        ],
        "steps": [
            step("Add your clients", "Set up profiles and goals so every session starts with context."),
            step("Plan workouts", "Create or pick templates tailored to each client’s program."),
            step("Track &amp; repeat", "Log sessions, adjust plans, and build a repeatable coaching system."),
        ],
        "privacy_points": [
            "Training data you enter is used to provide app features",
            "We do not sell your personal information",
            "Contact us to request data access or deletion",
            "See the full policy for third-party services used",
        ],
    },
    {
        "slug": "meshchat",
        "name": "MeshChat",
        "category": "Communication · Offline",
        "tagline": "Talk to people nearby — no internet, no account, no servers.",
        "overview": "MeshChat uses Bluetooth to connect devices in the same space. Message friends at events, camps, or anywhere signal fails — without creating an account or sending your chats through QAYHAM. Your conversations stay between devices.",
        "icon": "meshchat.png",
        "play_id": "com.qayham.meshchat",
        "privacy": "privacy.html",
        "stats": [stat("Offline", "No internet chat"), stat("P2P", "Direct Bluetooth"), stat("Private", "No sign-up")],
        "trust": ["No analytics SDKs", "No ad networks", "No QAYHAM chat servers", "Open privacy policy"],
        "pills": [("Bluetooth", "fa-bluetooth-b"), ("Offline", "fa-wifi-slash"), ("Local", "fa-mobile")],
        "highlights": [
            card("fa-comments", "Nearby messaging", "Discover and chat with devices running MeshChat in Bluetooth range."),
            card("fa-user-secret", "No account required", "Pick a display name locally — no email or phone number needed."),
            card("fa-server", "No cloud relay", "Messages travel device-to-device, not through our infrastructure."),
        ],
        "features": [
            card("fa-magnifying-glass", "Controlled discovery", "You choose when to scan for nearby users."),
            card("fa-history", "Local chat history", "Conversations stored on your phone until you delete them."),
            card("fa-sliders", "App preferences", "Theme and notification options kept on-device."),
            card("fa-shield", "Permission transparency", "Bluetooth permissions explained clearly in our policy."),
            card("fa-ban", "No tracking SDKs", "We do not integrate analytics or advertising networks."),
            card("fa-trash", "Easy reset", "Clear data or uninstall to remove all local messages."),
        ],
        "steps": [
            step("Enable Bluetooth", "Grant nearby-device permissions so the app can discover peers."),
            step("Find nearby users", "Scan when you are ready and connect to people you trust nearby."),
            step("Chat offline", "Send messages directly — no Wi‑Fi or mobile data required."),
        ],
        "privacy_points": [
            "Chats are not uploaded to QAYHAM servers",
            "No sign-up or personal account required",
            "Bluetooth permissions used only for discovery and messaging",
            "Full policy at /products/meshchat/privacy.html",
        ],
    },
    {
        "slug": "netdrop",
        "name": "NetDrop",
        "category": "Utilities · File transfer",
        "tagline": "Move files across your Wi‑Fi — fast, local, and under your control.",
        "overview": "NetDrop sends photos, videos, and documents directly between devices on the same network. No cloud middleman, no account, and no QAYHAM file servers — just pick a file, pick a device, and transfer.",
        "icon": "netdrop.png",
        "play_id": "com.qayham.netdrop",
        "privacy": "privacy.html",
        "stats": [stat("Local", "Wi‑Fi only"), stat("Direct", "Device-to-device"), stat("No cloud", "Your network")],
        "trust": ["No analytics SDKs", "No ad networks", "Optional HTTPS", "Open-source fonts only online"],
        "pills": [("Wi‑Fi", "fa-wifi"), ("Fast send", "fa-paper-plane"), ("History", "fa-clock-rotate-left")],
        "highlights": [
            card("fa-network-wired", "Local network transfers", "Files go straight to the device you approve on your LAN."),
            card("fa-user-check", "You stay in control", "Decline transfers you do not want and choose what to send."),
            card("fa-folder-tree", "Organized saves", "Received files land in sensible folders on your device."),
        ],
        "features": [
            card("fa-radar", "Device discovery", "Find NetDrop devices nearby using multicast on your network."),
            card("fa-gauge-high", "Progress tracking", "Watch transfers complete with clear in-app feedback."),
            card("fa-list", "Transfer history", "Local log of sends and receives — clear it anytime."),
            card("fa-lock", "Optional HTTPS", "Enable encrypted local traffic with on-device certificates."),
            card("fa-tag", "Custom device name", "Set an alias so others recognize your phone or tablet."),
            card("fa-rotate", "Reset when needed", "Wipe history and settings from inside the app."),
        ],
        "steps": [
            step("Connect to Wi‑Fi", "Join the same trusted network as the other device."),
            step("Pick files &amp; recipient", "Select what to send and choose an approved nearby device."),
            step("Transfer locally", "Files move directly — QAYHAM never stores them on a server."),
        ],
        "privacy_points": [
            "Files are not uploaded to QAYHAM servers",
            "Transfer history stays on your device",
            "Use only on networks you trust",
            "Read the full NetDrop privacy policy for permissions",
        ],
    },
    {
        "slug": "cloudnotes",
        "name": "Cloud Notes",
        "category": "Productivity · Sync",
        "tagline": "Notes that follow you — Android, web, online or offline.",
        "overview": "Cloud Notes is QAYHAM’s flagship note-taking app. Write on your phone, continue on the web, and pick up where you left off on another device. Google Sign-In and Firebase keep your notes synced, while offline support means you are never blocked when connectivity drops.",
        "icon": "cloudnotes.png",
        "play_id": "com.qayham.cloudnotes",
        "privacy": "/cloudnotes/privacy-policy.html",
        "extra_cta": '<a href="/cloudnotes/" class="btn btn-sky"><i class="fas fa-globe"></i> Open Web App</a>',
        "stats": [stat("Web + Android", "Two platforms"), stat("Sync", "Firebase cloud"), stat("Offline", "Always usable")],
        "trust": ["Google Sign-In", "Firebase storage", "Featured QAYHAM app", "Dedicated privacy policy"],
        "pills": [("Sync", "fa-cloud"), ("Web app", "fa-globe"), ("Offline", "fa-plane")],
        "highlights": [
            card("fa-arrows-rotate", "Real sync", "Changes propagate across signed-in devices automatically."),
            card("fa-laptop-mobile", "Web &amp; mobile", "Use the browser app or Android — same notes, either way."),
            card("fa-file-lines", "Focused writing", "A clean editor built for everyday notes, lists, and ideas."),
        ],
        "features": [
            card("fa-key", "Google Sign-In", "Secure authentication without a separate password to remember."),
            card("fa-database", "Firebase backend", "Industry-standard cloud storage with security rules."),
            card("fa-wifi", "Offline mode", "Keep working when connectivity is limited — sync when you are back."),
            card("fa-share-nodes", "Share &amp; collaborate", "Features for sharing notes where supported in-app."),
            card("fa-trash-can", "Account deletion", "Remove your account and data when you no longer need the service."),
            card("fa-star", "Flagship product", "Actively maintained by the QAYHAM team."),
        ],
        "steps": [
            step("Sign in with Google", "Create your account in seconds with Google Sign-In."),
            step("Write anywhere", "Capture notes on Android or at qayham.com/cloudnotes."),
            step("Stay in sync", "Edits appear on your other devices when you are online."),
        ],
        "privacy_points": [
            "Google Sign-In and Firebase process authentication data",
            "Notes stored to enable sync — not sold to third parties",
            "Dedicated Cloud Notes privacy policy available",
            "Contact QAYHAM for data requests or deletion",
        ],
    },
    {
        "slug": "quickunits",
        "name": "Quick Units",
        "category": "Utilities · Conversion",
        "tagline": "Convert anything in seconds — currencies, lengths, weights, and more.",
        "overview": "Quick Units is the everyday converter you keep on your home screen. Swap currencies with live rates, convert cooking measurements, check temperatures, and handle dozens of unit types without opening a bloated app or hunting through menus.",
        "icon": "quick-units.png",
        "play_id": "com.qayham.quickunits",
        "privacy": "privacy.html",
        "stats": [stat("Live rates", "Currencies"), stat("Lightweight", "Fast launch"), stat("Free", "Download")],
        "trust": ["Google Play distribution", "Minimal data collection", "Privacy policy published", "QAYHAM support"],
        "pills": [("Currency", "fa-dollar-sign"), ("Length", "fa-ruler"), ("Temp", "fa-temperature-half")],
        "highlights": [
            card("fa-money-bill-transfer", "Live currency rates", "Stay current when you need real-world exchange values."),
            card("fa-bolt", "Instant results", "Type a value and see conversions immediately."),
            card("fa-table-list", "Many categories", "Length, weight, volume, temperature, and more in one app."),
        ],
        "features": [
            card("fa-arrows-left-right", "Two-way conversion", "Edit either side and the other updates automatically."),
            card("fa-star", "Favorites", "Pin the unit pairs you use most often."),
            card("fa-clock", "Recent conversions", "Jump back to what you calculated last session."),
            card("fa-wifi", "Network for rates", "Currency updates fetch public rate data when online."),
            card("fa-mobile-screen-button", "One-hand friendly", "Compact layout for quick checks on the go."),
            card("fa-circle-info", "Clear disclosures", "See our privacy policy for network and ad practices."),
        ],
        "steps": [
            step("Pick a category", "Choose currency, length, weight, or another unit type."),
            step("Enter your value", "Type the number you want to convert — results update live."),
            step("Use the answer", "Copy, compare, or switch categories without leaving the app."),
        ],
        "privacy_points": [
            "No account required to use the converter",
            "Currency rates may use third-party APIs over the network",
            "Check Google Play Data safety for ad disclosures",
            "Email us with any privacy questions",
        ],
    },
    {
        "slug": "qrscanner",
        "name": "QR Scanner &amp; Generator",
        "category": "Utilities · Scanner",
        "tagline": "Scan, create, and share QR codes — the everyday tool in your pocket.",
        "overview": "QR Scanner &amp; Generator handles both sides of QR workflows: read codes in a flash with your camera, or create new ones for Wi‑Fi networks, URLs, contacts, and more. Core scanning works offline so you are covered even without data.",
        "icon": "qrscanner.png",
        "play_id": "com.qayham.qrscanner",
        "privacy": "privacy.html",
        "stats": [stat("Scan + create", "Two-in-one"), stat("Offline scan", "No data needed"), stat("Free", "With ads")],
        "trust": ["Camera-only permission for scan", "Local QR generation", "Privacy policy on-site", "Google Play verified"],
        "pills": [("Scan", "fa-qrcode"), ("Create", "fa-plus"), ("Offline", "fa-wifi-slash")],
        "highlights": [
            card("fa-camera", "Fast scanning", "Point your camera at any QR or barcode and get results instantly."),
            card("fa-wand-magic-sparkles", "Code generator", "Create codes for URLs, Wi‑Fi, contacts, and common formats."),
            card("fa-plane-slash", "Works offline", "Scanning and generation run on-device — no upload to our servers."),
        ],
        "features": [
            card("fa-wifi", "Wi‑Fi QR codes", "Share network credentials without typing long passwords."),
            card("fa-link", "URL &amp; text codes", "Generate scannable links and plain text in seconds."),
            card("fa-address-book", "Contact cards", "Encode vCard details for easy sharing."),
            card("fa-history", "Scan history", "Review recent scans locally on your device."),
            card("fa-copy", "Copy &amp; share", "Send decoded content to other apps you trust."),
            card("fa-ad", "Ad-supported free tier", "Ads may appear — see policy for ad network details."),
        ],
        "steps": [
            step("Allow camera access", "Required only for scanning — we do not access other sensors."),
            step("Scan or generate", "Read an existing code or build a new one from the generator."),
            step("Act on the result", "Open links, copy text, or share codes however you need."),
        ],
        "privacy_points": [
            "Scan data processed locally — not stored on QAYHAM servers",
            "Camera permission used only for QR scanning",
            "Third-party ads may collect device data per their policies",
            "Contact us in-app or by email for support",
        ],
    },
    {
        "slug": "compoundcalculator",
        "name": "Compound Calculator",
        "category": "Finance · Calculator",
        "tagline": "See exactly how compound interest grows — down to the detail.",
        "overview": "Compound Calculator goes beyond a basic formula. Model investments with flexible inputs, inspect period-by-period breakdowns, compare scenarios, and understand how time and rate shape your returns — with multi-currency support built in.",
        "icon": "compounding-calculator.png",
        "play_id": "com.bilalparray07.compoundingcalculator",
        "privacy": "privacy.html",
        "stats": [stat("Detailed", "Breakdowns"), stat("Multi-currency", "Global"), stat("Free", "Download")],
        "trust": ["Local calculations", "Google Play listing", "Privacy policy available", "QAYHAM published"],
        "pills": [("Growth", "fa-chart-line"), ("Breakdown", "fa-table"), ("Currency", "fa-coins")],
        "highlights": [
            card("fa-calculator", "Advanced modeling", "Principal, rate, frequency, and duration — all adjustable."),
            card("fa-chart-pie", "Visual summaries", "Understand totals and growth at a glance."),
            card("fa-coins", "Multi-currency", "Run scenarios in the currency that matches your plan."),
        ],
        "features": [
            card("fa-list-ol", "Period breakdowns", "Inspect how balance accumulates over each compounding period."),
            card("fa-sliders", "Flexible inputs", "Tune contribution timing, rate changes, and duration."),
            card("fa-floppy-disk", "Local preferences", "Settings and recents stored on your device."),
            card("fa-share-nodes", "Share results", "Export or share summaries when you need a second opinion."),
            card("fa-book-open", "Educational clarity", "Built to explain compound growth, not hide it."),
            card("fa-shield", "Transparent ads", "Free tier may show ads — see policy and Play Data safety."),
        ],
        "steps": [
            step("Enter your numbers", "Set principal, interest rate, compounding frequency, and timeline."),
            step("Review the breakdown", "See period-by-period growth and total returns clearly."),
            step("Compare scenarios", "Adjust inputs to understand how small changes affect outcomes."),
        ],
        "privacy_points": [
            "Financial inputs calculated locally on your device",
            "No account required",
            "Ad networks may apply their own data practices",
            "Email QAYHAM for privacy questions",
        ],
    },
    {
        "slug": "teamawesomesozeith",
        "name": "Team Awesome Sozeith",
        "category": "Sports · Fan app",
        "tagline": "Stats, stories, and updates for Team Awesome Sozeith fans.",
        "overview": "Team Awesome Sozeith keeps fans close to the action. Track performance, explore Awesomies stats, and enjoy a purpose-built interface for supporters who want quick access to the numbers and moments that matter.",
        "icon": "teamawesomesozeith.png",
        "play_id": "com.qayham.teamawesomesozeith",
        "privacy": "privacy.html",
        "stats": [stat("Fans", "Built for you"), stat("Stats", "At a glance"), stat("Free", "Download")],
        "trust": ["Google Play app", "In-app contact", "Privacy policy published", "QAYHAM support"],
        "pills": [("Stats", "fa-chart-bar"), ("Team", "fa-people-group"), ("Updates", "fa-bell")],
        "highlights": [
            card("fa-ranking-star", "Performance tracking", "Monitor team stats with an intuitive layout."),
            card("fa-heart", "Fan-first design", "Built for supporters, not generic sports clutter."),
            card("fa-mobile", "Always handy", "Check updates and stats from your phone anytime."),
        ],
        "features": [
            card("fa-table", "Clear stat views", "Readable tables and summaries for quick scanning."),
            card("fa-users", "Awesomies focus", "Content tailored to Team Awesome Sozeith."),
            card("fa-bell", "Stay in the loop", "Engage with updates inside the app experience."),
            card("fa-envelope", "Contact in-app", "Reach the developer without hunting for support links."),
            card("fa-ad", "Ad-supported", "Free access supported by third-party advertising."),
            card("fa-file-shield", "Published policy", "Full privacy details available on this website."),
        ],
        "steps": [
            step("Install from Play Store", "Get the official app published by QAYHAM."),
            step("Explore team stats", "Browse performance data and fan-focused views."),
            step("Stay engaged", "Return for updates and new content as the app evolves."),
        ],
        "privacy_points": [
            "We do not collect personal data on QAYHAM servers directly",
            "Third-party ad networks may collect device data",
            "Review ad network policies for more detail",
            "Contact us in-app or by email",
        ],
    },
]

SHELL = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{name} — QAYHAM</title>
    <meta name="description" content="{meta}" />
    <meta property="og:title" content="{name} — QAYHAM" />
    <meta property="og:description" content="{meta}" />
    <meta property="og:type" content="website" />
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
        <section class="app-landing-hero">
            <div class="app-hero-bg">
                <div class="app-hero-orb app-hero-orb-1"></div>
                <div class="app-hero-orb app-hero-orb-2"></div>
                <div class="app-hero-grid"></div>
            </div>
            <div class="container app-hero-split">
                <div class="app-hero-content reveal">
                    <nav class="app-breadcrumb" aria-label="Breadcrumb">
                        <a href="/">Home</a> / <a href="/#products">Products</a> / {name_plain}
                    </nav>
                    <p class="app-category"><i class="fas fa-layer-group"></i> {category}</p>
                    <span class="section-tag">QAYHAM App</span>
                    <h1>{name}</h1>
                    <p class="app-tagline">{tagline}</p>
                    <div class="app-hero-stats">
                        {stats_html}
                    </div>
                    <div class="app-hero-actions">
                        <a href="https://play.google.com/store/apps/details?id={play_id}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                            <i class="fab fa-google-play"></i> Get on Play Store
                        </a>
                        {extra_cta}
                        <a href="{privacy}" class="btn btn-outline">Privacy Policy</a>
                    </div>
                    <p class="app-meta">Package ID: <code>{play_id}</code> · Published by QAYHAM</p>
                </div>
                <div class="app-hero-visual reveal reveal-delay">
                    <div class="app-icon-frame">
                        <div class="app-icon-glow"></div>
                        <img src="../../images/products/{icon}" alt="{name_plain}" class="app-icon-xl" />
                    </div>
                    {pills_html}
                </div>
            </div>
        </section>

        <div class="app-trust-bar">
            <div class="container app-trust-inner">
                {trust_html}
            </div>
        </div>

        <section class="app-section">
            <div class="container">
                <div class="section-header reveal">
                    <span class="section-tag">Overview</span>
                    <h2>Built for real-world use</h2>
                </div>
                <p class="app-overview-text reveal">{overview}</p>
                <div class="app-highlights-grid">
                    {highlights_html}
                </div>
            </div>
        </section>

        <section class="app-section app-section-alt">
            <div class="container">
                <div class="section-header reveal">
                    <span class="section-tag">Features</span>
                    <h2>Everything you need, nothing you do not</h2>
                    <p>A closer look at what makes {name_plain} worth installing.</p>
                </div>
                <div class="app-features-grid">
                    {features_html}
                </div>
            </div>
        </section>

        <section class="app-section">
            <div class="container">
                <div class="section-header reveal">
                    <span class="section-tag">How it works</span>
                    <h2>Up and running in minutes</h2>
                </div>
                <div class="app-steps">
                    {steps_html}
                </div>
            </div>
        </section>

        <section class="app-section app-section-alt">
            <div class="container">
                <div class="section-header reveal">
                    <span class="section-tag">Trust</span>
                    <h2>Privacy &amp; transparency</h2>
                    <p>We publish clear policies for every QAYHAM app.</p>
                </div>
                <div class="app-privacy-panel reveal">
                    <div>
                        <h3>Your data, explained plainly</h3>
                        <p>{privacy_intro}</p>
                        <a href="{privacy}" class="btn btn-outline btn-sm">Read full privacy policy</a>
                    </div>
                    <ul class="app-privacy-list">
                        {privacy_points_html}
                    </ul>
                </div>
            </div>
        </section>

        <section class="app-landing-cta">
            <div class="container app-landing-cta-inner reveal">
                <h2>Ready to try {name_plain}?</h2>
                <p>Download free on Google Play — built and maintained by QAYHAM.{cta_extra}</p>
                <div class="app-landing-cta-actions">
                    <a href="https://play.google.com/store/apps/details?id={play_id}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
                        <i class="fab fa-google-play"></i> Install on Android
                    </a>
                    {extra_cta_bottom}
                    <a href="/#products" class="btn btn-ghost">Browse all apps</a>
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
                        <li><a href="https://play.google.com/store/apps/details?id={play_id}" target="_blank" rel="noopener noreferrer">Google Play</a></li>
                        <li><a href="{privacy}">Privacy Policy</a></li>
                        <li><a href="mailto:parraybilal34@gmail.com">Support</a></li>
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


def plain_name(name: str) -> str:
    return name.replace("&amp;", "&")


def render_stats(stats: list[dict]) -> str:
    return "\n                        ".join(
        f'<div class="app-stat"><span class="app-stat-value">{s["value"]}</span><span class="app-stat-label">{s["label"]}</span></div>'
        for s in stats
    )


def render_trust(items: list[str]) -> str:
    icons = ["fa-circle-check", "fa-shield-halved", "fa-lock", "fa-certificate"]
    return "\n                ".join(
        f'<span class="app-trust-item"><i class="fas {icons[i % len(icons)]}"></i> {item}</span>'
        for i, item in enumerate(items)
    )


def render_pills(pills: list[tuple[str, str]]) -> str:
    classes = ["app-float-pill-1", "app-float-pill-2", "app-float-pill-3"]
    return "\n                    ".join(
        f'<span class="app-float-pill {classes[i]}"><i class="fas {icon}"></i> {text}</span>'
        for i, (text, icon) in enumerate(pills[:3])
    )


def render_cards(cards: list[dict], card_class: str, use_icon_div: bool = False) -> str:
    blocks = []
    for i, item in enumerate(cards):
        delay = ' reveal-delay' if i % 3 == 1 else (' reveal-delay-2' if i % 3 == 2 else '')
        if use_icon_div:
            icon_html = f'<div class="app-highlight-icon"><i class="fas {item["icon"]}"></i></div>'
        else:
            icon_html = f'<i class="fas {item["icon"]}"></i>'
        blocks.append(
            f'<article class="{card_class} reveal{delay}">\n'
            f'                        {icon_html}\n'
            f'                        <h3>{item["title"]}</h3>\n'
            f'                        <p>{item["desc"]}</p>\n'
            f'                    </article>'
        )
    return "\n                    ".join(blocks)


def render_steps(steps: list[dict]) -> str:
    blocks = []
    for i, item in enumerate(steps):
        delay = ' reveal-delay' if i == 1 else (' reveal-delay-2' if i == 2 else '')
        blocks.append(
            f'<article class="app-step reveal{delay}">\n'
            f'                        <h3>{item["title"]}</h3>\n'
            f'                        <p>{item["desc"]}</p>\n'
            f'                    </article>'
        )
    return "\n                    ".join(blocks)


def render_privacy_points(points: list[str]) -> str:
    return "\n                        ".join(
        f'<li><i class="fas fa-check"></i> {point}</li>' for point in points
    )


def main() -> None:
    for app in APPS:
        extra = app.get("extra_cta", "")
        extra_bottom = ""
        cta_extra = ""
        if "cloudnotes" in app["slug"]:
            extra_bottom = extra.replace("btn-sky", "btn-sky").replace('class="btn btn-sky"', 'class="btn btn-sky btn-lg"')
            cta_extra = " Or open the web app instantly."

        html = SHELL.format(
            name=app["name"],
            name_plain=plain_name(app["name"]),
            category=app["category"],
            meta=plain_name(app["tagline"]),
            tagline=app["tagline"],
            overview=app["overview"],
            icon=app["icon"],
            play_id=app["play_id"],
            privacy=app["privacy"],
            extra_cta=extra,
            extra_cta_bottom=extra_bottom,
            cta_extra=cta_extra,
            stats_html=render_stats(app["stats"]),
            trust_html=render_trust(app["trust"]),
            pills_html=render_pills(app["pills"]),
            highlights_html=render_cards(app["highlights"], "app-highlight-card", True),
            features_html=render_cards(app["features"], "app-feature-card"),
            steps_html=render_steps(app["steps"]),
            privacy_intro=f"We believe you should understand what {plain_name(app['name'])} does with your information before you install.",
            privacy_points_html=render_privacy_points(app["privacy_points"]),
        )
        out_dir = ROOT / "products" / app["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"Wrote {out_dir / 'index.html'}")


if __name__ == "__main__":
    main()
