[app]

# Title of your application
title = InstagramDownloader

# Package name
package.name = instagramdownloader

# Source code where the main.py lives
source.dir = .

# Application versioning
version = 1.0

# Application requirements
requirements = python3, kivy, selenium, requests

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# Target Android API (should be as high as possible)
android.api = 29

# Minimum API your APK will support
android.minapi = 21

# Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# Android arch to build for (choices: armeabi-v7a, arm64-v8a, x86, x86_64)
android.arch = armeabi-v7a

# Android entry point (default is okay for Kivy-based app)
android.entrypoint = org.kivy.android.PythonActivity

# Indicate whether the application should be fullscreen or not
fullscreen = 0

# Presplash image filename
presplash.filename = %(source.dir)s/images/logo.png

# Icon filename
icon.filename = %(source.dir)s/images/logo.png

# Supported orientation (one of landscape, sensorLandscape, portrait, or all)
orientation = portrait
