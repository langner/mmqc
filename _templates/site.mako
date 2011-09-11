<%inherit file="base.mako" />

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>

    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    ${self.head()}
    </head>

    <body>

    <div id="header">
    ${self.header()}
    </div>

    <div id="menu">
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/about">About</a></li>
    </ul>
    </div>

    <div id="content">

    <div class="left">
    </div>

    <div class="right">
    ${next.body()}
    </div>

    <div style="clear: both;"></div>

    </div>

    <div id="footer">
    ${self.footer()}
    </div>

    </body>

</html>

<%def name="head()">
<%include file="head.mako" />
</%def>

<%def name="header()">
<%include file="header.mako" />
</%def>

<%def name="footer()">
<%include file="footer.mako" />
</%def>
