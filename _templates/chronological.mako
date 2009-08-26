<%inherit file="site.mako" />
<div class="blog_post">
<ul>
% for post in posts:
  <li><a href="${post.permapath()}" rel="bookmark" title="Permanent Link to ${post.title}">${post.title}</a>  
  <small>${post.date.strftime("%B %d, %Y at %I:%M %p")} | 
<% 
   category_links = []
   for category in post.categories:
       if post.draft:
           #For drafts, we don't write to the category dirs, so just write the categories as text
           category_links.append(category.name)
       else:
           category_links.append("<a href='%s'>%s</a>" % (category.path, category.name))
%>
   ${", ".join(category_links)} </small><p/>
% endfor
	 </ul>
</div>
% if prev_link:
 <a href="${prev_link}">« Previous Page</a>
% endif
% if prev_link and next_link:
  --  
% endif
% if next_link:
 <a href="${next_link}">Next Page »</a>
% endif

