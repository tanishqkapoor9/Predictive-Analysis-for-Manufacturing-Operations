## Predictive Analysis API

The **Predictive Analysis API** is a web-based application designed to facilitate predictive modeling workflows, providing endpoints for data upload, model training, and predictions. The API is built to handle various machine learning tasks, allowing users to interact with the system via simple HTTP requests.

### Key Features:
- **Upload Endpoint**: Allows users to upload datasets that will be used for training machine learning models. The system supports common file formats like CSV, Excel, and others.
- **Train Endpoint**: Provides an interface to trigger the training process of machine learning models on the uploaded data. It automatically processes the dataset and tunes the model for optimal performance.
- **Predict Endpoint**: Enables users to make predictions based on new input data using the trained model. It provides quick, real-time results for various types of predictive tasks.

### Technology Stack:
- **Flask**: A lightweight Python web framework for building the API.
- **Scikit-learn**: A powerful machine learning library used for model building and evaluation.
- **Pandas & Numpy**: For data manipulation and numerical operations.

### Usage:
1. **Setup**: Install dependencies by running the `requirements.txt` file.
2. **Running the App**: Start the server by running `python app.py`, which will serve the API locally.
3. **Endpoints**: Utilize the provided endpoints for uploading data, training models, and making predictions.

This API is ideal for users who need to automate and streamline their predictive analysis workflow with minimal setup.


<img width="861" alt="Screenshot 2025-01-21 at 1 31 53 PM" src="https://github.com/user-attachments/assets/2bb331f8-4b93-4778-8782-a5e1a1511a16" />

<img width="861" alt="Screenshot 2025-01-21 at 1 37 13 PM" src="https://github.com/user-attachments/assets/0e781a8b-b90a-408a-91b4-46e684643568" />

<img width="861" alt="Screenshot 2025-01-21 at 1 40 20 PM" src="https://github.com/user-attachments/assets/2100623b-65f5-4f32-9f36-608aea389785" />
