<%inherit file="_templates/site.mako" />

<h2>Recent posts</h2>

% for post in bf.config.blog.posts[:5]:
    <%include file="post_excerpt.mako" args="post=post" />
% endfor

