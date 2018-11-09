# Googler

Sublime Text plugin for easy googling.

## Features and Abilities:

* Open Google homepage
* Google current selection
* Auto-prefix file type with selection
* Selections/queries are editable before search
* Configurable search query prefixes & suffixes for each file type

## Usage

Press `super` then type `og`

* Without any selections, it will take you to Google
* With selections it will open a panel where you can edit the query (hit `Enter` after confirmation)

## Settings

From the menu bar:

`Sublime Text -> Preferences -> Package Settings -> Googler -> Settings - User`

Default and sample settings can be found in the `Settings - Default` file.

## Finding the file type

Press ``ctrl + ` `` to open the console in Sublime Text.
Paste in the below command and hit `Enter` to find the file type.

`self.view.scope_name(region.begin()).rpartition('.')[2].strip()`

You can then use this as the key in your settings file.

## Configuration

In your `Settings - User` file:

```
{
  "includeScope": false, // Disables file type configs
   "ruby": { // For .rb files the file type is 'ruby'
     "prefix": "rails", // Useful if you are working on a Rails project
     "suffix": "site:api.rubyonrails.org" // Restrict results to a site
   },
   "js": {
     "prefix": "", // Disable the prefix for this scope
     "suffix": "react docs"
   }
}
```



