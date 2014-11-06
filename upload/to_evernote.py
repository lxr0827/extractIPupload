__author__ = 'lxr0827'
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteTypes

developer_token = "S=s7:U=4d5ee:E=150d624adf8:C=1497e737ff8:P=1cd:A=en-devtoken:V=2:H=3e2cc053475801b183f1e2712cba0cd1"
note_name = "uploadTPLinkIP"
ip_content = "0.0.0.0"

def upload(ip_content):
    # Set up the NoteStore client
    client = EvernoteClient(token=developer_token,sandbox=False,service_host="app.yinxiang.com")
    note_store = client.get_note_store()

    # Make API calls
    noteFilter = NoteTypes.NoteFilter()
    noteFilter.words = note_name
    noteList = note_store.findNotes(noteFilter, 0, 1)

    if 0 < len(noteList.notes):
        note = noteList.notes[0]
        note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>%s</en-note>' % ip_content
        note_store.updateNote(note)
    else:
        note = Types.Note()
        note.title = note_name
        note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
        note.content += '<en-note>%s</en-note>' % ip_content
        note_store.createNote(note)
