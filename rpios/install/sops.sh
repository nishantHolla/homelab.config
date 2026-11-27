#!/bin/sh

VERSION="3.13.3"

curl -Lo sops \
  "https://github.com/getsops/sops/releases/download/v${VERSION}/sops-v${VERSION}.linux.arm64"

sudo install -m 755 sops /usr/local/bin/sops

rm sops
