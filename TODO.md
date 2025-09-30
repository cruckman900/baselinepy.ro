🧠 Bonus Ideas
- Add regex validation for tab content
- Limit file size with UploadFile.spool_max_size
- Log uploads with timestamps and user info
- Return metadata like line count or tab complexity

## 🪕 TODO — Expand Instrument Recognition & Tuning Support (2025-09-30 18:05 EDT)

- 🎯 Goal: Extend `detect_instrument()` and `extract_tuning()` to support non-standard string counts and alternate tunings.
- 🧩 Targets:
  - Add recognition logic for 7-string guitars (e.g., B-E-A-D-G-B-E).
  - Add support for ukulele tabs (typically 4 strings, e.g., G-C-E-A).
  - Consider 5-string bass and other extended-range instruments.
  - Enhance tuning extraction to handle alternate tunings (e.g., Drop D, DADGAD, baritone).
- 💡 Approach:
  - Refactor tuning detection to parse note names and infer instrument type.
  - Create a tuning map for known configurations.
  - Add test cases with sample tabs for each instrument type.
- 🔥 Bonus: Auto-suggest instrument based on tuning pattern if string count is ambiguous.

> “Let no string go unstrummed, no tuning go unsung.” 🎼

## 🚀 TODO — Full-Stack Architecture Kickoff (2025-09-30 18:14 EDT)

- 🔧 Backend
  - Set up Postgres schema for tab metadata and Cloudinary URLs
  - Implement file upload logic with Cloudinary SDK
  - Add validation and error handling for uploads/downloads

- ☁️ Cloudinary
  - Create new project-specific account
  - Configure secure API access
  - Test uploads and transformations

- 🌐 Front-End
  - Scaffold Netlify project with React or Next.js
  - Build tab upload form and preview component
  - Connect to backend API and display Cloudinary-hosted assets

> “Let the tabs flow, the uploads soar, and the riffs echo across the cloud.” 🎶
