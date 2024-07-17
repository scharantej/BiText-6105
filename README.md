## Website with Two Text Boxes

### HTML Files

**index.html**

- **Purpose**: Main HTML file that defines the layout of the website.
- **Bootstrap Included**: This file should include the necessary Bootstrap CSS and JavaScript files.
- **Text Boxes**: The HTML should include two text boxes for user input.

**Example Content:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>Text Box Example</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.6.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.6.1/js/bootstrap.min.js"></script>
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <label for="textbox1">Text Box 1:</label>
        <input type="text" class="form-control" id="textbox1">
      </div>
      <div class="col-md-6">
        <label for="textbox2">Text Box 2:</label>
        <input type="text" class="form-control" id="textbox2">
      </div>
    </div>
    <button class="btn btn-primary" type="button" onclick="submitText()">Submit</button>
  </div>
  <script>
    function submitText() {
      // Your JavaScript code to submit the text box values to the Flask route
    }
  </script>
</body>
</html>
```

### Routes

**app.py**

- **Main Python Script**: This file contains the Flask application and defines the necessary routes.

**Routes:**

1. **Root Route (/)**:
   - **Purpose**: Default route that renders the index.html file.

2. **Submit Route (/submit)**:
   - **Method**: POST
   - **Purpose**: Receives the text box values from the index.html file and performs the desired action (e.g., saving the values to a database).