# IPATool-py

Python version of IPATool!

## Installation

```
pip3 install -r requirements.txt
```

## Usage

### Quickstart: download app with specific bundleId into DIR:

```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP download -e APPLE_EMAIL -p APPLE_PWD -o DIR
```

### Specific usage:

1. Query app info:
    ```
    python3 main.py lookup -b com.touchingapp.potatsolite -c JP
    ```

2. Download app with specific appVerId (salableAdamId):
    ```
    python3 main.py downlaod -i 123456 -e APPLE_EMAIL -p APPLE_PWD
    ```

    Can also supply an optional output dir (e.g. ipa_output):
    ```
    python3 main.py downlaod -i 123456 -e APPLE_EMAIL -p APPLE_PWD -o ipa_output
    ```

3. Get history version (supply an appVerId for target app):
    ```
    python3 main.py historyver -i 123456 -e APPLE_EMAIL -p APPLE_PWD
    ```

4. Chain multiple command, last command's output will be passed to next command (so you don't need to supply some arguments like appVerId)
    ```
    python3 main.py lookup -b com.touchingapp.potatsolite -c JP historyver -e APPLE_EMAIL -p APPLE_PWD
    ```

5. Use json output for program using
    ```
    python3 main.py --json lookup -b com.touchingapp.potatsolite -c JP historyver -e APPLE_EMAIL -p APPLE_PWD
    ```

## Development

- All requests' reqBody and respBody are modeled using modified JSONSchema2PoPo2 (see my NyaMisty/JSONSchema2PoPo2), you can regenerate the binding by cd into `reqs/schemas` and execute `python3 -m schema_defs`

## Credit

- Thanks @majd's ipatool, which is written in swift
