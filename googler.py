import sublime
import webbrowser
import sublime_plugin

def google(query=None):
  url = "https://www.google.com"
  if query:
    url += "/search?q=%s" % query
  webbrowser.open(url)

class GooglerCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if region.empty():
        google()
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
