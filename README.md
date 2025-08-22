# 🦠 Coccidiosis Disease Classification

A robust, end-to-end deep learning pipeline for automated classification of Coccidiosis disease in chicken fecal images. This project leverages modern MLOps practices, modular code, and a reproducible workflow to streamline data ingestion, model training, evaluation, and deployment.

---

## 🌐 Project Links

- **Live Demo:** [View Project](https://your-live-project-url.com)
- **LinkedIn:** [Lakshit Jain](https://www.linkedin.com/in/jainlakshit/)

---

## 🚀 Tech Stack

- **Python 3.8+**
- **TensorFlow / Keras**
- **DVC** (Data Version Control)
- **PyYAML**
- **Flask** (for deployment)
- **Logging & Utilities**
- **Jupyter Notebooks** (for experimentation)
- **Git & GitHub Actions** (CI/CD)
- **VS Code** (recommended IDE)

---

## 🏗️ Project Structure

```
Coccidiosis-Disease-Classification/
│
├── config/                # YAML configuration files
├── research/              # Jupyter notebooks for experiments
├── src/
│   └── coccidiosisDiseaseClassification/
│       ├── components/    # Core pipeline components
│       ├── config/        # Configuration management
│       ├── constants/     # Constant values
│       ├── entity/        # Data classes for configs
│       ├── pipeline/      # Pipeline stage scripts
│       ├── utils/         # Utility functions
│
├── templates/             # Web app templates
├── dvc.yaml               # DVC pipeline definition
├── params.yaml            # Model & training parameters
├── requirements.txt
├── setup.py
└── README.md
```

---

## 🔬 Pipeline Stages

1. **Data Ingestion**
   - Downloads and extracts raw data.
2. **Prepare Base Model**
   - Loads and customizes a pre-trained CNN (e.g., VGG16).
3. **Training**
   - Trains the model on the dataset with augmentation and callbacks.
4. **Evaluation**
   - Evaluates model performance and logs metrics.
5. **Prediction (Deployment)**
   - Flask API for real-time inference.

---

## ⛓️ Pipeline DAG

![Pipeline DAG](images/image.png)

---

## 🧠 Model Architecture

![Model Structure](images/image-1.png)

---

## 🖼️ Example Images

![Project Image](images/image-2.png)

---

## ⚙️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/lakshitcodes/Coccidiosis-Disease-Classification.git
   cd Coccidiosis-Disease-Classification
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the pipeline**

   ```bash
   python3 main.py
   ```

4. **Start the web app**
   ```bash
   python3 app.py
   ```

---

## 📁 Configuration

- **config/config.yaml**: Pipeline and artifact paths
- **params.yaml**: Model hyperparameters

---

## ✨ Features

- Modular, maintainable codebase
- Reproducible experiments with DVC
- Automated logging and error handling
- Easy deployment with Flask
- Extensible for other image classification tasks

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---
