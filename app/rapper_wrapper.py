import os
import sys
import json
import subprocess
import re

rapperErrorsRegex = re.compile(r"^rapper: Error.*$")
rapperWarningsRegex = re.compile(r"^rapper: Warning.*$")
rapperTriplesRegex = re.compile(r"rapper: Parsing returned (\d+) triples")


def returnRapperErrors(rapperLog):
    errorMatches = []
    warningMatches = []
    for line in rapperLog.split("\n"):
        if rapperErrorsRegex.match(line):
            errorMatches.append(line)
        elif rapperWarningsRegex.match(line):
            warningMatches.append(line)
    return errorMatches, warningMatches


def getTripleNumberFromRapperLog(rapperlog):
    match = rapperTriplesRegex.search(rapperlog)
    if match != None:
        return int(match.group(1))
    else:
        return None


def parse_rdf_from_string(
    rdf_string, base_uri, input_type=None, output_type="ntriples"
):
    if input_type == None:
        command = ["rapper", "-I", base_uri, "-g", "-", "-o", output_type]
    else:
        command = ["rapper", "-I", base_uri, "-i", input_type, "-", "-o", output_type]

    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        input=bytes(rdf_string, "utf-8"),
    )
    triples = getTripleNumberFromRapperLog(process.stderr.decode("utf-8"))
    errors, warnings = returnRapperErrors(process.stderr.decode("utf-8"))
    return process.stdout.decode("utf-8"), triples, errors, warnings
