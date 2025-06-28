[app]

title = CalorEyes

source.main = main.py

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
requirements = python3,kivy,plyer,requests,python-dotenv

android.arch = arm64-v8a

# Camera will be used
android.manifest.intent_filters = android.hardware.camera

# Version
version = 0.1
