#!/usr/bin/env python3
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
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html

# ex.
# .action/solution_check_p1.py  part-1 asgt


import logging
import math
import os
import os.path
import sys
import pexpect
from assessment import solution_check_make, csv_solution_check_make

def run_p1(binary):
    """Run part-1"""
    status = []
    error_values = (
        [], # 0 arguments, too few
        ['ham'], # 1 arguments, too few
        ['ham', 'rye'], # 2 arguments, too few
        ['ham', 'rye', 'tomato', 'lettuce'], # 4 arguments, too many
    )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logging.info('Test %d - %s', test_number, val)
        rv = _run_p1_error(binary, val)
        if not rv:
            logging.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    
    values = (
                ['ham', 'rye', 'mayo'],
                ['tuna', 'wheat', 'mustard'],
                ['roast beef', 'kaiser roll', 'horse radish and mayo'],
                ['salami', 'white', 'cheddar'],
            )
    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logging.info('Test %d - %s', test_number, val)
        rv = _run_p1(binary, val)
        if not rv:
            logging.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p1_error(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1, args=values)

    try:
        proc.expect(r'(?i)\s*error:.+')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "error: you must supply three arguments"')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.close()

    if proc.exitstatus == 0:
        logging.error('Expected: non-zero exit code.')
        logging.error('Program returned zero, but non-zero is required')
        return status

    status = True
    return status

# based on lab 03, but modified to give input as command line arguments
def _run_p1(binary, values):
    """The actual test with the expected input and output"""
    status = False
    values = list(values)
    proc = pexpect.spawn(binary, timeout=1, args=values)

    try:
        regex = r'(?i)\s*Your\s+order.?\s+A\s+{}\s+sandwich\s+on\s+{}\s+with\s+{}.?\s*'.format(*values)
        proc.expect(regex)
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected:"Your order:\nA {} sandwich on {} with {}."'.format(*values))
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()

    if proc.exitstatus != 0:
        logging.error('Expected: zero exit code.')
        logging.error('Program returned non-zero, but zero is required')
        return status

    status = True
    return status


def run_p2(binary):
    """Run part-2"""
    status = []
    error_values = (
        [], # 0 arguments, too few
    )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logging.info('Test %d - %s', test_number, val)
        rv = _run_p2_error(binary, val)
        if not rv:
            logging.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)

    values = (
                [1, 2, 3, 2],
                [10, 20, 15],
                [5, 5, 5],
                [1.2, 1.8, 1.5],
                [-3, 5, 1],
                [-2, -4, -3],
                [2, 3, 2.5],
                [7, 1, 2, 3.333],
                [6, 6],
                [0, 0],
                [0, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5.5],
            )

    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logging.info('Test %d - %s', test_number, val)
        rv = _run_p2(binary, val)
        if not rv:
            logging.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p2_error(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1, args=values)

    try:
        proc.expect(r'(?i)\s*error:.+')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "error: you must supply at least one number"')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.close()

    if proc.exitstatus == 0:
        logging.error('Expected: non-zero exit code.')
        logging.error('Program returned zero, but non-zero is required')
        return status

    status = True
    return status

def _run_p2(binary, values):
    """The actual test with the expected input and output"""
    status = False
    expected = values[-1]
    proc = pexpect.spawn(binary, timeout=1, args=[str(val) for val in values[:-1]])
    values = list(map(str, values))

    try:
        # Match and extract the floating point number
        match_index = proc.expect(r'(?i)\s*average\s*=\s*([-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?)\s*')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "average = %f"', expected)
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    token = proc.match.group(1).decode("utf-8") 
    actual = float(token)
    # 1% tolerance
    if not math.isclose(expected, actual, rel_tol=.01): 
        logging.error('actual numeric output is %f, which does not equal %f', actual, expected)
        return status

    proc.close()

    if proc.exitstatus != 0:
        logging.error('Expected: zero exit code.')
        logging.error('Program returned non-zero, but zero is required')
        return status

    status = True
    return status

def run_p3(binary):
    """Run part-3"""
    status = []
    error_values = (
        ['king'],
        [-1]
    )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logging.info('Test %d - %s', test_number, val)
        rv = _run_p3_error(binary, val)
        if not rv:
            logging.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)

    values = (
        # one card except ace
        [2, 2],
        [3, 3],
        [4, 4],
        [5, 5],
        [6, 6],
        [7, 7],
        [8, 8],
        [9, 9],
        [10, 10],
        ['J', 10],
        ['Q', 10],
        ['K', 10],
        # no cards
        [0],
        # two cards, 5 first
        [5, 2, 7],
        [5, 3, 8],
        [5, 4, 9],
        [5, 5, 10],
        [5, 6, 11],
        [5, 7, 12],
        [5, 8, 13],
        [5, 9, 14],
        [5, 10, 15],
        [5, 'J', 15],
        [5, 'Q', 15],
        [5, 'K', 15],
        # three cards, no bust
        [2, 2, 2, 6],
        [2, 9, 8, 19],
        [3, 'Q', 2, 15],
        # 21 exactly
        ['K', 5, 6, 21],
        [2, 9, 'J', 21],
        ['Q', 6, 5, 21],
        # bust
        [10, 10, 10, 30],
        [7, 7, 8, 22],
        ['J', 'K', 3, 23],
        # ace counts as 1
        [5, 10, 'A', 16],
        ['J', 'K', 'A', 21],
        # ace counts as 11
        ['A', 11],
        ['Q', 'A', 21],
        [6, 'A', 17],
        ['A', 'A', 'A', 'A', 'A', 15],

    )

    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logging.info('Test %d - %s', test_number, val)
        rv = _run_p3(binary, val)
        if not rv:
            logging.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p3_error(binary, values):
    """The actual test with the expected input and output"""
    status = False
    values = list(map(str, values))
    proc = pexpect.spawn(binary, timeout=1, args=values)

    try:
        proc.expect(r'(?i)\s*error:.+')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "error: unknown card \'%s\'', values[0])
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.read()
    proc.close()

    if proc.exitstatus == 0:
        logging.error('Expected: non-zero exit code.')
        logging.error('Program returned zero, but non-zero is required')
        return status

    status = True
    return status

