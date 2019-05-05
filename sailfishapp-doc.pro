TEMPLATE = subdirs
SUBDIRS = doc examples

docs.depends += examples

OTHER_FILES += README \
    rpm/sailfishapp-doc.spec
