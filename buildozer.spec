[app]
title = Flux Mobile
package.name = fluxmobile
package.domain = org.test

version = 1.0
version.code = 1

source.dir = .
source.main = main.py

requirements = python3, kivy

android.permissions = INTERNET
android.minapi = 21
android.targetapi = 31

orientation = portrait

[buildozer]
log_level = 2
