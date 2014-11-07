__author__ = 'lxr0827'

from extract.from_tplink import extract
from upload.to_evernote import upload

upload(extract())