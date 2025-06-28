[app]

title = CalorEyes

source.main = main.py

requirements = python3,kivy,plyer,requests,python-dotenv

android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.ndk_api = 21

android.arch = armeabi-v7a

# Camera will be used
android.manifest.intent_filters = android.hardware.camera

# Version
version = 0.1
