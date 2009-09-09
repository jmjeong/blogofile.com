<%page args="post"/>

<div class="postheader">
<div class="posttitle">
<a name="${post.title}" />
<a href="${post.permapath()}" rel="bookmark" title="Permanent Link to ${post.title}">${post.title}</a>
</div>
<div class="postext">
${post.date.strftime("%b, %d")} | 
categories: 
<% 
   category_links = []
   for category in post.categories:
       if post.draft:
           #For drafts, we don't write to the category dirs, so just write the categories as text
           category_links.append(category.name)
       else:
           category_links.append("<a href='%s'>%s</a>" % (category.path, category.name))
%>
${", ".join(category_links)} | <a href="${post.permalink}#disqus_thread">View Comments</a>
</div>
</div>
<span class="post_prose">
  ${post.excerpt}
</span>