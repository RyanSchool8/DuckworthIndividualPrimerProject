# DuckworthIndividualPrimerProject  
Project Status: Final Phase  

Summary:
This project contains an html file where the user fills out a form with the information specified. Then based on the responses to the form the user will be delivered an HTML page with different content on it. If the user selects the radial button that corresponds to remote data, then the cgi script will display the first 5 results from a plain text file from the following URL: https://public.opencpu.org/ocpu/library/. If the cgi script is supplied no query string or if the query string does not conform to the conventions used by the script, then an HTML page indicating an error will be displayed and a link will be provided to the user to navigate back to the index.html form page.  

Changelog:
9/4/15 - Research on CGI basic concepts and apache server configuration.  
9/5/15 - Experimentation with test CGI scripts and test HTML pages.  
9/6/15 1:23pm - Initial readme created.  
9/6/15 1:35pm - index.html and simple.cgi initial file created.  
9/6/15 1:49pm - simple.cgi file updated to contain debugging and testing information.  
9/6/15 3:24pm - modified the simple.cgi file to respond to the html file form submission. Basic functionality regarding different responses depending on the content of the form was implemented.  
9/6/15 4:10pm - added a style.css sheet which will be used to style the HTML pages.  
9/6/15 10:35pm - updated index.html file to include a section in the form to capture information about sports interest.
9/6/15 10:37pm - updated styles.css to include appropriate formatting for the index.html page.  
9/6/15 11:57pm - updated simple.cgi to have css formatted html output
9/7/15 1:10am - updated the simple.cgi file to respond to different query strings based on their content.  
9/7/15 2:18am - uploaded images used for displaying and edited the simple.cgi script.  
9/7/15 3:34pm - updated the simple.cgi file to contain formatted html if there is an error parsing the query string or if there is no query string provided. Also updated the file to get some library information from a remote server. The index.html file was updated to give the option of getting the remote library information or not.  
9/7/15 3:38pm - .htaccess file was added on a testing basis.  
