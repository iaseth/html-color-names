
# html-color-names

| # | Name | className | Hex |
| --- | --- | --- | --- |{% for color in colors %}
| {{ loop.index }} | {{ color.name }} | {{ color.lowername }} | {{ color.hex }} |{% endfor %}


