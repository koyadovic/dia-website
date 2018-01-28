# Surveys app

To properly use this application follow this steps:

- Add surveys to INSTALLED_APPS.
- Don't forget `python manage.py migrate`.
- Inject ROOT_SERVER_URL in surveys.configuration from outside.
- Add all survey types needed through the admin.
- Modify the templates used for error, completed surveys and base for all surveys templates.

And that's all.

To create links to concrete surveys only need to call `create_survey_url(email, survey_type_slug)` of services module. This call will return a string representing the external url that can be used in an email sent to users. When clicked, survey will be shown. 

For new survey types, the format for fields field need to follow this structure:

```
[
    {
        "key": <key>,
        "type": <field type>,
        "display": <text of label>,
        "options": [] 
    }
]
```

There are the following valid field types: "evaluation", "select", "multiselect" and "text".

- The field type "text" it's rendered as a simple `<textarea>`.

- The field type "evaluation" shows a horizontal line of options. It's useful for evaluation purposes when only is presented numerical options, from 1 to 5 or whatever scale used.

- The field type "select" shows a vertical list of possible options. Only can be selected one of them.

- And the field type "multiselect" is the same as previous type, but for multiple selections.

Options is an obligatory key for field types "evaluation", "select" and "multiselect". Each option element is conformed of a "display" key, the text shown to clients, and "value", the value assigned to the field, if selected. A simple example:

`{ "display": <text to display>, "value": <internal value> }`

There is an special option with an interesting behavior. If it's added an option with "other" as value, if selected, it will be rendered an input text bellow to allow clients to write anything on it.

Enjoy!