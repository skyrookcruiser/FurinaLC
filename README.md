## Requirements

### Python [3.12]
- fastapi v0.115.0
- pydantic v2.9.2
- uvicorn v0.31.1
- pymongo v4.10.1
- ruff v0.6.9 (optional)

### MongoDB
- [Community Edition](https://www.mongodb.com/try/download/community-edition)

## Tutorial

#### 1. Clone this repo

#### 2. Create a MongoDB connection with default settings

#### 3. Run `python -m solemn.database --setup`
#### 4. Run `python -m server`
#### 5. Play the game

### Note: You will need a proxy to redirect traffic from the client to this private server. Two examples that you can use, and how to set them up:
<details>
<summary>Fiddler</summary>

#### Paste this in FiddlerScript menu and save
```
import System;
import System.Windows.Forms;
import Fiddler;
import System.Text.RegularExpressions;

class Handlers
{
    static function OnBeforeRequest(oS: Session) {
        if (oS.host.EndsWith(".limbuscompanyapi.com") || 
        oS.host.EndsWith(".limbuscompanyapi-2.com")) {
            oS.oRequest.headers.UriScheme = "http";
            oS.host = "127.0.0.1";
            oS.port = 21000;
        }
    }
};
```
</details>

<details>
<summary>FireflySR Proxy</summary>

#### Edit the config.json with this
```
{
  "DestinationHost": "localhost",
  "DestinationPort": 21000,
  "RedirectDomains": [
    ".limbuscompanyapi.com",
    ".limbuscompanyapi-2.com",
  ],
  < !! The rest of the config.json !! >
}
```

</details>
