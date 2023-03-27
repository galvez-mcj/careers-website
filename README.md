# Future Careers Website
Flask Web Application styled with Bootstrap and with Dynamic Data from MySQL database

Preview of web app:
![image](https://user-images.githubusercontent.com/123865026/227905065-1e233602-1d59-4c4d-87cb-4c6c63a9a9a2.png)


## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv venv
```

3. Then run the command:
```
$ .\venv\Scripts\activate
```
For windows:
```
$ venv\Scripts\activate.ps1
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
