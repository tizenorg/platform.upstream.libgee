include $(top_srcdir)/Makefile.decl

lib_LTLIBRARIES = \
	libgee-0.8.la
	$(NULL)

libgee_0_8_la_SOURCES = \
	assemblyinfo.vala \
	abstractbidirlist.vala \
	abstractbidirsortedset.vala \
	abstractbidirsortedmap.vala \
	abstractcollection.vala \
	abstractlist.vala \
	abstractmap.vala \
	abstractmultimap.vala \
	abstractmultiset.vala \
	abstractqueue.vala \
	abstractset.vala \
	abstractsortedmap.vala \
	abstractsortedset.vala \
	arraylist.vala \
	arrayqueue.vala \
	bidiriterator.vala \
	bidirlist.vala \
	bidirlistiterator.vala \
	bidirmapiterator.vala \
	bidirsortedset.vala \
	bidirsortedmap.vala \
	collection.vala \
	comparable.vala \
	concurrentlist.vala \
	concurrentset.vala \
	deque.vala \
	functions.vala \
	hashable.vala \
	hashmap.vala \
	hashmultimap.vala \
	hashmultiset.vala \
	hashset.vala \
	hazardpointer.vala \
	iterable.vala \
	iterator.vala \
	lazy.vala \
	linkedlist.vala \
	list.vala \
	listiterator.vala \
	map.vala \
	mapiterator.vala \
	multimap.vala \
	multiset.vala \
	priorityqueue.vala \
	queue.vala \
	readonlybidirlist.vala \
	readonlybidirsortedset.vala \
	readonlybidirsortedmap.vala \
	readonlycollection.vala \
	readonlylist.vala \
	readonlymap.vala \
	readonlymultimap.vala \
	readonlymultiset.vala \
	readonlyset.vala \
	readonlysortedmap.vala \
	readonlysortedset.vala \
	set.vala \
	sortedmap.vala \
	sortedset.vala \
	timsort.vala \
	traversable.vala \
	treemap.vala \
	treemultimap.vala \
	treemultiset.vala \
	treeset.vala \
	unfolditerator.vala \
	$(NULL)

libgee_0_8_la_VALAFLAGS = \
	-H gee.h --vapi gee-0.8.vapi \
	-h gee-internals.h \
	--internal-vapi gee-internals-0.8.vapi \
	--library gee-0.8 --gir Gee-0.8.gir \
	$(COVERAGE_VALAFLAGS) \
	$(VALAFLAGS) \
	$(NULL)

libgee_0_8_la_CPPFLAGS = \
	$(GLIB_CFLAGS) \
	$(COVERAGE_CFLAGS) \
	$(NULL)

libgee_0_8_la_LIBADD = \
	$(GLIB_LIBS) \
	$(COVERAGE_LIBS) \
	$(NULL)

libgee_0_8_la_LDFLAGS = \
	-version-info $(LIBGEE_LT_VERSION) \
	-no-undefined \
	$(NULL)

geeincludedir = $(includedir)/gee-0.8

geeinclude_HEADERS = \
	gee.h \
	$(NULL)

vapidir = $(datadir)/vala/vapi

dist_vapi_DATA = \
	gee-0.8.vapi \
	$(NULL)

if HAVE_INTROSPECTION
girdir = @INTROSPECTION_GIRDIR@

gir_DATA = \
	Gee-0.8.gir \
	$(NULL)

typelibdir = @INTROSPECTION_TYPELIBDIR@
typelib_DATA = \
	Gee-0.8.typelib \
	$(NULL)

# Extract dlname from libfolks.la; see bug #658002.
# This is what g-ir-scanner does.
libgee_dlname = \
	`$(SED) -nE "s/^dlname='([A-Za-z0-9.+-]+)'/\1/p" libgee-0.8.la`
INTROSPECTION_COMPILER_ARGS= \
	-l $(libgee_dlname)
Gee-0.8.typelib: Gee-0.8.gir
	@INTROSPECTION_COMPILER@ $(INTROSPECTION_COMPILER_ARGS) -o $@ $^
endif

Gee-0.8.gir gee-internals-0.8.vapi gee-0.8.vapi: libgee-0.8.la

CLEANFILES = \
	gee-0.8.vapi \
	gee-internals-0.8.vapi \
	Gee-0.8.typelib \
	Gee-0.8.gir \
	$(NULL)

