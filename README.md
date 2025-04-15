# Run to get the binaries
sudo apt-get update
pip install -r requirements.txt

## Running with Docker

1. Build the image:
   ```sh
   docker build -t auth-validator-service .
   ```

2. Run the container:
   ```sh
   docker run -p 5001:5001 auth-validator-service
   ```

3. Access the liveness endpoint:
   ```sh
   curl -O http://localhost:5001/liveness
   ```
4. To run 
   gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()" --timeout 900