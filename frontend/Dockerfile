# Use a lightweight Nginx image to serve static files
FROM nginx:alpine

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the frontend static files into the Nginx HTML directory
COPY . /usr/share/nginx/html

# Expose port 80 for the Nginx server
EXPOSE 80

# Command to start Nginx (default for this image)
CMD ["nginx", "-g", "daemon off;"]