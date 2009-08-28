<div id="right_sidebar">
  <div id="contact">
  <h3>Contact</h3>
    <ul>
      <li><a href="http://mailhide.recaptcha.net/d?k=01yleiHsdMkwiYRi2feqIlew==&amp;c=u_gRqM7YsegNq30vAk0q6v1WaoKk8YHS8o8P2gZutMY=" onclick="window.open('http://mailhide.recaptcha.net/d?k=01yleiHsdMkwiYRi2feqIlew==&amp;c=u_gRqM7YsegNq30vAk0q6v1WaoKk8YHS8o8P2gZutMY=', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">Email</a>
      <li><a href="/jmjeong/pgp_key.html">PGP public key</a></li>
	  <li><a href="http://twitter.com/jmjeong">Twitter</a></li>
    </ul>
  </div>
  <div id="blog_post_list">
  <h3>Latest blog posts</h3>
  <ul>
% for post in posts[:5]:
    <li><a href="${post.path}">${post.title}</a></li>
% endfor
  </ul>
  </div>
  <div id="on_twitter">
    <h3>On Twitteres</h3>
    <div id="blogofile_tweets"></div>
    <a href="http://twitter.com/jmjeong" style="float: right">See more tweets</a>
  </div>
  <div id="categories">
    <h3>Categories</h3>
    <ul>
% for category, num_posts in all_categories:
     <li><a href="${category.path}">${category}</a> (<a href="${category.path}/feed">rss</a>) (${num_posts})</li>
% endfor
    </ul>
  </div> 
  <div id="archives">			
    <h3>Archives</h3>
    <ul>
% for link, name, num_posts in archive_links:
      <li><a href="${link}" title="${name}">${name}</a>&nbsp;(${num_posts})</li>
% endfor
    </ul>
    
  </div>

</div>
