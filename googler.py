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

        self.view.window().run_command("googler_with_edit", { "query": "%s %s" %(scope, query) });

class GooglerWithEditCommand(sublime_plugin.WindowCommand):
  def run(self, query):
    self.window.show_input_panel('Search for:', query, self.on_done, self.on_change, self.on_cancel)

  def on_done(self, query):
      google(query)

  def on_change(self):
      pass

  def on_cancel(self):
    pass
