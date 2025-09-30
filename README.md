# 🎼 fanTABulous

*Where riffs are born, tabs are forged, and music meets code.*

fanTABulous is a web-based tablature editor and archive built for guitarists, bassists, and solo wolves who want to write, save, and share their musical ideas. Whether you're sketching out a solo or composing a full-blown anthem, fanTABulous gives you the tools to make it sing.

---

## 🚀 Features

- 🎸 FastAPI backend with SQLite for lightweight tab storage
- 🧠 Custom `.ftab` format for expressive, structured tablature
- 💾 Save tabs to the cloud until you're ready to download or print
- 🔍 Auto-generated API docs via Swagger UI
- 🛠️ CI/CD pipeline powered by Render (because deploys should rock)
- 🎨 Frontend (coming soon) with SVG fretboard rendering and Framer Motion flair

---

## 📁 File Format: `.ftab`

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
