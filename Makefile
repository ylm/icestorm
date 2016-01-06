include config.mk

all:
	$(MAKE) -C icebox
	$(MAKE) -C icepack
	$(MAKE) -C iceprog
	$(MAKE) -C icemulti
	$(MAKE) -C icepll
	# $(MAKE) -C icetime

clean:
	$(MAKE) -C icebox clean
	$(MAKE) -C icepack clean
	$(MAKE) -C iceprog clean
	$(MAKE) -C icemulti clean
	$(MAKE) -C icepll clean
	# $(MAKE) -C icetime clean

install:
	$(MAKE) -C icebox install
	$(MAKE) -C icepack install
	$(MAKE) -C iceprog install
	$(MAKE) -C icemulti install
	$(MAKE) -C icepll install
	# $(MAKE) -C icetime install

uninstall:
	$(MAKE) -C icebox uninstall
	$(MAKE) -C icepack uninstall
	$(MAKE) -C iceprog uninstall
	$(MAKE) -C icemulti uninstall
	$(MAKE) -C icepll uninstall
	# $(MAKE) -C icetime uninstall

.PHONY: all clean install uninstall

