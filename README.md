# POSS
POSS (Piece Of Shyt Server) is Y. Corp's Singularity. A shitty server reimplementation for Limbus Company.

## Requirements

### Python [3.12]
- fastapi v0.115.0
- pydantic v2.9.2
- uvicorn v0.31.1
- pymongo v4.10.1
- ruff v0.6.9 (optional)
- uv v0.4.22 (optional)

### MongoDB
- Windows: [Community Edition](https://www.mongodb.com/try/download/community-edition)
- Arch Linux: `yay -S mongodb-bin` then `sudo systemctl start mongodb`

### Mitmproxy
- Windows: https://mitmproxy.org/
- Arch Linux: `yay -S mitmproxy`

## Tutorial

1. Clone this repo
2. Run `uv run -m solemn.database --setup`
3. Run `uv run -m server`
4. Run `mitmproxy -s redirect.py`
4. Open Limbus Company and enjoy

If you don't want to use uv, replace `uv run` with `python`.

If you want to contribute, please do install `ruff`.
