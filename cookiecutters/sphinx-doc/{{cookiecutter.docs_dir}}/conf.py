# -*- coding: utf-8 -*-

project = u'{{cookiecutter.project_name}}'
copyright = u'XXXX {{cookiecutter.full_name}}'
version = 'FIXME {{cookiecutter.release}}'
release = '{{cookiecutter.release}}'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'alabaster']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'monokai'


html_theme = 'alabaster'
html_theme_options = {
    'github_user': '{{cookiecutter.github_username}}',
    'github_repo': '{{cookiecutter.repo_name}}',
    'description': '{{cookiecutter.tagline}}',
    'github_banner': True,
    'gratipay_user': '{{cookiecutter.github_username}}',
    'github_button': False,
    'show_powered_by': False,

    # required for monokai:
    'pre_bg': '#292429',
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

intersphinx_mapping = {'http://docs.python.org/': None,
                       }
