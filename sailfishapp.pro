TEMPLATE = subdirs
SUBDIRS = src doc data launcher tests examples

docs.depends += examples

OTHER_FILES += README \
    rpm/libsailfishapp.spec
