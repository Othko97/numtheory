kind: distutils
description: Python distutils project

depends:
- base.bst

sources:
- kind: local
  path: files/main

variables:
  python: python3

config:
  build-commands:
  - |
    %{python-build}

  install-commands:
  - |
    %{python-install}
