## FLASK-TUTORIAL
### This repo is just for learning flask
---

### Decorator

The **route()** decorator will tell Flask what URL should trigger our function `index`.

```python
@app.route("/")
def index():
    return "Hello, Flask!"
```

When we send a request to this URL, the `index` function will work and return the " Hello Flask! " to our browser. 
It returns the message we want to display in the user's browser. The default content type is **HTML**, so HTML in the string will be rendered by the browser.

> #### What is HTML?
>
> + HTML stands for Hyper Text Markup Language
>
> + HTML is the standard markup language for creating Web pages
> + HTML describes the structure of a Web page
> + HTML consists of a series of elements
> + HTML elements tell the browser how to display the content
> + HTML elements label pieces of content such as "this is a heading", "this is a paragraph", "this is a link", etc.

We will create a separate file for HTML because a website always has a lot of HTML codes, and writing them in a function isn't clear.

> #### How to return an HTML file's content?
>
> 1. import the package `reder_template `
> 2. modify the code `return "Hello Flask!"` to `return reder_template("index.html")`
> 3. By default, Flask will find the file `index.html` in `./templates/`

