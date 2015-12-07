# -*- coding: utf-8 -*-

project = u'{{project_name}}'
copyright = u'2015, {{user_full_name}}'
version = '{{version}}'
release = '{{release}}'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'alabaster']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = '{{pygments_style}}'

html_theme = 'alabaster'
html_theme_options = {
    'github_user': '{{user_github_account}}',
    'github_repo': '{{project_name}}',
    'description': '{{description}}',
    'github_banner': True,
    'github_button': False,
    'show_powered_by': False,

    {%- if pygments_style == "monokai" %}
    # required for monokai:
    'pre_bg': '#292429',
    {% endif %}
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

intersphinx_mapping = {
    'http://docs.python.org/': None,
}
