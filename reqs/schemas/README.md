# Schema Definitions for ipatool-py

In this directory, JSON Schema Definition files are stored in `schema_defs`, with corresponding plist examples in `schema_examples`

## How to generate schema from plist

1. Convert plist to corresponding JSON, using either `plistlib` or online tools
2. Use https://www.liquid-technologies.com/online-json-to-schema-converter to convert JSON to schema
3. Merge different request / response body's schema manually

## Regenerate schema bindings

Run this in current folder:
```
python3 -m schema_defs
```