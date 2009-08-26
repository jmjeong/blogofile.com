<% import urlparse %>
<div id="header" onclick="location.href='/';" style="cursor: pointer;">
  <div id="plugbanner"></div>
  <div id="blog_logo"></div>
  <h1><a href="/">
      <span id="blog_name">
        ${config.blog_name}
      </span>
    </a>
  </h1>
</div>
<div id="top_bar">
  <div class="ButtonBar">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="http://jmjeong.com/old">Previous Homepage</a></li>
      <li><a href="http://wiki.jmjeong.com">Palm Wiki</a></li>
      <li><a href="${config.util.blog_path_helper('')}">Blog List</a></li>
    </ul>
  </div>
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
