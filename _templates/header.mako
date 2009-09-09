<% import urlparse %>
<div class="header">
 <div class="title">${config.blog_name}</div>
 <div class="status"><nobr></nobr></div>
</div>

<div class="mainmenu">
 <a href="/">Home</a>
 <a href="http://jmjeong.com/old">Previous Homepage</a>
 <a href="http://wiki.jmjeong.com">Palm Wiki</a>
 <a href="${config.util.blog_path_helper('')}">Blog List</a>
 <div id="search">
   <form id="searchform" method="get" action="http://www.google.com/search">
     <input type="hidden" name="ie" value="UTF-8">
     <input type="hidden" name="oe" value="UTF-8">
     <input type="hidden" name="domains" value="${urlparse.urlparse(config.blog_url)[1]}">
     <input type="hidden" name="sitesearch" value="${urlparse.urlparse(config.blog_url)[1]}">
     <input name="q" id="q" size="20" value="search in blog..." onfocus="if(this.value==this.defaultValue) this.value='';" type="text">
   </form>
 </div>
</div>
