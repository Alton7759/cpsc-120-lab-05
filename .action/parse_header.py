#
# Copyright 2021 Michael Shafae
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
""" Parses the header define by the example given below. """
# https://docs.google.com/document/d/17WkDlxO92zpb26pYM1NIACPcMWtCOlKO7WCrWC6YxRo/edit#
# Example C++ header
# // Michael Shafae
# // CPSC 120-01
# // 2021-01-30
# // mshafae@csu.fullerton.edu
# // @mshafae
# //
# // Lab 00-00
# // Partners: @peteranteater, @ivclasers
# //
# // This is my first program and it prints out Hello World!
# //

import re

HEADER_REGEX = r"(#|/{2})[ \t]+([a-zA-Z0-9_-]+)[ \t]+([ a-zA-Z0-9_-]+)\s+(#|/{2})[ \t]+([a-zA-Z]{4}[ \t]+\d\d\d[a-zA-Z]?-\d\d)\s+(#|/{2})[ \t]+\d\d\d\d-\d\d?-\d\d?\s+(#|/{2})[ \t]+(\w+[.-_0-9\w]*@(csu\.)?fullerton\.edu)\s+(#|/{2})[ \t]+@([a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38})\s+(#|/{2})\s*\s+(#|/{2})[ \t]+(Lab \d\d-\d\d)\n(#|/{2})\s+Partners:(\s*@([a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38})(,\s?@([a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38}))?|)\s+(#|/{2})\s*\n(#|/{2})\s+(\w+.*)\s+(#|/{2})"


def parse_header(contents, keyword=None):
    """Given Given a single string, parse the header and return the keyword's value."""
    header_re = re.compile(HEADER_REGEX)
    matches = re.findall(header_re, contents)
    value = None
    header_matches = None
    if len(matches) >= 1:
        header_matches = matches[0]
    if header_matches:
        if keyword == 'name':
            value = '"{} {}"'.format(matches[1], matches[2])
        elif keyword == 'class':
            value = matches[4]
        elif keyword == 'email':
            value = matches[7]
        elif keyword == 'github':
            value = matches[10]
        elif keyword == 'asgt':
            value = matches[13]
        elif keyword == 'partners':
            value = matches[15]
        elif keyword == 'comment':
            value = matches[-2]
        elif keyword is None:
            value = header_matches
    return value


def dict_header(contents):
    """Given a single string, parse the header and return the result
    as a dictionary with the keys class, email, github, asgt, comment."""
    header_re = re.compile(HEADER_REGEX)
    matches = re.findall(header_re, contents)
    header_d = None
    if len(matches) >= 1:
        matches = matches[0]
        # for i, m in enumerate(matches):
        #     print(f'{i}:"{m}"')
        header_d = {
            'name': '{} {}'.format(matches[1], matches[2]),
            'class': matches[4],
            'email': matches[7],
            'github': matches[10],
            'asgt': matches[13],
            'partners': matches[15],
            'comment': matches[-2],
        }
    return header_d
