#!/usr/bin/env python3
import sys
import pathlib
import yaml
from yaml import load, dump


def render(args, data, template_path, output_path):
    # template
    import jinja2

    environment = jinja2.Environment(
        # autoescape=jinja2.select_autoescape(),
    )

    def strformat(v, fmt):
        return fmt % v

    environment.filters["strformat"] = strformat

    with open(template_path) as f:
        template = environment.from_string(f.read())

    with open(output_path, "w") as f:
        f.write(
            template.render(
                **data,
            )
        )

    if args.output:
        with open(output_path, "r") as f:
            print(f.read())


def main(args):
    path = f"{args.version_directory}/notes.yml"

    with open(path, "r") as f:
        raw = yaml.load(f, Loader=yaml.CLoader)

    data = {"data": raw}

    if args.dump_data:
        import json

        print(json.dumps(data, indent=4))
        quit(0)

    template_stem = pathlib.Path(pathlib.Path(args.template_path).stem)
    template_stem_ext = template_stem.suffix
    template_stem = template_stem.stem
    render(
        args,
        data,
        args.template_path,
        f"{args.version_directory}/output_{template_stem}{template_stem_ext}",
    )


def cli():
    import argparse

    parser = argparse.ArgumentParser(description="Render passed release notes")

    parser.add_argument(
        "version_directory", type=str, help="Subdirectory for the version to release"
    )
    parser.add_argument(
        "template_path",
        type=str,
        nargs="?",
        default="./template_discord.md.j2",
        help="",
    )

    parser.add_argument(
        "-d",
        "--dump-data",
        dest="dump_data",
        action="store_true",
        help="Dump data and exit",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        action="store_true",
        help="Output results to stdout",
    )

    args = parser.parse_args(sys.argv[1:])
    main(args)


if __name__ == "__main__":
    cli()
