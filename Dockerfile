FROM python:3.9

# Move to the app folder
WORKDIR /code

# Install the requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy all files
COPY . .

# Start the FastAPI server on port 7860 (Hugging Face's default)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
