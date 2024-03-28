import os
import requests
import subprocess
import shutil
from sonarqube import SonarQubeClient
import json
import pandas as pd
import time

sonarqube_url = "http://127.0.0.1:9000"
sonarqube_token = "squ_9933d4a5ee7a9e77b3050723952e31cdf87c9fcd"
sonar = SonarQubeClient(sonarqube_url=sonarqube_url, token=sonarqube_token)
df = pd.DataFrame()

def scan_project(foldername, sonarqube_url, sonarqube_token):
    # create the given project in the server
    r = requests.post(sonarqube_url + '/api/projects/create', data={"project":{ "key": foldername, "name": foldername, "qualifier": "FIL"}})
    # scan the project
    folder_path = "projects/" + foldername
    sonar_scanner_command = [
        r"C:\Users\bilel\Downloads\sonar-scanner-cli-5.0.1.3006-windows\sonar-scanner-5.0.1.3006-windows\bin\sonar-scanner.bat",
        f"-Dsonar.projectKey={foldername}",
        f"-Dsonar.host.url={sonarqube_url}",
        f"-Dsonar.login={sonarqube_token}",
        f"-Dsonar.projectBaseDir={folder_path}",
        f"-Dsonar.scm.disabled=true",
        f"-Dsonar.sources.inclusions=code.py"
    ]
    try:
        subprocess.run(sonar_scanner_command, check=True)
    except subprocess.CalledProcessError as e:
        print(e)

def generate_scan_reports():
    data_folder_path = "data"
    for filename in os.listdir(data_folder_path):
        file_path = os.path.join(data_folder_path, filename)
        folder_name = filename.split(".")[0].replace("-", "").replace("_", "")
        project_folder_path = os.path.join("projects", folder_name)
        mode = 0o777
        os.mkdir(project_folder_path, mode)
        src = file_path
        dst = project_folder_path + "/code.py"
        shutil.copyfile(src, dst)
        scan_project(folder_name, sonarqube_url, sonarqube_token)

def give_direct_value(json_var, elem):
    try:
        return json_var[elem]
    except:
        return ""

def give_embedded_value(json_var, elem1, rank, elem2):
    try:
        return json_var[elem1][rank][elem2]
    except:
        return ""

def process_issues(issues):
    global df
    for i in issues:
        new_row = {"project": give_direct_value(i, "project"), "rule": give_direct_value(i, "rule"),
        "severity": give_direct_value(i, "severity") ,"line": give_direct_value(i, "line"), "effort": give_direct_value(i, "effort"),
        "debt": give_direct_value(i, "debt"), "tags": "".join(give_direct_value(i, "tags")),
        "type": give_direct_value(i, "type"), "scope": give_direct_value(i, "scope"),
        "cleanCodeAttribute": give_direct_value(i, "cleanCodeAttribute"), "quickFixAvailable": give_direct_value(i, "quickFixAvailable"),
        "cleanCodeAttributeCategory": give_direct_value(i, "cleanCodeAttributeCategory"),
        "Software_Quality_Impact": give_embedded_value(i, "impacts", 0, "softwareQuality"),
        "Impact_Severity": give_embedded_value(i, "impacts", 0, "severity"), "message": give_direct_value(i, "message")}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

def export_scan_report(foldername, sonarqube_url, sonarqube_token):
    #r = requests.get(sonarqube_url + '/api/projects/search', headers={'Authorization': f'Bearer {sonarqube_token}', 'Content-Type': 'application/json'}, data={"project": foldername})
    issues = sonar.issues.search_issues(componentKeys=foldername)["issues"]
    print("++++++++++++++")
    print(issues)
    if (len(issues) > 0):
        process_issues(issues)
    df.to_csv('findings.csv', index=False)


def export_scan_reports():
    directory_path = "projects"
    for folder_name in os.listdir(directory_path):
        if os.path.isdir(os.path.join(directory_path, folder_name)):
            export_scan_report(folder_name, sonarqube_url, sonarqube_token)

generate_scan_reports()
time.sleep(120)
export_scan_reports()