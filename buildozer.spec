[app]
# Title of your application
title = Savemedia Video Downloader

# Package name
package.name = savemedia

# Package domain (needed for android)
package.domain = com.savemedia.video

# Source code where the main.py is
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# Version of the application
version = 1.0.0

# Requirements
requirements = python3,kivy==2.1.0,requests,urllib3,chardet,idna,certifi,android

# Presplash screen
presplash.filename = %(source.dir)s/assets/icon.png

# App icon
icon.filename = %(source.dir)s/assets/icon.png

# Supported orientations
orientation = portrait

# Android specific
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 33
android.gradle_dependencies = com.google.android.gms:play-services-ads:21.4.0

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Bootstrap
osx.bootstrap = sdl2
ios.bootstrap = sdl2
android.bootstrap = sdl2

# Kivy configuration
[app]
# Log level (0 = debug, 1 = info, 2 = warning, 3 = error)
log_level = 1

# Fullscreen (0 = window, 1 = fullscreen, 2 = fake fullscreen)
fullscreen = 0

# Window size for desktop
window.width = 360
window.height = 640

# Kivy configuration
[app]
# Preserve the Python console
preserve_python_console = 1

# Touch emulation
mouse = mouse
multitouch_emulate = 0

[buildozer]
# Buildozer log level
log_level = 2
