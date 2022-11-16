#!/usr/bin/env python3
import os
import json
from string import Template

NOCTIS_THEMES_DIR = "noctis/themes"
OUTPUT_DIR = "themes"


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    template = Template(open("template.yml").read())

    for variant in os.listdir(NOCTIS_THEMES_DIR):
        variant_name = variant.split(".")[0]
        with open(os.path.join(NOCTIS_THEMES_DIR, variant)) as f:
            variant_definition = json.load(f)

        theme = {
            "background": variant_definition["colors"]["terminal.background"],
            "foreground": variant_definition["colors"]["terminal.foreground"],
            "cursor_background": variant_definition["colors"]["terminalCursor.background"],
            "cursor_foreground": variant_definition["colors"]["terminalCursor.foreground"],
            "black": variant_definition["colors"]["terminal.ansiBlack"],
            "red": variant_definition["colors"]["terminal.ansiRed"],
            "green": variant_definition["colors"]["terminal.ansiGreen"],
            "yellow": variant_definition["colors"]["terminal.ansiYellow"],
            "blue": variant_definition["colors"]["terminal.ansiBlue"],
            "magenta": variant_definition["colors"]["terminal.ansiMagenta"],
            "cyan": variant_definition["colors"]["terminal.ansiCyan"],
            "white": variant_definition["colors"]["terminal.ansiWhite"],
            "bright_black": variant_definition["colors"]["terminal.ansiBrightBlack"],
            "bright_red": variant_definition["colors"]["terminal.ansiBrightRed"],
            "bright_green": variant_definition["colors"]["terminal.ansiBrightGreen"],
            "bright_yellow": variant_definition["colors"]["terminal.ansiBrightYellow"],
            "bright_blue": variant_definition["colors"]["terminal.ansiBrightBlue"],
            "bright_magenta": variant_definition["colors"]["terminal.ansiBrightMagenta"],
            "bright_cyan": variant_definition["colors"]["terminal.ansiBrightCyan"],
            "bright_white": variant_definition["colors"]["terminal.ansiBrightWhite"],
        }

        output_file = "noctis.yml" if variant_name == "noctis" else f"noctis-{variant_name}.yml"
        with open(os.path.join(OUTPUT_DIR, output_file), "w") as f:
            f.write(template.substitute(theme))


if __name__ == "__main__":
    main()
