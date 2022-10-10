#
# Copyright 2021-2022 Michael Shafae
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

TARGET = average
# C++ Files
CXXFILES = average.cc
# Headers
HEADERS = 

CXX = clang++
CXXFLAGS += -g -O3 -Wall -pedantic -pipe -std=c++17
LDFLAGS += -g -O3 -Wall -pedantic -pipe -std=c++17

UNAME_S = $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    CXXFLAGS += -D LINUX
	# Note in Ubuntu 22 clang++ has it's own std. library
	# clang++ -nostdinc++ -nostdlib++ -isystem /usr/lib/llvm-14/include/c++/v1 -L /usr/lib/llvm-14/lib -Wl,-rpath,/usr/lib/llvm-14/lib -lc++ -std=c++17 
endif
ifeq ($(UNAME_S),Darwin)
	ifeq (,$(wildcard "/opt/local/bin/port"))
		# Use MacPorts clang++'s standard library
		CXXFLAGS += -D OSX -nostdinc++ -I/opt/local/include/libcxx/v1
		LDFLAGS += -L/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib -L/opt/local/lib/libcxx
	else
		# Use Apple's standard library (not recommended)
		CXXFLAGS += -D OSX
	endif
endif
UNAME_M = $(shell uname -m)
ifeq ($(UNAME_M),x86_64)
	CXXFLAGS += -D AMD64
endif
ifneq ($(filter %86,$(UNAME_M)),)
	CXXFLAGS += -D IA32
endif
ifneq ($(filter arm%,$(UNAME_M)),)
	CXXFLAGS += -D ARM
endif

DOXYGEN = doxygen
DOCDIR = doc

OBJECTS = $(CXXFILES:.cc=.o)

DEP = $(CXXFILES:.cc=.d)

MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PART_PATH := $(dir $(MKFILE_PATH))
LAB_PART := $(notdir $(patsubst %/,%,$(dir $(MKFILE_PATH))))

.SILENT: doc lint format header test

default all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(LDFLAGS) -o $(TARGET) $(OBJECTS) $(LLDLIBS)

-include $(DEP)

%.d: %.cc
	set -e; $(CXX) -MM $(CXXFLAGS) $< \
	| sed 's/\($*\)\.o[ :]*/\1.o $@ : /g' > $@; \
	[ -s $@ ] || rm -f $@

%.o: %.cc
	$(CXX) $(CXXFLAGS) -c $<

clean:
	-rm -f $(OBJECTS) core $(TARGET).core

spotless: clean
	-rm -f $(TARGET) $(DEP) a.out
	-rm -rf $(DOCDIR)
	-rm -rf $(TARGET).dSYM
	-rm -f compile_commands.json

doc: $(CXXFILES) $(HEADERS)
	(cat Doxyfile; echo "PROJECT_NAME = ${TARGET}") | $(DOXYGEN) -

compilecmd:
	@echo "$(CXX) $(CXXFLAGS)"

format:
	python3 ../.action/format_check.py $(CXXFILES) $(HEADERS)

lint:
	python3 ../.action/lint_check.py $(CXXFILES) $(HEADERS)

header:
	python3 ../.action/header_check.py $(CXXFILES) $(HEADERS)

test:
	python3 ../.action/solution_check.py $(LAB_PART) . $(TARGET)
