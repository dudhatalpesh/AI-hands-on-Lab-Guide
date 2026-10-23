.PHONY: install test check demo api
install:
	python -m pip install -r requirements-dev.txt
test:
	python -m unittest discover -s tests -v
check:
	python scripts/check_repo.py
	python -m ruff check .
demo:
	python -m streamlit run scripts/dashboard.py
api:
	python -m uvicorn src.advisor.api:app --host 127.0.0.1 --port 8000
