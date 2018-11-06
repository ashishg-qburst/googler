import sublime
import webbrowser
import sublime_plugin

def google(query):
  urlWithQuery = "https://www.google.com/search?q=%s" % query
  webbrowser.open(urlWithQuery)

def open_google():
  webbrowser.open("https://www.google.com")

class GooglerCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      location = False
      if region.empty():
          open_google()
      else:
        location = region
        if location and not location.empty():
            query = self.view.substr(location)
        google(query)
