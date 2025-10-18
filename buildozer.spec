[app]
title = Flux Mobile
package.name = fluxmobile
package.domain = org.flux

version = 1.0
version.code = 1

source.dir = .
source.main = main.py

requirements = python3, kivy, openssl

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.minapi = 21
android.targetapi = 34

orientation = portrait

[buildozer]
log_level = 2