FROM node:alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

# Build the application
ENV NODE_ENV=production
ENV NEXT_PUBLIC_BACKEND_API_URL=https://news-backend-sindre-test-644994207224.europe-north1.run.app

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]