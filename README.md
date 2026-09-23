# Fabula

Local AI writing app. Describe a story, get an outline, then let a local LLM write it scene by scene – optionally in a style learned from sample texts. Everything runs on your PC through [KoboldCpp](https://github.com/LostRuins/koboldcpp).

## Setup (Windows, NVIDIA GPU with 16 GB VRAM)

The model and KoboldCpp are not in the repo (too big). Download them into place:

```
curl -L --create-dirs -o koboldcpp/koboldcpp.exe https://github.com/LostRuins/koboldcpp/releases/download/v1.121/koboldcpp.exe
curl -L --create-dirs -o models/Cydonia-24B-v4.3-IQ4_XS.gguf https://huggingface.co/bartowski/TheDrummer_Cydonia-24B-v4.3-GGUF/resolve/main/TheDrummer_Cydonia-24B-v4.3-IQ4_XS.gguf
```

You also need Python 3 (standard library only).

## More models

Every `.gguf` in `models/` shows up in the model dropdown in the app's header. Picking one reloads KoboldCpp with it (~20 s), using the GPU and context settings from `fabula.kcpps`. If a model fails to load, KoboldCpp falls back to the one `start.bat` started with.

These fit in 16 GB of VRAM with the 16k context. They were picked by their scores on the [UGI Leaderboard](https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard): *W/10* is willingness (no refusals), *Writing* is prose quality, *NSFW*/*Dark* show how explicitly the model actually writes such scenes (low = soft censorship: euphemisms, fading out).

| Model | Size | W/10 | Writing | NSFW | Dark | Notes |
|---|---|---|---|---|---|---|
| Impish Bloodmoon 12B (default) | 10.1 GB | 6.5 | 31.7 | 9.8 | 8.8 | most explicit and darkest of all ≤27B models |
| Core 24B V.1 | 12.8 GB | 6.0 | 37.8 | 9.4 | 8.8 | nearly as explicit, better prose |
| Dark-Osmosis 24B | 12.8 GB | 5.5 | 33.3 | 9.7 | 8.4 | ReadyArt, NSFW-focused |
| Dark-Nexus 24B v2.0 | 12.8 GB | 7.5 | 29.8 | 9.5 | 7.6 | ReadyArt, the most willing of these |
| Broken-Tutu 24B Unslop v2.0 | 12.8 GB | 7.2 | 37.2 | 9.0 | 6.5 | ReadyArt |
| WeirdCompound v1.7 24B | 12.8 GB | 8.0 | 47.0 | 7.8 | 7.5 | best prose of all ≤27B models, a bit less explicit |
| Cydonia 24B v4.3 | 12.8 GB | 7.0 | 41.4 | 3.4 | 3.4 | good writer, but tames explicit scenes |

```
curl -L -o models/Impish-Bloodmoon-12B-Q6_K.gguf https://huggingface.co/mradermacher/Impish_Bloodmoon_12B-i1-GGUF/resolve/main/Impish_Bloodmoon_12B.i1-Q6_K.gguf
curl -L -o models/Core-24B-V.1-IQ4_XS.gguf https://huggingface.co/mradermacher/Core_24B_V.1-i1-GGUF/resolve/main/Core_24B_V.1.i1-IQ4_XS.gguf
curl -L -o models/Dark-Osmosis-24B-v1.0-IQ4_XS.gguf https://huggingface.co/ReadyArt/Dark-Osmosis-24B-v1.0-GGUF/resolve/main/Dark-Osmosis-24B-v1.0-i1-IQ4_XS.gguf
curl -L -o models/Dark-Nexus-24B-v2.0-IQ4_XS.gguf https://huggingface.co/mradermacher/Dark-Nexus-24B-v2.0-i1-GGUF/resolve/main/Dark-Nexus-24B-v2.0.i1-IQ4_XS.gguf
curl -L -o models/Broken-Tutu-24B-Unslop-v2.0-IQ4_XS.gguf https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ4_XS.gguf
curl -L -o models/WeirdCompound-v1.7-24B-IQ4_XS.gguf https://huggingface.co/mradermacher/WeirdCompound-v1.7-24b-i1-GGUF/resolve/main/WeirdCompound-v1.7-24b.i1-IQ4_XS.gguf
```

Looking for more? Other GGUF models work too, as long as the file contains a chat template (KoboldCpp reads it from there). Sort the leaderboard by NSFW and Dark, not only W/10: models tagged *abliterated*, *heretic* or *uncensored* merely stop refusing and usually still write tamely (NSFW 2–4). Bigger models don't help either: the 30–120B MoE models score lower on NSFW than these fine-tunes.

## Run

Double-click `start.bat`. KoboldCpp loads the model (~20 s) and the app opens at http://localhost:5002.

Projects and styles are saved as JSON files in `data/` (not tracked by git). To change the model loaded at startup, edit `MODEL` in `start.bat`.
