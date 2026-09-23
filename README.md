# Fabula

Local AI writing app. Describe a story, get an outline, then let a local LLM write it scene by scene – optionally in a style learned from sample texts. Everything runs on your PC through [KoboldCpp](https://github.com/LostRuins/koboldcpp).

## Setup (Windows, NVIDIA GPU with 16 GB VRAM)

The model and KoboldCpp are not in the repo (too big). Download them into place:

```
curl -L --create-dirs -o koboldcpp/koboldcpp.exe https://github.com/LostRuins/koboldcpp/releases/download/v1.121/koboldcpp.exe
curl -L --create-dirs -o models/Cydonia-24B-v4.3-IQ4_XS.gguf https://huggingface.co/bartowski/TheDrummer_Cydonia-24B-v4.3-GGUF/resolve/main/TheDrummer_Cydonia-24B-v4.3-IQ4_XS.gguf
```

You also need Python 3 (standard library only).

## Run

Double-click `start.bat`. KoboldCpp loads the model (~20 s) and the app opens at http://localhost:5002.

Projects and styles are saved as JSON files in `data/` (not tracked by git). To use a different model, change the `--model` path in `start.bat`.
