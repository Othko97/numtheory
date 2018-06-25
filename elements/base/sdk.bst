kind: import
description: Import the base freedesktop SDK
sources:
- kind: ostree
  url: gnomesdk:repo/
  gpg-key: keys/gnome-sdk.gpg
  track: runtime/org.freedesktop.BaseSdk/x86_64/1.4
  ref: 0d9d255d56b08aeaaffb1c820eef85266eb730cb5667e50681185ccf5cd7c882


config:
  source: files
  target: usr
