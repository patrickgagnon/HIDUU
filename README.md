<a href="https://badge.fury.io/py/HIDUU"><img src="https://badge.fury.io/py/HIDUU.svg" alt="PyPI version" height="18"></a>

# HealtheIntent Data Upload Utility 

<img src="https://logos-download.com/wp-content/uploads/2016/10/Cerner_Corporation_logo.png" alt="Cerner" width="200"/>

## What is Cerner HIDUU?
>**HealtheIntent Data Upload Utility (HIDUU)** enables you to upload different data sets into the HealtheIntent cloudbased system. HIDUU is intended to replace Data Upload Utility (DUU) as the primary means for uploading data in batch to the HealtheIntent system; for more information, see Benefits of HealtheIntent Data Upload Utility Over DUU. The HIDUU is a Java-based command-line application that wraps Web services. It can be executed from either Microsoft Windows or Unix operating systems. It performs some file-level, client-side validation before uploading the file. OAuth is used to authorize the system from which the file is originating. The endpoint is protected by the Cerner Care OAuth service. You can achieve automation by scripting the execution of the utility's various commands.

## What is this repository for?
This repository contains updated production code that made it possible to upload files using the HIDUU utility. This wrapper provides functionality for both UNIX and Windows systems.

## System and Package Configuration
For this package to work the software, hi-Data_upload_utility, must be fully installed and initialized on the machine running these processes. Configuring this wrapper to your HIDUU installation requires the user to then create and maintain a settings file in their local environment. This file contains all the parameters and arguments necessary for a HIDUU command to be executed.

## Further Documentation:
### Cerner Corporation
[Cerner Corporation Homepage](https://www.cerner.com/)

### Cerner Code
[Cerner Code API Page](https://docs.healtheintent.com/#introduction)

### Montana DHHS
[Montana DHHS HIDUU Documentation](https://dphhs.mt.gov/Portals/85/hrd/documents/MPATHDAPHHIDUUDataSubmissionOverviewandInstructions.pdf)
