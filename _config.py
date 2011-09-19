# -*- coding: utf-8 -*-

######################################################################
# This is your site's Blogofile configuration file.
# www.Blogofile.com
#
# This file doesn't list every possible setting, it relies on defaults
# set in the core blogofile _config.py. To see where the default
# configuration is on your system run 'blogofile info'
#
######################################################################

######################################################################
# Basic Settings
#  (almost all sites will want to configure these settings)
######################################################################

## site_url -- Your site's full URL
# Your "site" is the same thing as your _site directory.
#  If you're hosting a blogofile powered site as a subdirectory of a larger
#  non-blogofile site, then you would set the site_url to the full URL
#  including that subdirectory: "http://www.yoursite.com/path/to/blogofile-dir"
site.url = "http://mmqc.org"

# ignored paths
site.file_ignore_patterns += [ ".*/README.*" ]

####################
# Blog Settings ####
####################

blog = controllers.blog

## blog_enabled -- Should the blog be enabled?
#  (You don't _have_ to use blogofile to build blogs)
blog.enabled = True

## blog_path -- Blog path.
#  This is the path of the blog relative to the site_url.
#  If your site_url is "http://www.yoursite.com/~ryan"
#  and you set blog_path to "/blog" your full blog URL would be
#  "http://www.yoursite.com/~ryan/blog"
#  Leave blank "" to set to the root of site_url
blog.path = "/notes"

## blog_name -- Your Blog's name.
# This is used repeatedly in default blog templates
blog.name = "mmqc"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog.description = "Perambulations of a physicist"

## blog_timezone -- the timezone that you normally write your blog posts from
blog.timezone = "Europe/Amsterdam"

#### disqus.com comment integration ####
blog.disqus.enabled = True
blog.disqus.name = "langner"

### Syntax highlighter ###
# You can change the style to any builtin Pygments style
# or, make your own: http://pygments.org/docs/styles
blog.filters.syntax_highlight.style = "fruity"
blog.filters.syntax_highlight.css_dir = "/css"
blog.filters.syntax_highlight.preload_styles = ["murphy", "monokai", "fruity"]

#### Custom blog index ####
# If you want to create your own index page at your blog root
# turn this on. Otherwise blogofile assumes you want the
# first X posts displayed instead
blog.custom_index = False

#Post excerpts
#If you want to generate excerpts of your posts in addition to the
#full post content turn this feature on
blog.post_excerpts.enabled = True
blog.post_excerpts.word_length = 30

# blog posts per page
blog.posts_per_page = 5

# blog permalinks
blog.auto_permalink.enabled = True
blog.auto_permalink.path = ":blog_path/:year/:title"

# pagination directory
blog.pagination_dir = "page"

# default filters
blog.post_default_filters = {
    "markdown": "syntax_highlight, markdown",
    "textile": "syntax_highlight, textile",
    "org": "syntax_highlight, org",
    "rst": "syntax_highlight, rst",
    "html": "syntax_highlight"
}
                    
# similar posts
blog.similar_posts.enabled = True
blog.similar_posts.count = 5


