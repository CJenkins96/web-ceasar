import webapp2
import ceasar
import cgi
form = """
<!DOCTPYE html>
<html>
    <head>
        <title>Web Ceasar!</title>
    </head>
    <body>
    <form method="post">
        <h1>Web Ceasar!</h1>
        <div style="color:red;">%(rot_error)s</div>
        <label>Rotate by:</label>
        <input type="number" name="rotation">
        <div style="color:red;">%(msg_error)s</div>
        <label>Type a message:</label>
        <textarea name="message">%(encrypted)s</textarea>

        <br>
        <input type="submit" value="ENCRYPT!">
    </form>
    </body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def write_form(self, encrypted = "", rot_error = "", msg_error = ""):    
        self.response.write(form % {"rot_error": rot_error, 
                                    "msg_error": msg_error, "encrypted": encrypted})

    def get(self):
        self.write_form()

    def post(self):
        message = self.request.get("message")
        if self.request.get("rotation").isdigit():
            rotate = int(self.request.get("rotation"))
            encrypted_message = ceasar.encrypt(message, rotate)
            self.write_form(cgi.escape(encrypted_message))
        else:
            self.write_form(message, "\tThat's not a valid number!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
