# behave-plain-color-formatter
Formatter for [behave][] that uses color but not fancy terminal repositioning

![screenshot](https://raw.githubusercontent.com/msabramo/behave-plain-color-formatter/master/screenshot.png)

## Installation
```bash
pip install behave-plain-color-formatter
````

## Usage
You can specify the formatter directly in the command line using the -f argument:
```bash
behave -f behave_plain_color_formatter:PlainColorFormatter
```
or
```bash
behave --format behave_plain_color_formatter:PlainColorFormatter
```

You can also register the formatter to be available through a simple name:
```ini
# -- FILE: behave.ini
[behave.formatters]
plain.color = behave_plain_color_formatter:PlainColorFormatter
```
and the use it like:
```bash
behave -f plain.color
```


[behave]: https://github.com/behave/behave
