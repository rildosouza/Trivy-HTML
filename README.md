# Trivy-HTML
Create a personal report in html format using Trivy

The Trivy doesn't no support HTML format and of course it is not possible to group vulnerabilities by severity. Given these facts, the idea emerged to take the report in json format and create a script that converts it to HTML in a way that allows the user to specify.

License and author

This application is distributed under the GNU license.

Contact the author at rildo.ras@gmail.com

Dependency, Library and Environment:

Trivy Reports has been tested in the following environment:

Python 3.10.12 Trivy 0.47 to 0.48.3

Running the Application

1 - You need a Trivy json scan file(First)

2 - Install Python 3.10.12

3 - Install ninja2 library

4 - Create your html template(we provide a example)

5 - Inform the file path(json kics file)

6 - Inform the output file path (html file)

7 - python3 trivy_json_to_html.py
