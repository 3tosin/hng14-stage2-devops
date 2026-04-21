FROM node:18-alpine

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Install deps
COPY package*.json ./
RUN npm install --only=production

# Copy app
COPY . .

USER appuser

EXPOSE 3000

HEALTHCHECK CMD wget --no-verbose --tries=1 --spider http://localhost:3000 || exit 1

CMD ["node", "app.js"]
