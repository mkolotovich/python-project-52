dev:
	python3 manage.py runserver
install:
	poetry install
messages:
	python3 ../../manage.py makemessages -l ru
compile:
	python3 ../manage.py compilemessages