# CST8919 Lab 2 - Building a Web App with Threat Detection using Azure Monitor and KQL

## Student

**Muhannad Jaber**

---

## Project Overview

In this lab, I developed a Python Flask web application with a login page and deployed it to Azure App Service. I configured Azure Monitor and Log Analytics to collect application logs, created Kusto Query Language (KQL) queries to detect failed login attempts, and configured an Azure Monitor Alert Rule that sends an email notification when multiple failed login attempts occur within a short period.

---

## What I Learned

- How to deploy a Python Flask application to Azure App Service.
- How to create and configure a Log Analytics Workspace.
- How to enable Diagnostic Settings for Azure App Service.
- How to use Kusto Query Language (KQL) to search and analyze application logs.
- How to create an Azure Monitor Alert Rule to detect suspicious login activity.
- How Azure Monitor and Application Insights work together to monitor application health.

---

## Challenges I Faced

- Configuring Azure Diagnostic Settings so application logs were sent to Log Analytics.
- Learning how to write KQL queries to filter failed login attempts.
- Creating the Azure Monitor Alert Rule and Action Group.
- Understanding the difference between Azure's built-in Failure Anomalies rule and my custom log search alert.

---

## How I Would Improve the Detection Logic

In a real-world environment, I would improve the detection by:

- Tracking failed login attempts by IP address.
- Detecting brute-force attacks against specific user accounts.
- Automatically blocking IP addresses after multiple failed login attempts.
- Logging additional information such as browser, device, and geographic location.
- Integrating Microsoft Sentinel for more advanced threat detection.

---

## KQL Query

```kusto
AppServiceConsoleLogs
| where ResultDescription contains "FAILED LOGIN"
| summarize FailedAttempts = count() by bin(TimeGenerated, 5m)
| order by TimeGenerated desc
```

### Query Explanation

This query searches the App Service console logs for entries containing **"FAILED LOGIN"**, counts the number of failed login attempts within 5-minute intervals, and sorts the results by time. This query is used by the Azure Monitor Alert Rule to detect potential brute-force login attempts.

---

## Azure Alert Rule

- **Alert Name:** Failed Login Detection
- **Condition:** More than **5** failed login attempts within **5 minutes**
- **Action:** Send an email notification using an Azure Monitor Action Group.

---

## YouTube Demonstration

**Video Link:**  
https://youtu.be/vFGl4DkquHk

---

## Technologies Used

- Python
- Flask
- Microsoft Azure App Service
- Azure Monitor
- Azure Log Analytics
- Kusto Query Language (KQL)
- Azure Monitor Alert Rules
- Git & GitHub
