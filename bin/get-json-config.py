#!/usr/bin/python3

'''Utility to dump json section from the crucible run file'''

import argparse
import sys
import json

def process_options():
    """Handle the CLI argument parsing options"""

    parser = argparse.ArgumentParser(description = "Read a config section from crucible run file")

    parser.add_argument("--json",
                        dest = "json_file",
                        help = "Crucible config settings json file (e.g. crucible-run.json)",
                        type = str)

    parser.add_argument("--config",
                        dest = "config",
                        required = True,
                        help = "Configuration type to get from the json file",
                        choices = [ "mv-params", "tool-params", "passthru-args" ])

    args = parser.parse_args()
    return args

def dump_json(obj, format = 'readable'):
    """Dump json in readable or parseable format"""
    # Parseable format has no indentation
    indentation = None
    sep = ':'
    if format == 'readable':
        indentation = 4
        sep += ' '

    return json.dumps(obj, indent = indentation, separators = (',', sep),
                      sort_keys = True)

def load_json_file(json_file):
    """Load JSON file and return a json object"""
    try:
         input_fp = open(json_file, 'r')
         input_json = json.load(input_fp)
         input_fp.close()
    except:
         print("Could not load JSON file %s" % (json_file))
         return None
    return input_json

def main():
    """Main function of get-json-config.py tool"""

    global args

    input_json = load_json_file(args.json_file)
    print(dump_json(input_json[args.config]))


if __name__ == "__main__":
    args = process_options()
    exit(main())

