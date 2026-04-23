# ---------- BUILD STAGE ----------
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# ---------- FINAL STAGE ----------
FROM python:3.11-slim

WORKDIR /app

# create non-root user
RUN useradd -m appuser

# copy dependencies from builder
COPY --from=builder /root/.local /root/.local

# copy app
COPY . .

ENV PATH=/root/.local/bin:$PATH

USER appuser

CMD ["python", "main.py"]
