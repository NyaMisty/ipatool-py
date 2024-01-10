# IPATool-py

Python version of IPATool! 

**Now Supports**:
  - **Purchasing App via `--purchase`**
  - **Downloading Old IPA via iTunes Server**

## Installation

```
pip3 install -r requirements.txt
```

## Usage

There're three commands: lookup, historyver, download. Each command's usage can be found by `-h` option.

You can also chain multiple command, last command's output will be passed to next command (so you don't need to supply some arguments like appVerId)

### Download Newest Version

Download an app using bundleID (-o can be omited)
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP download -e APPLE_EMAIL -p APPLE_PWD -o DIR
```

Or appID (`XXXXX` in the `apps.apple.com/app/xxxx/idXXXXXX`)
```
python3 main.py download -i XXXXX
```

You can also purchase apps when downloading using `--purchase`:
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP download --purchase -e APPLE_EMAIL -p APPLE_PWD -o DIR
```

### Download OLD Version

Old versions must be downloaded together with `iTunes Server`. You can get `iTunes Server` in several ways:
- Using [action-ipadown](https://github.com/NyaMisty/action-ipadown) directly, which integrated this tool
    - NOTE: this method does not support 2FA
- Manually way with Windows: (supports 2FA)
    - download this repo: https://github.com/NyaMisty/actions-iTunes-header
    - install iTunes 12.6.5.3, from https://secure-appldnld.apple.com/itunes12/091-87819-20180912-69177170-B085-11E8-B6AB-C1D03409AD2A6/iTunes64Setup.exe
    - patch the iTunes using `actions-iTunes-header/workflow_helper/iTunesInstall/patch_itunes.py`
    - install frida: `pip3 install frida`
    - open iTunes, sign out & re-login your account
    - run: `actions-iTunes-header/workflow_helper/iTunesDownload/get_header.py`
- Manually way with jailbroken iOS device: (supports 2FA)
    - download [KbsyncTool](https://github.com/Lessica/KbsyncTool/releases)
    - install `com.darwindev.kbsync_XXX.deb` on your jailbroken device
    - exec `kbsynctool -s 9000` on your jailbroken device
    - you will find log `Using -s http://192.168.100.227:9000/...`, use it as server address in next step

After setting up the server, you can run this tool to download a specific version
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP download -s http://127.0.0.1:9000 --appVerId 833889087
```

NOTE: Some users are reporting that you need to **authorize computer** and make first purchase in iTunes with marked "do not ask for password" before using the iTunes server. (See #26)

### Get History Ver (usually used together with JSON)

Get all appVerId of app from Apple
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP historyver -e APPLE_EMAIL -p APPLE_PWD
```

### Lookup (usually used together with JSON)

Query app basic information:
- By bundleID: `python3 main.py lookup -b com.touchingapp.potatsolite -c JP`
- By appID: `python3 main.py lookup -i 1239860606 -c JP`

Query appVerId:
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP --get-verid
```

### Headless Usage

For each command you can use `--json` switch to get result of command in JSON

```
python3 main.py --json lookup -b com.touchingapp.potatsolite -c JP --get-verid
python3 main.py --json lookup -b com.touchingapp.potatsolite -c JP historyver -e APPLE_EMAIL -p APPLE_PWD
```

### For Large Scale Scraping

You can download all versions of an app like this:
```
python3 main.py --json download --itunes-server http://XXX.XXX.XXX.XXX:9000 --appId 414478124 --purchase --downloadAllVersion
```

- In this mode, errors will only be logged instead of interrupting the whole process
- For each downloaded app version, it will output a line of json in stdout like this:
  ```
  {"appName": "WeChat", "appBundleId": "com.tencent.xin", "appVer": "6.5.13.34", "appId": 414478124, "appVerId": 822899148, "downloadedIPA": "wechat\\com.tencent.xin-6.5.13.34-414478124-822899148.ipa", "downloadedVerId": 822899148}
  ```
  Logs will only be printed to stderr, so you can parse this line for automation. 


## Development

- All requests' reqBody and respBody are modeled using modified JSONSchema2PoPo2 (see my NyaMisty/JSONSchema2PoPo2), you can regenerate the binding by cd into `reqs/schemas` and execute `python3 -m schema_defs`
- See more information on how to generate schema in reqs/schemas directory

## Credit

- Thanks @majd's ipatool, which is written in swift
