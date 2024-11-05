# mitmlimbus - messy mitmproxy stuff for limbus
redirect.py:
 - redirects limbus api traffic to `127.0.0.1:21000`
 - doesnt redirect download.limbuscompany.site

redirect_all.py:
 - redirects limbus api traffic to `127.0.0.1:21000`
 - needs miniserver (`cargo run --release`), this listens at `127.0.0.1:2070`
 - redirects download.limbuscompany.site to miniserver, so you can play offline
   - note: this won't redirect if version is not found in `version.json`
   - you also still need to download update for first time, only after that you can use `redirect_all.py` and play fully offline
 - redirects battlelog.limbuscompanyapi.com to miniserver's dummy handler

scrape.py 
 - doesn't redirect anything
 - scrapes request and response packets 
 - saves scraped packets as json files in `./scrapes`, make sure to click on flows you want to save because the save function only gets called when you view them

## credits:
- https://github.com/LEAGUE-OF-NINE/limbus-private-server/blob/master/tooling/limbus_encryption.py
