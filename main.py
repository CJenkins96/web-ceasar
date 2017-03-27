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
        <label>Rotate by:</label>
        <input type="number" name="rotation">
        <br>
        <label>Type a message:</label>
        <textarea name="message">%s</textarea>

        <br>
        <input type="submit" value="ENCRYPT!">
    </form>
    </body>
</html>
"""
class MainHandler(webapp2.RequestHandler):
    def write_form(self, encrypted = ""):    
        self.response.write(form % encrypted)

    def get(self):
        self.write_form()

    def post(self):
        message = self.request.get("message")
        rotate = int(self.request.get("rotation"))
        encrypted_message = ceasar.encrypt(message, rotate)
        self.write_form(cgi.escape(encrypted_message))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
