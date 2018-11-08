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
        selection = self.view.substr(region)
        settings = sublime.load_settings("googler.sublime-settings")

        if settings.get('includeScope'):
          scope = self.view.scope_name(region.begin()).rpartition('.')[2].strip()
          qc = settings.get(scope) or {}
          query = ' '.join(filter(None, [(qc.get('prefix') or scope), selection, qc.get('suffix')]))
        else:
          query = selection

        self.view.window().run_command("googler_with_edit", { "query": query });

class GooglerWithEditCommand(sublime_plugin.WindowCommand):
  def run(self, query):
    self.window.show_input_panel('Search for:', query, self.on_done, None, None)

  def on_done(self, query):
    google(query)
