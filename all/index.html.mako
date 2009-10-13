<%inherit file="site.mako" />
<ul>
% for post in posts:
  <li><a href="${post.permapath()}" rel="bookmark" title="Permanent Link to ${post.title}">${post.title}</a>  
  <small>${post.updated.strftime("%B %d, %Y")} | categories:
<% 
   category_links = []
   for category in post.categories:
       if post.draft:
           #For drafts, we don't write to the category dirs, so just write the categories as text
           category_links.append(category.name)
       else:
           category_links.append("<a href='%s'>%s</a>" % (category.path, category.name))
%>
   ${", ".join(category_links)} </small>
% endfor
</ul>
