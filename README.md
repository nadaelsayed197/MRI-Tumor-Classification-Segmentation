# 🧠 Brain Tumor Classification & Segmentation

This project focuses on building deep learning models for **brain tumor detection** using MRI images.  
It includes two main tasks:
1. **Classification** – Classify MRI images into **Tumor** or **No Tumor**.
2. **Segmentation** – Detect and highlight the tumor region in MRI scans.

---

## 📌 Dataset
We used publicly available brain MRI datasets:
- **Classification Dataset:** Contains MRI scans labeled as *tumor* or *no tumor*.  
- **Segmentation Dataset:** Includes MRI scans with their corresponding *tumor masks*.  

*(Datasets can be found on [Kaggle](https://www.kaggle.com/) or other open repositories.)*

---

## ⚙️ Models & Techniques
- **Classification Model:**
  - Convolutional Neural Networks (CNNs)
  - Metrics: Accuracy, Precision, Recall, F1-score
- **Segmentation Model:**
  - U-Net architecture
  - Dice Coefficient & IoU for evaluation

---

## 🚀 Installation & Usage
Clone the repository:
```bash
git clone https://github.com/YourUsername/brain-tumor-detection.git
cd brain-tumor-detection
