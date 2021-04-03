import xml.etree.ElementTree as ET
import os

base_dir = '../glyph_definitions'


def tabulate_params(input_files, full_name=True):
    all_params = set(['glyphtype', 'soterms'])

    rows = []

    for file in input_files:

        (base_name, extension) = os.path.splitext(file.name)

        if not full_name:
            base_name = base_name.split('/')[-1]

        # if extension != ".svg":
        #    continue

        tree = ET.parse(file)
        svg_tree = tree.getroot()

        param_string = svg_tree.attrib['{https://parametric-svg.github.io/v0.2}defaults']

        assignments = param_string.split(';')

        row = {'name': base_name}
        for assignment in assignments:
            (var_name, value) = assignment.split('=')
            row[var_name] = value
            all_params.add(var_name)

        row['glyphtype'] = svg_tree.attrib['glyphtype']
        row['soterms'] = svg_tree.attrib['soterms']

        rows.append(row)

    fieldnames = ['name']
    fieldnames.extend(all_params)

    return fieldnames, rows
