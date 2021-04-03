# Parametric SVG Utility

`parametric-svg-utility` is a commandline utility for applying various transformations to Parametric SVG files.

It is written in Python, using the [click](https://click.palletsprojects.com) library for commandline interfaces, and follows the same pattern as the [imagepipe example](https://github.com/pallets/click/blob/master/examples/imagepipe/imagepipe.py) for [multi-command chaining](https://click.palletsprojects.com/en/7.x/commands/#multi-command-chaining).



## Examples

```
parametric-svg-utility parameters glyph_definitions/*



parametric-svg-utility open -i glyph_definitions/Aptamer.svg -i glyph_definitions/CDS.svg remove_parametric_params save
parametric-svg-utility open -i glyph_definitions/Aptamer.svg -i glyph_definitions/CDS.svg remove_parametric_params save --format all
parametric-svg-utility open -i glyph_definitions/Aptamer.svg -i glyph_definitions/CDS.svg remove_parametric_params delete_by_class -c baseline save 
parametric-svg-utility  open -i glyph_definitions/Aptamer.svg apply_transformation save 

parametric-svg-utility  open -i glyph_definitions/Aptamer.svg \
style_class -c "baseline" -s "opacity:1;fill:none;fill-opacity:1;stroke:#b3b3b3;stroke-width:0.49999994; stroke-linecap:round;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:1,0.5; stroke-dashoffset:0;stroke-opacity:1" \
save

parametric-svg-utility  open -i glyph_definitions/Aptamer.svg \
substitute -o width -n w \
save

```
