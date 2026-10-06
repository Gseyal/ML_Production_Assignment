# Iris Flower Classifier

A FastAPI application that predicts an Iris flower’s species:
**Iris-setosa**, **Iris-versicolor**, or **Iris-virginica**.

The model uses four measurements in centimeters: sepal length,
sepal width, petal length, and petal width.

## Example request

Send a POST request to `/predict` with this JSON body:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example response:

```json
{
  "prediction": "Iris-setosa"
}
```

## Run locally

Keep `main.py`, `index.html`, `model.pkl`, and `requirements.txt`
in the same directory.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application from the project directory:

```bash
python -m uvicorn main:app --reload
```

Open:

- Web form: http://localhost:8000
- API documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/health
