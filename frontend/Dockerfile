FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE ${FRONTEND_PORT}
EXPOSE ${LIVE_UPDATE_PORT}

# Run the development server binding to all interfaces
CMD ["npm", "run", "dev"]
