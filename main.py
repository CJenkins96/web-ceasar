import webapp2
import ceasar
import cgi

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = ""
        encrypted_message = ceasar.encrypt(message, 13)
        textarea = "<textarea>" + encrypted_message + "</textarea>"
        button = "<input type='submit' value='ENCRYPT!'>"
        form = "<form>" + textarea + button + "</form>"
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
