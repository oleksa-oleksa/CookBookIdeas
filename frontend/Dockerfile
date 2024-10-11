# Use the official Node.js image as base
FROM node:16-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Build the Angular app
RUN npm run build --prod

# Serve the app with a simple static server
RUN npm install -g http-server
CMD ["http-server", "dist/my-receipt-app", "-p", "4200"]
