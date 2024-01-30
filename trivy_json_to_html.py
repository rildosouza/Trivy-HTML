# Script created by Rildo Souza - rildo.ras@gmail.com
# Data: 15/01/2024

import json
from jinja2 import Template

# Severity Order
severity_ranking = {
    'CRITICAL': 1,
    'HIGH': 2,
    'MEDIUM': 3,
    'LOW': 4,
    'INFO': 5
}

# Function to get the value based in the severity
def get_severity_ranking(vulnerability):
    return severity_ranking.get(vulnerability['Severity'], 5)


# Specify which json file we will be working with (Trivy file that was created)
with open('/dir/trivy-example.json', 'r') as file:
    trivy_report_data = json.load(file)

# Order by vulnerabilities by severity
for result in trivy_report_data.get('Results', []):
    result['Vulnerabilities'].sort(key=get_severity_ranking)

# Create a template to display the data
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Trivy Scan Report</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Trivy Scan Report</h1>
    {% for result in results %}
    <h2>Target: {{ result['Target'] }}</h2>
    <table>
        <thead>
            <tr>
                <th>Vulnerability ID</th>
                <th>Package Name</th>
                <th>Installed Version</th>
                <th>Fixed Version</th>
                <th>Title</th>
                <th>Severity</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            {% for vulnerability in result['Vulnerabilities'] %}
            <tr>
                <td>{{ vulnerability['VulnerabilityID'] }}</td>
                <td>{{ vulnerability['PkgName'] }}</td>
                <td>{{ vulnerability['InstalledVersion'] }}</td>
                <td>{{ vulnerability['FixedVersion'] }}</td>
                <td>{{ vulnerability['Title'] }}</td>
                <td>{{ vulnerability['Severity'] }}</td>
                <td>{{ vulnerability['Description'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% endfor %}
</body>
</html>
"""

# Creating a HTML file
template = Template(html_template)
html_content = template.render(results=trivy_report_data.get('Results', []))


# Save the html file
output_html_path = '/dir/filename.html'
with open(output_html_path, 'w') as html_file:
    html_file.write(html_content)

print(output_html_path)
