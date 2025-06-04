# 📧 Spam Message Classifier API

This project is a simple machine learning application that classifies SMS messages as **Spam** or **Not Spam** using a Naive Bayes classifier trained on the classic SMS Spam dataset.

## 🚀 Features

- Pretrained model using `TfidfVectorizer + MultinomialNB`
- Flask API to predict messages
- Dockerized for easy deployment
- Deployable to Render in 1 click

---

## 📂 Project Structure

```
├── app.py               # Flask API
├── train_model.py       # Model training script
├── model.pkl            # Trained model (generated at runtime)
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker setup
```

---

## 🧠 Model Info

- **Algorithm**: Multinomial Naive Bayes
- **Vectorizer**: TF-IDF
- **Dataset**: [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

---

## 🧪 Local Testing

```bash
docker build -t spam-api .
docker run -p 5000:5000 spam-api
```

### Sample API Request (via curl or Postman):

```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"message": "Congratulations! You won a free iPhone."}'
```

---

## 🌐 Deploy to Render

1. Push this code to a GitHub repository.
2. Go to [https://render.com](https://render.com)
3. Create a **New Web Service**
4. Choose:
   - Runtime: **Docker**
   - Repository: Your GitHub repo
5. Render will automatically build and serve your app!

---

## ✅ Author

Built with ❤️ using Python, Flask, and Scikit-learn.