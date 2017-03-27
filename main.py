import webapp2
import ceasar

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hello, world!"
        encrypted_message = ceasar.encrypt(message, 13)
        self.response.write(encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
