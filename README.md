# 🎼 fanTABulous

![Python](https://img.shields.io/badge/python-3.11-blue)
[![Tests](https://github.com/cruckman900/baselinepy.ro/actions/workflows/test.yml/badge.svg)](https://github.com/cruckman900/baselinepy.ro/actions)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
[![Render](https://render.com/api/v1/badges/srv-d3dt963ipnbc73cle5m0?style=flat)](https://dashboard.render.com/web/srv-d3dt963ipnbc73cle5m0)

*Where riffs are born, tabs are forged, and music meets code.*

fanTABulous is a web-based tablature editor and archive built for guitarists, bassists, and solo wolves who want to write, save, and share their musical ideas. Whether you're sketching out a solo or composing a full-blown anthem, fanTABulous gives you the tools to make it sing.

# 🧠 fanTABulous Backend

This is the backend engine of **fanTABulous**—a FastAPI-powered system for tab parsing, metadata extraction, and backend milestone logging.

![License](https://badgen.net/badge/license/Proprietary/black?icon=shield)

## ⚙️ Overview

Handles:
- Tab file uploads
- Instrument and tuning detection
- Metadata parsing
- Backend milestone logging (poetic changelogs included)

Built with FastAPI, SQLModel, modular route architecture, and expressive logging.

## 🔐 License

This software is **proprietary and confidential**. Unauthorized use, distribution, or modification is strictly prohibited.

Access is granted only to licensed users under explicit agreement.  
See [`LICENSE.txt`](./LICENSE.txt) for full terms, including:

- Jurisdiction: Ohio, USA
- Enforcement: Legal action for breach
- Licensing tiers: Personal, Commercial, Enterprise
- Audit rights, termination clause, and survivability

## 🌐 Related Repos

- [fanTABulous Frontend](https://github.com/cruckman900/nuxt.riffdaddy) — Nuxt-powered tab preview and UI magic

---

## 🚀 Features

- 🎸 FastAPI backend with SQLite for lightweight tab storage
- 🧠 Custom `.ftab` format for expressive, structured tablature
- 💾 Save tabs to the cloud until you're ready to download or print
- 🔍 Auto-generated API docs via Swagger UI
- 🛠️ CI/CD pipeline powered by Render (because deploys should rock)
- 🎨 Frontend (coming soon) with SVG fretboard rendering and Framer Motion flair

---
🛠️ CI/CD with Render
This repo includes a render.yaml for automated deploys. Just connect your GitHub repo to Render and let the pipeline shred.

🤘 Contributing
Pull requests are welcome. If you’ve got ideas for new features—like MIDI playback, tab sharing, or alternate tunings—open an issue and let’s riff.

📜 License
MIT. Because music should be free, and so should your code.

✨ Credits
Built with love, Python, and a whole lotta caffeine by Christopher Ruckman. Powered by poetic survival and a passion for expressive UI.

Want to add badges, animated previews, or a poetic changelog stanza next? I’m ready to jam. Let’s make this README legendary.

## 📁 File Format: `.ftab`

---

Tabs are stored as structured JSON with timing, tuning, and note data:

```json
{
  "title": "Hazard Anthem",
  "artist": "LinearDescent",
  "tuning": ["E", "A", "D", "G", "B", "E"],
  "tempo": 120,
  "measures": [
    {
      "time_signature": "4/4",
      "notes": [
        { "string": 6, "fret": 0, "beat": 1 },
        { "string": 5, "fret": 2, "beat": 1.5 }
      ]
    }
  ]
}

