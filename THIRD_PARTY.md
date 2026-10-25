# Third-party notices

Hojas Studio is made by Hojas (Rakan Alzahrani). Parts of it were inspired by or adapted from the projects below. Full license texts are in `LICENSES/`.

## HyperFrames, Apache License 2.0
Copyright (c) 2026 HeyGen, Inc. https://github.com/heygen-com/hyperframes
Ideas adapted and rewritten for Hojas Studio's canvas renderer (no files copied): velocity-matched seam transitions, motion rules, oversized cursor, caption grouping and QA rules, story structures and card-count formula, beat analysis approach, voice EQ presets, color-grade presets.
In 4.8: the timings and layouts of the motion-kit templates (`type=mg`: stat, slam, check, steps, callout, quote, ring, compare, sting) follow HyperFrames registry items (count-up, headline-slam, marker-checklist-card, state-chip-rail, vox-annotate, testimonial-proof-card, split-tilt-cards, logo-sting), and `engine/references/motion-kit.md` summarizes its animation, typography and caption rules in Arabic. All drawing code is our own.
License text: `LICENSES/Apache-2.0.txt`.

## lemo-opuscar, MIT License
Copyright (c) 2026 LemoLab. https://github.com/lemomo-ai/lemo-opuscar
The film-style catalog in engine/references/looks.md is summarized from its style list, and several Hojas "looks" are inspired by its styles (4.8 adds gameshow, crt, briefing and spy). The director checks in `engine/references/motion-kit.md` are summarized from its DIRECTOR.md and TECHNIQUE.md.
License text: `LICENSES/MIT-lemo-opuscar.txt`.

## Remotion, facts and rules only
https://www.remotion.dev and its agent skills (github.com/remotion-dev/skills). **No code or text from Remotion is included.** `engine/references/motion-kit.md` and `engine/references/remotion.md` summarize, in our own Arabic words, publicly documented rules (sequencing, determinism, render settings, caption paging). The spring curve in our canvas engine is the standard closed-form damped-spring equation, written from scratch. The optional Remotion export path downloads Remotion on the user's machine under the Remotion License.

## gbro-collage-broll, MIT License
Copyright (c) 2026 pyang5166. https://github.com/pyang5166/gbro-collage-broll
The paper-collage look, its color meanings and the metaphor, still, animate approval idea inspired Hojas's `collage` layer, which is rendered locally without any API.
License text: `LICENSES/MIT-gbro-collage-broll.txt`.

## agent-video-editor, MIT License (text) and CC0 1.0 (audio)
Copyright (c) 2026 kmilo93sd. https://github.com/kmilo93sd/agent-video-editor
The editing rules in `engine/references/editing-rules.md` are adapted and translated to Arabic from its references and recipes (pacing, hooks, captions and text timing, graphics timing, audio levels, sound effects, shorts). Its sources are listed there.
The 128 sounds and music tracks with ids starting `cc-` in `sfxlib.json` are CC0 1.0 (public domain dedication), reviewed source by source in its `library/LICENSES.md`. They are not shipped inside Hojas Studio: each computer downloads them from the repository, pinned to commit 8e32c0a, on first use. Arabic names and usage notes are ours.
License text: `LICENSES/MIT-agent-video-editor.txt`.

## onetake, ideas only
https://github.com/feitangyuan/onetake is licensed PolyForm Noncommercial 1.0.0. **No code, text or presets from onetake are included in Hojas Studio.** General ideas (carry elements across beats instead of replacing them, rhythm and rest checks) were described in our own words and implemented from scratch.

## MediaPipe, Apache License 2.0
engine/vision contains MediaPipe Tasks Vision and two models (face detection, selfie segmentation). Copyright Google LLC. https://github.com/google-ai-edge/mediapipe
License text: `LICENSES/Apache-2.0.txt`.

## RNNoise speech model (rnnoise-models, not subject to copyright)
engine/audio/sh.rnnn is the "somnolent-hogwash" model (recording noise, speech signal) from https://github.com/GregorR/rnnoise-models. Its README states the models are not creative work and not subject to copyright. It is loaded by FFmpeg's `arnndn` filter (RNNoise by Jean-Marc Valin, BSD-3-Clause, part of FFmpeg).

## qr.js, MIT License
Copyright (c) 2009 Kazuhiko Arase. The license notice is at the top of `qr.js`.

## Images
engine/scripts/collage-assets: public domain images from Wikimedia Commons (sources in `collage-assets/LICENSES.md`).

## Not bundled, downloaded on the user's machine
- Sound library (`sfxlib.json`): links to Mixkit sound effects, downloaded from mixkit.co when first used, under the Mixkit Free License. The sound files are not included in this package.
- Fonts in the studio and captions: loaded from Google Fonts (SIL Open Font License) when online.
- Images and clips from `hs media`: fetched from Wikimedia Commons with their license recorded in the project's `credits.txt`.
- Company logos (`hs logo`, motion kind `logo`): SVG icons from Simple Icons (https://github.com/simple-icons/simple-icons, CC0 1.0), downloaded on first use and cached in `~/.hojas-studio/logos`. Logos are trademarks of their owners and are shown only to identify the company being talked about. Brands not in Simple Icons show an initial unless the user adds the official file with `hs logo add`.
- Brand fonts (Thmanyah): never bundled. Hojas Studio only uses them when the user has a licensed copy installed on their own device (`hs fonts install <zip>`, stored in `~/.hojas-studio/fonts`), and copies them into that user's local projects. Font files are excluded from the repository and the public package.

## Interface font
The public package does not include a custom interface font. The studio uses IBM Plex Sans Arabic (SIL OFL 1.1). To use your own font, put it at `fonts/nt-panorama-naskh-long.otf` (any Arabic OTF file with that name) and make sure you have the right to use it.
GUIDE.html embeds IBM Plex Sans Arabic, IBM Plex Mono and Noto Naskh Arabic (SIL Open Font License 1.1).

## Claude mark
The Claude logo in the studio and the library (path data from Simple Icons, CC0 1.0, https://simpleicons.org) is a trademark of Anthropic, used only to point to Claude.

## ChatGPT and Gemini marks
The OpenAI and Google Gemini logos in the library settings (path data from Simple Icons, CC0 1.0, https://simpleicons.org) are trademarks of OpenAI and Google, used only to point to those services.
