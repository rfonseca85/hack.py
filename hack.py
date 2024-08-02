from flask import Flask, request, make_response
import os

app = Flask(__name__)

@app.route('/')
def index():
    cookie_data = []

    if request.cookies:
        cookies = request.cookies
        cookie_data = [f"{key}: {value}" for key, value in cookies.items()]
        cookies_info = "<br>".join(cookie_data)
        
        # Save cookies to a text file
        with open("cookies.txt", "a") as file:
            file.write("\n".join(cookie_data) + "\n")
        
        return f"Cookies received:<br>{cookies_info}"
    else:
        resp = make_response("No cookies found!")
        return resp

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)


