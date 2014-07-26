<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" /> 
<title>{{ value }}</title>
<link rev="made" rel="author" href="mailto:{{ CONTACT }}" />
<style type="text/css"><!--/*--><![CDATA[/*><!--*/ 
    body { color: #000000; background-color: #FFFFFF; }
    a:link { color: #0000CC; }
    p, address {margin-left: 3em;}
    span {font-size: smaller;}
/*]]>*/--></style>
</head>
<body>
<h1>Error {{ key }} {{ value }}</h1>
<p>
If you think this is a server error, please contact
the <a href="mailto:{{ CONTACT }}">{{ CONTACT }}</a>.
</p>
<address>
  <a href="/">{{ SERVER_NAME }}</a><br />
  <span>{{ SERVER_SOFTWARE }}</span>
</address>
</body>
</html>