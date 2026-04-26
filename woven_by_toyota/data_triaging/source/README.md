# Source Folder Organization

Source materials for the Woven by Toyota data triaging engagement. These files are raw inputs (transcripts, emails, call preps, documents) and are **never modified** after landing here. All interpretation and decomposition happens in `../research/`.

## Folder Structure

Source files are organized by upload date into two levels:

```
source/
  week_YYYY-MM-DD/         <- Monday of the week the file was uploaded
    day_YYYY-MM-DD/        <- actual date the file was uploaded
      <source_file>.txt
```

- **Week folder:** Monday of the week the file was dropped in. Files uploaded anywhere between Monday and Sunday go in the same week folder.
- **Day folder:** the specific date the file was uploaded (not the date of the source material itself).
- **Filename:** reflects the source material date, not the upload date (per singularity Hard Rule 7).

## Current Contents

- `week_2026-04-20/day_2026-04-23/woven_internal_sync_2026-04-13.txt` — Teams transcript of the internal BayOne sync between Colin Moore, Jesse Smith, and Pratik Sharda discussing the Woven by Toyota data triaging opportunity. Meeting held April 13, 2026, 11:30 AM PST.
- `week_2026-04-20/day_2026-04-23/email_thread_2026-04-22.txt` — Email thread between Colin, Jesse, and Pratik coordinating the follow-up discovery call with Travis Millet. Most recent message April 22, 2026.
