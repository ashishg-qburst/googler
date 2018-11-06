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
      if region.empty():
          open_google()
      else:
        scope = self.view.scope_name(region.begin()).rpartition('.')[2].strip()
        query = self.view.substr(region)
        google("%s %s" %(scope, query))
