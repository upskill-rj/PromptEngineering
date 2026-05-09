# Google Cloud Storage (GCS)

Google Cloud Storage (GCS) is Google’s **object storage service**, designed to store files of any size (from a few KB to petabytes) in a secure, durable, and highly available way.  
It’s the **GCP equivalent of AWS S3 or Azure Blob Storage** and is widely used in DevOps for storing artifacts, logs, backups, and static assets.

---

## 🔹 Key Features of GCS

### 1. **Object Storage**
- Stores data as **objects** (file + metadata) inside **buckets**.  
- Ideal for unstructured data like logs, media, backups, and CI/CD artifacts.  

---

### 2. **Durability**
- GCS provides **11 nines (99.999999999%) durability**.  
- Data is automatically replicated across multiple physical devices.  
- This means your data is extremely safe from hardware failures.  

---

### 3. **Availability & Storage Classes**
- GCS offers different storage classes depending on how often you access data:  
  - **Standard** → For frequently accessed data.  
  - **Nearline** → For data accessed once a month.  
  - **Coldline** → For data accessed once a quarter.  
  - **Archive** → For rarely accessed, long-term storage.  
- Classes differ in **cost per GB** and **retrieval charges**.  

---

### 4. **Regions and Multi-Regions**
- You choose where your data is stored:  
  - **Region** → Data stays in one location (e.g., `asia-south1`).  
  - **Dual-Region** → Data is stored in two regions automatically.  
  - **Multi-Region** → Data is spread across a continent (e.g., US, Europe, Asia).  
- **Multi-region storage** improves availability and global access speeds.  

---

### 5. **Security**
- All data is **encrypted at rest and in transit** by default.  
- Fine-grained **IAM roles** (e.g., Storage Object Viewer, Storage Object Admin).  
- Supports **service accounts** for keyless authentication from apps/VMs.  

---

### 6. **Cost Highlights**
- **Pay only for what you use** (no upfront capacity planning).  
- Costs include:  
  - Storage per GB/month (cheaper for Coldline/Archive).  
  - Network egress (downloading data out of GCP).  
  - API requests (PUT/GET/LIST).  
- ✅ Tip: Use **lifecycle policies** to automatically move older data to cheaper classes.  

---

### 7. **Performance**
- High throughput, low latency access to objects.  
- Strong **read-after-write consistency** globally (you always get the latest object after upload).  

---

### 8. **Integration with DevOps Tools**
- **CI/CD** → Store build artifacts, Helm charts, Terraform state files.  
- **Observability** → Centralized log storage.  
- **Static hosting** → Host websites or documentation directly from GCS.  
- **Analytics** → Integrates with BigQuery, Dataflow, and AI/ML pipelines.  

---

## ✅ Quick Recap
- **Buckets** are the main container in GCS.  
- Data is **durable, secure, and highly available**.  
- Multiple **storage classes** help balance cost and performance.  
- **Multi-region support** makes global apps faster.  
- Perfect for **DevOps workflows** like CI/CD artifacts, backups, and log storage.  

======================

# 🚀 Hands-On Demo: Google Cloud Storage with Compute Engine VM

In this demo, we will connect **Google Cloud Storage (GCS)** with a **Compute Engine VM** using the **Google Cloud Console (UI only)**.  
You will learn how to create a bucket, set up IAM with a service account, launch a VM, and securely access storage from inside the VM.

---

## 🔑 Learning Objectives
By completing this demo, you will:
- Create a **Cloud Storage bucket**.  
- Create and configure a **Service Account** for secure access.  
- Launch a **Compute Engine VM** with the Service Account attached.  
- Use the VM to **read and write objects** in the bucket.  
- Clean up resources when finished.  

---

## 📝 Step-by-Step Instructions

### **Step 1: Create a Cloud Storage Bucket**
1. Go to the **Google Cloud Console** → **Navigation Menu (☰) → Cloud Storage → Buckets**.  
2. Click **Create bucket**.  
3. Enter a **unique name** (e.g., `gcs-demo-bucket-2025`).  
   - Bucket names must be globally unique across GCP.  
4. Choose **Location type → Region** and pick a region close to you (e.g., `asia-south1 (Mumbai)`).  
5. Leave the **Storage class** as **Standard**.  
6. Under **Access control**, keep it at **Uniform** (recommended).  
7. Click **Create**.  

✅ You now have a storage bucket ready.  

---

### **Step 2: Create a Service Account**
1. Navigate to **Navigation Menu → IAM & Admin → Service Accounts**.  
2. Click **Create Service Account**.  
3. Enter the name: `gcs-demo-sa`.  
4. Click **Create and continue**.  
5. In **Grant this service account access to project**, select the role:  
   - **Storage → Storage Object Admin** (allows the VM to read/write bucket objects).  
6. Click **Continue → Done**.  

✅ A service account is now available for attaching to your VM.  

---

### **Step 3: Launch a Compute Engine VM**
1. Go to **Navigation Menu → Compute Engine → VM Instances**.  
2. Click **Create Instance**.  
3. Configure:
   - **Name:** `gcs-demo-vm`.  
   - **Region/Zone:** Same as your bucket (for lower latency).  
   - **Machine type:** `e2-micro` (eligible for free tier).  
   - **Boot disk:** Keep the default (Debian/Ubuntu).  
4. Scroll down to **Identity and API access**:
   - Under **Service account**, choose `gcs-demo-sa`.  
   - For **Access scopes**, choose **Allow full access to all Cloud APIs** (simpler for this demo).  
5. Click **Create**.  

✅ You now have a VM that can access GCS without any keys.  

---

### **Step 4: Upload a File to Your Bucket**
1. Go to **Cloud Storage → Buckets → your bucket name**.  
2. Click **Upload Files**.  
3. Select a local file (e.g., `hello.txt`).  
4. Verify that the file is visible in the bucket.  

✅ This file will be accessed from the VM.  

---

### **Step 5: Access the Bucket from the VM**
1. Go to **Compute Engine → VM instances**.  
2. Click **SSH** next to your VM (`gcs-demo-vm`) to open a browser terminal.  
3. Inside the VM terminal, run the following commands:  

   - **List files in your bucket:**
     ```
     gcloud storage ls gs://<your-bucket-name>
     ```

   - **Download the uploaded file:**
     ```
     gcloud storage cp gs://<your-bucket-name>/hello.txt hello-vm.txt
     cat hello-vm.txt
     ```

   - **Upload a new file back to GCS:**
     ```
     echo "Hello from Compute Engine VM" > vm-upload.txt
     gcloud storage cp vm-upload.txt gs://<your-bucket-name>/vm-upload.txt
     ```

4. Go back to the **Cloud Storage Console** and confirm that `vm-upload.txt` is present in your bucket.  

✅ The VM can now read and write objects to GCS using its service account.  

---

### **Step 6: Cleanup Resources**
When done, clean up to avoid charges:  
1. Delete the **VM** → Go to **Compute Engine → VM Instances → Select VM → Delete**.  
2. Delete the **Bucket** → Go to **Cloud Storage → Buckets → Select Bucket → Delete**.  
3. Delete the **Service Account** → Go to **IAM & Admin → Service Accounts → Delete**.  
4. If this project was created just for testing, you can delete the **entire project**, which removes all resources.  

---

## 🎯 Key Takeaways
- **Cloud Storage** is the default choice for storing objects like logs, backups, and artifacts.  
- **Service Accounts** provide **secure, keyless authentication** for applications and VMs.  
- **Compute Engine VMs** can interact with GCS easily when IAM roles are attached.  
- Always **clean up resources** after hands-on work to avoid unexpected billing.  
