# About jijnja2
- jinja2 [doc](https://jinja.palletsprojects.com/en/3.0.x/)

>Jinja is a fast, expressive, extensible templating engine. Special placeholders in 
>the template allow writing code similar to Python syntax. Then the template is passed 
>data to render the final document.
>
> from `https://jinja.palletsprojects.com/en/3.0.x/`

# Templates
Templates are text files that contain fields that can be filled with data. jinja2 supports many 
file formats such as plain text, html, xml, latex and others.

You will use `html` templates in this exercise: [html tutorial](https://www.w3schools.com/html/)


## Simple html template

```html
 <!DOCTYPE html>
<html>
<head>
<title>{{ title }}</title>
</head>
<body>

<h1>{{ header1 }}</h1>

{{ table }}

</body>
</html> 
```

# In brief
- create the `templates` and` reports` directories
- save the template as a text file, e.g. `templ_01.html`
- create an environment object:
```python
env = Environment(
    loader=jinja2.FileSystemLoader("templates",encoding='utf-8'),
    autoescape=select_autoescape()
)
```

- prepare the data for the form:
```python
data = {'title': 'some title', 'header1': '....', 'table': html_table}
```

- get template, render it and save the result to disk:
```python
templ = env.get_template('templ_01.html')
templ.render(data)

# save
with open(...) as f:
    f.write(...)

```

