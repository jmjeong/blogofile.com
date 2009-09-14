<p id="credits">
Powered by <a href="http://www.blogofile.com">Blogofile</a>.
RSS feeds for <a href="${config.util.blog_path_helper('feed')}">Entries</a> and <a href="http://${config.disqus_name}.disqus.com/latest.rss">Comments</a>.
</p>

<script type="text/javascript">
//<![CDATA[
(function() {
		var links = document.getElementsByTagName('a');
		var query = '?';
		for(var i = 0; i < links.length; i++) {
			if(links[i].href.indexOf('#disqus_thread') >= 0) {
				query += 'url' + i + '=' + encodeURIComponent(links[i].href) + '&';
			}
		}
		document.write('<script charset="utf-8" type="text/javascript" src="http://disqus.com/forums/${config.disqus_name}/get_num_replies.js' + query + '"></' + 'script>');
	})();
//]]>
</script>

<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-998709-1";
urchinTracker();
</script>