def _run_p3(binary, values):
    """The actual test with the expected input and output"""
    status = False
    expected = values[-1]
    proc = pexpect.spawn(binary, timeout=1, args=[str(val) for val in values[:-1]])
    values = list(map(str, values))

    try:
        # if expected > 21:
        #     # Output requires BUST
        #     regex = fr'(?i)\s*Score\s+is\s+({expected})(,\s+(BUST))\s*'
        # else:
        #     # Output may have BUST but shouldn't
        regex = r'(?i)\s*Score\s+is\s+(\d+)(,\s+(BUST))?\s*'
        proc.expect(regex)
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        if expected > 21:
            logging.error('Expected: "Score is %i, BUST"', expected)
        else:
            logging.error('Expected: "Score is %i"', expected)
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        # return status
    
    if proc.match and proc.match.group(1):
        token = proc.match.group(1).decode("utf-8")
        actual = int(token)
        if actual != expected:
            logging.error('Your program calculated a score of %i. The expected correct score is %i', actual, expected)
            return status
        else:
            logging.debug('score matches expected value')
    else:
        # proc.match doesn't exist or proc.match.group(1) doesn't exist which means
        # that the output was not close to what was expected.
        logging.debug('Computed score not detected.')
        return status
        
    if expected > 21 and proc.match and not proc.match.group(3):
        token = proc.match.group(3).decode("utf-8")
        logging.error('The expected score is over 21. Your program did not tell the player that their hand busted.')
        logging.debug('"BUST" not found in output')
        return status
    else:
        logging.debug('"BUST" shown in output.')

    # proc.read() # regex may not have consumed all output
    proc.close()

    if proc.exitstatus != 0:
        logging.error('Expected: zero exit code.')
        logging.error('Program returned non-zero, but zero is required')
        return status

    status = True
    return status

tidy_opts = (
    '-checks="*,-misc-unused-parameters,'
    '-modernize-use-trailing-return-type,-google-build-using-namespace,'
    '-cppcoreguidelines-avoid-magic-numbers,-readability-magic-numbers,'
    '-fuchsia-default-arguments-calls"'
    ' -config="{CheckOptions: [{key: readability-identifier-naming.ClassCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ClassMemberCase, value: lower_case}, '
    '{key: readability-identifier-naming.ConstexprVariableCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ConstexprVariablePrefix, value: k}, '
    '{key: readability-identifier-naming.EnumCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.FunctionCase, value: CamelCase}, '
    '{key: readability-identifier-naming.GlobalConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.GlobalConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.StaticConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.StaticConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.StaticVariableCase, value: lower_case}, '
    '{key: readability-identifier-naming.MacroDefinitionCase, value: UPPER_CASE}, '
    '{key: readability-identifier-naming.MacroDefinitionIgnoredRegexp, value: \'^[A-Z]+(_[A-Z]+)*_$\'}, '
    '{key: readability-identifier-naming.MemberCase, value: lower_case}, '
    '{key: readability-identifier-naming.PrivateMemberSuffix, value: _}, '
    '{key: readability-identifier-naming.PublicMemberSuffix, value: \'\'}, '
    '{key: readability-identifier-naming.NamespaceCase, value: lower_case}, '
    '{key: readability-identifier-naming.ParameterCase, value: lower_case}, '
    '{key: readability-identifier-naming.TypeAliasCase, value: CamelCase}, '
    '{key: readability-identifier-naming.TypedefCase, value: CamelCase}, '
    '{key: readability-identifier-naming.VariableCase, value: lower_case}, '
    '{key: readability-identifier-naming.IgnoreMainLikeFunctions, value: 1}]}"'
)

if __name__ == '__main__':
    cwd = os.getcwd()
    repo_name = os.path.basename(os.path.dirname(cwd))
    if sys.argv[1] == 'part-1':
        # solution_check_make(
        #     target_directory=sys.argv[2],
        #     program_name=sys.argv[3],
        #     run=run_p1,
        #     tidy_options=tidy_opts,
        # )
        csv_solution_check_make(
            csv_key=repo_name,
            target_directory=sys.argv[2],
            program_name=sys.argv[3],
            run=run_p1,
            tidy_options=tidy_opts,
        )
    elif sys.argv[1] == 'part-2':
        # solution_check_make(
        #     target_directory=sys.argv[2],
        #     program_name=sys.argv[3],
        #     run=run_p2,
        #     tidy_options=tidy_opts,
        # )
        csv_solution_check_make(
            csv_key=repo_name,
            target_directory=sys.argv[2],
            program_name=sys.argv[3],
            run=run_p2,
            tidy_options=tidy_opts,
        )
    elif sys.argv[1] == 'part-3':
        # solution_check_make(
        #     target_directory=sys.argv[2],
        #     program_name=sys.argv[3],
        #     run=run_p2,
        #     tidy_options=tidy_opts,
        # )
        csv_solution_check_make(
            csv_key=repo_name,
            target_directory=sys.argv[2],
            program_name=sys.argv[3],
            run=run_p3,
            tidy_options=tidy_opts,
        )
    else:
        print('Error: no match.')
