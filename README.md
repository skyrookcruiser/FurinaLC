
---

# FurinaLC

**FurinaLC** is a server reimplementation for *Limbus Company*, named after the second-best girl from *Genshin Impact*.

## Getting Started

This guide is Windows-oriented. If you use Linux, you already know how to set it all up, I'm sure. (I use arch btw.)

### Requirements

~~Most important requirement: a brain.~~

Before you start, ensure you have the following installed:

- **Python 3.13+**  
  Download from [Python's official website](https://www.python.org/downloads/).
  
- **uv (v0.4.22+)**  
  Install **uv** by running the following PowerShell command:
  ```bash
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

- **MongoDB (v8.0.3+)**  
  Download and install from [MongoDB's official website](https://www.mongodb.com/try/download/community-edition).

- **Git**  
  Install **Git** from [Git's official website](https://git-scm.com/downloads). This is required for cloning the repository.

- **Fiddler Classic**  
  Download from [Telerik's official website](https://www.telerik.com/fiddler/fiddler-classic).  
  Alternatively, you can use any HTTP proxy tool that allows modifying requests.

---

## Step-by-Step Setup

### 1. **Setting Up MongoDB**

- **Install MongoDB**:  
  Follow the installation guide for your operating system from the [MongoDB installation page](https://www.mongodb.com/try/download/community-edition).

- **Configure MongoDB Connection**:  
  Once installed, connect to MongoDB by using the following connection string:
  ```bash
  mongodb://127.0.0.1:27017
  ```

That’s all for MongoDB setup!

---

### 2. **Setting Up Fiddler Classic (Proxy)**

Fiddler Classic redirects API requests to your local server. Follow these steps to configure it:

1. **Install Fiddler Classic**:  
   Download and install it from [Telerik's website](https://www.telerik.com/fiddler/fiddler-classic).

2. **Configure the Fiddler Script**:  
   - Open Fiddler.
   - Go to the **FiddlerScript** tab.
   - Copy and paste the following script, then save it:
   ```csharp
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
   This script will redirect API requests to your local server.

---

### 3. **Setting Up FurinaLC**

Now that you have MongoDB and Fiddler configured, follow these steps to set up **FurinaLC**:

1. **Clone the Repository**:  
   Clone the repository to your machine using Git:
   ```bash
   git clone --recursive https://github.com/LEAGUE-OF-NINE/FurinaLC.git
   ```
   Recursive flag is required for submodules.

2. **Navigate to the Project Directory**:  
   Open a terminal or command prompt and navigate to the directory where you downloaded or cloned **FurinaLC**.

3. **Start the Server**:  
   Run the following command to start the server:
   ```bash
   uv run -m server
   ```

---

### 4. **Play the Game**

Once the server is running, you can launch **Limbus Company**. Make sure that Fiddler is running and properly redirecting the API requests to your local server.
