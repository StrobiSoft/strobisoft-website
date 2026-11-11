# StrobiSoft FamilyMail downloads

This directory is reserved for verified Windows installer releases and their update manifest.

Do not publish `familymail/windows/stable.json` until the corresponding installer has been uploaded to a publicly accessible HTTPS URL, SHA-256 verified, and Windows installer smoke-tested. The client treats a missing manifest as no update and continues normal startup.

Stable manifest fields: `version`, `url`, `sha256`, `notes`. The URL must be HTTPS on an approved host. The SHA-256 must match the actual final EXE bytes. Version must exceed the installed version before the update is offered.

The public website must not include private source, credentials, or internal infrastructure details.
