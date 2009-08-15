######################################################################
# This is the main Blogofile configuration file.
# www.Blogofile.com
#
# This file has the following ordered sections:
#  * Basic Settings
#  * Intermediate Settings
#  * Advanced Settings
#
#  You really only _need_ to change the Basic Settings.
######################################################################

######################################################################
# Basic Settings
#  (almost all sites will want to configure these settings)
######################################################################
#Your Blog's name. This is used repeatedly in default blog templates
blog_name        = "Blogofile"
#Your Blog's full URL
blog_url         = "http://www.blogofile.com/blog"
#A short one line description of the blog, used in the RSS/Atom feeds.
blog_description = "A static blog engine/compiler"
#The timezone that you normally write your blog posts from
blog_timezone    = "US/Eastern"
#Blog posts per page
blog_posts_per_page = 5
#If permalink is not defined in post article, this value is used
# :year, :month, :day -> post's date
# :title              -> post's title
# :uuid               -> sha hash based on title
# :filename           -> article's filename without suffix
permalink        = "/blog/:filename"

######################################################################
# Intermediate Settings
######################################################################
#### Disqus.com comment integration ####
disqus_enabled = True
disqus_name    = "blogofile"

#### Emacs org-mode Converter ####
orgmode_enabled = True
# emacs binary (orgmode must be installed)
emacs_binary    = "/usr/bin/emacs"               # emacs 22 or 23 is recommended
emacs_preload_elisp = "_emacs/setup.el"          # preloaded elisp file
orgmode_preamble = r"#+OPTIONS: H:3 num:nil toc:nil \n:nil"   # added in preamble

#### Blog post syntax highlighting ####
syntax_highlight_enabled = True
# You can change the style to any builtin Pygments style
# or, make your own: http://pygments.org/docs/styles
syntax_highlight_style   = "murphy"

#### Custom blog index ####
# If you want to create your own index page at your blog root
# turn this on. Otherwise blogofile assumes you want the
# first X posts displayed instead
blog_custom_index = False

#Post excerpts
#If you want to generate excerpts of your posts in addition to the
#full post content turn this feature on
post_excerpt_enabled     = True
post_excerpt_word_length = 25
#Also, if you don't like the way the post excerpt is generated
#You can define a new function
#below called post_excerpt(content, num_words)

#### Blog pagination directory ####
# blogofile places extra pages of your blog or category in
# a secondary directory like the following:
# http://www.yourblog.com/blog_root/page/4
# http://www.yourblog.com/blog_root/category_1/page/4
# You can rename the "page" part here:
blog_pagination_dir = "page"

######################################################################
# Advanced Settings
######################################################################
# These are the default ignore patterns for excluding files and dirs
# from the _site directory
# These can be strings or compiled patterns.
# Strings are assumed to be case insensitive.
ignore_patterns = [
    r".*[\/]_.*",   #All files that start with an underscore
    r".*[\/]#.*",   #Emacs temporary files
    r".*~$]",       #Emacs temporary files
    r".*[\/]\.git", #Git VCS dir
    r".*[\/]\.hg",  #Mercurial VCS dir
    r".*[\/]\.bzr", #Bazaar VCS dir
    r".*[\/]\.svn", #Subversion VCS dir
    r".*[\/]CVS"    #CVS dir
    ]

### Pre/Post build hooks:
def pre_build():
    #Do whatever you want before the _site is built
    pass
def post_build():
    #Do whatever you want after the _site is built
    pass

