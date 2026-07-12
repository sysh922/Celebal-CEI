# Week 4 Azure Data Factory Assignment

## Project Overview

This project demonstrates how to build an Azure Data Factory (ADF) pipeline to copy a CSV file from one Azure Blob Storage container to another while retrieving file metadata. It also includes Azure IAM role assignments and pipeline execution monitoring.

---

## Objectives

- Create Azure resources required for data integration.
- Upload and manage CSV files in Azure Blob Storage.
- Create Linked Services and Datasets in Azure Data Factory.
- Use Get Metadata activity to retrieve file information.
- Use Copy Data activity to transfer files.
- Execute and monitor the pipeline.
- Configure IAM permissions and access controls.

---

## Architecture

```text
Source CSV File
      |
      v
Azure Blob Storage
      |
      v
Get Metadata Activity
      |
      v
Copy Data Activity
      |
      v
Destination Blob Storage
```

---

## Services Used

- Azure Resource Group
- Azure Storage Account
- Azure Blob Storage
- Azure Data Factory (ADF)
- Azure IAM (Identity and Access Management)

---

## Step 1: Create Resource Group

1. Open Azure Portal.
2. Navigate to Resource Groups.
3. Click Create.
4. Enter:
   - Subscription
   - Resource Group Name
   - Region
5. Click Review + Create.

### Output
Resource Group successfully created.

---

## Step 2: Create Storage Account

1. Navigate to Storage Accounts.
2. Click Create.
3. Provide:
   - Subscription
   - Resource Group
   - Storage Account Name
   - Region
4. Click Create.

### Create Containers

Create the following containers:

- source-container
- destination-container

### Upload CSV File

1. Open source-container.
2. Click Upload.
3. Select a CSV file.
4. Upload successfully.

---

## Step 3: Create Azure Data Factory

1. Search for Data Factory.
2. Click Create.
3. Enter:
   - Resource Group
   - Factory Name
   - Region
4. Click Review + Create.

### Launch ADF Studio

After deployment:

1. Open Data Factory.
2. Click Launch Studio.

---

## Step 4: Create Linked Service

1. Open Manage section.
2. Select Linked Services.
3. Click New.
4. Choose Azure Blob Storage.
5. Configure authentication.
6. Test connection.
7. Create linked service.

### Purpose

Allows Azure Data Factory to connect to Blob Storage.

---

## Step 5: Create Datasets

### Source Dataset

- Type: Delimited Text
- Linked Service: Blob Storage
- File Path: Source CSV

### Destination Dataset

- Type: Delimited Text
- Linked Service: Blob Storage
- Container: destination-container

### Purpose

Datasets define source and destination data locations.

---

## Step 6: Create Pipeline

### Add Get Metadata Activity

Configure:

- Dataset: Source Dataset

Fields:

- Exists
- Size
- Last Modified

### Add Copy Data Activity

Configure:

#### Source

- Source Dataset

#### Sink

- Destination Dataset

### Connect Activities

```text
Get Metadata
      |
      v
   Copy Data
```

---

## Step 7: Execute Pipeline

1. Click Debug.
2. Wait for execution.
3. Verify Success status.

### Monitor Execution

1. Open Monitor tab.
2. View pipeline runs.
3. Confirm successful execution.

---

## Step 8: Configure IAM Roles

### Reader Role

Assign Reader access through:

Resource Group → IAM → Add Role Assignment

### Contributor Role

Assign Contributor access through:

Resource Group → IAM → Add Role Assignment

### Storage Access

Assign:

- Storage Blob Data Contributor

to Azure Data Factory Managed Identity.

---

## Validation Checklist

- [x] Resource Group Created
- [x] Storage Account Created
- [x] Source Container Created
- [x] Destination Container Created
- [x] CSV Uploaded
- [x] Linked Service Configured
- [x] Source Dataset Created
- [x] Destination Dataset Created
- [x] Get Metadata Activity Added
- [x] Copy Data Activity Added
- [x] Pipeline Executed Successfully
- [x] IAM Roles Assigned
- [x] File Copied Successfully

---

## Expected Output

- Metadata successfully retrieved.
- CSV file copied from source to destination.
- Pipeline execution status shows **Succeeded**.
- IAM permissions configured correctly.

---

## Screenshots Included

1. Resource Group
2. Storage Account
3. Source Container
4. Uploaded CSV File
5. Linked Service
6. Datasets
7. Get Metadata Activity
8. Pipeline Design
9. Pipeline Success Run
10. IAM Role Assignments
11. Destination Container with Copied File

---

## Author

Shivanshu Yadav

Azure Data Factory – Week 4 Assignment
